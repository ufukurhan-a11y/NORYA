"""Hata log merkezi: error_logs tablosu."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import ErrorLog

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def errors_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), limit: int = 100):
    logs = list(db.exec(select(ErrorLog).order_by(ErrorLog.id.desc()).limit(limit)).all())
    rows = [
        {
            "id": e.id,
            "user_id": e.user_id,
            "endpoint": e.endpoint or "-",
            "method": e.method or "-",
            "error_message": (e.error_message or "-")[:200],
            "created_at": e.created_at.strftime("%d.%m.%Y %H:%M:%S") if e.created_at else "-",
        }
        for e in logs
    ]
    return templates.TemplateResponse("admin/errors_list.html", {"request": request, "errors": rows})


@router.get("/{error_id}", response_class=HTMLResponse)
def error_detail(request: Request, error_id: int, _=Depends(require_admin_cookie), db: Session = Depends(get_db)):
    from fastapi import HTTPException
    e = db.get(ErrorLog, error_id)
    if not e:
        raise HTTPException(404, "Log bulunamadı.")
    return templates.TemplateResponse(
        "admin/error_detail.html",
        {
            "request": request,
            "e": e,
            "created_at": e.created_at.strftime("%d.%m.%Y %H:%M:%S") if e.created_at else "-",
        },
    )
