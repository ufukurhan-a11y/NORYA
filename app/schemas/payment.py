from typing import Literal

from pydantic import BaseModel


class CreateSessionRequest(BaseModel):
    """Önce ödeme: checkout session açılır, ödeme sonrası webhook ile hak tanınır."""
    product: Literal["single", "monthly", "yearly"]
    success_url: str | None = None
    cancel_url: str | None = None
    coupon_code: str | None = None
    consent_mesafeli: bool = False  # Mesafeli Satış Sözleşmesi kabulü (PayTR zorunlu)
    consent_kvkk: bool = False  # Gizlilik/KVKK kabulü (PayTR zorunlu)


class GrantPaymentRequest(BaseModel):
    """Destek: Ödedim hak gelmedi durumunda manuel hak tanıma."""
    merchant_oid: str
    admin_secret: str | None = None


class GuestSessionRequest(BaseModel):
    """Kayıt olmadan tek analiz ödemesi: sadece product=single kabul edilir."""
    product: Literal["single"] = "single"
    email: str
    full_name: str | None = None
    success_url: str | None = None
    cancel_url: str | None = None
    coupon_code: str | None = None
    consent_mesafeli: bool = False
    consent_kvkk: bool = False


class PaytrInitRequest(BaseModel):
    """PayTR tam sayfa ödeme başlatma: plan_code, opsiyonel kupon, dil (success/fail ve PayTR sayfası)."""
    plan_code: str  # single_13eur | monthly_50eur | yearly_99eur
    quantity: int = 1  # Tek analiz: adet (1-10); Aylık: ay (1-6); Yıllık: yıl (1-3)
    user_id: int | None = None
    email: str | None = None
    name: str | None = None
    coupon_code: str | None = None  # Ödeme sayfasında uygulanan kupon; backend doğrular.
    lang: str | None = None  # Ödeme sayfası dili; success/fail ve PayTR ekranı bu dilde (tr, en vb.)
