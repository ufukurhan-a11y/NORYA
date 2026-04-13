import os
from pathlib import Path

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

    # SQLite path'leri `cwd`'ye göre değişmesin diye projedeki mutlak path'e çeviriyoruz.
    # Bu özellikle "attempt to write a readonly database" hatasını azaltır.
    if raw_url.startswith("sqlite:///"):
        file_part = raw_url[len("sqlite:///") :]
        if file_part in (":memory:", ""):
            return raw_url

        # Proje kökü: app/core/database.py -> app/core -> app -> repo kökü
        proj_root = Path(__file__).resolve().parent.parent.parent

        # sqlite:///./norya.db  -> <proj_root>/norya.db
        if file_part.startswith("./"):
            abs_path = (proj_root / file_part[2:]).resolve()
            return f"sqlite:///{abs_path}"

        # sqlite:///norya.db (./ yok) -> <proj_root>/norya.db
        if not file_part.startswith("/") and not file_part.startswith(":"):
            abs_path = (proj_root / file_part).resolve()
            return f"sqlite:///{abs_path}"

        return raw_url

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
            "ALTER TABLE auditlog ADD COLUMN city TEXT",
            "ALTER TABLE analysisrecord ADD COLUMN original_filename TEXT",
            "ALTER TABLE analysisrecord ADD COLUMN original_stored_path TEXT",
            "ALTER TABLE user ADD COLUMN is_banned BOOLEAN DEFAULT 0",
            "ALTER TABLE user ADD COLUMN last_login_at DATETIME",
            "ALTER TABLE user ADD COLUMN account_claimed_at DATETIME",
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
            "ALTER TABLE analysisrecord ADD COLUMN plan_type VARCHAR(16) DEFAULT 'single'",
            "ALTER TABLE paymentorder ADD COLUMN admin_note TEXT",
            "ALTER TABLE paymentorder ADD COLUMN invoice_ettn TEXT",
            "ALTER TABLE paymentorder ADD COLUMN invoice_gib_no TEXT",
            "ALTER TABLE paymentorder ADD COLUMN paid_at DATETIME",
            "ALTER TABLE paymentorder ADD COLUMN paytr_payment_amount TEXT",
            "ALTER TABLE paymentorder ADD COLUMN paytr_status TEXT",
            "ALTER TABLE paymentorder ADD COLUMN raw_callback_json TEXT",
            "ALTER TABLE paymentorder ADD COLUMN refunded_at DATETIME",
            "ALTER TABLE paymentorder ADD COLUMN refund_amount_kurus INTEGER",
            "ALTER TABLE paymentorder ADD COLUMN customer_email TEXT",
            "ALTER TABLE analysis_jobs ADD COLUMN prompt_tokens INTEGER",
            "ALTER TABLE analysis_jobs ADD COLUMN completion_tokens INTEGER",
            "ALTER TABLE discountcode ADD COLUMN is_active BOOLEAN DEFAULT 1",
            "ALTER TABLE discountcode ADD COLUMN auto_show_on_checkout BOOLEAN DEFAULT 0",
            "ALTER TABLE discountcode ADD COLUMN auto_apply BOOLEAN DEFAULT 0",
            "ALTER TABLE discountcode ADD COLUMN display_label VARCHAR(120)",
            "ALTER TABLE discountcode ADD COLUMN display_note VARCHAR(256)",
            "ALTER TABLE discountcode ADD COLUMN campaign_badge VARCHAR(64)",
            "ALTER TABLE discountcode ADD COLUMN old_price_single_cents INTEGER",
            "ALTER TABLE discountcode ADD COLUMN new_price_single_cents INTEGER",
            "ALTER TABLE discountcode ADD COLUMN old_price_monthly_cents INTEGER",
            "ALTER TABLE discountcode ADD COLUMN new_price_monthly_cents INTEGER",
            "ALTER TABLE discountcode ADD COLUMN old_price_yearly_cents INTEGER",
            "ALTER TABLE discountcode ADD COLUMN new_price_yearly_cents INTEGER",
            "ALTER TABLE paymentorder ADD COLUMN quantity INTEGER DEFAULT 1",
            "ALTER TABLE analysisrecord ADD COLUMN institution_id INTEGER",
            "ALTER TABLE auditlog ADD COLUMN institution_id INTEGER",
            "ALTER TABLE auditlog ADD COLUMN entity_type VARCHAR(64)",
            "ALTER TABLE auditlog ADD COLUMN entity_id INTEGER",
            "ALTER TABLE auditlog ADD COLUMN metadata_json TEXT",
            "ALTER TABLE institutions ADD COLUMN status VARCHAR(32) DEFAULT 'pilot'",
            "ALTER TABLE institutions ADD COLUMN seat_limit INTEGER DEFAULT 25",
            "ALTER TABLE institutions ADD COLUMN active_languages VARCHAR(255) DEFAULT 'tr,en'",
            "ALTER TABLE institutions ADD COLUMN onboarding_completed BOOLEAN DEFAULT 0",
            "ALTER TABLE institutions ADD COLUMN updated_at DATETIME",
            # Lead e-posta onayları (KVKK/GDPR)
            "ALTER TABLE email_leads ADD COLUMN consent_kvkk BOOLEAN DEFAULT 0",
            "ALTER TABLE email_leads ADD COLUMN consent_gdpr BOOLEAN DEFAULT 0",
            "ALTER TABLE email_leads ADD COLUMN consent_at DATETIME",
            # Lead UTM tracking
            "ALTER TABLE email_leads ADD COLUMN utm_source VARCHAR(128)",
            "ALTER TABLE email_leads ADD COLUMN utm_medium VARCHAR(128)",
            "ALTER TABLE email_leads ADD COLUMN utm_campaign VARCHAR(128)",
            "ALTER TABLE email_leads ADD COLUMN utm_content VARCHAR(128)",
            "ALTER TABLE email_leads ADD COLUMN utm_term VARCHAR(128)",
            "ALTER TABLE email_leads ADD COLUMN drip_step INTEGER DEFAULT 0",
            "ALTER TABLE email_leads ADD COLUMN drip_last_sent_at DATETIME",
            "ALTER TABLE email_leads ADD COLUMN unsubscribed BOOLEAN DEFAULT 0",
            # User registration tracking (email verification admin)
            "CREATE TABLE IF NOT EXISTS userregistration (id INTEGER, email VARCHAR, full_name VARCHAR DEFAULT '', status VARCHAR DEFAULT 'pending', user_id INTEGER, verification_mail_sent_at DATETIME, mail_send_error VARCHAR, source VARCHAR, ip_address VARCHAR, user_agent VARCHAR, created_at DATETIME, verified_at DATETIME, PRIMARY KEY (id))",
            "CREATE INDEX IF NOT EXISTS ix_userregistration_email ON userregistration (email)",
            "CREATE INDEX IF NOT EXISTS ix_userregistration_status ON userregistration (status)",
            "CREATE INDEX IF NOT EXISTS ix_userregistration_user_id ON userregistration (user_id)",
            "CREATE INDEX IF NOT EXISTS ix_userregistration_created_at ON userregistration (created_at)",
            # Frontend IP (tarayıcı tarafı, cookie'den)
            "ALTER TABLE userregistration ADD COLUMN frontend_ip_address VARCHAR",
            # Multi-tenant fields
            "ALTER TABLE institutions ADD COLUMN tenant_slug VARCHAR(128)",
            "ALTER TABLE institutions ADD COLUMN billing_wallet_balance INTEGER DEFAULT 0",
            "ALTER TABLE institutions ADD COLUMN cost_per_analysis INTEGER DEFAULT 100",
            "ALTER TABLE institutions ADD COLUMN subdomain VARCHAR(255)",
            "ALTER TABLE institutions ADD COLUMN wallet_low_threshold INTEGER DEFAULT 20000",
            "ALTER TABLE institutions ADD COLUMN wallet_last_alert DATETIME",
            "CREATE TABLE IF NOT EXISTS tenant_wallet_transactions (id INTEGER, institution_id INTEGER, amount_cents INTEGER, transaction_type VARCHAR(32), description VARCHAR(512), created_at DATETIME, PRIMARY KEY (id), FOREIGN KEY(institution_id) REFERENCES institutions(id))",
            "CREATE INDEX IF NOT EXISTS ix_tenant_wallet_transactions_institution_id ON tenant_wallet_transactions (institution_id)",
            # Tenant customization fields
            "ALTER TABLE institutions ADD COLUMN logo_url VARCHAR(512)",
            "ALTER TABLE institutions ADD COLUMN primary_color VARCHAR(16)",
            "ALTER TABLE institutions ADD COLUMN secondary_color VARCHAR(16)",
            "ALTER TABLE institutions ADD COLUMN report_header_text VARCHAR(256)",
            "ALTER TABLE institutions ADD COLUMN report_footer_text VARCHAR(256)",
            "ALTER TABLE institutions ADD COLUMN custom_css TEXT",
            # Tenant rate limiting
            "ALTER TABLE institutions ADD COLUMN daily_analysis_limit INTEGER",
            "ALTER TABLE institutions ADD COLUMN hourly_analysis_limit INTEGER",
            # Tenant alert settings
            "ALTER TABLE institutions ADD COLUMN alert_email_enabled BOOLEAN DEFAULT 1",
            "ALTER TABLE institutions ADD COLUMN alert_sms_enabled BOOLEAN DEFAULT 0",
            "ALTER TABLE institutions ADD COLUMN alert_phone VARCHAR(64)",
            # Tenant audit log
            "CREATE TABLE IF NOT EXISTS tenant_audit_logs (id INTEGER, institution_id INTEGER, user_id INTEGER, action VARCHAR(64), entity_type VARCHAR(64), entity_id INTEGER, ip_address VARCHAR(64), user_agent VARCHAR(512), detail VARCHAR(1024), metadata_json TEXT, created_at DATETIME, PRIMARY KEY (id), FOREIGN KEY(institution_id) REFERENCES institutions(id), FOREIGN KEY(user_id) REFERENCES user(id))",
            "CREATE INDEX IF NOT EXISTS ix_tenant_audit_logs_institution_id ON tenant_audit_logs (institution_id)",
            "CREATE INDEX IF NOT EXISTS ix_tenant_audit_logs_user_id ON tenant_audit_logs (user_id)",
            "CREATE INDEX IF NOT EXISTS ix_tenant_audit_logs_action ON tenant_audit_logs (action)",
            # Tenant API keys
            "CREATE TABLE IF NOT EXISTS tenant_api_keys (id INTEGER, institution_id INTEGER, name VARCHAR(128), key_hash VARCHAR(128), key_prefix VARCHAR(16), is_active BOOLEAN DEFAULT 1, last_used_at DATETIME, expires_at DATETIME, created_by_user_id INTEGER, created_at DATETIME, updated_at DATETIME, PRIMARY KEY (id), FOREIGN KEY(institution_id) REFERENCES institutions(id), FOREIGN KEY(created_by_user_id) REFERENCES user(id))",
            "CREATE UNIQUE INDEX IF NOT EXISTS ix_tenant_api_keys_key_hash ON tenant_api_keys (key_hash)",
            "CREATE INDEX IF NOT EXISTS ix_tenant_api_keys_institution_id ON tenant_api_keys (institution_id)",
        ):
            try:
                with engine.connect() as conn:
                    conn.execute(text(stmt))
                    conn.commit()
            except Exception:
                # Mevcut kurulumlarda sütun zaten varsa veya tablo yoksa sessizce devam et
                pass
    # PostgreSQL: admin dashboard ve maliyet sorguları bu sütunlara ihtiyaç duyar.
    # SQLite için yukarıdaki blokta ekleniyordu; eski Postgres kurulumlarında eksik kalabiliyordu (500).
    if DATABASE_URL.startswith("postgresql"):
        for stmt in (
            "ALTER TABLE analysis_jobs ADD COLUMN IF NOT EXISTS prompt_tokens INTEGER",
            "ALTER TABLE analysis_jobs ADD COLUMN IF NOT EXISTS completion_tokens INTEGER",
        ):
            try:
                with engine.begin() as conn:
                    conn.execute(text(stmt))
            except Exception:
                pass
    # Bazı ortamlarda yukarıdaki ALTER sessizce başarısız olabiliyor; şema denetimi ile tamamla
    if DATABASE_URL.startswith("sqlite"):
        try:
            insp = inspect(engine)
            if insp.has_table("paymentorder"):
                col_names = {c["name"] for c in insp.get_columns("paymentorder")}
                if "quantity" not in col_names:
                    with engine.begin() as conn:
                        conn.execute(
                            text("ALTER TABLE paymentorder ADD COLUMN quantity INTEGER DEFAULT 1")
                        )
        except Exception:
            pass
