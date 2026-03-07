import os

from sqlalchemy import inspect, text
from sqlalchemy.exc import OperationalError as SQLOperationalError
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from .config import settings

try:
    import fcntl
except ImportError:
    fcntl = None  # Windows


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


def _init_db_tables():
    inspector = inspect(engine)
    for table in SQLModel.metadata.sorted_tables:
        if inspector.has_table(table.name):
            continue
        try:
            table.create(engine)
        except SQLOperationalError as e:
            if "already exists" not in str(e).lower() and "zaten mevcut" not in str(e).lower():
                raise
        except Exception as e:
            msg = (str(e) + str(getattr(e, "__cause__", "")) + str(getattr(e, "orig", ""))).lower()
            if "already exists" in msg or "zaten mevcut" in msg:
                pass
            else:
                raise


def init_db():
    # Gunicorn 2 worker aynı anda init_db çalıştırıyor; dosya kilidi ile tek işlem tablo oluştursun.
    fd = None
    if fcntl is not None:
        try:
            lock_path = os.environ.get("NORYA_INIT_DB_LOCK", "/tmp/norya_init_db.lock")
            fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o600)
            fcntl.flock(fd, fcntl.LOCK_EX)
        except OSError:
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
                fd = None
    try:
        _init_db_tables()
    finally:
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
                os.close(fd)
            except OSError:
                pass
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
            "ALTER TABLE paymentorder ADD COLUMN invoice_ettn TEXT",
            "ALTER TABLE paymentorder ADD COLUMN invoice_gib_no TEXT",
            "ALTER TABLE paymentorder ADD COLUMN paid_at DATETIME",
            "ALTER TABLE paymentorder ADD COLUMN paytr_payment_amount TEXT",
            "ALTER TABLE paymentorder ADD COLUMN paytr_status TEXT",
            "ALTER TABLE paymentorder ADD COLUMN raw_callback_json TEXT",
            "ALTER TABLE paymentorder ADD COLUMN refunded_at DATETIME",
            "ALTER TABLE paymentorder ADD COLUMN refund_amount_kurus INTEGER",
            "ALTER TABLE analysis_jobs ADD COLUMN prompt_tokens INTEGER",
            "ALTER TABLE analysis_jobs ADD COLUMN completion_tokens INTEGER",
            "ALTER TABLE discountcode ADD COLUMN is_active BOOLEAN DEFAULT 1",
            "ALTER TABLE discountcode ADD COLUMN auto_show_on_checkout BOOLEAN DEFAULT 0",
            "ALTER TABLE discountcode ADD COLUMN auto_apply BOOLEAN DEFAULT 0",
            "ALTER TABLE discountcode ADD COLUMN display_label VARCHAR(120)",
            "ALTER TABLE discountcode ADD COLUMN display_note VARCHAR(256)",
        ):
            try:
                with engine.connect() as conn:
                    conn.execute(text(stmt))
                    conn.commit()
            except Exception:
                # Mevcut kurulumlarda sütun zaten varsa veya tablo yoksa sessizce devam et
                pass
