import sys
import os
from datetime import datetime, timedelta
from sqlalchemy import or_, func

# Add the current directory to sys.path so we can import models
sys.path.append(os.path.join(os.getcwd()))

from models.database import SessionLocal
from models.models import TestSession

def search_sessions():
    db = SessionLocal()
    try:
        # Search for ALL sessions to see what's in the database
        print("Listing all sessions in the database (last 10)...")
        all_sessions = db.query(TestSession).order_by(TestSession.finished_at.desc()).limit(10).all()
        
        if all_sessions:
            print(f"Found {len(all_sessions)} sessions:")
            for s in all_sessions:
                print(f"ID: {s.id}, Name: {s.user_name}, Finished: {s.finished_at}, Score: {s.score}")
        else:
            print("No sessions found in the database.")

        # Search for "Alina" case-insensitive
        print("\nSearching for 'Alina' (case-insensitive)...")
        alina_sessions = db.query(TestSession).filter(
            func.lower(TestSession.user_name).like("%alina%")
        ).all()
        
        if alina_sessions:
            print(f"Found {len(alina_sessions)} sessions for 'Alina':")
            for s in alina_sessions:
                print(f"ID: {s.id}, Name: {s.user_name}, Finished: {s.finished_at}, Score: {s.score}")
        else:
            print("No sessions found for 'Alina'.")

        # Search for sessions finished today or yesterday
        print("\nSearching for sessions finished today or yesterday...")
        yesterday = datetime.now() - timedelta(days=2) # Using 2 days to be safe
        recent_sessions = db.query(TestSession).filter(
            TestSession.finished_at >= yesterday
        ).order_by(TestSession.finished_at.desc()).all()

        if recent_sessions:
            print(f"Found {len(recent_sessions)} recent sessions:")
            for s in recent_sessions:
                print(f"ID: {s.id}, Name: {s.user_name}, Finished: {s.finished_at}, Score: {s.score}")
        else:
            print("No recent sessions found.")

    finally:
        db.close()

if __name__ == "__main__":
    search_sessions()
