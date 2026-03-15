"""add plan_type to analysisrecord

Sonuç akışında paket tipi: single | monthly | yearly (feature gating altyapısı).
Mevcut kayıtlar varsayılan 'single' alır (backward compatibility).
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import text

revision: str = "0007_analysis_plan_type"
down_revision: Union[str, None] = "0006_user_account_claimed_at"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        conn = op.get_bind()
        conn.execute(text("ALTER TABLE analysisrecord ADD COLUMN plan_type VARCHAR(16) DEFAULT 'single'"))
    except Exception:
        pass


def downgrade() -> None:
    pass
