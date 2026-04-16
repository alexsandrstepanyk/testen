from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import get_db
from models.models import TestSession
from schemas.schemas import SessionCreate, SessionFinish, SessionOut
from datetime import datetime, timezone
from services.report_pdf import build_test_report_pdf
from services.question_resolver import get_questions_by_test_number, get_test_label
from services.telegram import is_enabled, send_message, send_pdf_document
from fastapi import File, UploadFile
from services.telegram import send_video

router = APIRouter()


def get_derived_teil5_score(session: TestSession) -> int:
    answers = session.answers_json or {}
    if isinstance(answers, dict):
        meta_score = answers.get("__teil5_score")
        if isinstance(meta_score, int):
            return meta_score
        if isinstance(meta_score, str) and meta_score.isdigit():
            return int(meta_score)

    total = session.score or 0
    return max(0, total - sum([
        session.teil1_score or 0,
        session.teil2_score or 0,
        session.teil3_score or 0,
        session.teil4_score or 0,
    ]))

@router.post("/start", response_model=SessionOut)
def start_session(data: SessionCreate, db: Session = Depends(get_db)):
    total_questions = len(get_questions_by_test_number(db, data.test_number))
    session = TestSession(
        user_name=data.user_name.strip(),
        test_number=data.test_number,
        total_questions=total_questions,
    )
    db.add(session); db.commit(); db.refresh(session)
    if is_enabled():
        msg = (
            "Neue Test-Session gestartet\n"
            f"Name: {session.user_name}\n"
            f"Test: {get_test_label(session.test_number or 1, db)}\n"
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
    answers_payload = data.answers.copy() if isinstance(data.answers, dict) else dict(data.answers)
    answers_payload["__teil5_score"] = data.teil5_score or 0
    session.answers_json = answers_payload
    session.teil1_score = data.teil1_score
    session.teil2_score = data.teil2_score
    session.teil3_score = data.teil3_score
    session.teil4_score = data.teil4_score or 0
    resolved_total = len(get_questions_by_test_number(db, session.test_number or 1))
    session.total_questions = resolved_total or session.total_questions or 0
    db.commit(); db.refresh(session)

    response_payload = SessionOut.model_validate(session).model_dump()
    response_payload["teil5_score"] = get_derived_teil5_score(session)

    if is_enabled():
        try:
            questions = get_questions_by_test_number(db, session.test_number or 1)
            pdf_bytes, mistakes = build_test_report_pdf(session, questions)
            filename = f"Testbericht_T{session.test_number}_{session.user_name.replace(' ', '_')}_{session.id}.pdf"
            caption = (
                f"Neues Testergebnis: {session.user_name} ({get_test_label(session.test_number or 1, db)})\n"
                f"Punkte: {session.score}/{(session.total_questions or 55) + 10} | {session.percentage}%\n"
                f"Fehler: {len(mistakes)}"
            )
            send_pdf_document(pdf_bytes, filename, caption)
        except Exception:
            # Telegram delivery must never break the test flow
            pass

    return response_payload

@router.get("/{session_id}", response_model=SessionOut)
def get_session(session_id: int, db: Session = Depends(get_db)):
    s = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not s: raise HTTPException(status_code=404, detail="Session not found")
    payload = SessionOut.model_validate(s).model_dump()
    payload["teil5_score"] = get_derived_teil5_score(s)
    return payload

@router.post("/{session_id}/upload-video")
def upload_presentation_video(session_id: int, video: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload presentation video to Telegram and save file_id to session"""
    session = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    try:
        # Read video file
        video_bytes = video.file.read()
        if not video_bytes:
            raise HTTPException(status_code=400, detail="Empty video file")
        
        # Limit file size to 20MB for Telegram
        max_size = 20 * 1024 * 1024
        if len(video_bytes) > max_size:
            raise HTTPException(status_code=413, detail=f"Video too large (max 20MB, got {len(video_bytes) / (1024*1024):.1f}MB)")
        
        original_name = (video.filename or "presentation.webm").strip() or "presentation.webm"
        safe_name = original_name.replace("/", "_").replace("\\", "_")
        filename = f"presentation_{session.user_name.replace(' ', '_')}_{session_id}_{safe_name}"
        caption = f"Präsentation von {session.user_name}\nSession ID: {session_id}"
        content_type = (video.content_type or "video/mp4").strip()
        
        # Upload to Telegram
        file_id = send_video(video_bytes, filename, caption, content_type=content_type)
        
        if not file_id:
            raise HTTPException(status_code=500, detail="Failed to upload video to Telegram")
        
        # Save file_id to session
        session.video_url = file_id
        db.commit()
        db.refresh(session)
        
        return {
            "status": "ok",
            "session_id": session.id,
            "file_id": file_id,
            "message": "Video uploaded successfully"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)[:100]}")
