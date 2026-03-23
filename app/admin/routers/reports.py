"""Admin raporlar: tarih aralığı, metrikler, CSV export."""
from datetime import datetime, timedelta
from io import StringIO

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from app.core.templating import Jinja2Templates
from sqlmodel import Session, select, func

from app.admin.deps import require_admin_cookie
from app.core.database import get_db
from app.models import AnalysisRecord, PaymentOrder, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def _scalar(row, default=0):
    """Sorgu sonucu Row/tuple ise ilk değeri al, None ise default dön."""
    if row is None:
        return default
    if hasattr(row, "__getitem__"):
        try:
            v = row[0]
            return default if v is None else v
        except (IndexError, KeyError):
            return default
    return default if row is None else row


def _parse_date(s: str | None) -> datetime | None:
    if not s or not s.strip():
        return None
    try:
        return datetime.strptime(s.strip()[:10], "%Y-%m-%d").replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        return None


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def reports_page(
    request: Request,
    _=Depends(require_admin_cookie),
    db: Session = Depends(get_db),
    date_from: str | None = None,
    date_to: str | None = None,
    export: str | None = None,
):
    try:
        now = datetime.utcnow()
        default_end = now
        default_start = now - timedelta(days=30)
        start = _parse_date(date_from) or default_start
        end = _parse_date(date_to) or default_end
        if start > end:
            start, end = end, start
        end_of_day = end.replace(hour=23, minute=59, second=59, microsecond=999999)

        new_users = _scalar(db.exec(select(func.count(User.id)).where(User.created_at >= start).where(User.created_at <= end_of_day)).one())
        analyses_count = _scalar(db.exec(
            select(func.count(AnalysisRecord.id)).where(AnalysisRecord.created_at >= start).where(AnalysisRecord.created_at <= end_of_day)
        ).one())
        payments_count = _scalar(db.exec(
            select(func.count(PaymentOrder.id)).where(PaymentOrder.status == "completed").where(PaymentOrder.created_at >= start).where(PaymentOrder.created_at <= end_of_day)
        ).one())
        revenue_kurus = _scalar(db.exec(
            select(func.sum(PaymentOrder.amount_kurus))
            .where(PaymentOrder.status == "completed")
            .where(PaymentOrder.created_at >= start)
            .where(PaymentOrder.created_at <= end_of_day)
        ).one())
        revenue_eur = float(revenue_kurus) / 100

        if export == "csv":
            buf = StringIO()
            buf.write("tarih;yeni_kullanici;analiz_sayisi;odeme_sayisi;ciro_eur\n")
            buf.write(f"{start.date()};{end.date()};{new_users};{analyses_count};{payments_count};{revenue_eur:.2f}\n")
            buf.write("\n")
            buf.write("Ozet (secili aralik)\n")
            buf.write(f"Yeni kullanici;{new_users}\n")
            buf.write(f"Analiz sayisi;{analyses_count}\n")
            buf.write(f"Tamamlanan odeme;{payments_count}\n")
            buf.write(f"Ciro (EUR);{revenue_eur:.2f}\n")
            filename = f"rapor_{start.date()}__{end.date()}.csv"
            return StreamingResponse(
                iter([buf.getvalue()]),
                media_type="text/csv; charset=utf-8",
                headers={"Content-Disposition": f'attachment; filename="{filename}"'},
            )

        return templates.TemplateResponse(
            "admin/reports.html",
            {
                "request": request,
                "date_from": start.strftime("%Y-%m-%d"),
                "date_to": end.strftime("%Y-%m-%d"),
                "new_users": new_users,
                "analyses_count": analyses_count,
                "payments_count": payments_count,
                "revenue_eur": f"{revenue_eur:.2f}",
            },
        )
    except Exception as e:
        now = datetime.utcnow()
        default_end = now.strftime("%Y-%m-%d")
        default_start = (now - timedelta(days=30)).strftime("%Y-%m-%d")
        return templates.TemplateResponse(
            "admin/reports.html",
            {
                "request": request,
                "date_from": (date_from or default_start)[:10],
                "date_to": (date_to or default_end)[:10],
                "new_users": 0,
                "analyses_count": 0,
                "payments_count": 0,
                "revenue_eur": "0.00",
                "error": f"Rapor yüklenirken sorun oluştu: {str(e)[:200]}",
            },
        )
