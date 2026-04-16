#!/usr/bin/env python3
import json
from sqlalchemy import create_engine, text

url = 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1'
engine = create_engine(url, pool_pre_ping=True)

with engine.begin() as conn:
    # Fix Alex's test_number to match the answers
    conn.execute(text('UPDATE test_sessions SET test_number=2 WHERE LOWER(user_name)=:name'), 
                {'name': 'alex'})
    
    # Verify the fix
    row = conn.execute(text('SELECT id, user_name, test_number FROM test_sessions WHERE LOWER(user_name)=:name ORDER BY id DESC LIMIT 1'), 
                      {'name': 'alex'}).mappings().first()
    
    if row:
        print(f"✅ Fixed!")
        print(f"Session ID: {row['id']}")
        print(f"User: {row['user_name']}")
        print(f"Test Number: {row['test_number']} (corrected to match answer question IDs 201-255)")

engine.dispose()
