from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.database import get_db
from models.questions_data import get_all_questions
from services.question_resolver import get_available_tests, get_questions_by_test_number

router = APIRouter()

@router.get("/")
def list_tests(db: Session = Depends(get_db)):
    return {
        "available_tests": get_available_tests(db)
    }

@router.get("/test/{test_number}")
def get_test(test_number: int, db: Session = Depends(get_db)):
    qs = get_questions_by_test_number(db, test_number)
    if not qs:
        raise HTTPException(status_code=404, detail="Test not found")
    safe = [{k: v for k, v in q.items() if k not in ("correct","explanation")} for q in qs]
    return {"test_number": test_number, "total": len(safe), "questions": safe}

@router.get("/test/{test_number}/with-answers")
def get_test_with_answers(test_number: int, db: Session = Depends(get_db)):
    qs = get_questions_by_test_number(db, test_number)
    if not qs:
        raise HTTPException(status_code=404, detail="Test not found")
    return {"test_number": test_number, "total": len(qs), "questions": qs}

@router.get("/test/{test_number}/teil/{teil_number}")
def get_teil(test_number: int, teil_number: int, db: Session = Depends(get_db)):
    if teil_number not in [1, 2, 3, 4]:
        raise HTTPException(status_code=404, detail="Teil must be 1, 2, 3 or 4.")
    questions = get_questions_by_test_number(db, test_number)
    if not questions:
        raise HTTPException(status_code=404, detail="Test not found")
    qs = [q for q in questions if q["teil"] == teil_number]
    safe = [{k: v for k, v in q.items() if k not in ("correct","explanation")} for q in qs]
    return {"test_number": test_number, "teil": teil_number, "total": len(safe), "questions": safe}
