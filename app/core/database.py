from sqlalchemy import text
from sqlmodel import Session, SQLModel, create_engine

from .config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {},
)


def get_db():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
    # Mevcut tablolara yeni sütunlar (SQLite)
    for stmt in (
        "ALTER TABLE user ADD COLUMN email_verified_at DATETIME",
        "ALTER TABLE analysisrecord ADD COLUMN doctor_notes TEXT",
        "ALTER TABLE user ADD COLUMN plan TEXT DEFAULT 'free'",
        "ALTER TABLE user ADD COLUMN extra_credits INTEGER DEFAULT 0",
        "ALTER TABLE user ADD COLUMN created_at DATETIME",
        "ALTER TABLE user ADD COLUMN phone TEXT",
        "ALTER TABLE user ADD COLUMN country TEXT",
        "ALTER TABLE auditlog ADD COLUMN country TEXT",
        "ALTER TABLE analysisrecord ADD COLUMN original_filename TEXT",
        "ALTER TABLE analysisrecord ADD COLUMN original_stored_path TEXT",
        "ALTER TABLE user ADD COLUMN is_banned BOOLEAN DEFAULT 0",
        "ALTER TABLE user ADD COLUMN last_login_at DATETIME",
        "ALTER TABLE presence ADD COLUMN ip TEXT",
        "ALTER TABLE presence ADD COLUMN country TEXT",
        "ALTER TABLE presence ADD COLUMN current_page TEXT",
        "ALTER TABLE paymentorder ADD COLUMN paytr_transaction_id TEXT",
        "ALTER TABLE paymentorder ADD COLUMN currency TEXT",
    ):
        try:
            with engine.connect() as conn:
                conn.execute(text(stmt))
                conn.commit()
        except Exception:
            pass
