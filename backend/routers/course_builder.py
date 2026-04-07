from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import Union

from models.database import get_db
from models.models import CustomCourse, CustomQuestion
from routers.teacher import require_teacher_auth
from schemas.schemas import (
    CustomCourseCreate,
    CustomCourseOut,
    CustomCourseUpdate,
    CustomQuestionCreate,
    CustomQuestionOut,
    CustomQuestionUpdate,
)


router = APIRouter(prefix="/courses", tags=["Course Builder"], dependencies=[Depends(require_teacher_auth)])


def serialize_question(question: CustomQuestion) -> dict:
    return CustomQuestionOut.model_validate(question).model_dump()


def serialize_course(course: CustomCourse) -> dict:
    payload = CustomCourseOut.model_validate(course).model_dump()
    payload["question_count"] = len(course.questions)
    payload["actual_counts"] = {
        "teil1": len([q for q in course.questions if q.teil == 1]),
        "teil2": len([q for q in course.questions if q.teil == 2]),
        "teil3": len([q for q in course.questions if q.teil == 3]),
        "teil4": len([q for q in course.questions if q.teil == 4]),
    }
    return payload


def validate_question_payload(payload: Union[CustomQuestionCreate, CustomQuestionUpdate]) -> None:
    allowed_types = {"mc", "rf", "text"}
    if payload.question_type not in allowed_types:
        raise HTTPException(status_code=400, detail="question_type must be mc, rf, or text")

    if payload.question_type in {"mc", "text"}:
        options = payload.options_json or []
        if len(options) < 2:
            raise HTTPException(status_code=400, detail="At least 2 answer options are required")
        if payload.correct_answer is None or str(payload.correct_answer).strip() == "":
            raise HTTPException(status_code=400, detail="correct_answer is required")
    else:
        if str(payload.correct_answer).lower() not in {"true", "false"}:
            raise HTTPException(status_code=400, detail="correct_answer for rf must be true or false")


@router.get("")
def list_courses(db: Session = Depends(get_db)):
    courses = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .order_by(CustomCourse.updated_at.desc(), CustomCourse.id.desc())
        .all()
    )
    return {"total": len(courses), "courses": [serialize_course(course) for course in courses]}


@router.post("")
def create_course(payload: CustomCourseCreate, db: Session = Depends(get_db)):
    course = CustomCourse(**payload.model_dump())
    db.add(course)
    db.commit()
    db.refresh(course)
    course = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .filter(CustomCourse.id == course.id)
        .first()
    )
    return serialize_course(course)


@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .filter(CustomCourse.id == course_id)
        .first()
    )
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return serialize_course(course)


@router.put("/{course_id}")
def update_course(course_id: int, payload: CustomCourseUpdate, db: Session = Depends(get_db)):
    course = db.query(CustomCourse).filter(CustomCourse.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    for key, value in payload.model_dump().items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    course = (
        db.query(CustomCourse)
        .options(joinedload(CustomCourse.questions))
        .filter(CustomCourse.id == course.id)
        .first()
    )
    return serialize_course(course)


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(CustomCourse).filter(CustomCourse.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"ok": True}


@router.post("/{course_id}/questions")
def create_question(course_id: int, payload: CustomQuestionCreate, db: Session = Depends(get_db)):
    course = db.query(CustomCourse).filter(CustomCourse.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    validate_question_payload(payload)
    question = CustomQuestion(course_id=course_id, **payload.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return serialize_question(question)


@router.put("/{course_id}/questions/{question_id}")
def update_question(course_id: int, question_id: int, payload: CustomQuestionUpdate, db: Session = Depends(get_db)):
    question = (
        db.query(CustomQuestion)
        .filter(CustomQuestion.id == question_id, CustomQuestion.course_id == course_id)
        .first()
    )
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    validate_question_payload(payload)
    for key, value in payload.model_dump().items():
        setattr(question, key, value)

    db.commit()
    db.refresh(question)
    return serialize_question(question)


@router.delete("/{course_id}/questions/{question_id}")
def delete_question(course_id: int, question_id: int, db: Session = Depends(get_db)):
    question = (
        db.query(CustomQuestion)
        .filter(CustomQuestion.id == question_id, CustomQuestion.course_id == course_id)
        .first()
    )
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    db.delete(question)
    db.commit()
    return {"ok": True}