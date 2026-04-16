from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import HTTPException
from sqlalchemy import inspect, text
import os
from pathlib import Path

from routers import questions, sessions, results, schreiben, teacher, course_builder
from models.database import engine, Base

Base.metadata.create_all(bind=engine)


def ensure_schema_updates() -> None:
    inspector = inspect(engine)
    with engine.begin() as connection:
        custom_question_columns = {column["name"] for column in inspector.get_columns("custom_questions")}
        if "audio_url" not in custom_question_columns:
            connection.execute(text("ALTER TABLE custom_questions ADD COLUMN audio_url TEXT"))

        session_columns = {column["name"] for column in inspector.get_columns("test_sessions")}
        if "video_url" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN video_url TEXT"))
        if "self_intro_video_url" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN self_intro_video_url TEXT"))
        if "image_description_video_url" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN image_description_video_url TEXT"))
        if "presentation_score" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN presentation_score INTEGER DEFAULT 0"))
        if "self_intro_score" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN self_intro_score INTEGER DEFAULT 0"))
        if "image_description_score" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN image_description_score INTEGER DEFAULT 0"))
        if "feedback_text" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN feedback_text TEXT DEFAULT ''"))
        if "self_intro_feedback_text" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN self_intro_feedback_text TEXT DEFAULT ''"))
        if "image_description_feedback_text" not in session_columns:
            connection.execute(text("ALTER TABLE test_sessions ADD COLUMN image_description_feedback_text TEXT DEFAULT ''"))


ensure_schema_updates()

app = FastAPI(
    title="Deutsch B1 Übungstest",
    description="API for German B1 practice tests with letter writing & download",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router,  prefix="/api/questions",  tags=["Questions"])
app.include_router(sessions.router,   prefix="/api/sessions",   tags=["Sessions"])
app.include_router(results.router,    prefix="/api/results",    tags=["Results"])
app.include_router(schreiben.router,  prefix="/api/schreiben",  tags=["Schreiben"])
app.include_router(teacher.router,    prefix="/api/teacher",    tags=["Teacher"])
app.include_router(course_builder.router, prefix="/api/teacher", tags=["Course Builder"])

frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")


def html_response(filename: str) -> FileResponse:
    return FileResponse(
        os.path.join(frontend_path, filename),
        headers={
            "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )


if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/", include_in_schema=False)
    def serve_frontend():
        return html_response("index.html")

    @app.get("/robots.txt", include_in_schema=False)
    def serve_robots():
        return FileResponse(os.path.join(frontend_path, "robots.txt"), media_type="text/plain")

    @app.get("/sitemap.xml", include_in_schema=False)
    def serve_sitemap():
        return FileResponse(os.path.join(frontend_path, "sitemap.xml"), media_type="application/xml")

    @app.get("/impressum", include_in_schema=False)
    def serve_impressum():
        return html_response("impressum.html")

    @app.get("/datenschutz", include_in_schema=False)
    def serve_datenschutz():
        return html_response("datenschutz.html")

    @app.get("/teacher", include_in_schema=False)
    def serve_teacher(_auth: str = Depends(teacher.require_teacher_auth)):
        return html_response("teacher.html")

    @app.get("/leaderboard", include_in_schema=False)
    def serve_leaderboard():
        return html_response("index.html")

@app.get("/api/health")
def health():
    return {"status": "ok", "version": "2.0.0", "message": "Deutsch B1 API läuft 🇩🇪"}


@app.get("/api/presentation/images/{test_number}")
def presentation_images(test_number: int):
    if test_number < 1 or test_number > 5:
        raise HTTPException(status_code=400, detail="test_number must be between 1 and 5")

    folder_map = {
        1: "alltag-grammatik",
        2: "freizeit-reisen",
        3: "arbeit-bildung",
        4: "gesellschaft-technik",
        5: "umwelt-zukunft",
    }
    folder_name = folder_map[test_number]
    folder = Path(frontend_path) / "uploads" / "presentation" / folder_name
    if not folder.exists():
        return {"test_number": test_number, "images": []}

    allowed = {".jpg", ".jpeg", ".png", ".webp"}
    files = sorted(
        [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in allowed],
        key=lambda p: p.name.lower(),
    )

    urls = [f"/static/uploads/presentation/{folder_name}/{p.name}" for p in files]
    return {"test_number": test_number, "folder": folder_name, "images": urls}
