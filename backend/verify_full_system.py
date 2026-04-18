#!/usr/bin/env python3
"""Comprehensive validation for Deutsch B1 tests.

Checks:
1) Data integrity per test (counts, IDs, field types)
2) Answer-key consistency (MC correct index bounds, RF boolean correctness)
3) Scoring consistency for perfect and empty attempts
4) PDF generation validity for each theme (1..5)
5) Basic text quality checks (missing punctuation / empty explanation)
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple

from models.questions_data import get_questions_for_test, SCHREIBEN_AUFGABEN
from services.report_pdf import build_test_report_pdf, build_speaking_report_pdf


@dataclass
class FakeSession:
    id: int
    user_name: str
    test_number: int
    finished_at: datetime
    duration_seconds: int
    score: int
    total_questions: int
    percentage: float
    passed: bool
    answers_json: Dict
    teil1_score: int
    teil2_score: int
    teil3_score: int
    teil4_score: int

@dataclass
class FakeSessionSpeaking:
    id: int
    user_name: str
    user_email: str
    user_phone: str
    finished_at: datetime
    presentation_score: int
    feedback_text: str


def count_by_teil(questions: List[dict]) -> Dict[int, int]:
    out: Dict[int, int] = {}
    for q in questions:
        t = int(q.get("teil", 0))
        out[t] = out.get(t, 0) + 1
    return out


def score_attempt(questions: List[dict], answers: Dict) -> Tuple[int, Dict[int, int]]:
    total = 0
    by_teil = {1: 0, 2: 0, 3: 0, 4: 0}
    for q in questions:
        qid = q["id"]
        ua = answers.get(str(qid), answers.get(qid))
        ok = False
        if q["type"] == "rf":
            if isinstance(ua, bool):
                ok = ua == bool(q["correct"])
            elif ua is not None:
                s = str(ua).strip().lower()
                if s in {"true", "false"}:
                    ok = (s == "true") == bool(q["correct"])
        else:
            if ua is not None:
                try:
                    ok = int(ua) == int(q["correct"])
                except Exception:
                    ok = False
        if ok:
            total += 1
            by_teil[q["teil"]] += 1
    return total, by_teil


def make_perfect_answers(questions: List[dict]) -> Dict[str, str]:
    answers: Dict[str, str] = {}
    for q in questions:
        qid = str(q["id"])
        if q["type"] == "rf":
            answers[qid] = "true" if bool(q["correct"]) else "false"
        else:
            answers[qid] = str(q["correct"])
    return answers


def validate_one_test(test_num: int) -> List[str]:
    errors: List[str] = []
    questions = get_questions_for_test(test_num)

    if len(questions) != 55:
        errors.append(f"T{test_num}: expected 55 questions, got {len(questions)}")

    counts = count_by_teil(questions)
    expected_counts = {1: 20, 2: 10, 3: 15, 4: 10}
    for teil, expected in expected_counts.items():
        got = counts.get(teil, 0)
        if got != expected:
            errors.append(f"T{test_num}: teil {teil} expected {expected}, got {got}")

    seen_ids = set()
    for q in questions:
        qid = q.get("id")
        if qid in seen_ids:
            errors.append(f"T{test_num}: duplicate question id {qid}")
        seen_ids.add(qid)

        qtype = q.get("type")
        if qtype not in {"mc", "rf", "text"}:
            errors.append(f"T{test_num}/Q{qid}: invalid type {qtype}")

        question_text = str(q.get("question", "")).strip()
        if not question_text:
            errors.append(f"T{test_num}/Q{qid}: empty question text")

        explanation = str(q.get("explanation", "")).strip()
        if not explanation:
            errors.append(f"T{test_num}/Q{qid}: empty explanation")

        # Basic punctuation quality check (heuristic)
        # Allow trailing closing quote/bracket after sentence punctuation.
        stripped_tail = question_text.rstrip("'\"”’)] ")
        if stripped_tail and stripped_tail[-1] not in {"?", ".", "!"}:
            errors.append(f"T{test_num}/Q{qid}: question text missing terminal punctuation")

        if qtype == "rf":
            if not isinstance(q.get("correct"), bool):
                errors.append(f"T{test_num}/Q{qid}: rf correct must be bool")
        else:
            opts = q.get("options") or []
            if len(opts) != 3:
                errors.append(f"T{test_num}/Q{qid}: expected 3 options, got {len(opts)}")
            corr = q.get("correct")
            if not isinstance(corr, int) or corr < 0 or corr >= len(opts):
                errors.append(f"T{test_num}/Q{qid}: invalid correct index {corr}")

    # Scoring checks
    perfect_answers = make_perfect_answers(questions)
    perfect_score, perfect_by_teil = score_attempt(questions, perfect_answers)
    if perfect_score != 55:
        errors.append(f"T{test_num}: perfect attempt should score 55, got {perfect_score}")

    if perfect_by_teil != {1: 20, 2: 10, 3: 15, 4: 10}:
        errors.append(f"T{test_num}: perfect per-teil mismatch {perfect_by_teil}")

    empty_score, _ = score_attempt(questions, {})
    if empty_score != 0:
        errors.append(f"T{test_num}: empty attempt should score 0, got {empty_score}")

    # PDF generation check
    session = FakeSession(
        id=1000 + test_num,
        user_name="QA Student",
        test_number=test_num,
        finished_at=datetime.utcnow(),
        duration_seconds=1337,
        score=65,
        total_questions=55,
        percentage=100.0,
        passed=True,
        answers_json={**perfect_answers, "schreiben": "Sehr geehrte Damen und Herren, dies ist ein Testbrief." * 6, "__teil5_score": 10},
        teil1_score=20,
        teil2_score=10,
        teil3_score=15,
        teil4_score=10,
    )
    try:
        pdf_bytes, mistakes = build_test_report_pdf(session, questions)
        if not pdf_bytes.startswith(b"%PDF"):
            errors.append(f"T{test_num}: generated report is not a valid PDF header")
        if len(pdf_bytes) < 3000:
            errors.append(f"T{test_num}: generated PDF is unexpectedly small ({len(pdf_bytes)} bytes)")
        if mistakes:
            errors.append(f"T{test_num}: perfect session should have no mistakes, got {len(mistakes)}")
    except Exception as exc:
        errors.append(f"T{test_num}: PDF generation failed: {exc}")

    # Speaking certificate (Teil 6 & 7) simulation
    speaking_session = FakeSessionSpeaking(
        id=2000 + test_num,
        user_name="QA Student",
        user_email="qa@example.com",
        user_phone="+49123456789",
        finished_at=datetime.utcnow(),
        presentation_score=9,
        feedback_text="Hervorragende Aussprache und fließende Rede."
    )
    try:
        sp_pdf_bytes = build_speaking_report_pdf(speaking_session)
        if not sp_pdf_bytes.startswith(b"%PDF"):
            errors.append(f"T{test_num}: Speaking report is not a valid PDF")
        if len(sp_pdf_bytes) < 2000:
            errors.append(f"T{test_num}: Speaking PDF is too small ({len(sp_pdf_bytes)} bytes)")
    except Exception as exc:
        errors.append(f"T{test_num}: Speaking PDF generation failed: {exc}")

    return errors


def main() -> int:
    all_errors: List[str] = []
    for test_num in range(1, 6):
        errs = validate_one_test(test_num)
        if errs:
            all_errors.extend(errs)

    if all_errors:
        print("FAILED: issues found")
        for e in all_errors:
            print(f"- {e}")
        return 1

    print("OK: all 5 themes passed integrity, scoring, and PDF checks")
    print("- Question distribution per theme: 20 + 10 + 15 + 10")
    print("- Perfect score simulation: 55/55 + Teil 5 (Review and PDF)")
    print("- PDF generation: Main Certificate and Speaking Certificate (Teil 6 & 7)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
