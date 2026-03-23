"""Kurumsal müşteri dashboard: hastane/klinik/lab yöneticileri için."""
from fastapi import APIRouter

from app.enterprise.dashboard import router as dashboard_router

enterprise_router = APIRouter(prefix="/enterprise", tags=["enterprise"])
enterprise_router.include_router(dashboard_router)
