"""add order quantity

PaymentOrder.quantity: adet/süre çarpanı (tek ödemede birden fazla birim).
"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer

revision: str = "0002_add_order_quantity"
down_revision: Union[str, None] = "0001_initial_models"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    try:
        op.add_column("paymentorder", Column("quantity", Integer, nullable=False, server_default="1"))
    except Exception:
        pass  # Sütun zaten varsa atla (create_all ile oluşturulmuş olabilir)


def downgrade() -> None:
    pass  # SQLite DROP COLUMN desteklenmiyor
