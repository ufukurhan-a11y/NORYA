"""İndirim kuponu / kampanya: kod, yüzde/sabit indirim, geçerlilik, checkout’ta gösterim."""
from datetime import date, datetime

from sqlmodel import Field, SQLModel


class DiscountCode(SQLModel, table=True):
    """İndirim kodu / kampanya: admin tarafından oluşturulur; ödeme sayfasında manuel veya otomatik gösterilir."""

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True, max_length=64)  # örn: INDIRIM20
    discount_type: str = Field(max_length=16)  # "percent" | "fixed"
    discount_value: int = Field()  # percent: 1-100, fixed: euro cent
    valid_from: date | None = Field(default=None)  # Başlangıç (dahil)
    valid_until: date | None = Field(default=None)  # Bitiş (dahil)
    valid_days_of_month: str | None = Field(default=None, max_length=128)  # Boş = her gün
    max_uses: int | None = Field(default=None)
    use_count: int = Field(default=0)
    # Hangi planlarda geçerli: boş = hepsi. Örn: "single,monthly,yearly"
    products: str | None = Field(default=None, max_length=64)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)

    # Kampanya: checkout’ta otomatik gösterim ve uygulama
    is_active: bool = Field(default=True)  # Admin’den kapatılabilir
    auto_show_on_checkout: bool = Field(default=False)  # Ödeme sayfasında kampanya alanı göster
    auto_apply: bool = Field(default=False)  # True ise sayfa açıldığında otomatik uygula
    display_label: str | None = Field(default=None, max_length=120)  # Örn: "%20 indirim"
    display_note: str | None = Field(default=None, max_length=256)  # Kısa açıklama
