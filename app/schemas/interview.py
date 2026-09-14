from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InterviewCreate(BaseModel):
    interview_date: datetime
    interview_type: Optional[str] = None
    result: Optional[str] = None


class InterviewResponse(BaseModel):
    id: int
    interview_date: datetime
    interview_type: Optional[str]
    result: Optional[str]
    application_id: int

    class Config:
        from_attributes = True