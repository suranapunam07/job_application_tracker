from pydantic import BaseModel
from datetime import date
from typing import Optional


class ApplicationCreate(BaseModel):
    company_name: str
    job_title: str
    job_url: Optional[str] = None
    status: str = "applied"
    applied_date: Optional[date] = None
    deadline: Optional[date] = None
    salary: Optional[float] = None


class ApplicationResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    job_url: Optional[str]
    status: str
    applied_date: Optional[date]
    deadline: Optional[date]
    salary: Optional[float]
    user_id: int

    class Config:
        from_attributes = True