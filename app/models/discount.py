"""İndirim kuponu: kod, yüzde/sabit indirim, geçerlilik tarihi ve ayın belirli günleri."""
from datetime import date, datetime

from sqlmodel import Field, SQLModel


class DiscountCode(SQLModel, table=True):
    """İndirim kodu: admin tarafından oluşturulur, ödeme sırasında kullanılır."""

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True, max_length=64)  # örn: indirim20
    discount_type: str = Field(max_length=16)  # "percent" | "fixed"
    discount_value: int = Field()  # percent: 1-100, fixed: euro cent
    valid_from: date | None = Field(default=None)  # Bu tarihten itibaren geçerli (dahil)
    valid_until: date | None = Field(default=None)  # Bu tarihe kadar geçerli (dahil)
    # Ayın sadece bu günlerinde geçerli; boş = her gün. Örn: "1,2,3,4,5,6,7" veya "1-7"
    valid_days_of_month: str | None = Field(default=None, max_length=128)
    max_uses: int | None = Field(default=None)  # null = sınırsız
    use_count: int = Field(default=0)
    # Hangi ürünlerde geçerli: boş = hepsi. Örn: "single,monthly"
    products: str | None = Field(default=None, max_length=64)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)
