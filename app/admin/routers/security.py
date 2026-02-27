"""Güvenlik paneli: başarısız login, rate limit, şüpheli aktivite."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import SecurityLog

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def security_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), limit: int = 100, event: str | None = None):
    stmt = select(SecurityLog).order_by(SecurityLog.id.desc()).limit(limit)
    if event and event in ("failed_login", "rate_limit", "suspicious"):
        stmt = stmt.where(SecurityLog.event == event)
    logs = list(db.exec(stmt).all())
    rows = [
        {
            "id": s.id,
            "event": s.event,
            "user_id": s.user_id,
            "ip": s.ip or "-",
            "endpoint": s.endpoint or "-",
            "detail": (s.detail or "-")[:150],
            "created_at": s.created_at.strftime("%d.%m.%Y %H:%M:%S") if s.created_at else "-",
        }
        for s in logs
    ]
    return templates.TemplateResponse(
        "admin/security_list.html",
        {"request": request, "logs": rows, "event_filter": event or ""},
    )
