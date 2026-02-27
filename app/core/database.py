from sqlalchemy import text
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from .config import settings


def _normalized_database_url(raw_url: str) -> str:
    """
    DATABASE_URL normalizasyonu:
    - postgres:// veya postgresql:// ise psycopg3 dialekti ile çalışacak şekilde dönüştür.
    - Diğer tüm durumlarda olduğu gibi bırak (SQLite vs.).
    """
    if not raw_url:
        return "sqlite:///./norya.db"
    raw_url = raw_url.strip()
    # postgres://...  -> postgresql+psycopg://...
    if raw_url.startswith("postgres://"):
        return "postgresql+psycopg://" + raw_url[len("postgres://") :]
    # postgresql://... (driver belirtilmemiş) -> postgresql+psycopg://...
    if raw_url.startswith("postgresql://") and "+psycopg" not in raw_url.split("://", 1)[0]:
        return "postgresql+psycopg://" + raw_url[len("postgresql://") :]
    return raw_url


DATABASE_URL = _normalized_database_url(settings.database_url)

# In-memory SQLite: tek bağlantı kullan ki init_db tabloları tüm isteklerde görünsün (testler için)
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
_use_static_pool = DATABASE_URL.startswith("sqlite") and ":memory:" in DATABASE_URL
engine = create_engine(
    DATABASE_URL,
    connect_args=_connect_args,
    poolclass=StaticPool if _use_static_pool else None,
)


def get_db():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
    # Mevcut tablolara yeni sütunlar (Yalnızca SQLite için incremental ALTER komutları)
    if DATABASE_URL.startswith("sqlite"):
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
            "ALTER TABLE paymentorder ADD COLUMN is_processed BOOLEAN DEFAULT 0",
            "ALTER TABLE paymentorder ADD COLUMN processed_at DATETIME",
            "CREATE UNIQUE INDEX IF NOT EXISTS ix_paymentorder_paytr_transaction_id ON paymentorder (paytr_transaction_id)",
            "ALTER TABLE paymentorder ADD COLUMN coupon_code_used TEXT",
            "ALTER TABLE analysisrecord ADD COLUMN is_favorite BOOLEAN DEFAULT 0",
            "ALTER TABLE paymentorder ADD COLUMN admin_note TEXT",
        ):
            try:
                with engine.connect() as conn:
                    conn.execute(text(stmt))
                    conn.commit()
            except Exception:
                # Mevcut kurulumlarda sütun zaten varsa veya tablo yoksa sessizce devam et
                pass
