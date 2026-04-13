"""Admin tenant management: activate/deactivate tenants, wallet management."""
from datetime import datetime

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.models.institution import Institution
from app.models.tenant_wallet_transaction import TenantWalletTransaction
from app.models.enterprise_case import EnterpriseCase
from app.services import wallet_service
from app.tenants import onboarding

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/tenants")
async def admin_tenants_list(
    request: Request,
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """List all tenants with status, wallet balance, usage stats."""
    institutions = db.exec(
        select(Institution).order_by(Institution.created_at.desc())
    ).all()

    tenant_data = []
    for inst in institutions:
        # Count cases for this institution
        case_count = db.exec(
            select(EnterpriseCase).where(EnterpriseCase.institution_id == inst.id)
        ).all()

        tenant_data.append({
            "institution": inst,
            "case_count": len(case_count),
            "remaining_analyses": (
                inst.billing_wallet_balance // inst.cost_per_analysis
                if inst.cost_per_analysis > 0
                else 0
            ),
            "is_low_balance": inst.billing_wallet_balance <= inst.wallet_low_threshold,
        })

    return templates.TemplateResponse(
        "admin/tenant_management.html",
        {
            "request": request,
            "tenant_data": tenant_data,
        },
    )


@router.post("/tenants/create")
async def admin_create_tenant(
    request: Request,
    name: str = Form(...),
    institution_type: str = Form(default="hospital"),
    contact_email: str = Form(default=""),
    contact_phone: str = Form(default=""),
    initial_credits_cents: int = Form(default=0),
    cost_per_analysis: int = Form(default=100),
    wallet_low_threshold: int = Form(default=20000),
    notes: str = Form(default=""),
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """Create a new tenant institution."""
    institution = onboarding.create_tenant(
        session=db,
        name=name,
        institution_type=institution_type,
        contact_email=contact_email or None,
        contact_phone=contact_phone or None,
        initial_credits_cents=initial_credits_cents,
        cost_per_analysis=cost_per_analysis,
        wallet_low_threshold=wallet_low_threshold,
        notes=notes or None,
    )

    return RedirectResponse(url="/admin/tenants", status_code=303)


@router.post("/tenants/{institution_id}/activate")
async def admin_activate_tenant(
    institution_id: int,
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """Activate a tenant institution."""
    onboarding.activate_tenant(db, institution_id)
    return RedirectResponse(url="/admin/tenants", status_code=303)


@router.post("/tenants/{institution_id}/suspend")
async def admin_suspend_tenant(
    institution_id: int,
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """Suspend a tenant institution."""
    onboarding.suspend_tenant(db, institution_id)
    return RedirectResponse(url="/admin/tenants", status_code=303)


@router.post("/tenants/{institution_id}/deactivate")
async def admin_deactivate_tenant(
    institution_id: int,
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """Deactivate a tenant institution."""
    onboarding.deactivate_tenant(db, institution_id)
    return RedirectResponse(url="/admin/tenants", status_code=303)


@router.post("/tenants/{institution_id}/load-credits")
async def admin_load_credits(
    institution_id: int,
    amount_cents: int = Form(...),
    description: str = Form(default="Admin credit load"),
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """Add credits to a tenant's wallet."""
    result = wallet_service.load_credits(db, institution_id, amount_cents, description)

    if not result["success"]:
        # TODO: Add flash message support
        pass

    return RedirectResponse(url="/admin/tenants", status_code=303)


@router.get("/tenants/{institution_id}/wallet-history")
async def admin_wallet_history(
    request: Request,
    institution_id: int,
    db: Session = Depends(get_db),
    _admin=Depends(require_admin_cookie),
):
    """View wallet transaction history for a tenant."""
    institution = db.get(Institution, institution_id)
    if not institution:
        return HTMLResponse("Institution not found", status_code=404)

    transactions = db.exec(
        select(TenantWalletTransaction)
        .where(TenantWalletTransaction.institution_id == institution_id)
        .order_by(TenantWalletTransaction.created_at.desc())
    ).all()

    return templates.TemplateResponse(
        "admin/wallet_history.html",
        {
            "request": request,
            "institution": institution,
            "transactions": transactions,
        },
    )
