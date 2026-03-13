"""auditlog city column

Admin Live Analytics: ülke + şehir takibi (GA4 / Search Console benzeri).
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, String

revision: str = "0004_auditlog_city"
down_revision: Union[str, None] = "0003_pricing_plan_and_campaign_display"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        op.add_column("auditlog", Column("city", String(128), nullable=True))
    except Exception:
        pass  # Sütun zaten varsa atla


def downgrade() -> None:
    pass  # SQLite DROP COLUMN desteklenmiyor
