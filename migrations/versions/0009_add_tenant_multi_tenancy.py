"""add multi-tenant support: tenant_slug, wallet fields, tenant_wallet_transactions table

Multi-tenant hospital platform:
- tenant_slug: unique URL-safe identifier for path-based routing (/hastane/{slug}/...)
- billing_wallet_balance: prepaid wallet in cents
- cost_per_analysis: credit cost per analysis in cents
- wallet_low_threshold: alert threshold for low balance
- wallet_last_alert: timestamp of last low balance alert
- subdomain: optional custom domain (future-proofing)
- tenant_wallet_transactions: audit trail for wallet operations
- tenant_audit_logs: KVKK/GDPR compliant activity logging
- tenant_api_keys: API key management for hospital integrations
- customization fields: logo, colors, report templates
- rate limiting: daily/hourly analysis limits per tenant
- alert settings: email/SMS low balance alerts
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

revision: str = "0009_add_tenant_multi_tenancy"
down_revision: Union[str, None] = "0008_add_lead_consents"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add tenant fields to institutions table
    columns_to_add = [
        ("tenant_slug", sa.String(128), True),
        ("billing_wallet_balance", sa.Integer(), False, 0),
        ("cost_per_analysis", sa.Integer(), False, 100),
        ("subdomain", sa.String(255), True),
        ("wallet_low_threshold", sa.Integer(), False, 20000),
        ("wallet_last_alert", sa.DateTime(), True),
        # Customization fields
        ("logo_url", sa.String(512), True),
        ("primary_color", sa.String(16), True),
        ("secondary_color", sa.String(16), True),
        ("report_header_text", sa.String(256), True),
        ("report_footer_text", sa.String(256), True),
        ("custom_css", sa.Text(), True),
        # Rate limiting
        ("daily_analysis_limit", sa.Integer(), True),
        ("hourly_analysis_limit", sa.Integer(), True),
        # Alert settings
        ("alert_email_enabled", sa.Boolean(), False, True),
        ("alert_sms_enabled", sa.Boolean(), False, False),
        ("alert_phone", sa.String(64), True),
        # Auto-renew (recurring payment)
        ("auto_renew_enabled", sa.Boolean(), False, False),
        ("auto_renew_amount_cents", sa.Integer(), False, 100000),
        ("auto_renew_threshold_cents", sa.Integer(), False, 20000),
        ("auto_renew_interval_days", sa.Integer(), False, 30),
        ("auto_renew_last_at", sa.DateTime(), True),
        ("paytr_utoken", sa.String(256), True),
        ("paytr_ctoken", sa.String(256), True),
    ]

    for col_def in columns_to_add:
        col_name = col_def[0]
        col_type = col_def[1]
        nullable = col_def[2]
        default = col_def[3] if len(col_def) > 3 else None

        try:
            col = sa.Column(col_name, col_type, nullable=nullable)
            if default is not None:
                col.server_default = sa.text(str(default))
            op.add_column("institutions", col)
        except Exception:
            # Column may already exist
            pass

    # Create unique index on tenant_slug
    try:
        op.create_index("ix_institutions_tenant_slug", "institutions", ["tenant_slug"], unique=True)
    except Exception:
        pass

    # Create tenant_wallet_transactions table
    try:
        op.create_table(
            "tenant_wallet_transactions",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("institution_id", sa.Integer(), sa.ForeignKey("institutions.id"), nullable=False, index=True),
            sa.Column("amount_cents", sa.Integer(), nullable=False),
            sa.Column("transaction_type", sa.String(32), nullable=False),
            sa.Column("description", sa.String(512), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        )
        op.create_index("ix_tenant_wallet_transactions_institution_id", "tenant_wallet_transactions", ["institution_id"])
    except Exception:
        pass

    # Create tenant_audit_logs table
    try:
        op.create_table(
            "tenant_audit_logs",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("institution_id", sa.Integer(), sa.ForeignKey("institutions.id"), nullable=False, index=True),
            sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=True, index=True),
            sa.Column("action", sa.String(64), nullable=False),
            sa.Column("entity_type", sa.String(64), nullable=True),
            sa.Column("entity_id", sa.Integer(), nullable=True, index=True),
            sa.Column("ip_address", sa.String(64), nullable=True),
            sa.Column("user_agent", sa.String(512), nullable=True),
            sa.Column("detail", sa.String(1024), nullable=True),
            sa.Column("metadata_json", sa.Text(), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        )
        op.create_index("ix_tenant_audit_logs_institution_id", "tenant_audit_logs", ["institution_id"])
        op.create_index("ix_tenant_audit_logs_user_id", "tenant_audit_logs", ["user_id"])
        op.create_index("ix_tenant_audit_logs_action", "tenant_audit_logs", ["action"])
    except Exception:
        pass

    # Create tenant_api_keys table
    try:
        op.create_table(
            "tenant_api_keys",
            sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
            sa.Column("institution_id", sa.Integer(), sa.ForeignKey("institutions.id"), nullable=False, index=True),
            sa.Column("name", sa.String(128), nullable=False),
            sa.Column("key_hash", sa.String(128), nullable=False, unique=True, index=True),
            sa.Column("key_prefix", sa.String(16), nullable=False),
            sa.Column("is_active", sa.Boolean(), nullable=False, server_default="1"),
            sa.Column("last_used_at", sa.DateTime(), nullable=True),
            sa.Column("expires_at", sa.DateTime(), nullable=True),
            sa.Column("created_by_user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
            sa.Column("updated_at", sa.DateTime(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        )
        op.create_index("ix_tenant_api_keys_institution_id", "tenant_api_keys", ["institution_id"])
    except Exception:
        pass

    # Add tenant user fields to user table
    try:
        op.add_column("user", sa.Column("institution_id", sa.Integer(), nullable=True))
        op.add_column("user", sa.Column("tenant_role", sa.String(32), nullable=False, server_default="member"))
        op.add_column("user", sa.Column("tenant_is_active", sa.Boolean(), nullable=False, server_default="1"))
        op.create_index("ix_user_institution_id", "user", ["institution_id"])
    except Exception:
        pass

    # Backfill tenant_slug for existing institutions that don't have one
    try:
        conn = op.get_bind()
        result = conn.execute(text("SELECT id, name FROM institutions WHERE tenant_slug IS NULL"))
        import re
        for row in result:
            inst_id = row[0]
            name = row[1]
            slug = re.sub(r'[^\w\s-]', '', name.lower().strip())
            slug = re.sub(r'[\s_]+', '-', slug)
            slug = re.sub(r'-+', '-', slug).strip('-')

            base_slug = slug
            counter = 1
            while True:
                existing = conn.execute(text("SELECT id FROM institutions WHERE tenant_slug = :slug"), {"slug": slug}).first()
                if not existing:
                    break
                slug = f"{base_slug}-{counter}"
                counter += 1

            conn.execute(
                text("UPDATE institutions SET tenant_slug = :slug WHERE id = :id"),
                {"slug": slug, "id": inst_id}
            )
            conn.commit()
    except Exception:
        pass


def downgrade() -> None:
    pass
