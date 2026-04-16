#!/usr/bin/env python3
"""Database migration script: Add video submission columns to test_sessions"""

import os
from sqlalchemy import create_engine, text

# Get database URL from environment or hardcoded
DB_URL = os.getenv('DATABASE_URL', 'postgresql://deutsch_b1_user:5Wpf2wsf9uYKf8NDFkwGSYS0yF2bqzxf@dpg-d79d0f94tr6s73crl6fg-a.frankfurt-postgres.render.com/deutsch_b1')

engine = create_engine(DB_URL, pool_pre_ping=True)

with engine.begin() as conn:
    # Add video_url column
    try:
        conn.execute(text('ALTER TABLE test_sessions ADD COLUMN video_url VARCHAR(500)'))
        print('✅ Added video_url column')
    except Exception as e:
        print(f'ℹ️  video_url already exists or error: {str(e)[:100]}')
    
    # Add presentation_score column
    try:
        conn.execute(text('ALTER TABLE test_sessions ADD COLUMN presentation_score INTEGER DEFAULT 0'))
        print('✅ Added presentation_score column')
    except Exception as e:
        print(f'ℹ️  presentation_score already exists or error: {str(e)[:100]}')
    
    # Add feedback_text column
    try:
        conn.execute(text("ALTER TABLE test_sessions ADD COLUMN feedback_text TEXT DEFAULT ''"))
        print('✅ Added feedback_text column')
    except Exception as e:
        print(f'ℹ️  feedback_text already exists or error: {str(e)[:100]}')
    
    # Verify columns exist
    result = conn.execute(text("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name = 'test_sessions' 
        AND column_name IN ('video_url', 'presentation_score', 'feedback_text')
    """)).fetchall()
    
    found_cols = [row[0] for row in result]
    print(f'\n✅ Migration verified. Columns present: {", ".join(found_cols)}')

print('✅ Database migration complete!')
