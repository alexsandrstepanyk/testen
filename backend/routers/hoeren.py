from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

from models.hoeren_data import get_hoeren_questions

router = APIRouter(tags=["hoeren"])


# ─── Response schemas ────────────────────────────────────────────────────────

class HoerenQuestion(BaseModel):
    id: int
    question: str
    audio_url: str
    options: list[str]
    # correct is intentionally excluded from client response


class HoerenTestResponse(BaseModel):
    test_number: int
    total: int
    questions: list[HoerenQuestion]


class HoerenSubmitRequest(BaseModel):
    test_number: int
    answers: Dict[int, int]  # question_id → chosen option index (0/1/2)


class HoerenSubmitResponse(BaseModel):
    score: int
    total: int
    percent: float
    results: list[dict]  # per-question: id, correct, chosen, is_correct


# ─── Endpoints ───────────────────────────────────────────────────────────────

@router.get("/hoeren/{test_number}", response_model=HoerenTestResponse)
def get_hoeren_test(test_number: int):
    questions = get_hoeren_questions(test_number)
    if not questions:
        raise HTTPException(status_code=404, detail=f"Hören Test {test_number} nicht gefunden")

    return HoerenTestResponse(
        test_number=test_number,
        total=len(questions),
        questions=[
            HoerenQuestion(
                id=q["id"],
                question=q["question"],
                audio_url=q["audio_url"],
                options=q["options"],
            )
            for q in questions
        ],
    )


@router.post("/hoeren/submit", response_model=HoerenSubmitResponse)
def submit_hoeren(payload: HoerenSubmitRequest):
    questions = get_hoeren_questions(payload.test_number)
    if not questions:
        raise HTTPException(status_code=404, detail=f"Hören Test {payload.test_number} nicht gefunden")

    results = []
    score = 0
    for q in questions:
        chosen = payload.answers.get(q["id"])
        is_correct = chosen == q["correct"]
        if is_correct:
            score += 1
        results.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
            "correct": q["correct"],
            "chosen": chosen,
            "is_correct": is_correct,
        })

    total = len(questions)
    percent = round(score / total * 100, 1) if total else 0.0

    return HoerenSubmitResponse(
        score=score,
        total=total,
        percent=percent,
        results=results,
    )
