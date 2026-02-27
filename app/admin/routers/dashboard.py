"""Dashboard: özet metrikler, son işlemler."""
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select, func

from app.admin.deps import ADMIN_COOKIE, _admin_cookie_value, require_admin_cookie
from app.core.config import settings
from app.core.database import get_db
from app.models import AnalysisJob, PaymentOrder, Presence, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
def admin_login_page(request: Request, err: str | None = None):
    if not (settings.admin_secret or "").strip():
        return templates.TemplateResponse("admin/login.html", {"request": request, "err": "config"})
    return templates.TemplateResponse("admin/login.html", {"request": request, "err": err})


@router.post("/login")
def admin_login_submit(admin_secret: str | None = Form(None)):
    if not (admin_secret or "").strip() or admin_secret.strip() != (settings.admin_secret or "").strip():
        return RedirectResponse(url="/admin/login?err=1", status_code=302)
    response = RedirectResponse(url="/admin/dashboard", status_code=302)
    response.set_cookie(key=ADMIN_COOKIE, value=_admin_cookie_value(), httponly=True, samesite="lax", max_age=86400)
    return response


@router.get("/", response_class=HTMLResponse)
def admin_index(_=Depends(require_admin_cookie)):
    return RedirectResponse(url="/admin/dashboard", status_code=302)


@router.get("/legacy", response_class=HTMLResponse)
def admin_legacy_page(_=Depends(require_admin_cookie)):
    """Eski admin paneli (API + tek sayfa JS)."""
    from app.api.admin import get_admin_html
    return get_admin_html()


@router.get("/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request, _=Depends(require_admin_cookie), db: Session = Depends(get_db)):
    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    month_start = (now.replace(day=1, hour=0, minute=0, second=0, microsecond=0))
    active_threshold = now - timedelta(minutes=2)

    # Günlük/aylık satış (tamamlanan ödemeler, EUR)
    daily = db.exec(
        select(func.sum(PaymentOrder.amount_kurus)).where(PaymentOrder.status == "completed").where(PaymentOrder.created_at >= today_start)
    ).one()
    monthly = db.exec(
        select(func.sum(PaymentOrder.amount_kurus)).where(PaymentOrder.status == "completed").where(PaymentOrder.created_at >= month_start)
    ).one()
    daily_sales = (daily or 0) / 100  # euro cent -> EUR
    monthly_sales = (monthly or 0) / 100

    total_users = db.exec(select(func.count(User.id))).one() or 0
    active_users = db.exec(select(func.count(Presence.id)).where(Presence.last_seen_at >= active_threshold)).one() or 0

    # Ortalama analiz süresi (analysis_jobs done)
    avg_duration = db.exec(
        select(func.avg(AnalysisJob.duration_ms)).where(AnalysisJob.status == "done").where(AnalysisJob.duration_ms.isnot(None))
    ).one()
    avg_analysis_time = f"{(avg_duration or 0):.0f} ms" if avg_duration else "-"

    failed_payments = db.exec(select(func.count(PaymentOrder.id)).where(PaymentOrder.status == "failed")).one() or 0

    # Son 10 işlem (payment)
    orders = list(
        db.exec(
            select(PaymentOrder).order_by(PaymentOrder.id.desc()).limit(10)
        ).all()
    )
    user_ids = {o.user_id for o in orders}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or ""
    last_transactions = [
        {
            "created_at": (o.created_at.strftime("%d.%m.%Y %H:%M") if o.created_at else "-"),
            "merchant_oid": o.merchant_oid or "-",
            "user_id": o.user_id,
            "user_email": users_map.get(o.user_id, ""),
            "product": o.product or "-",
            "amount_kurus": o.amount_kurus or 0,
            "status": o.status or "pending",
        }
        for o in orders
    ]

    return templates.TemplateResponse(
        "admin/dashboard.html",
        {
            "request": request,
            "daily_sales": f"{daily_sales:.2f}",
            "monthly_sales": f"{monthly_sales:.2f}",
            "total_users": total_users,
            "active_users": active_users,
            "avg_analysis_time": avg_analysis_time,
            "failed_payments": failed_payments,
            "last_transactions": last_transactions,
        },
    )
