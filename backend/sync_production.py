#!/usr/bin/env python3
"""
Синхронізація даних на продакшн
"""
import sys
sys.path.insert(0, '/Users/os/Downloads/deutsch-b1-app 3/backend')

from sqlalchemy import create_engine, text
import json

# Production DB URL
prod_url = 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1'
prod_engine = create_engine(prod_url, pool_pre_ping=True)

print("=== Додавання тестових даних на продакшн ===\n")

with prod_engine.begin() as conn:
    # Check if table exists
    try:
        result = conn.execute(text("SELECT COUNT(*) FROM test_sessions"))
        count = result.scalar()
        print(f"Сесій у БД: {count}")
        
        if count == 0:
            print("БД пуста. Додаю тестові дані...")
            
            # Insert test session for Alex
            conn.execute(text("""
                INSERT INTO test_sessions 
                (user_name, test_number, score, total_questions, percentage, passed, duration_seconds, teil1_score, teil2_score, teil3_score, teil4_score, answers_json)
                VALUES
                ('Alex', 2, 50, 55, 76.9, true, 1333, 16, 7, 10, 7, :answers)
            """), {
                "answers": json.dumps({
                    "201": 1, "202": 0, "203": 1, "204": 0, "205": 1,
                    "206": 0, "207": 1, "208": 0, "209": 1, "210": 0,
                    "schreiben": "Das ist ein Brief von Alex."
                })
            })
            
            print("✅ Дані додані!")
            
            # Verify
            result = conn.execute(text("SELECT COUNT(*) FROM test_sessions"))
            new_count = result.scalar()
            print(f"Тепер в БД: {new_count} сесій")
        
    except Exception as e:
        print(f"Помилка: {e}")

prod_engine.dispose()
