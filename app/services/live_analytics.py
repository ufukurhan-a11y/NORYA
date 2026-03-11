"""Live Analytics: metrikler mevcut event, payment, analysis tablolarından; device/traffic ileride bağlanacak."""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

from sqlmodel import Session, select, func

from app.models import AnalysisRecord, AuditLog, PaymentOrder, Presence, User

# İzin verilen periyotlar (dakika): 30, 60, 360, 1440
PERIOD_OPTIONS = (30, 60, 360, 1440)
DEFAULT_PERIOD = 30


def _period_minutes(period: int | None) -> int:
    if period is None:
        return DEFAULT_PERIOD
    return period if period in PERIOD_OPTIONS else DEFAULT_PERIOD


def get_live_analytics(db: Session, period_minutes: int | None = None) -> dict[str, Any]:
    """
    Canlı analitik verileri döndürür.
    period_minutes: 30, 60, 360 veya 1440 (dakika); aktif kullanıcı ve dakika grafiği buna göre.
    """
    period = _period_minutes(period_minutes)
    now = datetime.utcnow()
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    period_ago = now - timedelta(minutes=period)
    twenty_four_h_ago = now - timedelta(hours=24)

    # Son N dakikada aktif kullanıcı (Presence)
    active_users_period = (
        db.exec(
            select(func.count(Presence.id)).where(Presence.last_seen_at >= period_ago)
        ).one()
        or 0
    )

    # Dakika bazlı: 30/60 dk için her dakika; 6h/24h için bucket (max 60 nokta)
    minute_labels: list[str] = []
    minute_counts: list[int] = []
    if period <= 60:
        step_minutes = 1
        n_buckets = period
    else:
        step_minutes = max(1, period // 60)
        n_buckets = 60
    for i in range(n_buckets):
        bucket_start = period_ago + timedelta(minutes=i * step_minutes)
        bucket_end = bucket_start + timedelta(minutes=step_minutes)
        if bucket_end > now:
            bucket_end = now
        cnt = (
            db.exec(
                select(func.count(Presence.id))
                .where(Presence.last_seen_at >= bucket_start)
                .where(Presence.last_seen_at < bucket_end)
            ).one()
            or 0
        )
        minute_labels.append(bucket_start.strftime("%H:%M"))
        minute_counts.append(cnt)

    # Ülkelere göre ziyaretçi (AuditLog son 24 saat; country dolu kayıtlar)
    country_rows = (
        db.exec(
            select(AuditLog.country, func.count(AuditLog.id))
            .where(AuditLog.created_at >= twenty_four_h_ago)
            .where(AuditLog.country.isnot(None))
            .where(AuditLog.country != "")
            .group_by(AuditLog.country)
            .order_by(func.count(AuditLog.id).desc())
            .limit(15)
        ).all()
    )
    by_country = [{"country": c or "?", "count": n} for c, n in country_rows]

    # Bugünkü toplam analiz sayısı
    today_analyses = (
        db.exec(
            select(func.count(AnalysisRecord.id)).where(AnalysisRecord.created_at >= today_start)
        ).one()
        or 0
    )

    # Bugünkü ödeme/satış sayısı (completed)
    today_payments = (
        db.exec(
            select(func.count(PaymentOrder.id))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= today_start)
        ).one()
        or 0
    )

    # Bugünkü gelir (EUR) — tamamlanan ödemelerin toplamı
    today_revenue_cents = (
        db.exec(
            select(func.coalesce(func.sum(PaymentOrder.amount_kurus), 0))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= today_start)
        ).one()
        or 0
    )
    today_revenue_eur = round((today_revenue_cents / 100), 2)

    # Conversion: ödeme/analiz oranı (yüzde); analiz 0 ise 0
    conversion_pct = (
        (today_payments / today_analyses * 100) if today_analyses else 0.0
    )

    # Son işlemler (son 10 ödeme)
    orders = list(
        db.exec(
            select(PaymentOrder).order_by(PaymentOrder.id.desc()).limit(10)
        ).all()
    )
    user_ids = {o.user_id for o in orders}
    users_map: dict[int, str] = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or f"#{u.id}"
    last_transactions = [
        {
            "created_at": o.created_at.strftime("%d.%m.%Y %H:%M") if o.created_at else "-",
            "user_email": users_map.get(o.user_id, f"#{o.user_id}"),
            "product": o.product or "-",
            "amount_eur": round((o.amount_kurus or 0) / 100, 2),
            "status": o.status or "pending",
        }
        for o in orders
    ]

    # Cihaz dağılımı: şimdilik mock; ileride AuditLog veya ayrı event tablosuna device alanı eklenebilir
    device_distribution = [
        {"label": "Mobil", "value": 62, "color": "#0EA5A4"},
        {"label": "Masaüstü", "value": 32, "color": "#14b8a6"},
        {"label": "Tablet", "value": 6, "color": "#2dd4bf"},
    ]

    # Trafik kaynakları: şimdilik mock; ileride UTM/Referer ile doldurulabilir
    traffic_sources = [
        {"label": "Organic", "value": 45, "color": "#0EA5A4"},
        {"label": "Reklam", "value": 25, "color": "#0d9488"},
        {"label": "Direct", "value": 20, "color": "#14b8a6"},
        {"label": "Referral", "value": 10, "color": "#2dd4bf"},
    ]

    return {
        "period_minutes": period,
        "active_users_period": active_users_period,
        "minute_labels": minute_labels,
        "minute_counts": minute_counts,
        "by_country": by_country,
        "today_analyses": today_analyses,
        "today_payments": today_payments,
        "today_revenue_eur": today_revenue_eur,
        "conversion_pct": round(conversion_pct, 1),
        "last_transactions": last_transactions,
        "device_distribution": device_distribution,
        "traffic_sources": traffic_sources,
        "last_updated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_updated_display": now.strftime("%d.%m.%Y %H:%M:%S"),
    }
