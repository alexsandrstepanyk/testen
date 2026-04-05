from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from models.database import get_db
from models.models import TestSession

router = APIRouter()

@router.get("/leaderboard")
def get_leaderboard(limit: int = Query(default=50, le=200),
                    test_number: int = Query(default=0),
                    db: Session = Depends(get_db)):
    q = db.query(TestSession).filter(TestSession.score.isnot(None))
    if test_number in range(1, 6):
        q = q.filter(TestSession.test_number == test_number)
    sessions = q.order_by(desc(TestSession.score), TestSession.duration_seconds).limit(limit).all()
    return {"leaderboard": [
        {"rank": i+1, "user_name": s.user_name, "test_number": s.test_number or 1,
         "score": s.score, "total_questions": s.total_questions,
         "percentage": s.percentage, "duration_seconds": s.duration_seconds,
         "passed": s.passed, "teil1_score": s.teil1_score,
         "teil2_score": s.teil2_score, "teil3_score": s.teil3_score,
         "teil4_score": s.teil4_score or 0,
         "finished_at": s.finished_at.isoformat() if s.finished_at else None}
        for i, s in enumerate(sessions)
    ], "total_entries": len(sessions)}

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(TestSession).filter(TestSession.score.isnot(None)).count()
    if not total:
        return {"total_attempts":0,"pass_rate":0,"avg_score":0,"avg_duration_seconds":0}
    passed = db.query(TestSession).filter(TestSession.passed==True).count()
    avg_s = db.query(func.avg(TestSession.score)).filter(TestSession.score.isnot(None)).scalar()
    avg_d = db.query(func.avg(TestSession.duration_seconds)).filter(TestSession.duration_seconds.isnot(None)).scalar()
    return {"total_attempts":total,"total_passed":passed,
            "pass_rate":round(passed/total*100,1),
            "avg_score":round(avg_s,1) if avg_s else 0,
            "avg_duration_seconds":int(avg_d) if avg_d else 0}

@router.delete("/leaderboard/clear")
def clear(db: Session = Depends(get_db)):
    db.query(TestSession).delete(); db.commit()
    return {"message": "All results cleared"}
