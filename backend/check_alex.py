#!/usr/bin/env python3
import os, sys, json, traceback
sys.path.insert(0, '.')
from sqlalchemy import create_engine, text
from models.database import get_db
from models.models import TestSession
from models.questions_data import get_questions_for_test

url = os.environ.get('DATABASE_URL', 'sqlite:///test_results.db')
eng = create_engine(url, pool_pre_ping=True)

with eng.connect() as raw_conn:
    row = raw_conn.execute(text(
        "SELECT id, test_number, answers_json FROM test_sessions WHERE lower(user_name)='alex' ORDER BY id DESC LIMIT 1"
    )).mappings().first()
    print('Session id:', row['id'], 'test_number:', row['test_number'])
    aj = row['answers_json']
    print('answers_json type:', type(aj).__name__)
    print('all keys:', list(aj.keys()) if isinstance(aj, dict) else 'N/A')

# Now simulate what get_session_details does using ORM
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=eng)
db = Session()

try:
    session = db.query(TestSession).filter(TestSession.id == row['id']).first()
    print('\nORM session loaded OK')
    print('test_number:', session.test_number)
    print('finished_at:', session.finished_at)
    
    user_answers = json.loads(session.answers_json) if isinstance(session.answers_json, str) else session.answers_json
    print('user_answers keys:', list(user_answers.keys())[:5] if user_answers else '(empty)')
    
    questions = get_questions_for_test(session.test_number or 1)
    questions_by_id = {q['id']: q for q in questions}
    print('questions loaded:', len(questions_by_id), 'IDs like', list(questions_by_id.keys())[:3])
    
    mistakes = []
    for q_id, user_answer in user_answers.items():
        if q_id == 'schreiben' or str(q_id).startswith('__'):
            continue
        try:
            q_id_int = int(q_id) if isinstance(q_id, str) else q_id
        except Exception:
            continue
        question = questions_by_id.get(q_id_int)
        if not question:
            continue
        mistakes.append({'q_id': q_id_int, 'val': user_answer})
    
    print('mistakes found:', len(mistakes))
    
    # Serialize to JSON to check for issues
    import fastapi.encoders as enc
    result = {
        'id': session.id,
        'user_name': session.user_name,
        'test_number': session.test_number,
        'score': session.score,
        'percentage': session.percentage,
        'passed': session.passed,
        'teil1_score': session.teil1_score,
        'teil2_score': session.teil2_score,
        'teil3_score': session.teil3_score,
        'teil4_score': session.teil4_score,
        'finished_at': session.finished_at.isoformat() if session.finished_at else None,
        'answers_json': user_answers,
        'mistakes': mistakes
    }
    print('\nJSON serialization test...')
    j = json.dumps(result, default=str)
    print('OK, JSON length:', len(j))
    
except Exception as e:
    print('ERROR:', e)
    traceback.print_exc()
finally:
    db.close()

