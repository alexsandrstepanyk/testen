from typing import Any, Dict, List, Optional, Tuple

from sqlalchemy.orm import Session, joinedload

from models.models import CustomCourse
from models.questions_data import ALL_TESTS, get_questions_for_test

CUSTOM_TEST_OFFSET = 1000


def encode_custom_test_number(course_id: int) -> int:
    return CUSTOM_TEST_OFFSET + int(course_id)


def decode_custom_test_number(test_number: int) -> Optional[int]:
    if test_number is None:
        return None
    if int(test_number) > CUSTOM_TEST_OFFSET:
        return int(test_number) - CUSTOM_TEST_OFFSET
    return None


def is_custom_test_number(test_number: int) -> bool:
    return decode_custom_test_number(test_number) is not None


def _normalize_correct_answer(question_type: str, correct_answer: Any) -> Any:
    if question_type == "rf":
        return str(correct_answer).lower() == "true"
    try:
        return int(correct_answer)
    except Exception:
        return 0


def serialize_custom_course_question(question: Any) -> Dict[str, Any]:
    q_type = question.question_type or "mc"
    options = question.options_json or []
    return {
        "id": question.id,
        "teil": question.teil,
        "type": q_type,
        "question": question.question_text,
        "context": question.context_text,
        "options": options,
        "correct": _normalize_correct_answer(q_type, question.correct_answer),
        "explanation": question.explanation or "",
    }


def get_questions_by_test_number(db: Session, test_number: int) -> List[Dict[str, Any]]:
    custom_course_id = decode_custom_test_number(test_number)
    if custom_course_id is None:
        return get_questions_for_test(test_number)

    course = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .filter(CustomCourse.id == custom_course_id)
        .first()
    )
    if not course:
        return []

    return [serialize_custom_course_question(q) for q in course.questions]


def get_test_label(test_number: int, db: Optional[Session] = None) -> str:
    custom_course_id = decode_custom_test_number(test_number)
    if custom_course_id is None:
        return f"Test {test_number}"

    if db is None:
        return f"Kurs {custom_course_id}"

    course = db.query(CustomCourse).filter(CustomCourse.id == custom_course_id).first()
    if not course:
        return f"Kurs {custom_course_id}"
    return f"Kurs {course.title}"


def get_available_tests(db: Session) -> List[Dict[str, Any]]:
    tests: List[Dict[str, Any]] = []
    for t, qs in ALL_TESTS.items():
        tests.append({
            "test_number": t,
            "label": f"Test {t}",
            "title": None,
            "is_custom": False,
            "total_questions": len(qs),
            "teil1": len([q for q in qs if q["teil"] == 1]),
            "teil2": len([q for q in qs if q["teil"] == 2]),
            "teil3": len([q for q in qs if q["teil"] == 3]),
            "teil4": len([q for q in qs if q["teil"] == 4]),
        })

    custom_courses = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .filter(CustomCourse.is_published == True)
        .order_by(CustomCourse.updated_at.desc(), CustomCourse.id.desc())
        .all()
    )
    for course in custom_courses:
        custom_test_number = encode_custom_test_number(course.id)
        tests.append({
            "test_number": custom_test_number,
            "label": f"Kurs {course.id}",
            "title": course.title,
            "is_custom": True,
            "course_id": course.id,
            "total_questions": len(course.questions),
            "teil1": len([q for q in course.questions if q.teil == 1]),
            "teil2": len([q for q in course.questions if q.teil == 2]),
            "teil3": len([q for q in course.questions if q.teil == 3]),
            "teil4": len([q for q in course.questions if q.teil == 4]),
        })

    return tests


def get_custom_course_theme_meta(index: int) -> Tuple[str, str]:
    palette = [
        ("🧩", "Spezialkurs"),
        ("🏠", "Wohnen"),
        ("🗣️", "Kommunikation"),
        ("📈", "Praxis"),
        ("🧠", "Intensiv"),
    ]
    return palette[index % len(palette)]
