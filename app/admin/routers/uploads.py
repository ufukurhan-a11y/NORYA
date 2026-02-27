"""Dosya upload logları."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import UploadLog

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def uploads_list(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db), limit: int = 100):
    logs = list(db.exec(select(UploadLog).order_by(UploadLog.id.desc()).limit(limit)).all())
    rows = [
        {
            "id": u.id,
            "user_id": u.user_id,
            "filename": u.filename or "-",
            "file_size_bytes": u.file_size_bytes or 0,
            "status": u.status,
            "error_message": (u.error_message or "-")[:100],
            "duration_ms": u.duration_ms or "-",
            "created_at": u.created_at.strftime("%d.%m.%Y %H:%M") if u.created_at else "-",
        }
        for u in logs
    ]
    return templates.TemplateResponse("admin/uploads_list.html", {"request": request, "uploads": rows})

