"""add customer_email to PaymentOrder

Store email at purchase for guest/linked access and account linking.
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, String

revision: str = "0005_add_customer_email"
down_revision: Union[str, None] = "0004_auditlog_city"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        op.add_column("paymentorder", Column("customer_email", String(255), nullable=True))
    except Exception:
        pass


def downgrade() -> None:
    pass  # SQLite DROP COLUMN not supported
