"""pricing plan and campaign display overrides

- pricingplan tablosu: merkezi plan fiyatları (EUR cent)
- discountcode: campaign_badge, old/new_price_*_cents (gösterim override)
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String

revision: str = "0003_pricing_plan_and_campaign_display"
down_revision: Union[str, None] = "0002_add_order_quantity"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # pricingplan tablosu
    op.create_table(
        "pricingplan",
        Column("id", Integer(), primary_key=True, autoincrement=True),
        Column("code", String(32), nullable=False),
        Column("product", String(16), nullable=False),
        Column("price_cents", Integer(), nullable=False),
        Column("display_order", Integer(), nullable=False, server_default="0"),
    )
    op.create_index("ix_pricingplan_code", "pricingplan", ["code"], unique=True)
    # Seed
    op.execute(
        "INSERT OR IGNORE INTO pricingplan (code, product, price_cents, display_order) VALUES ('single_13eur', 'single', 1404, 0)"
    )
    op.execute(
        "INSERT OR IGNORE INTO pricingplan (code, product, price_cents, display_order) VALUES ('monthly_50eur', 'monthly', 5400, 1)"
    )
    op.execute(
        "INSERT OR IGNORE INTO pricingplan (code, product, price_cents, display_order) VALUES ('yearly_99eur', 'yearly', 10692, 2)"
    )
    # discountcode: campaign display override sütunları
    for col_name in (
        "campaign_badge",
        "old_price_single_cents",
        "new_price_single_cents",
        "old_price_monthly_cents",
        "new_price_monthly_cents",
        "old_price_yearly_cents",
        "new_price_yearly_cents",
    ):
        try:
            if "badge" in col_name:
                op.add_column("discountcode", Column(col_name, String(64), nullable=True))
            else:
                op.add_column("discountcode", Column(col_name, Integer(), nullable=True))
        except Exception:
            pass


def downgrade() -> None:
    pass
