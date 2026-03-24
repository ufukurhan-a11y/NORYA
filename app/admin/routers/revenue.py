"""Gelir analitik sayfası: ürün bazlı kırılım, dönüşüm oranı, AOV, kupon etkisi, aylık trend."""
from datetime import date, datetime, timedelta

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse
from app.core.templating import Jinja2Templates
from sqlmodel import Session, select, func
from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import PaymentOrder, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

MONTH_NAMES_TR = ("Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara")


def _month_minus(d: date, n: int) -> date:
    y, m = d.year, d.month
    m -= n
    while m <= 0:
        m += 12
        y -= 1
    return date(y, m, 1)


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def revenue_dashboard(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    months: int = Query(12, ge=1, le=36),
):
    now = datetime.utcnow()
    today = now.date()

    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = today_start - timedelta(days=today.weekday())
    month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    year_start = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    def _completed_sum(since: datetime) -> float:
        val = db.exec(
            select(func.sum(PaymentOrder.amount_kurus))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= since)
        ).one() or 0
        return val / 100.0

    def _completed_count(since: datetime) -> int:
        return db.exec(
            select(func.count(PaymentOrder.id))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= since)
        ).one() or 0

    daily_eur = _completed_sum(today_start)
    weekly_eur = _completed_sum(week_start)
    monthly_eur = _completed_sum(month_start)
    yearly_eur = _completed_sum(year_start)

    daily_count = _completed_count(today_start)
    weekly_count = _completed_count(week_start)
    monthly_count = _completed_count(month_start)
    yearly_count = _completed_count(year_start)

    total_completed = db.exec(select(func.count(PaymentOrder.id)).where(PaymentOrder.status == "completed")).one() or 0
    total_all = db.exec(select(func.count(PaymentOrder.id))).one() or 0
    total_revenue = db.exec(select(func.sum(PaymentOrder.amount_kurus)).where(PaymentOrder.status == "completed")).one() or 0
    total_revenue_eur = total_revenue / 100.0

    conversion_rate = (total_completed / total_all * 100) if total_all > 0 else 0
    aov = (total_revenue_eur / total_completed) if total_completed > 0 else 0

    total_refunded = db.exec(
        select(func.sum(PaymentOrder.refund_amount_kurus))
        .where(PaymentOrder.refund_amount_kurus > 0)
    ).one() or 0
    total_refunded_eur = total_refunded / 100.0

    # ── Ürün bazlı kırılım ──
    product_rows = db.exec(
        select(
            PaymentOrder.product,
            func.count(PaymentOrder.id),
            func.sum(PaymentOrder.amount_kurus),
        )
        .where(PaymentOrder.status == "completed")
        .group_by(PaymentOrder.product)
        .order_by(func.sum(PaymentOrder.amount_kurus).desc())
    ).all()
    product_breakdown = [
        {
            "product": r[0] or "bilinmiyor",
            "count": r[1],
            "total_eur": (r[2] or 0) / 100.0,
            "avg_eur": ((r[2] or 0) / 100.0) / r[1] if r[1] > 0 else 0,
        }
        for r in product_rows
    ]

    # ── Kupon etkisi ──
    coupon_used_count = db.exec(
        select(func.count(PaymentOrder.id))
        .where(PaymentOrder.status == "completed")
        .where(PaymentOrder.coupon_code_used.isnot(None))
        .where(PaymentOrder.coupon_code_used != "")
    ).one() or 0
    coupon_used_revenue = db.exec(
        select(func.sum(PaymentOrder.amount_kurus))
        .where(PaymentOrder.status == "completed")
        .where(PaymentOrder.coupon_code_used.isnot(None))
        .where(PaymentOrder.coupon_code_used != "")
    ).one() or 0
    no_coupon_count = total_completed - coupon_used_count
    no_coupon_revenue = total_revenue - (coupon_used_revenue or 0)

    top_coupons = db.exec(
        select(
            PaymentOrder.coupon_code_used,
            func.count(PaymentOrder.id),
            func.sum(PaymentOrder.amount_kurus),
        )
        .where(PaymentOrder.status == "completed")
        .where(PaymentOrder.coupon_code_used.isnot(None))
        .where(PaymentOrder.coupon_code_used != "")
        .group_by(PaymentOrder.coupon_code_used)
        .order_by(func.count(PaymentOrder.id).desc())
        .limit(10)
    ).all()
    top_coupons_data = [
        {"code": r[0], "count": r[1], "total_eur": (r[2] or 0) / 100.0}
        for r in top_coupons
    ]

    # ── Aylık trend (ürün bazlı) ──
    chart_labels = []
    chart_single = []
    chart_monthly_plan = []
    chart_yearly = []
    chart_total = []

    for i in range(months - 1, -1, -1):
        m_start = _month_minus(today, i)
        m_end = _month_minus(today, i - 1)
        dt_start = datetime(m_start.year, m_start.month, m_start.day)
        dt_end = datetime(m_end.year, m_end.month, m_end.day)
        chart_labels.append(f"{MONTH_NAMES_TR[m_start.month - 1]} {m_start.year}")

        rows = db.exec(
            select(
                PaymentOrder.product,
                func.sum(PaymentOrder.amount_kurus),
            )
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= dt_start)
            .where(PaymentOrder.created_at < dt_end)
            .group_by(PaymentOrder.product)
        ).all()
        product_map = {r[0]: (r[1] or 0) / 100.0 for r in rows}
        chart_single.append(round(product_map.get("single", 0), 2))
        chart_monthly_plan.append(round(product_map.get("monthly", 0), 2))
        chart_yearly.append(round(product_map.get("yearly", 0), 2))
        chart_total.append(round(sum(product_map.values()), 2))

    # ── Dönüşüm oranı trend (aylık) ──
    chart_conversion = []
    for i in range(months - 1, -1, -1):
        m_start = _month_minus(today, i)
        m_end = _month_minus(today, i - 1)
        dt_start = datetime(m_start.year, m_start.month, m_start.day)
        dt_end = datetime(m_end.year, m_end.month, m_end.day)
        m_total = db.exec(
            select(func.count(PaymentOrder.id))
            .where(PaymentOrder.created_at >= dt_start)
            .where(PaymentOrder.created_at < dt_end)
        ).one() or 0
        m_completed = db.exec(
            select(func.count(PaymentOrder.id))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= dt_start)
            .where(PaymentOrder.created_at < dt_end)
        ).one() or 0
        chart_conversion.append(round(m_completed / m_total * 100, 1) if m_total > 0 else 0)

    # ── En çok harcayan müşteriler (top 10) ──
    top_customers = db.exec(
        select(
            PaymentOrder.user_id,
            func.count(PaymentOrder.id),
            func.sum(PaymentOrder.amount_kurus),
        )
        .where(PaymentOrder.status == "completed")
        .group_by(PaymentOrder.user_id)
        .order_by(func.sum(PaymentOrder.amount_kurus).desc())
        .limit(10)
    ).all()
    top_customer_ids = [r[0] for r in top_customers]
    cust_map = {}
    if top_customer_ids:
        for u in db.exec(select(User).where(User.id.in_(top_customer_ids))).all():
            cust_map[u.id] = u.email or ""
    top_customers_data = [
        {
            "user_id": r[0],
            "email": cust_map.get(r[0], ""),
            "order_count": r[1],
            "total_eur": (r[2] or 0) / 100.0,
        }
        for r in top_customers
    ]

    return templates.TemplateResponse(
        "admin/revenue.html",
        {
            "request": request,
            "daily_eur": daily_eur, "weekly_eur": weekly_eur,
            "monthly_eur": monthly_eur, "yearly_eur": yearly_eur,
            "daily_count": daily_count, "weekly_count": weekly_count,
            "monthly_count": monthly_count, "yearly_count": yearly_count,
            "total_revenue_eur": total_revenue_eur,
            "total_completed": total_completed,
            "total_all": total_all,
            "conversion_rate": conversion_rate,
            "aov": aov,
            "total_refunded_eur": total_refunded_eur,
            "product_breakdown": product_breakdown,
            "coupon_used_count": coupon_used_count,
            "coupon_used_revenue_eur": (coupon_used_revenue or 0) / 100.0,
            "no_coupon_count": no_coupon_count,
            "no_coupon_revenue_eur": (no_coupon_revenue or 0) / 100.0,
            "top_coupons": top_coupons_data,
            "chart_labels": chart_labels,
            "chart_single": chart_single,
            "chart_monthly_plan": chart_monthly_plan,
            "chart_yearly": chart_yearly,
            "chart_total": chart_total,
            "chart_conversion": chart_conversion,
            "top_customers": top_customers_data,
            "months": months,
        },
    )
