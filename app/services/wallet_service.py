"""Prepaid wallet billing service for tenant institutions.

Handles credit loading, deduction per analysis, and balance checking.
"""
import logging
from datetime import datetime

from sqlmodel import Session, select

from app.models.institution import Institution
from app.models.tenant_wallet_transaction import TenantWalletTransaction

logger = logging.getLogger(__name__)


def load_credits(
    session: Session,
    institution_id: int,
    amount_cents: int,
    description: str = "Credit load",
) -> dict:
    """Add credits to a tenant's wallet with row-level locking.

    Args:
        session: Database session
        institution_id: Institution ID
        amount_cents: Amount to add in cents (must be positive)
        description: Description for the transaction

    Returns:
        dict with success status, new balance, and transaction
    """
    from sqlalchemy import text

    if amount_cents <= 0:
        return {"success": False, "error": "Amount must be positive"}

    # Row-level lock
    lock_stmt = text(
        "SELECT id, billing_wallet_balance FROM institutions "
        "WHERE id = :inst_id FOR UPDATE"
    )
    result = session.execute(lock_stmt, {"inst_id": institution_id})
    row = result.first()

    if not row:
        return {"success": False, "error": "Institution not found"}

    current_balance = row[1]
    new_balance = current_balance + amount_cents

    # Update balance directly via SQL
    session.execute(
        text(
            "UPDATE institutions SET billing_wallet_balance = :new_balance, "
            "updated_at = :now WHERE id = :inst_id"
        ),
        {"new_balance": new_balance, "now": datetime.utcnow(), "inst_id": institution_id},
    )

    # Create transaction record
    transaction = TenantWalletTransaction(
        institution_id=institution_id,
        amount_cents=amount_cents,
        transaction_type="load",
        description=description,
        created_at=datetime.utcnow(),
    )
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    logger.info(
        f"Loaded {amount_cents} cents to institution {institution_id} "
        f"(new balance: {new_balance})"
    )

    return {
        "success": True,
        "new_balance": new_balance,
        "transaction": transaction,
    }


def spend_credits(
    session: Session,
    institution_id: int,
    amount_cents: int,
    description: str = "Analysis credit spend",
) -> dict:
    """Deduct credits from a tenant's wallet with row-level locking.

    Args:
        session: Database session
        institution_id: Institution ID
        amount_cents: Amount to deduct in cents (must be positive)
        description: Description for the transaction

    Returns:
        dict with success status, new balance, and transaction
    """
    from sqlalchemy import text

    if amount_cents <= 0:
        return {"success": False, "error": "Amount must be positive"}

    # Row-level lock
    lock_stmt = text(
        "SELECT id, billing_wallet_balance FROM institutions "
        "WHERE id = :inst_id FOR UPDATE"
    )
    result = session.execute(lock_stmt, {"inst_id": institution_id})
    row = result.first()

    if not row:
        return {"success": False, "error": "Institution not found"}

    current_balance = row[1]

    if current_balance < amount_cents:
        session.rollback()  # Release the lock
        return {
            "success": False,
            "error": "Insufficient credits",
            "current_balance": current_balance,
            "required": amount_cents,
        }

    new_balance = current_balance - amount_cents

    # Update balance directly via SQL
    session.execute(
        text(
            "UPDATE institutions SET billing_wallet_balance = :new_balance, "
            "updated_at = :now WHERE id = :inst_id"
        ),
        {"new_balance": new_balance, "now": datetime.utcnow(), "inst_id": institution_id},
    )

    # Create transaction record
    transaction = TenantWalletTransaction(
        institution_id=institution_id,
        amount_cents=-amount_cents,  # Negative for spend
        transaction_type="spend",
        description=description,
        created_at=datetime.utcnow(),
    )
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    logger.info(
        f"Spent {amount_cents} cents from institution {institution_id} "
        f"(new balance: {new_balance})"
    )

    return {
        "success": True,
        "new_balance": new_balance,
        "transaction": transaction,
    }


def check_and_deduct(
    session: Session,
    institution_id: int,
    cost_cents: int,
    description: str = "Analysis",
    auto_commit: bool = True,
) -> dict:
    """Atomic check + deduct operation with row-level locking.

    Uses SELECT ... FOR UPDATE to prevent race conditions when
    multiple concurrent requests try to deduct from the same wallet.

    Args:
        session: Database session
        institution_id: Institution ID
        cost_cents: Cost of the analysis in cents
        description: Description for the transaction
        auto_commit: If True, commits the transaction. If False, caller
                     is responsible for committing (useful for atomic
                     operations that include multiple DB writes).

    Returns:
        dict with success status and details
    """
    from sqlalchemy import text

    # Row-level lock: SELECT ... FOR UPDATE prevents concurrent modifications
    # This ensures only one transaction can read+modify the balance at a time
    lock_stmt = text(
        "SELECT id, billing_wallet_balance FROM institutions "
        "WHERE id = :inst_id FOR UPDATE"
    )
    result = session.execute(lock_stmt, {"inst_id": institution_id})
    row = result.first()

    if not row:
        return {"success": False, "error": "Institution not found"}

    current_balance = row[1]

    if current_balance < cost_cents:
        session.rollback()  # Release the lock
        return {
            "success": False,
            "error": "Insufficient credits. Please contact your administrator.",
            "current_balance": current_balance,
            "required": cost_cents,
        }

    # Deduct credits (row is already locked, safe to modify)
    new_balance = current_balance - cost_cents

    # Update balance directly via SQL to avoid ORM stale data issues
    session.execute(
        text(
            "UPDATE institutions SET billing_wallet_balance = :new_balance, "
            "updated_at = :now WHERE id = :inst_id"
        ),
        {"new_balance": new_balance, "now": datetime.utcnow(), "inst_id": institution_id},
    )

    # Create transaction record
    transaction = TenantWalletTransaction(
        institution_id=institution_id,
        amount_cents=-cost_cents,
        transaction_type="spend",
        description=description,
        created_at=datetime.utcnow(),
    )
    session.add(transaction)

    if auto_commit:
        session.commit()
        session.refresh(transaction)

    return {
        "success": True,
        "new_balance": new_balance,
        "transaction": transaction,
    }


def get_balance(session: Session, institution_id: int) -> dict:
    """Get current wallet balance for an institution.

    Returns:
        dict with balance, cost_per_analysis, and remaining analyses count
    """
    stmt = select(Institution).where(Institution.id == institution_id)
    institution = session.exec(stmt).first()

    if not institution:
        return {"success": False, "error": "Institution not found"}

    cost_per_analysis = institution.cost_per_analysis
    remaining_analyses = (
        institution.billing_wallet_balance // cost_per_analysis
        if cost_per_analysis > 0
        else 0
    )

    return {
        "success": True,
        "balance": institution.billing_wallet_balance,
        "balance_formatted": f"${institution.billing_wallet_balance / 100:.2f}",
        "cost_per_analysis": cost_per_analysis,
        "cost_per_analysis_formatted": f"${cost_per_analysis / 100:.2f}",
        "remaining_analyses": remaining_analyses,
        "is_low_balance": institution.billing_wallet_balance <= institution.wallet_low_threshold,
    }


def get_transactions(
    session: Session,
    institution_id: int,
    limit: int = 50,
    offset: int = 0,
) -> list[TenantWalletTransaction]:
    """Get transaction history for an institution."""
    stmt = (
        select(TenantWalletTransaction)
        .where(TenantWalletTransaction.institution_id == institution_id)
        .order_by(TenantWalletTransaction.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    return list(session.exec(stmt).all())


def check_low_balance_alerts(session: Session) -> list[dict]:
    """Check all institutions for low balance alerts.

    Returns list of institutions that need alerts.
    Note: Actual email sending should be handled by a scheduled task.
    """
    from datetime import timedelta

    stmt = select(Institution).where(
        Institution.is_active == True,
        Institution.billing_wallet_balance <= Institution.wallet_low_threshold,
    )
    institutions = session.exec(stmt).all()

    alerts = []
    for inst in institutions:
        # Avoid spamming - only alert if last alert was > 24 hours ago
        if inst.wallet_last_alert:
            time_since_last = datetime.utcnow() - inst.wallet_last_alert
            if time_since_last < timedelta(hours=24):
                continue

        alerts.append({
            "institution_id": inst.id,
            "name": inst.name,
            "tenant_slug": inst.tenant_slug,
            "contact_email": inst.contact_email,
            "balance": inst.billing_wallet_balance,
            "threshold": inst.wallet_low_threshold,
        })

        # Update last alert time
        inst.wallet_last_alert = datetime.utcnow()
        session.add(inst)

    session.commit()
    return alerts
