"""add account_claimed_at to user

Guest users (created at checkout) have None; set when they claim account via register.
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, DateTime

revision: str = "0006_user_account_claimed_at"
down_revision: Union[str, None] = "0005_add_customer_email"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        op.add_column("user", Column("account_claimed_at", DateTime, nullable=True))
    except Exception:
        pass


def downgrade() -> None:
    pass
