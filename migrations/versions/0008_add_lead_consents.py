"""add consent fields to email_leads

KVKK/GDPR e-posta iletişimi onaylarını saklamak için:
- consent_kvkk (bool)
- consent_gdpr (bool)
- consent_at (datetime)
"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy import Boolean, Column, DateTime

revision: str = "0008_add_lead_consents"
down_revision: Union[str, None] = "0007_analysis_plan_type"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        op.add_column("email_leads", Column("consent_kvkk", Boolean, nullable=False, server_default="0"))
    except Exception:
        pass
    try:
        op.add_column("email_leads", Column("consent_gdpr", Boolean, nullable=False, server_default="0"))
    except Exception:
        pass
    try:
        op.add_column("email_leads", Column("consent_at", DateTime, nullable=True))
    except Exception:
        pass


def downgrade() -> None:
    pass  # SQLite DROP COLUMN desteklenmiyor

