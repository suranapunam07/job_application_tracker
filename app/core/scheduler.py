from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, timedelta

from app.db.database import SessionLocal
from app.models.application import Application

scheduler = BackgroundScheduler()

def check_deadlines():
    db = SessionLocal()

    try:
        today = date.today()
        upcoming_date = today + timedelta(days=3)

        applications = db.query(Application).filter(
            Application.deadline != None,
            Application.deadline <= upcoming_date,
            Application.deadline >= today
        ).all()

        for application in applications:
            print(
                f"Reminder: {application.company_name} - "
                f"{application.job_title} deadline is"
                f"{application.deadline}"
            )

    finally:
        db.close()

def start_scheduler():
    scheduler.add_job(
        check_deadlines,
        "interval",
        hours=24,
        id="deadline_checker",
        replace_existing=True
    )

    scheduler.start()

