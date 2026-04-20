from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, JSON, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class TestSession(Base):
    __tablename__ = "test_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    user_email = Column(String(150), nullable=True)
    user_phone = Column(String(50), nullable=True)
    test_number = Column(Integer, default=1)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True), nullable=True)
    duration_seconds = Column(Integer, nullable=True)
    score = Column(Integer, nullable=True)
    total_questions = Column(Integer, default=45)
    percentage = Column(Float, nullable=True)
    passed = Column(Boolean, nullable=True)
    answers_json = Column(JSON, nullable=True)
    teil1_score = Column(Integer, nullable=True)
    teil2_score = Column(Integer, nullable=True)
    teil3_score = Column(Integer, nullable=True)
    teil4_score = Column(Integer, nullable=True, default=0)
    video_url = Column(String(500), nullable=True)
    self_intro_video_url = Column(String(500), nullable=True)
    image_description_video_url = Column(String(500), nullable=True)
    presentation_score = Column(Integer, nullable=True, default=0)
    self_intro_score = Column(Integer, nullable=True, default=0)
    image_description_score = Column(Integer, nullable=True, default=0)
    feedback_text = Column(Text, nullable=True, default="")
    self_intro_feedback_text = Column(Text, nullable=True, default="")
    image_description_feedback_text = Column(Text, nullable=True, default="")
    hoeren_score = Column(Integer, nullable=True, default=None)


class CustomCourse(Base):
    __tablename__ = "custom_courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    level = Column(String(20), nullable=False, default="B1")
    teil1_count = Column(Integer, nullable=False, default=20)
    teil2_count = Column(Integer, nullable=False, default=10)
    teil3_count = Column(Integer, nullable=False, default=15)
    writing_required = Column(Boolean, nullable=False, default=True)
    time_limit_minutes = Column(Integer, nullable=False, default=65)
    is_published = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    questions = relationship(
        "CustomQuestion",
        back_populates="course",
        cascade="all, delete-orphan",
        order_by="CustomQuestion.order_index",
    )


class CustomQuestion(Base):
    __tablename__ = "custom_questions"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("custom_courses.id", ondelete="CASCADE"), nullable=False, index=True)
    order_index = Column(Integer, nullable=False, default=1)
    teil = Column(Integer, nullable=False, default=1)
    question_type = Column(String(20), nullable=False, default="mc")
    question_text = Column(Text, nullable=False)
    context_text = Column(Text, nullable=True)
    audio_url = Column(Text, nullable=True)
    options_json = Column(JSON, nullable=True)
    correct_answer = Column(String(50), nullable=True)
    explanation = Column(Text, nullable=True)
    points = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    course = relationship("CustomCourse", back_populates="questions")


class TeacherAccount(Base):
    __tablename__ = "teacher_accounts"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(200), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    teacher_username = Column(String(100), nullable=False)
    action = Column(String(50), nullable=False)       # create | update | delete | publish
    resource_type = Column(String(50), nullable=False) # course | question
    resource_id = Column(Integer, nullable=True)
    detail = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
