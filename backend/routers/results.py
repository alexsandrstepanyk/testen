from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc, func, not_, or_
from models.database import get_db
from models.models import TestSession
import io
from services.report_pdf import build_test_report_pdf
from services.question_resolver import get_questions_by_test_number, get_test_label

router = APIRouter()

TEST_NAME_PATTERNS = [
    "%test-student%",
    "%copilot qa%",
    "%live qa demo%",
    "%qa render test%",
    "%telegram qa%",
]


def get_derived_teil5_score(session: TestSession) -> int:
    answers = session.answers_json or {}
    if isinstance(answers, dict):
        meta_score = answers.get("__teil5_score")
        if isinstance(meta_score, int):
            return meta_score
        if isinstance(meta_score, str) and meta_score.isdigit():
            return int(meta_score)
    return max(0, (session.score or 0) - sum([
        session.teil1_score or 0,
        session.teil2_score or 0,
        session.teil3_score or 0,
        session.teil4_score or 0,
    ]))

@router.get("/leaderboard")
def get_leaderboard(limit: int = Query(default=50, le=200),
                    test_number: int = Query(default=0),
                    db: Session = Depends(get_db)):
    q = db.query(TestSession).filter(TestSession.score.isnot(None))
    q = q.filter(not_(or_(*[TestSession.user_name.ilike(p) for p in TEST_NAME_PATTERNS])))
    if test_number in range(1, 6):
        q = q.filter(TestSession.test_number == test_number)
    sessions = q.order_by(desc(TestSession.score), TestSession.duration_seconds).limit(limit).all()
    return {"leaderboard": [
        {"rank": i+1, "user_name": s.user_name, "test_number": s.test_number or 1,
         "test_label": get_test_label(s.test_number or 1, db),
         "score": s.score, "total_questions": s.total_questions,
         "percentage": s.percentage, "duration_seconds": s.duration_seconds,
         "passed": s.passed, "teil1_score": s.teil1_score,
         "teil2_score": s.teil2_score, "teil3_score": s.teil3_score,
         "teil4_score": s.teil4_score or 0,
         "teil5_score": get_derived_teil5_score(s),
         "hoeren_score": s.hoeren_score,
         "finished_at": s.finished_at.isoformat() if s.finished_at else None}
        for i, s in enumerate(sessions)
    ], "total_entries": len(sessions)}

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(TestSession).filter(TestSession.score.isnot(None)).count()
    if not total:
        return {"total_attempts":0,"pass_rate":0,"avg_score":0,"avg_duration_seconds":0}
    passed = db.query(TestSession).filter(TestSession.passed==True).count()
    avg_s = db.query(func.avg(TestSession.score)).filter(TestSession.score.isnot(None)).scalar()
    avg_d = db.query(func.avg(TestSession.duration_seconds)).filter(TestSession.duration_seconds.isnot(None)).scalar()
    return {"total_attempts":total,"total_passed":passed,
            "pass_rate":round(passed/total*100,1),
            "avg_score":round(avg_s,1) if avg_s else 0,
            "avg_duration_seconds":int(avg_d) if avg_d else 0}

@router.delete("/leaderboard/clear")
def clear(db: Session = Depends(get_db)):
    db.query(TestSession).delete(); db.commit()
    return {"message": "All results cleared"}


@router.get("/report/{session_id}/pdf")
def download_result_pdf(
    session_id: int,
    user_name: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    session = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.score is None:
        raise HTTPException(status_code=400, detail="Session is not finished yet")
    if session.user_name.strip().lower() != user_name.strip().lower():
        raise HTTPException(status_code=403, detail="This report is not available for this user")

    questions = get_questions_by_test_number(db, session.test_number or 1)
    pdf_bytes, _mistakes = build_test_report_pdf(session, questions)
    pdf_stream = io.BytesIO(pdf_bytes)
    safe_name = session.user_name.replace(" ", "_")
    filename = f"Testbericht_{(get_test_label(session.test_number or 1, db)).replace(' ', '_')}_{safe_name}_{session.id}.pdf"
    return StreamingResponse(
        pdf_stream,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/history")
def get_student_history(
    name: str = Query(..., min_length=1, max_length=100),
    contact: str = Query(..., min_length=1, max_length=150),
    db: Session = Depends(get_db),
):
    """
    Return all finished sessions for a student identified by name + email or phone.
    contact can be an email address or a phone number.
    """
    name_clean = name.strip()
    contact_clean = contact.strip()

    q = (
        db.query(TestSession)
        .filter(
            TestSession.score.isnot(None),
            TestSession.user_name.ilike(name_clean),
            or_(
                TestSession.user_email.ilike(contact_clean),
                TestSession.user_phone.ilike(contact_clean),
            ),
        )
        .order_by(desc(TestSession.finished_at))
        .limit(50)
    )

    sessions = q.all()
    if not sessions:
        raise HTTPException(status_code=404, detail="Keine Testergebnisse gefunden.")

    result = []
    for s in sessions:
        teil5 = get_derived_teil5_score(s)
        result.append({
            "id": s.id,
            "test_number": s.test_number or 1,
            "test_label": get_test_label(s.test_number or 1, db),
            "finished_at": s.finished_at.isoformat() if s.finished_at else None,
            "duration_seconds": s.duration_seconds,
            "score": s.score,
            "total_questions": s.total_questions,
            "percentage": s.percentage,
            "passed": s.passed,
            "teil1_score": s.teil1_score,
            "teil2_score": s.teil2_score,
            "teil3_score": s.teil3_score,
            "teil4_score": s.teil4_score or 0,
            "teil5_score": teil5,
            "hoeren_score": s.hoeren_score,
            "self_intro_feedback_text": s.self_intro_feedback_text or "",
            "image_description_feedback_text": s.image_description_feedback_text or "",
        })

    return {"user_name": sessions[0].user_name, "total": len(result), "sessions": result}

