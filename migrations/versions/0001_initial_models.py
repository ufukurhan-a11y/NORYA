"""initial models

Baseline migration generated from current SQLModel metadata.
Existing SQLite tables are assumed to match these models.

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel  # noqa: F401


revision: str = "0001_initial_models"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Bu migration, mevcut canlı veritabanını bozmayacak şekilde boş bırakıldı.
    # Yeni ortamlarda tablolar SQLModel.metadata.create_all(engine) ile oluşturuluyor.
    pass


def downgrade() -> None:
    # Bilinçli olarak no-op; geriye dönük tablo silme yapılmaz.
    pass

