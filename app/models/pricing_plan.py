"""Merkezi fiyat planları: single, monthly, yearly. Admin'den güncellenir; tüm sayfalar buradan beslenir."""
from sqlmodel import Field, SQLModel


class PricingPlan(SQLModel, table=True):
    """Plan baz fiyatı (EUR cent). code: single_13eur | monthly_50eur | yearly_99eur."""

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(unique=True, index=True, max_length=32)  # single_13eur, monthly_50eur, yearly_99eur
    product: str = Field(max_length=16)  # single | monthly | yearly
    price_cents: int = Field()  # EUR cent (1404 = 14.04 €)
    display_order: int = Field(default=0)  # Sıralama (0,1,2)
