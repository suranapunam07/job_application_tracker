from pydantic import BaseModel
from datetime import datetime


class NoteCreate(BaseModel):
    content: str


class NoteResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    application_id: int

    class Config:
        from_attributes = True