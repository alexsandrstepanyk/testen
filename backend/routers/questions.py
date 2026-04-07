from fastapi import APIRouter, HTTPException
from models.questions_data import ALL_TESTS, get_questions_for_test, get_all_questions

router = APIRouter()

@router.get("/")
def list_tests():
    return {
        "available_tests": [
            {"test_number": t, "total_questions": len(qs),
             "teil1": len([q for q in qs if q["teil"]==1]),
             "teil2": len([q for q in qs if q["teil"]==2]),
             "teil3": len([q for q in qs if q["teil"]==3]),
             "teil4": len([q for q in qs if q["teil"]==4])}
            for t, qs in ALL_TESTS.items()
        ]
    }

@router.get("/test/{test_number}")
def get_test(test_number: int):
    if test_number not in range(1, 6):
        raise HTTPException(status_code=404, detail="Test not found. Use 1-5.")
    qs = get_questions_for_test(test_number)
    safe = [{k: v for k, v in q.items() if k not in ("correct","explanation")} for q in qs]
    return {"test_number": test_number, "total": len(safe), "questions": safe}

@router.get("/test/{test_number}/with-answers")
def get_test_with_answers(test_number: int):
    if test_number not in range(1, 6):
        raise HTTPException(status_code=404, detail="Test not found. Use 1-5.")
    qs = get_questions_for_test(test_number)
    return {"test_number": test_number, "total": len(qs), "questions": qs}

@router.get("/test/{test_number}/teil/{teil_number}")
def get_teil(test_number: int, teil_number: int):
    if test_number not in range(1, 6):
        raise HTTPException(status_code=404, detail="Test not found.")
    if teil_number not in [1, 2, 3, 4]:
        raise HTTPException(status_code=404, detail="Teil must be 1, 2, 3 or 4.")
    qs = [q for q in get_questions_for_test(test_number) if q["teil"] == teil_number]
    safe = [{k: v for k, v in q.items() if k not in ("correct","explanation")} for q in qs]
    return {"test_number": test_number, "teil": teil_number, "total": len(safe), "questions": safe}
