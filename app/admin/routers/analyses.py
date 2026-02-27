"""Admin analiz geçmişi: tüm analizler, filtre."""
from datetime import datetime

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AnalysisRecord, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def _parse_date(s: str | None) -> datetime | None:
    if not s or not s.strip():
        return None
    try:
        return datetime.strptime(s.strip()[:10], "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        return None


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def analyses_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    q: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    source: str | None = None,
    limit: int = 200,
):
    stmt = select(AnalysisRecord).order_by(AnalysisRecord.created_at.desc()).limit(limit)
    if date_from:
        start = _parse_date(date_from)
        if start:
            stmt = stmt.where(AnalysisRecord.created_at >= start)
    if date_to:
        end = _parse_date(date_to)
        if end:
            end_of_day = end.replace(hour=23, minute=59, second=59, microsecond=999999)
            stmt = stmt.where(AnalysisRecord.created_at <= end_of_day)
    if source and source.strip().lower() in ("text", "pdf", "image"):
        stmt = stmt.where(AnalysisRecord.source == source.strip().lower())
    if q and q.strip():
        q = q.strip()
        try:
            uid = int(q)
            stmt = stmt.where(AnalysisRecord.user_id == uid)
        except ValueError:
            users = list(db.exec(select(User).where(User.email.contains(q))).all())
            user_ids = [u.id for u in users if u.id is not None]
            if user_ids:
                stmt = stmt.where(AnalysisRecord.user_id.in_(user_ids))
            else:
                stmt = stmt.where(AnalysisRecord.id == -1)
    records = list(db.exec(stmt).all())
    user_ids = list({r.user_id for r in records})
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or ""
    rows = [
        {
            "id": r.id,
            "user_id": r.user_id,
            "email": users_map.get(r.user_id, "-"),
            "created_at": r.created_at.strftime("%d.%m.%Y %H:%M") if r.created_at else "-",
            "source": r.source or "text",
            "input_preview": (r.input_text or "")[:100] + ("…" if len(r.input_text or "") > 100 else ""),
        }
        for r in records
    ]
    return templates.TemplateResponse(
        "admin/analyses_list.html",
        {
            "request": request,
            "analyses": rows,
            "q": q or "",
            "date_from": date_from or "",
            "date_to": date_to or "",
            "source": source or "",
        },
    )
