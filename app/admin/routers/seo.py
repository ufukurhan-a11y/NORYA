"""SEO Dashboard: Google Search Console verilerini admin panelinden görüntüleme."""
from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse

from app.admin.deps import require_admin_cookie
from app.core.templating import Jinja2Templates
from app.services import gsc

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def seo_dashboard(
    request: Request,
    _=Depends(require_admin_cookie),
    days: int = Query(28, ge=7, le=90),
):
    configured = gsc.is_configured()
    site_url = gsc.get_site_url()

    ctx: dict = {
        "request": request,
        "configured": configured,
        "site_url": site_url,
        "days": days,
    }

    if not configured:
        return templates.TemplateResponse("admin/seo_dashboard.html", ctx)

    daily = gsc.get_daily_performance(days)
    queries = gsc.get_top_queries(days, limit=50)
    pages = gsc.get_top_pages(days, limit=50)
    sitemaps = gsc.get_sitemaps_status()
    countries = gsc.get_performance_by_country(days)
    devices = gsc.get_performance_by_device(days)

    total_clicks = sum(daily.get("clicks", [])) if daily else 0
    total_impressions = sum(daily.get("impressions", [])) if daily else 0
    avg_ctr = 0.0
    avg_position = 0.0
    if daily and daily.get("ctr"):
        avg_ctr = round(sum(daily["ctr"]) / len(daily["ctr"]), 2)
    if daily and daily.get("position"):
        avg_position = round(sum(daily["position"]) / len(daily["position"]), 1)

    ctx.update({
        "daily": daily,
        "queries": queries or [],
        "pages": pages or [],
        "sitemaps": sitemaps or [],
        "countries": countries or [],
        "devices": devices or [],
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "avg_ctr": avg_ctr,
        "avg_position": avg_position,
    })

    return templates.TemplateResponse("admin/seo_dashboard.html", ctx)


@router.get("/api/inspect", response_class=JSONResponse)
def seo_inspect_url(
    _=Depends(require_admin_cookie),
    url: str = Query(..., description="Denetlenecek URL"),
):
    if not gsc.is_configured():
        return JSONResponse({"error": "GSC yapılandırılmamış"}, status_code=400)
    result = gsc.inspect_url(url)
    if result is None:
        return JSONResponse({"error": "API hatası"}, status_code=500)
    return JSONResponse(result)
