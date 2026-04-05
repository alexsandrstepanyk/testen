from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

class SessionCreate(BaseModel):
    user_name: str
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

class SessionOut(BaseModel):
    id: int
    user_name: str
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
    class Config:
        from_attributes = True
