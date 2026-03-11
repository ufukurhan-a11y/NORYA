"""Live Analytics Dashboard: sadece admin girişi sonrası görünür, premium metrik kartları."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.services.live_analytics import (
    PERIOD_OPTIONS,
    get_live_analytics,
)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/live-analytics", response_class=HTMLResponse)
def live_analytics_page(
    request: Request,
    period: int | None = None,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """Live Analytics Dashboard sayfası; sadece admin cookie ile erişilir."""
    data = get_live_analytics(db, period_minutes=period)
    return templates.TemplateResponse(
        "admin/live_analytics.html",
        {"request": request, "period_options": PERIOD_OPTIONS, **data},
    )


@router.get("/api/live-analytics", response_class=JSONResponse)
def live_analytics_api(
    period: int | None = None,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """JSON API: istemci tarafında yenileme / auto-refresh için."""
    data = get_live_analytics(db, period_minutes=period)
    return JSONResponse(data)
