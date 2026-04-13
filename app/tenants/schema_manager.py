"""PostgreSQL schema-per-tenant lifecycle management.

In development (SQLite), schema isolation is not available.
Tenant isolation is enforced at the application level via institution_id filtering.
"""
import logging
from sqlmodel import Session, text

logger = logging.getLogger(__name__)

# Tables that are duplicated per tenant schema
TENANT_TABLES = [
    "enterprise_cases",
    "enterprise_reports",
    "analysisrecord",
]


def is_postgresql(database_url: str) -> bool:
    """Check if the database URL points to PostgreSQL."""
    return database_url.startswith("postgresql")


def ensure_tenant_schema(session: Session, tenant_slug: str, database_url: str) -> bool:
    """Create a dedicated schema for a tenant and mirror tenant-specific tables.

    Only works with PostgreSQL. Returns True if successful, False if not applicable (SQLite).
    """
    if not is_postgresql(database_url):
        logger.info("SQLite mode: schema-per-tenant not available, using application-level isolation")
        return False

    schema_name = f"tenant_{tenant_slug}"

    try:
        # Create the schema
        session.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
        session.commit()

        # Mirror tenant-specific tables into the new schema
        for table_name in TENANT_TABLES:
            # Create table in tenant schema with same structure as public
            session.execute(text(f"""
                CREATE TABLE IF NOT EXISTS {schema_name}.{table_name}
                (LIKE public.{table_name} INCLUDING ALL)
            """))
            session.commit()

        logger.info(f"Created tenant schema '{schema_name}' with tables: {TENANT_TABLES}")
        return True

    except Exception as e:
        session.rollback()
        logger.error(f"Failed to create tenant schema '{schema_name}': {e}")
        raise


def drop_tenant_schema(session: Session, tenant_slug: str, database_url: str) -> bool:
    """Remove a tenant's dedicated schema and all its data.

    Only works with PostgreSQL. Returns True if successful, False if not applicable (SQLite).
    """
    if not is_postgresql(database_url):
        return False

    schema_name = f"tenant_{tenant_slug}"

    try:
        session.execute(text(f"DROP SCHEMA IF EXISTS {schema_name} CASCADE"))
        session.commit()
        logger.info(f"Dropped tenant schema '{schema_name}'")
        return True

    except Exception as e:
        session.rollback()
        logger.error(f"Failed to drop tenant schema '{schema_name}': {e}")
        raise


def set_tenant_search_path(session: Session, tenant_slug: str, database_url: str) -> bool:
    """Set PostgreSQL search_path to tenant schema + public.

    This ensures that queries resolve to tenant-specific tables first.
    Only works with PostgreSQL. Returns True if successful, False if not applicable (SQLite).
    """
    if not is_postgresql(database_url):
        return False

    schema_name = f"tenant_{tenant_slug}"

    try:
        session.execute(text(f"SET search_path TO {schema_name}, public"))
        return True

    except Exception as e:
        logger.error(f"Failed to set search_path to '{schema_name}': {e}")
        raise


def reset_search_path(session: Session, database_url: str) -> bool:
    """Reset PostgreSQL search_path to public only.

    Only works with PostgreSQL. Returns True if successful, False if not applicable (SQLite).
    """
    if not is_postgresql(database_url):
        return False

    try:
        session.execute(text("SET search_path TO public"))
        return True

    except Exception as e:
        logger.error(f"Failed to reset search_path: {e}")
        raise
