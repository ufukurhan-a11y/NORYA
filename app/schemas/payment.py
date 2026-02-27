from typing import Literal

from pydantic import BaseModel


class CreateSessionRequest(BaseModel):
    """Önce ödeme: checkout session açılır, ödeme sonrası webhook ile hak tanınır."""
    product: Literal["single", "monthly", "yearly"]
    success_url: str | None = None
    cancel_url: str | None = None
    coupon_code: str | None = None


class GrantPaymentRequest(BaseModel):
    """Destek: Ödedim hak gelmedi durumunda manuel hak tanıma (admin_secret gerekir)."""
    merchant_oid: str
    admin_secret: str


class GuestSessionRequest(BaseModel):
    """Kayıt olmadan tek analiz ödemesi: sadece product=single kabul edilir."""
    product: Literal["single"] = "single"
    email: str
    full_name: str | None = None
    success_url: str | None = None
    cancel_url: str | None = None
    coupon_code: str | None = None
