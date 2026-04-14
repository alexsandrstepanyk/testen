from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy import inspect, text
import os

from routers import questions, sessions, results, schreiben, teacher, course_builder
from models.database import engine, Base

Base.metadata.create_all(bind=engine)


def ensure_schema_updates() -> None:
    inspector = inspect(engine)
    columns = {column["name"] for column in inspector.get_columns("custom_questions")}
    if "audio_url" in columns:
        return

    with engine.begin() as connection:
        connection.execute(text("ALTER TABLE custom_questions ADD COLUMN audio_url TEXT"))


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
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/", include_in_schema=False)
    def serve_frontend():
        return FileResponse(os.path.join(frontend_path, "index.html"))

    @app.get("/robots.txt", include_in_schema=False)
    def serve_robots():
        return FileResponse(os.path.join(frontend_path, "robots.txt"), media_type="text/plain")

    @app.get("/sitemap.xml", include_in_schema=False)
    def serve_sitemap():
        return FileResponse(os.path.join(frontend_path, "sitemap.xml"), media_type="application/xml")

    @app.get("/impressum", include_in_schema=False)
    def serve_impressum():
        return FileResponse(os.path.join(frontend_path, "impressum.html"))

    @app.get("/datenschutz", include_in_schema=False)
    def serve_datenschutz():
        return FileResponse(os.path.join(frontend_path, "datenschutz.html"))

    @app.get("/teacher", include_in_schema=False)
    def serve_teacher(_auth: str = Depends(teacher.require_teacher_auth)):
        return FileResponse(os.path.join(frontend_path, "teacher.html"))

    @app.get("/leaderboard", include_in_schema=False)
    def serve_leaderboard():
        return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/api/health")
def health():
    return {"status": "ok", "version": "2.0.0", "message": "Deutsch B1 API läuft 🇩🇪"}
