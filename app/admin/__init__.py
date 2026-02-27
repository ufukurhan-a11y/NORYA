"""Production admin panel: modüler router'lar, Jinja2, /admin altında."""
from fastapi import APIRouter

from app.admin.routers import (
    analyses,
    coupons,
    dashboard,
    errors,
    live,
    payments,
    queue,
    reports,
    security,
    uploads,
    users,
)

admin_router = APIRouter(prefix="/admin", tags=["admin"])

admin_router.include_router(dashboard.router, include_in_schema=False)
admin_router.include_router(users.router, prefix="/users", tags=["admin-users"])
admin_router.include_router(analyses.router, prefix="/analyses", tags=["admin-analyses"])
admin_router.include_router(reports.router, prefix="/reports", tags=["admin-reports"])
admin_router.include_router(live.router, prefix="/live", tags=["admin-live"])
admin_router.include_router(coupons.router, prefix="/coupons", tags=["admin-coupons"])
admin_router.include_router(payments.router, prefix="/payments", tags=["admin-payments"])
admin_router.include_router(errors.router, prefix="/errors", tags=["admin-errors"])
admin_router.include_router(uploads.router, prefix="/uploads", tags=["admin-uploads"])
admin_router.include_router(queue.router, prefix="/queue", tags=["admin-queue"])
admin_router.include_router(security.router, prefix="/security", tags=["admin-security"])
