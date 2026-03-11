# -*- coding: utf-8 -*-
"""Merkezi fiyatlandırma: tüm landing, pricing card ve payment tek kaynaktan (PricingPlan + kampanya)."""
from __future__ import annotations

from datetime import date

from sqlmodel import Session, select

from app.models import DiscountCode, PricingPlan

# Varsayılan fiyatlar (DB boşsa veya hata durumunda; sadece fallback)
# Tek analiz: 14.00 €, Aylık: 54.00 €, Yıllık: 99.00 €
DEFAULT_BASE_CENTS = {"single": 1400, "monthly": 5400, "yearly": 9900}
DEFAULT_PLAN_CODE_MAP = {
    "single_13eur": ("single", 1400),
    "monthly_50eur": ("monthly", 5400),
    "yearly_99eur": ("yearly", 9900),
}


def get_base_prices_cents(db: Session) -> dict[str, int]:
    """Plan baz fiyatlarını (EUR cent) döner. Kaynak: PricingPlan tablosu."""
    try:
        rows = list(db.exec(select(PricingPlan).order_by(PricingPlan.display_order)).all())
        if not rows:
            return dict(DEFAULT_BASE_CENTS)
        out = {}
        for r in rows:
            out[r.product] = r.price_cents
        return out if out else dict(DEFAULT_BASE_CENTS)
    except Exception:
        return dict(DEFAULT_BASE_CENTS)


def get_plan_code_to_product_cents(db: Session) -> dict[str, tuple[str, int]]:
    """plan_code -> (product, price_cents). Pay/checkout ve API için tek kaynak."""
    base = get_base_prices_cents(db)
    return {
        "single_13eur": ("single", base["single"]),
        "monthly_50eur": ("monthly", base["monthly"]),
        "yearly_99eur": ("yearly", base["yearly"]),
    }


def get_campaign_display_overrides(coupon: DiscountCode) -> dict[str, dict[str, int | None]]:
    """Kampanya için eski/yeni fiyat gösterim override'ları (product -> old_cents, new_cents)."""
    overrides = {
        "single": (
            getattr(coupon, "old_price_single_cents", None),
            getattr(coupon, "new_price_single_cents", None),
        ),
        "monthly": (
            getattr(coupon, "old_price_monthly_cents", None),
            getattr(coupon, "new_price_monthly_cents", None),
        ),
        "yearly": (
            getattr(coupon, "old_price_yearly_cents", None),
            getattr(coupon, "new_price_yearly_cents", None),
        ),
    }
    return {p: {"old_cents": o, "new_cents": n} for p, (o, n) in overrides.items()}


def get_active_campaign_with_display(
    db: Session,
    plan_code: str,
    base_prices_cents: dict[str, int] | None = None,
) -> dict | None:
    """
    Seçilen plan için aktif kampanyayı döner; kampanya varsa gösterim için old/new fiyat bilgisi ekler.
    base_prices_cents verilmezse get_base_prices_cents(db) ile alınır.
    """
    from app.services.coupon import get_active_campaign_for_checkout

    if base_prices_cents is None:
        base_prices_cents = get_base_prices_cents(db)
    plan_map = get_plan_code_to_product_cents(db)
    product = (plan_map.get((plan_code or "").strip().lower()) or (None, 0))[0]
    if not product:
        return None
    campaign = get_active_campaign_for_checkout(db, plan_code, plan_code_to_amount=plan_map)
    if not campaign:
        return None
    # Kampanya kaydını bul (display override için)
    code = (campaign.get("code") or "").strip()
    if not code:
        return campaign
    coupon = db.exec(select(DiscountCode).where(DiscountCode.code == code.upper())).first()
    if not coupon:
        return campaign
    overrides = get_campaign_display_overrides(coupon)
    base_cents = base_prices_cents.get(product, 0)
    discount_cents = campaign.get("discount_cents") or 0
    new_cents = base_cents - discount_cents
    old_cents = base_cents
    ov = overrides.get(product, {})
    if ov.get("old_cents") is not None:
        old_cents = ov["old_cents"]
    if ov.get("new_cents") is not None:
        new_cents = ov["new_cents"]
    campaign["old_price_cents"] = old_cents
    campaign["new_price_cents"] = new_cents
    campaign["campaign_badge"] = (getattr(coupon, "campaign_badge", None) or "").strip()
    return campaign
