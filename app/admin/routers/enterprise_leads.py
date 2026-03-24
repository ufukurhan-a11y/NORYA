"""Kurumsal demo talepleri: listeleme ve detay görüntüleme."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select, func

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.core.templating import Jinja2Templates
from app.models.enterprise_lead import EnterpriseLead

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

KURUM_TIPI_LABELS = {
    "hospital": "Hastane",
    "clinic": "Klinik",
    "lab": "Laboratuvar",
    "network": "Sağlayıcı Ağı",
    "other": "Diğer",
}


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def enterprise_leads_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    q: str | None = None,
):
    stmt = select(EnterpriseLead).order_by(EnterpriseLead.id.desc())
    if q and q.strip():
        term = q.strip()
        stmt = stmt.where(
            EnterpriseLead.kurum_adi.contains(term)
            | EnterpriseLead.email.contains(term)
            | EnterpriseLead.yetkili_ad.contains(term)
        )
    leads = list(db.exec(stmt).all())

    rows = [
        {
            "id": ld.id,
            "kurum_adi": ld.kurum_adi,
            "yetkili_ad": ld.yetkili_ad,
            "email": ld.email,
            "telefon": ld.telefon or "—",
            "kurum_tipi": KURUM_TIPI_LABELS.get(ld.kurum_tipi or "", ld.kurum_tipi or "—"),
            "aylik_rapor": ld.aylik_rapor or "—",
            "mesaj": ld.mesaj or "",
            "created_at": ld.created_at.strftime("%d.%m.%Y %H:%M") if ld.created_at else "—",
        }
        for ld in leads
    ]
    return templates.TemplateResponse("admin/enterprise_leads.html", {
        "request": request,
        "leads": rows,
        "q": q or "",
        "total": len(rows),
    })
