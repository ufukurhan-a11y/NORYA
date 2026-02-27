"""AI analiz kuyruğu: analysis_jobs."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AnalysisJob, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def queue_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), limit: int = 100, status_filter: str | None = None):
    stmt = select(AnalysisJob).order_by(AnalysisJob.id.desc()).limit(limit)
    if status_filter and status_filter in ("pending", "processing", "done", "failed"):
        stmt = stmt.where(AnalysisJob.status == status_filter)
    jobs = list(db.exec(stmt).all())
    user_ids = {j.user_id for j in jobs}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or ""
    rows = [
        {
            "id": j.id,
            "user_id": j.user_id,
            "user_email": users_map.get(j.user_id, ""),
            "analysis_record_id": j.analysis_record_id,
            "status": j.status,
            "duration_ms": j.duration_ms or "-",
            "error_message": (j.error_message or "-")[:80],
            "created_at": (j.created_at.strftime("%d.%m.%Y %H:%M") if j.created_at else "-"),
        }
        for j in jobs
    ]
    return templates.TemplateResponse(
        "admin/queue_list.html",
        {"request": request, "jobs": rows, "status_filter": status_filter or ""},
    )
