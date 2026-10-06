from fastapi import APIRouter, HTTPException, status
from fastapi.params import Query

from app.schemas.issue import IssueCreate, IssuePriority, IssueStatus

router = APIRouter(
    prefix="/issues",
    tags=["Issues"]
)

issues = []


@router.post("/",status_code=status.HTTP_201_CREATED)
def create_issue(issue: IssueCreate):
    issues.append(issue)

    return issue


@router.get("/")
def get_issues(
    status: IssueStatus | None = None,
    priority: IssuePriority | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):
    return issues;


@router.get("/{issue_id}")
def get_issue(issue_id: int):
    return issues[issue_id]


@router.put("/{issue_id}")
def update_issue(issue_id: int, issue: dict):
    issues[issue_id] = issue

    return issue


@router.delete("/{issue_id}")
def delete_issue(issue_id: int):
    issues.pop(issue_id)

    return {
        "message": "Issue deleted"
    }

from fastapi import FastAPI

from app.api.routes.issues import router as issue_router

app = FastAPI()

app.include_router(issue_router)