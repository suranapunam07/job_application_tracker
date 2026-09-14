from fastapi import FastAPI
from importlib import import_module

from app.api.auth import router as auth_router
from app.api.applications import router as applications_router
from app.api.stats import router as stats_router
from app.core.scheduler import start_scheduler


app = FastAPI(
    title="Job Application Tracker"
)


app.include_router(auth_router)
app.include_router(applications_router)
app.include_router(stats_router)

# The interviews module is optional so the application can start even when it
# is not present in the current checkout.
try:
    interviews_router = import_module("app.api.interviews").router
except ModuleNotFoundError:
    interviews_router = None

if interviews_router is not None:
    app.include_router(interviews_router)


start_scheduler()


@app.get("/")
def home():
    return {
        "message": "Job Application Tracker API is running"
    }