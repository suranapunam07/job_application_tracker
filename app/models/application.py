from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    job_url = Column(String, nullable=True)
    status = Column(String, nullable=False, default="applied")
    applied_date = Column(Date, nullable=True)
    deadline = Column(Date, nullable=True)
    salary = Column(Float, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="applications")

    interviews = relationship(
        "Interview",
        back_populates="application",
        cascade="all, delete-orphan"
    )

    notes = relationship(
        "Note",
        back_populates="application",
        cascade="all, delete-orphan"
    )