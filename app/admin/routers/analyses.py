"""Admin analiz geçmişi: tüm analizler, filtre."""
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, Response
from app.core.templating import Jinja2Templates
from sqlmodel import Session, select

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AnalysisRecord, User
from app.services.report_pdf import build_report_pdf

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

_UPLOADS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "data" / "uploads"


def _parse_date(s: str | None) -> datetime | None:
    if not s or not s.strip():
        return None
    try:
        return datetime.strptime(s.strip()[:10], "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        return None


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def analyses_list(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    q: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    source: str | None = None,
    limit: int = 200,
):
    stmt = select(AnalysisRecord).order_by(AnalysisRecord.created_at.desc()).limit(limit)
    if date_from:
        start = _parse_date(date_from)
        if start:
            stmt = stmt.where(AnalysisRecord.created_at >= start)
    if date_to:
        end = _parse_date(date_to)
        if end:
            end_of_day = end.replace(hour=23, minute=59, second=59, microsecond=999999)
            stmt = stmt.where(AnalysisRecord.created_at <= end_of_day)
    if source and source.strip().lower() in ("text", "pdf", "image"):
        stmt = stmt.where(AnalysisRecord.source == source.strip().lower())
    if q and q.strip():
        q = q.strip()
        try:
            uid = int(q)
            stmt = stmt.where(AnalysisRecord.user_id == uid)
        except ValueError:
            users = list(db.exec(select(User).where(User.email.contains(q))).all())
            user_ids = [u.id for u in users if u.id is not None]
            if user_ids:
                stmt = stmt.where(AnalysisRecord.user_id.in_(user_ids))
            else:
                stmt = stmt.where(AnalysisRecord.id == -1)
    records = list(db.exec(stmt).all())
    user_ids = list({r.user_id for r in records})
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = {"email": u.email or "", "country": u.country or ""}
    rows = [
        {
            "id": r.id,
            "user_id": r.user_id,
            "email": users_map.get(r.user_id, {}).get("email", "-"),
            "country": users_map.get(r.user_id, {}).get("country", "-"),
            "created_at": r.created_at.strftime("%d.%m.%Y %H:%M") if r.created_at else "-",
            "source": r.source or "text",
            "input_preview": (r.input_text or "")[:100] + ("…" if len(r.input_text or "") > 100 else ""),
            "result_preview": (r.result_text or "")[:150] + ("…" if len(r.result_text or "") > 150 else ""),
            "has_original": bool(getattr(r, "original_stored_path", None)),
        }
        for r in records
    ]
    return templates.TemplateResponse(
        "admin/analyses_list.html",
        {
            "request": request,
            "analyses": rows,
            "q": q or "",
            "date_from": date_from or "",
            "date_to": date_to or "",
            "source": source or "",
        },
    )


@router.get("/{analysis_id:int}/pdf", response_class=Response)
def analyses_pdf(
    analysis_id: int,
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    lang: str = Query("tr", description="Rapor dili: tr, en, de, fr, es, it, he, ar, hi, el, cs, sr"),
):
    """Norya raporu PDF: dashboard cookie ile korunur, 403 olmaz."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Analiz bulunamadı.")
    report_date = None
    if getattr(rec, "created_at", None):
        dt = rec.created_at
        report_date = dt.strftime("%d.%m.%Y %H:%M") if hasattr(dt, "strftime") else str(dt)
    report_lang = (lang or "tr").strip().lower()[:5]
    user = db.get(User, rec.user_id) if rec.user_id else None
    try:
        pdf_bytes = build_report_pdf(
            result_text=rec.result_text or "",
            report_date=report_date,
            lang=report_lang,
            report_id=analysis_id,
            user_identifier=user.email if user else None,
            patient_name=user.full_name if user else None,
            plan_name=user.plan if user else None,
            source_type=getattr(rec, "source", None) or None,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    filename = f"norya-rapor-{analysis_id}.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )


@router.get("/{analysis_id:int}/original", response_class=Response)
def analyses_original(
    analysis_id: int,
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
):
    """Müşteri belgesi: dashboard cookie ile korunur, 403 olmaz."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or not getattr(rec, "original_stored_path", None):
        raise HTTPException(status_code=404, detail="Orijinal belge yok.")
    path = _UPLOADS_DIR / rec.original_stored_path
    if not path.is_file():
        raise HTTPException(status_code=404, detail="Dosya bulunamadı.")
    content = path.read_bytes()
    filename = getattr(rec, "original_filename", None) or f"orijinal-{analysis_id}"
    ext = path.suffix.lower()
    media_types = {
        ".pdf": "application/pdf",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }
    media_type = media_types.get(ext, "application/octet-stream")
    return Response(
        content=content,
        media_type=media_type,
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )
