#!/usr/bin/env python3
import os
import json
from sqlalchemy import create_engine, text

# Get DB URL - already set in environment from previous commands
url = 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1'
engine = create_engine(url, pool_pre_ping=True)

with engine.begin() as conn:
    # Get Alex's session
    row = conn.execute(text('SELECT id, user_name, test_number, score, total_questions, answers_json FROM test_sessions WHERE LOWER(user_name)=:name ORDER BY id DESC LIMIT 1'), 
                      {'name': 'alex'}).mappings().first()
    
    if row:
        print("=== Alex's Session ===")
        print(f"Session ID: {row['id']}")
        print(f"User: {row['user_name']}")
        print(f"Test Number: {row['test_number']}")
        print(f"Score: {row['score']}")
        print(f"Total Questions: {row['total_questions']}")
        
        # Parse answers JSON
        answers = row['answers_json']
        if isinstance(answers, str):
            answers = json.loads(answers)
        
        print(f"\nAnswers JSON type: {type(answers)}")
        if answers:
            keys = list(answers.keys())[:10]
            print(f"First 10 keys: {keys}")
            print(f"Total keys: {len(answers)}")
        
        # Now check which questions exist for test_number=3
        print("\n=== Checking questions for test_number=3 ===")
        q_rows = conn.execute(text('SELECT id FROM questions WHERE test_number=:tn'), 
                             {'tn': 3}).scalars().all()
        print(f"Questions count for test_number=3: {len(q_rows)}")
        if q_rows:
            print(f"First 5 question IDs: {q_rows[:5]}")
    else:
        print("No session found for user 'alex'")

engine.dispose()
