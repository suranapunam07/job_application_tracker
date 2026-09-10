from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)
    interview_date = Column(DateTime, nullable=False)
    interview_type = Column(String, nullable=True)
    result = Column(String, nullable=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id"),
        nullable=False
    )

    application = relationship(
        "Application",
        back_populates="interviews"
    )