"""Dashboard: özet metrikler, son işlemler, aylık trend grafiği."""
from datetime import date, datetime, timedelta

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select, func

from app.admin.deps import (
    ADMIN_COOKIE,
    ADMIN_LOCKOUT_MINUTES,
    ADMIN_LOGIN_MAX_FAILURES,
    _admin_cookie_value,
    _admin_secret_constant_time_compare,
    get_client_ip,
    require_admin_cookie,
)
from app.core.config import settings
from app.core.database import get_db
from app.models import AnalysisJob, AnalysisRecord, PaymentOrder, Presence, SecurityLog, User

# Ay adları (grafik etiketleri)
MONTH_NAMES_TR = ("Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara")


def _month_minus(d: date, n: int) -> date:
    """d tarihinden n ay öncesi (ayın 1'i)."""
    y, m = d.year, d.month
    m -= n
    while m <= 0:
        m += 12
        y -= 1
    while m > 12:
        m -= 12
        y += 1
    return date(y, m, 1)


def _last_24_months_monthly_stats(db: Session, now: datetime) -> tuple[list[str], list[int], list[float], list[int]]:
    """Son 24 ay (eskiden yeniye) için: etiketler, analiz sayısı, satış (EUR), yeni kullanıcı."""
    today = now.date() if hasattr(now, "date") else date(now.year, now.month, now.day)
    labels = []
    analyses = []
    sales = []
    users = []
    for i in range(23, -1, -1):  # 23 ay önce ... bu ay
        m_start = _month_minus(today, i)
        m_end = _month_minus(today, i - 1)  # bir sonraki ayın 1'i (i=0 için gelecek ay)
        dt_start = datetime(m_start.year, m_start.month, m_start.day, 0, 0, 0, 0)
        dt_end = datetime(m_end.year, m_end.month, m_end.day, 0, 0, 0, 0)
        labels.append(f"{MONTH_NAMES_TR[m_start.month - 1]} {m_start.year}")
        n_analyses = db.exec(
            select(func.count(AnalysisRecord.id)).where(AnalysisRecord.created_at >= dt_start).where(AnalysisRecord.created_at < dt_end)
        ).one() or 0
        analyses.append(n_analyses)
        total_cents = db.exec(
            select(func.sum(PaymentOrder.amount_kurus))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= dt_start)
            .where(PaymentOrder.created_at < dt_end)
        ).one() or 0
        sales.append(round((total_cents / 100), 2))
        n_users = db.exec(
            select(func.count(User.id)).where(User.created_at >= dt_start).where(User.created_at < dt_end)
        ).one() or 0
        users.append(n_users)
    return labels, analyses, sales, users

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/login", response_class=HTMLResponse)
def admin_login_page(request: Request, err: str | None = None):
    if not (settings.admin_secret or "").strip():
        return templates.TemplateResponse("admin/login.html", {"request": request, "err": "config"})
    return templates.TemplateResponse("admin/login.html", {"request": request, "err": err})


@router.post("/login")
def admin_login_submit(
    request: Request,
    admin_secret: str | None = Form(None),
    db: Session = Depends(get_db),
):
    if not (settings.admin_secret or "").strip():
        return RedirectResponse(url="/admin/login?err=config", status_code=302)
    ip = get_client_ip(request)
    cutoff = datetime.utcnow() - timedelta(minutes=ADMIN_LOCKOUT_MINUTES)
    fail_count = (
        db.exec(
            select(func.count(SecurityLog.id)).where(SecurityLog.event == "admin_login_failed").where(SecurityLog.ip == ip).where(SecurityLog.created_at >= cutoff)
        ).one()
        or 0
    )
    if fail_count >= ADMIN_LOGIN_MAX_FAILURES:
        try:
            db.add(SecurityLog(event="admin_lockout", ip=ip, detail="lockout_15m"))
            db.commit()
        except Exception:
            pass
        return RedirectResponse(url="/admin/login?err=lockout", status_code=302)
    if not _admin_secret_constant_time_compare(admin_secret, settings.admin_secret):
        try:
            db.add(SecurityLog(event="admin_login_failed", ip=ip, endpoint="/admin/login"))
            db.commit()
        except Exception:
            pass
        return RedirectResponse(url="/admin/login?err=1", status_code=302)
    response = RedirectResponse(url="/admin/dashboard", status_code=302)
    secure = (settings.environment or "").strip().lower() == "production"
    response.set_cookie(
        key=ADMIN_COOKIE,
        value=_admin_cookie_value(),
        httponly=True,
        secure=secure,
        samesite="lax",
        max_age=86400,
    )
    return response


@router.get("/", response_class=HTMLResponse)
def admin_index():
    """ /admin/ her zaman önce login sayfasına yönlendirsin. """
    return RedirectResponse(url="/admin/login", status_code=302)


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

    # Son 24 ay trend (grafik için)
    chart_labels, chart_analyses, chart_sales, chart_users = _last_24_months_monthly_stats(db, now)

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
            "chart_labels": chart_labels,
            "chart_analyses": chart_analyses,
            "chart_sales": chart_sales,
            "chart_users": chart_users,
        },
    )
