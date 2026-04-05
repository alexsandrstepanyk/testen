from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from models.models import TestSession
from models.questions_data import get_questions_for_test
from schemas.schemas import SessionCreate, SessionFinish, SessionOut
from datetime import datetime, timezone
from services.report_pdf import build_test_report_pdf
from services.telegram import is_enabled, send_message, send_pdf_document

router = APIRouter()

@router.post("/start", response_model=SessionOut)
def start_session(data: SessionCreate, db: Session = Depends(get_db)):
    session = TestSession(user_name=data.user_name.strip(), test_number=data.test_number)
    db.add(session); db.commit(); db.refresh(session)
    if is_enabled():
        msg = (
            "Neue Test-Session gestartet\n"
            f"Name: {session.user_name}\n"
            f"Test: {session.test_number or 1}\n"
            f"Session ID: {session.id}"
        )
        send_message(msg)
    return session

@router.post("/{session_id}/finish", response_model=SessionOut)
def finish_session(session_id: int, data: SessionFinish, db: Session = Depends(get_db)):
    session = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.finished_at = datetime.now(timezone.utc)
    session.duration_seconds = data.duration_seconds
    session.score = data.score
    session.percentage = data.percentage
    session.passed = data.passed
    session.answers_json = data.answers
    session.teil1_score = data.teil1_score
    session.teil2_score = data.teil2_score
    session.teil3_score = data.teil3_score
    session.teil4_score = data.teil4_score or 0
    db.commit(); db.refresh(session)

    if is_enabled():
        try:
            questions = get_questions_for_test(session.test_number or 1)
            pdf_bytes, mistakes = build_test_report_pdf(session, questions)
            filename = f"Testbericht_T{session.test_number}_{session.user_name.replace(' ', '_')}_{session.id}.pdf"
            caption = (
                f"Neues Testergebnis: {session.user_name} (Test {session.test_number or 1})\n"
                f"Punkte: {session.score}/{(session.total_questions or 45) + 10} | {session.percentage}%\n"
                f"Fehler: {len(mistakes)}"
            )
            send_pdf_document(pdf_bytes, filename, caption)
        except Exception:
            # Telegram delivery must never break the test flow
            pass

    return session

@router.get("/{session_id}", response_model=SessionOut)
def get_session(session_id: int, db: Session = Depends(get_db)):
    s = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not s: raise HTTPException(status_code=404, detail="Session not found")
    return s
