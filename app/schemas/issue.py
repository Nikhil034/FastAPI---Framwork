from enum import Enum

from pydantic import BaseModel, Field


class IssueStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)

    description: str | None = None

    priority: IssuePriority = IssuePriority.MEDIUM


class IssueResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: str
