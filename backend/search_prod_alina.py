import sys
import os
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text
import json

# Production DB URL from sync_production.py
prod_url = 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1'

def search_production():
    print(f"Connecting to production database...")
    engine = create_engine(prod_url)
    
    try:
        with engine.connect() as conn:
            # 1. List latest 10 sessions
            print("\nListing last 10 sessions in PRODUCTION:")
            result = conn.execute(text("SELECT id, user_name, finished_at, score FROM test_sessions ORDER BY id DESC LIMIT 10"))
            rows = result.fetchall()
            if rows:
                for row in rows:
                    print(f"ID: {row.id}, Name: {row.user_name}, Finished: {row.finished_at}, Score: {row.score}")
            else:
                print("No sessions found.")

            # 2. Search for "Alina"
            print("\nSearching for 'Alina' in PRODUCTION (case-insensitive):")
            result = conn.execute(text("SELECT id, user_name, finished_at, score FROM test_sessions WHERE LOWER(user_name) LIKE :name"), {"name": "%alina%"})
            rows = result.fetchall()
            if rows:
                for row in rows:
                    print(f"ID: {row.id}, Name: {row.user_name}, Finished: {row.finished_at}, Score: {row.score}")
            else:
                print("No sessions found for 'Alina'.")

            # 3. Search for recent sessions (last 2 days)
            print("\nSearching for sessions finished in last 2 days in PRODUCTION:")
            yesterday = datetime.now() - timedelta(days=2)
            result = conn.execute(text("SELECT id, user_name, finished_at, score FROM test_sessions WHERE finished_at >= :since ORDER BY finished_at DESC"), {"since": yesterday})
            rows = result.fetchall()
            if rows:
                for row in rows:
                    print(f"ID: {row.id}, Name: {row.user_name}, Finished: {row.finished_at}, Score: {row.score}")
            else:
                print("No recent sessions found.")

    except Exception as e:
        print(f"Error connecting to production: {e}")
    finally:
        engine.dispose()

if __name__ == "__main__":
    search_production()
