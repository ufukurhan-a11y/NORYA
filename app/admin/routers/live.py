"""Canlı kullanıcı takibi: aktif kullanıcılar, IP, ülke, sayfa."""
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import Presence, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def live_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db)):
    # Son 2 dakikada heartbeat atanlar = aktif
    threshold = datetime.utcnow() - timedelta(minutes=2)
    presences = list(db.exec(select(Presence).where(Presence.last_seen_at >= threshold).order_by(Presence.last_seen_at.desc())).all())
    user_ids = [p.user_id for p in presences]
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u
    rows = [
        {
            "user_id": p.user_id,
            "email": (users_map[p.user_id].email if p.user_id in users_map else f"#{p.user_id}"),
            "ip": getattr(p, "ip", None) or "-",
            "country": getattr(p, "country", None) or "-",
            "current_page": getattr(p, "current_page", None) or "-",
            "last_seen_at": p.last_seen_at.strftime("%d.%m.%Y %H:%M:%S") if p.last_seen_at else "-",
        }
        for p in presences
    ]
    return templates.TemplateResponse("admin/live_list.html", {"request": request, "presences": rows})

