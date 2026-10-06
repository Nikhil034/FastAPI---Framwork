from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text


class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True)

    title = Column(String(100), nullable=False)

    description = Column(Text)

    status = Column(String(20), nullable=False)

    priority = Column(String(20), nullable=False)

    project_id = Column(
        ForeignKey("projects.id")
    )

    created_at = Column(DateTime)