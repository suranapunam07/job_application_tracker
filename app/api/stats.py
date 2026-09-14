from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import SessionLocal
from app.models.application import Application
from app.core.security import get_current_user


router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_statistics(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    total_applications = db.query(Application).filter(
        Application.user_id == int(user_id)
    ).count()

    status_counts = db.query(
        Application.status,
        func.count(Application.id)
    ).filter(
        Application.user_id == int(user_id)
    ).group_by(
        Application.status
    ).all()

    by_status = {}

    for status, count in status_counts:
        by_status[status] = count

    return {
        "total_applications": total_applications,
        "by_status": by_status
    }