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
    ):
        try:
            with engine.connect() as conn:
                conn.execute(text(stmt))
                conn.commit()
        except Exception:
            pass
