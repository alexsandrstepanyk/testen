from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime

class SessionCreate(BaseModel):
    user_name: str
    user_email: Optional[str] = None
    user_phone: Optional[str] = None
    test_number: int = 1

class SessionFinish(BaseModel):
    duration_seconds: int
    score: int
    percentage: float
    passed: bool
    answers: Dict[str, Any]
    teil1_score: int
    teil2_score: int
    teil3_score: int
    teil4_score: Optional[int] = 0
    teil5_score: Optional[int] = 0

class SessionOut(BaseModel):
    id: int
    user_name: str
    user_email: Optional[str] = None
    user_phone: Optional[str] = None
    test_number: Optional[int]
    started_at: datetime
    finished_at: Optional[datetime]
    duration_seconds: Optional[int]
    score: Optional[int]
    total_questions: int
    percentage: Optional[float]
    passed: Optional[bool]
    teil1_score: Optional[int]
    teil2_score: Optional[int]
    teil3_score: Optional[int]
    teil4_score: Optional[int]
    teil5_score: Optional[int] = 0
    video_url: Optional[str] = None
    self_intro_video_url: Optional[str] = None
    image_description_video_url: Optional[str] = None
    presentation_score: Optional[int] = 0
    self_intro_score: Optional[int] = 0
    image_description_score: Optional[int] = 0
    feedback_text: Optional[str] = ""
    self_intro_feedback_text: Optional[str] = ""
    image_description_feedback_text: Optional[str] = ""
    class Config:
        from_attributes = True


class CustomQuestionBase(BaseModel):
    order_index: int = Field(default=1, ge=1)
    teil: int = Field(default=1, ge=1, le=4)
    question_type: str = Field(default="mc")
    question_text: str
    context_text: Optional[str] = None
    audio_url: Optional[str] = None
    options_json: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    points: int = Field(default=1, ge=1, le=100)


class CustomQuestionCreate(CustomQuestionBase):
    pass


class CustomQuestionUpdate(CustomQuestionBase):
    pass


class CustomQuestionOut(CustomQuestionBase):
    id: int
    course_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CustomCourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    level: str = Field(default="B1")
    teil1_count: int = Field(default=20, ge=0, le=200)
    teil2_count: int = Field(default=10, ge=0, le=200)
    teil3_count: int = Field(default=15, ge=0, le=200)
    writing_required: bool = True
    time_limit_minutes: int = Field(default=65, ge=1, le=600)
    is_published: bool = False


class CustomCourseCreate(CustomCourseBase):
    pass


class CustomCourseUpdate(CustomCourseBase):
    pass


class CustomCourseOut(CustomCourseBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    questions: List[CustomQuestionOut] = []

    class Config:
        from_attributes = True
