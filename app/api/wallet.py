"""Wallet API endpoints for tenant credit management."""
import logging

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.services import wallet_service
from app.tenants.isolation import require_tenant_active
from app.models.institution import Institution

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/wallet", tags=["wallet"])


class LoadCreditsRequest(BaseModel):
    amount_cents: int
    description: str = "Admin credit load"


class WalletBalanceResponse(BaseModel):
    balance: int
    balance_formatted: str
    cost_per_analysis: int
    cost_per_analysis_formatted: str
    remaining_analyses: int
    is_low_balance: bool


class WalletTransactionResponse(BaseModel):
    id: int
    amount_cents: int
    transaction_type: str
    description: str | None
    created_at: str


@router.get("/balance", response_model=WalletBalanceResponse)
async def get_wallet_balance(
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get current tenant wallet balance."""
    result = wallet_service.get_balance(db, tenant.id)

    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["error"])

    return WalletBalanceResponse(
        balance=result["balance"],
        balance_formatted=result["balance_formatted"],
        cost_per_analysis=result["cost_per_analysis"],
        cost_per_analysis_formatted=result["cost_per_analysis_formatted"],
        remaining_analyses=result["remaining_analyses"],
        is_low_balance=result["is_low_balance"],
    )


@router.get("/transactions")
async def get_wallet_transactions(
    limit: int = 50,
    offset: int = 0,
    tenant: Institution = Depends(require_tenant_active),
    db: Session = Depends(get_db),
):
    """Get wallet transaction history for current tenant."""
    transactions = wallet_service.get_transactions(db, tenant.id, limit=limit, offset=offset)

    return [
        {
            "id": t.id,
            "amount_cents": t.amount_cents,
            "transaction_type": t.transaction_type,
            "description": t.description,
            "created_at": t.created_at.isoformat() if t.created_at else None,
        }
        for t in transactions
    ]


@router.post("/load")
async def load_credits(
    request: LoadCreditsRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Load credits to current tenant wallet (admin only).

    Note: In production, this should be protected by admin role check.
    """
    # TODO: Add admin role check
    # if not user.is_admin:
    #     raise HTTPException(status_code=403, detail="Admin access required")

    # This endpoint loads credits to a specific institution
    # For tenant-scoped requests, use the current tenant
    from app.tenants.context import get_current_tenant

    tenant_ctx = get_current_tenant()
    if not tenant_ctx:
        raise HTTPException(status_code=400, detail="No tenant context. Use /admin/tenants/{id}/load-credits instead.")

    result = wallet_service.load_credits(
        db,
        tenant_ctx.institution_id,
        request.amount_cents,
        request.description,
    )

    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["error"])

    return {
        "success": True,
        "new_balance": result["new_balance"],
        "transaction_id": result["transaction"].id,
    }
