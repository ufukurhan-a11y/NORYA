import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

# Proje kökünü sys.path'e ekle (app.* importları için)
BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

from app.core.database import DATABASE_URL  # noqa: E402

# Alembic Config nesnesi; alembic.ini'den gelir
config = context.config

# sqlalchemy.url'i uygulamadaki DATABASE_URL ile override et
if config.get_main_option("sqlalchemy.url") != str(DATABASE_URL):
    config.set_main_option("sqlalchemy.url", str(DATABASE_URL))

# Log yapılandırması
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Hedef metadata: tüm SQLModel tabloları
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """'offline' mod: engine oluşturmadan sadece SQL üretir."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """'online' mod: gerçek veritabanı bağlantısı ile migration çalıştırır."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

