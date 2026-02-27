"""İndirim kuponu doğrulama ve indirim hesaplama."""
from datetime import date, datetime, timezone

from sqlmodel import Session, select

from app.models import DiscountCode


def _parse_days_of_month(s: str | None) -> set[int] | None:
    """'1-7' veya '1,15,20' gibi metni gün numaraları setine çevirir. Boş/None -> None (her gün)."""
    if not s or not (s := s.strip()):
        return None
    out: set[int] = set()
    for part in s.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            try:
                lo, hi = int(a.strip()), int(b.strip())
                if 1 <= lo <= 31 and 1 <= hi <= 31:
                    out.update(range(lo, hi + 1))
            except ValueError:
                continue
        else:
            try:
                n = int(part)
                if 1 <= n <= 31:
                    out.add(n)
            except ValueError:
                continue
    return out if out else None


def validate_coupon(
    db: Session,
    code: str,
    product: str,
    base_amount_cents: int,
) -> tuple[int, str | None]:
    """
    Kuponu doğrular ve indirim tutarını (euro cent) döner.
    (indirim_tutarı_cent, hata_mesajı). Hata yoksa hata_mesajı None.
    """
    if not code or not (code := code.strip()):
        return 0, "İndirim kodu girilmedi."
    code_upper = code.upper().strip()
    stmt = select(DiscountCode).where(DiscountCode.code == code_upper)
    coupon = db.exec(stmt).first()
    if not coupon:
        return 0, "Geçersiz indirim kodu."

    today = date.today()
    if coupon.valid_from and today < coupon.valid_from:
        return 0, "Bu indirim kodu henüz geçerli değil."
    if coupon.valid_until and today > coupon.valid_until:
        return 0, "Bu indirim kodunun süresi dolmuş."

    days_ok = _parse_days_of_month(coupon.valid_days_of_month)
    if days_ok is not None and today.day not in days_ok:
        return 0, "Bu indirim kodu bugün geçerli değil (sadece ayın belirli günlerinde geçerli)."

    if coupon.max_uses is not None and coupon.use_count >= coupon.max_uses:
        return 0, "Bu indirim kodunun kullanım limiti dolmuş."

    if coupon.products:
        allowed = [p.strip().lower() for p in coupon.products.split(",") if p.strip()]
        if allowed and product.lower() not in allowed:
            return 0, "Bu indirim kodu seçilen ürün için geçerli değil."

    if coupon.discount_type == "percent":
        if not (1 <= coupon.discount_value <= 100):
            return 0, "Geçersiz indirim oranı."
        discount_cents = int(base_amount_cents * coupon.discount_value / 100)
    elif coupon.discount_type == "fixed":
        discount_cents = min(coupon.discount_value, base_amount_cents)
    else:
        return 0, "Geçersiz indirim tipi."

    if discount_cents <= 0:
        return 0, None
    return discount_cents, None


def apply_coupon_use(db: Session, code: str) -> None:
    """Kupon kullanım sayacını artırır (ödeme tamamlandığında çağrılabilir)."""
    code_upper = code.upper().strip()
    stmt = select(DiscountCode).where(DiscountCode.code == code_upper)
    coupon = db.exec(stmt).first()
    if coupon:
        coupon.use_count = (coupon.use_count or 0) + 1
        db.add(coupon)
        db.commit()
