from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.application import Application
from app.models.interview import Interview
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse
)
from app.schemas.interview import InterviewCreate, InterviewResponse

from app.core.security import get_current_user


router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ApplicationResponse)
def create_application(
    application_data: ApplicationCreate,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_application = Application(
        company_name=application_data.company_name,
        job_title=application_data.job_title,
        job_url=application_data.job_url,
        status=application_data.status,
        applied_date=application_data.applied_date,
        deadline=application_data.deadline,
        salary=application_data.salary,
        user_id=int(user_id)
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application

@router.get("/",response_model=list[ApplicationResponse])
def get_applications(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    applications = db.query(Application).filter(Application.user_id == int(user_id)).all()#user cannot see the other user's data

    return applications

@router.put("/{application_id}",response_model=ApplicationResponse)
def update_application(
    application_id: int,
    application_data: ApplicationCreate,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == int(user_id)
    ).first()

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    application.company_name = application_data.company_name
    application.job_title = application_data.job_title
    application.job_url = application_data.job_url
    application.status = application_data.status
    application.applied_date = application_data.applied_date
    application.deadline = application_data.deadline
    application.salary = application_data.salary

    db.commit()
    db.refresh(application)

    return application

@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == int(user_id)
    ).first()

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db.delete(application)
    db.commit()

    return {
        "message": "Application deleted successfully"
    }

@router.post(
    "/{application_id}/interviews",
    response_model=InterviewResponse
)
def create_interview(
    application_id: int,
    interview_data: InterviewCreate,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == int(user_id)
    ).first()

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    new_interview = Interview(
        interview_date=interview_data.interview_date,
        interview_type=interview_data.interview_type,
        result=interview_data.result,
        application_id=application_id
    )

    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)

    return new_interview

@router.get(
    "/{application_id}/interviews",
    response_model=list[InterviewResponse]
)
def get_interviews(
    application_id: int,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == int(user_id)
    ).first()

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return db.query(Interview).filter(
        Interview.application_id == application_id
    ).all()