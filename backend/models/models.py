from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, JSON
from sqlalchemy.sql import func
from .database import Base

class TestSession(Base):
    __tablename__ = "test_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
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
