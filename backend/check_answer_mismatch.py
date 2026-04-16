#!/usr/bin/env python3
import json
from sqlalchemy import create_engine, text

url = 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1'
engine = create_engine(url, pool_pre_ping=True)

with engine.begin() as conn:
    row = conn.execute(text('SELECT id, user_name, test_number, answers_json FROM test_sessions WHERE LOWER(user_name)=:name ORDER BY id DESC LIMIT 1'), 
                      {'name': 'alex'}).mappings().first()
    
    if row:
        print(f"Session ID: {row['id']}")
        print(f"Test Number: {row['test_number']}")
        
        answers = row['answers_json']
        if isinstance(answers, str):
            answers = json.loads(answers)
        
        # Extract numeric keys (question IDs)
        q_ids = []
        for key in answers:
            if key and not key.startswith('__'):
                try:
                    q_ids.append(int(key))
                except:
                    pass
        
        if q_ids:
            q_ids.sort()
            print(f"\nAnswer question IDs (sorted):")
            print(f"  First 10: {q_ids[:10]}")
            print(f"  Last 10: {q_ids[-10:]}")
            print(f"  Min: {min(q_ids)}, Max: {max(q_ids)}")
            
            # Infer which test these answers belong to
            min_id = min(q_ids)
            test_num = min_id // 100
            print(f"\nInferred test number from question IDs: {test_num}")
            print(f"Actual test_number in DB: {row['test_number']}")
            
            if test_num != row['test_number']:
                print(f"\n⚠️  MISMATCH! Answers are from test {test_num} but session says test {row['test_number']}")

engine.dispose()
