from datetime import datetime

from sqlmodel import Field, SQLModel


class PaymentOrder(SQLModel, table=True):
    """Ödeme siparişi: merchant_oid ile callback'te kullanıcıya hak tanınır. Tahsilat EUR."""

    id: int | None = Field(default=None, primary_key=True)
    merchant_oid: str = Field(unique=True, index=True)
    user_id: int
    product: str  # "single" | "monthly" | "yearly"
    amount_kurus: int  # Tutar en küçük birimde: EUR için cent (13,00 € = 1300)
    currency: str = "EUR"  # Para birimi (tahsilat EUR)
    status: str = "pending"  # pending | completed | failed
    paytr_transaction_id: str | None = Field(default=None, index=True)
    # Idempotent işleme bayrağı
    is_processed: bool = False
    processed_at: datetime | None = None
    coupon_code_used: str | None = Field(default=None, max_length=64)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
    admin_note: str | None = None  # İade / not (admin panelinden)
    # E-arşiv fatura (GİB)
    invoice_ettn: str | None = Field(default=None, index=True)   # GİB'deki fatura ETTN
    invoice_gib_no: str | None = Field(default=None)            # GİB belge numarası (GIB2025...)
