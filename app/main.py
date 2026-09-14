from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.applications import router as applications_router


app = FastAPI(
    title="Job Application Tracker"
)


app.include_router(auth_router)
app.include_router(applications_router)


@app.get("/")
def home():
    return {
        "message": "Job Application Tracker API is running"
    }