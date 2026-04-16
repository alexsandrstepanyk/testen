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
from pathlib import Path
import os

router = APIRouter()

FRONTEND_PATH = Path(__file__).resolve().parents[2] / "frontend"
LOCAL_VIDEO_DIR = FRONTEND_PATH / "uploads" / "presentation_videos"

VIDEO_KIND_LABELS = {
    "self-intro": "Selbstvorstellung",
    "image-description": "Bildbeschreibung",
}


def resolve_video_field(video_kind: str) -> str:
    if video_kind == "self-intro":
        return "self_intro_video_url"
    if video_kind == "image-description":
        return "image_description_video_url"
    raise HTTPException(status_code=400, detail="video_kind must be 'self-intro' or 'image-description'")


def store_video_for_kind(session: TestSession, video_kind: str, file_id: str) -> None:
    field_name = resolve_video_field(video_kind)
    setattr(session, field_name, file_id)
    if video_kind == "image-description":
        session.video_url = file_id


def save_video_locally(session: TestSession, video_kind: str, video_bytes: bytes, filename: str) -> str:
    safe_name = filename.replace("/", "_").replace("\\", "_")
    suffix = Path(safe_name).suffix or ".webm"
    kind_folder = "self_intro" if video_kind == "self-intro" else "image_description"
    target_dir = LOCAL_VIDEO_DIR / kind_folder
    target_dir.mkdir(parents=True, exist_ok=True)
    target_name = f"session_{session.id}_{session.user_name.replace(' ', '_')}{suffix}"
    target_path = target_dir / target_name
    target_path.write_bytes(video_bytes)
    return f"/static/uploads/presentation_videos/{kind_folder}/{target_name}"


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

def upload_video_for_kind(session_id: int, video_kind: str, video: UploadFile, db: Session) -> dict:
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
        prefix = "self_intro" if video_kind == "self-intro" else "image_description"
        label = VIDEO_KIND_LABELS[video_kind]
        filename = f"{prefix}_{session.user_name.replace(' ', '_')}_{session_id}_{safe_name}"
        caption = f"{label} von {session.user_name}\nSession ID: {session_id}"
        content_type = (video.content_type or "video/mp4").strip()
        
        file_id = None
        upload_mode = "telegram"

        if is_enabled():
            file_id = send_video(video_bytes, filename, caption, content_type=content_type)

        if not file_id:
            file_id = save_video_locally(session, video_kind, video_bytes, filename)
            upload_mode = "local"
        
        store_video_for_kind(session, video_kind, file_id)
        db.commit()
        db.refresh(session)
        
        return {
            "status": "ok",
            "session_id": session.id,
            "video_kind": video_kind,
            "file_id": file_id,
            "storage": upload_mode,
            "message": "Video uploaded successfully"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)[:100]}")


@router.post("/{session_id}/upload-video")
def upload_presentation_video(session_id: int, video: UploadFile = File(...), db: Session = Depends(get_db)):
    """Legacy upload endpoint kept for compatibility."""
    return upload_video_for_kind(session_id, "image-description", video, db)


@router.post("/{session_id}/upload-video/{video_kind}")
def upload_presentation_video_by_kind(
    session_id: int,
    video_kind: str,
    video: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload a speaking video for a specific part and save file_id to session."""
    return upload_video_for_kind(session_id, video_kind, video, db)
