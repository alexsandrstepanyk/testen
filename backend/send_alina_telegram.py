
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Add the project root to path to import backend modules correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from backend.models.models import TestSession
from backend.services.report_pdf import build_test_report_pdf
from backend.services.telegram import send_pdf_document

# Database setup
DB_URL = "sqlite:///test_results.db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def send_alina_results():
    db = SessionLocal()
    try:
        # Search for Alina in local DB (synced from prod manually or via sync script)
        # Based on previous search, Alina has ID 90 and 93 in prod.
        # Assuming we want the latest or highest score. Let's try to find by name.
        sessions = db.query(TestSession).filter(TestSession.user_name.contains("Alina")).filter(TestSession.finished_at != None).all()
        
        if not sessions:
            print("No finished sessions found for Alina in local DB.")
            return

        # Sort by finished_at descending to get the latest
        sessions.sort(key=lambda s: s.finished_at, reverse=True)
        session = sessions[0]

        print(f"Generating PDF for session ID: {session.id}, User: {session.user_name}, Score: {session.score}")

        # Build PDF
        pdf_bytes = build_test_report_pdf(session)
        
        filename = f"Result_Report_{session.user_name.replace(' ', '_')}_{session.id}.pdf"
        caption = (
            f"🎯 Результати тесту: {session.user_name}\n"
            f"📊 Бали: {session.score}/{session.total_questions or 55}\n"
            f"📈 Відсоток: {session.percentage}%\n"
            f"✅ Статус: {'Pass' if session.passed else 'Fail'}"
        )

        # Send to Telegram
        success = send_pdf_document(pdf_bytes, filename, caption)
        if success:
            print("✅ Результати Аліни успішно надіслано в Telegram!")
        else:
            print("❌ Помилка при відправці в Telegram. Перевірте TELEGRAM_BOT_TOKEN.")

    finally:
        db.close()

if __name__ == "__main__":
    if not os.getenv("TELEGRAM_BOT_TOKEN"):
        print("Error: TELEGRAM_BOT_TOKEN environment variable is not set.")
        # Try to read from .env if it exists
        try:
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("TELEGRAM_BOT_TOKEN="):
                        os.environ["TELEGRAM_BOT_TOKEN"] = line.split("=")[1].strip()
                    if line.startswith("TELEGRAM_CHAT_ID="):
                        os.environ["TELEGRAM_CHAT_ID"] = line.split("=")[1].strip()
        except FileNotFoundError:
            pass

    send_alina_results()
