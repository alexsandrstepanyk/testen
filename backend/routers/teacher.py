from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_
from models.database import get_db
from models.models import TestSession
from services.question_resolver import get_questions_by_test_number, get_test_label
from datetime import datetime, date
from typing import Optional, List, Dict, Any
import json
import secrets

security = HTTPBasic()


def require_teacher_auth(credentials: HTTPBasicCredentials = Depends(security)):
    valid_username = secrets.compare_digest(credentials.username, "admin")
    valid_password = secrets.compare_digest(credentials.password, "admin")
    if not (valid_username and valid_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid teacher credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


router = APIRouter(dependencies=[Depends(require_teacher_auth)])


def get_derived_teil5_score(session: TestSession) -> int:
    answers = session.answers_json or {}
    if isinstance(answers, dict):
        meta_score = answers.get("__teil5_score")
        if isinstance(meta_score, int):
            return meta_score
        if isinstance(meta_score, str) and meta_score.isdigit():
            return int(meta_score)
    return max(0, (session.score or 0) - sum([
        session.teil1_score or 0,
        session.teil2_score or 0,
        session.teil3_score or 0,
        session.teil4_score or 0,
    ]))


def is_answer_correct(question: Dict[str, Any], user_answer: Any) -> bool:
    if question.get("type") == "rf":
        return (str(user_answer).lower() == "true" and bool(question.get("correct"))) or \
               (str(user_answer).lower() == "false" and not bool(question.get("correct")))

    answer_map = {"a": 0, "b": 1, "c": 2}
    user_text = str(user_answer).lower()
    if user_text.isdigit():
        user_idx = int(user_text)
    else:
        user_idx = answer_map.get(user_text, -1)
    return user_idx == question.get("correct")


class TeacherSessionOut:
    """Extended session data for teacher view"""
    def __init__(self, session: TestSession, mistakes: List[Dict[str, Any]]):
        self.id = session.id
        self.user_name = session.user_name
        self.test_number = session.test_number or 1
        self.started_at = session.started_at.isoformat() if session.started_at else None
        self.finished_at = session.finished_at.isoformat() if session.finished_at else None
        self.duration_seconds = session.duration_seconds
        self.score = session.score
        self.total_questions = session.total_questions
        self.percentage = session.percentage
        self.passed = session.passed
        self.teil1_score = session.teil1_score
        self.teil2_score = session.teil2_score
        self.teil3_score = session.teil3_score
        self.teil4_score = session.teil4_score or 0
        self.teil5_score = get_derived_teil5_score(session)
        self.mistakes = mistakes
        self.answers_json = session.answers_json or {}


@router.get("/sessions")
def get_all_sessions(
    limit: int = Query(default=100, le=500),
    test_number: Optional[int] = Query(default=None, ge=1, le=5),
    passed: Optional[bool] = Query(default=None),
    user_name: Optional[str] = Query(default=None),
    db: Session = Depends(get_db)
):
    """Get all test sessions with optional filters"""
    q = db.query(TestSession).filter(TestSession.score.isnot(None))
    
    if test_number is not None:
        q = q.filter(TestSession.test_number == test_number)
    if passed is not None:
        q = q.filter(TestSession.passed == passed)
    if user_name:
        q = q.filter(TestSession.user_name.ilike(f"%{user_name}%"))
    
    sessions = q.order_by(desc(TestSession.finished_at)).limit(limit).all()
    
    return {
        "total": len(sessions),
        "sessions": [
            {
                "id": s.id,
                "user_name": s.user_name,
                "test_number": s.test_number or 1,
                "test_label": get_test_label(s.test_number or 1, db),
                "started_at": s.started_at.isoformat() if s.started_at else None,
                "finished_at": s.finished_at.isoformat() if s.finished_at else None,
                "duration_seconds": s.duration_seconds,
                "score": s.score,
                "total_questions": s.total_questions,
                "percentage": s.percentage,
                "passed": s.passed,
                "teil1_score": s.teil1_score,
                "teil2_score": s.teil2_score,
                "teil3_score": s.teil3_score,
                "teil4_score": s.teil4_score or 0,
                "teil5_score": get_derived_teil5_score(s)
            }
            for s in sessions
        ]
    }


@router.get("/sessions/{session_id}/details")
def get_session_details(session_id: int, db: Session = Depends(get_db)):
    """Get detailed session info with mistakes analysis"""
    try:
        session = db.query(TestSession).filter(TestSession.id == session_id).first()
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        if not session.answers_json:
            session_out = TeacherSessionOut(session, [])
            return jsonable_encoder(session_out.__dict__)
        
        # Parse JSON string to dict
        try:
            user_answers = json.loads(session.answers_json) if isinstance(session.answers_json, str) else session.answers_json
        except Exception as e:
            print(f"JSON parse error: {e}")
            user_answers = {}
        
        if not user_answers:
            session_out = TeacherSessionOut(session, [])
            return jsonable_encoder(session_out.__dict__)
        
        # Get questions for this test
        questions = get_questions_by_test_number(db, session.test_number or 1)
        questions_by_id = {q["id"]: q for q in questions}
        
        # Analyze mistakes
        mistakes = []
        
        for q_id, user_answer in user_answers.items():
            # Skip 'schreiben' key
            if q_id == 'schreiben' or str(q_id).startswith('__'):
                continue
                
            try:
                q_id_int = int(q_id) if isinstance(q_id, str) else q_id
            except Exception:
                continue
            question = questions_by_id.get(q_id_int)
            if not question:
                continue
            
            correct_answer = question.get("correct")
            is_correct = is_answer_correct(question, user_answer)
            
            if not is_correct:
                mistake_info = {
                    "question_id": q_id_int,
                    "question_text": question.get("question", ""),
                    "context": question.get("context", ""),
                    "teil": question.get("teil", 0),
                    "user_answer": str(user_answer),
                    "correct_answer": correct_answer,
                    "correct_letter": ["a", "b", "c"][correct_answer] if isinstance(correct_answer, int) else correct_answer,
                    "explanation": question.get("explanation", ""),
                    "options": question.get("options", [])
                }
                mistakes.append(mistake_info)
        
        session_out = TeacherSessionOut(session, mistakes)
        return jsonable_encoder(session_out.__dict__)
    except Exception as e:
        print(f"Error in get_session_details: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats/overview")
def get_stats_overview(
    test_number: Optional[int] = Query(default=None, ge=1, le=5),
    db: Session = Depends(get_db)
):
    """Get overall statistics for teacher dashboard"""
    try:
        q = db.query(TestSession).filter(TestSession.score.isnot(None))
        if test_number is not None:
            q = q.filter(TestSession.test_number == test_number)

        all_sessions = q.all()
        total = len(all_sessions)
        
        if total == 0:
            return {
                "total_attempts": 0,
                "total_passed": 0,
                "pass_rate": 0,
                "avg_score": 0,
                "avg_percentage": 0,
                "avg_duration_seconds": 0,
                "by_test": [],
                "top_students": []
            }

        passed = len([s for s in all_sessions if s.passed])
        
        # Calculate averages
        scores = [s.score for s in all_sessions if s.score is not None]
        percentages = [s.percentage for s in all_sessions if s.percentage is not None]
        durations = [s.duration_seconds for s in all_sessions if s.duration_seconds is not None]
        
        avg_s = sum(scores) / len(scores) if scores else 0
        avg_pct = sum(percentages) / len(percentages) if percentages else 0
        avg_d = sum(durations) / len(durations) if durations else 0

        # Stats by test number
        by_test = []
        for t in range(1, 6):
            t_sessions = [s for s in all_sessions if s.test_number == t]
            t_total = len(t_sessions)
            if t_total > 0:
                t_passed = len([s for s in t_sessions if s.passed])
                t_scores = [s.score for s in t_sessions if s.score is not None]
                t_avg = sum(t_scores) / len(t_scores) if t_scores else 0
                by_test.append({
                    "test_number": t,
                    "attempts": t_total,
                    "passed": t_passed,
                    "pass_rate": round(t_passed / t_total * 100, 1),
                    "avg_score": round(t_avg, 1)
                })

        # Top students (sorted by percentage desc, duration asc)
        sorted_sessions = sorted(all_sessions, key=lambda s: (-(s.percentage or 0), s.duration_seconds or 999999))
        top_students = [
            {
                "user_name": s.user_name,
                "test_number": s.test_number or 1,
                "percentage": s.percentage,
                "score": s.score,
                "duration_seconds": s.duration_seconds,
                "passed": s.passed
            }
            for s in sorted_sessions[:10]
        ]

        return {
            "total_attempts": total,
            "total_passed": passed,
            "pass_rate": round(passed / total * 100, 1),
            "avg_score": round(avg_s, 1),
            "avg_percentage": round(avg_pct, 1),
            "avg_duration_seconds": int(avg_d) if avg_d else 0,
            "by_test": by_test,
            "top_students": top_students
        }
    except Exception as e:
        print(f"Error in get_stats_overview: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/students")
def get_students_list(
    test_number: Optional[int] = Query(default=None, ge=1, le=5),
    db: Session = Depends(get_db)
):
    """Get list of all students with their best scores"""
    q = db.query(
        TestSession.user_name,
        TestSession.test_number,
        TestSession.score,
        TestSession.percentage,
        TestSession.passed,
        TestSession.finished_at
    ).filter(TestSession.score.isnot(None))
    
    if test_number is not None:
        q = q.filter(TestSession.test_number == test_number)
    
    results = q.all()
    
    # Group by student name and get best result
    students = {}
    for r in results:
        name = r[0]
        if name not in students or r[3] > students[name]["best_percentage"]:
            students[name] = {
                "user_name": name,
                "best_score": r[2],
                "best_percentage": r[3],
                "best_passed": r[4],
                "last_attempt": r[5].isoformat() if r[5] else None,
                "test_number": r[1] or 1
            }
    
    return {
        "total_students": len(students),
        "students": sorted(
            list(students.values()),
            key=lambda x: x["best_percentage"] or 0,
            reverse=True
        )
    }
