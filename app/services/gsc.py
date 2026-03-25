"""Google Search Console API integration for SEO dashboard."""
import logging
import time
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from app.core.config import settings

logger = logging.getLogger(__name__)

_cache: dict[str, Any] = {}
_CACHE_TTL = 300  # 5 min

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]

COUNTRY_NAMES = {
    "tur": "Türkiye", "deu": "Almanya", "usa": "ABD", "gbr": "Birleşik Krallık",
    "fra": "Fransa", "ita": "İtalya", "esp": "İspanya", "nld": "Hollanda",
    "bel": "Belçika", "aut": "Avusturya", "che": "İsviçre", "can": "Kanada",
    "aus": "Avustralya", "bra": "Brezilya", "ind": "Hindistan", "isr": "İsrail",
    "are": "BAE", "sau": "S. Arabistan", "egy": "Mısır", "mex": "Meksika",
    "arg": "Arjantin", "col": "Kolombiya", "jpn": "Japonya", "kor": "G. Kore",
    "pol": "Polonya", "swe": "İsveç", "nor": "Norveç", "dnk": "Danimarka",
    "fin": "Finlandiya", "prt": "Portekiz", "grc": "Yunanistan", "rou": "Romanya",
    "bgr": "Bulgaristan", "hrv": "Hırvatistan", "cze": "Çekya", "hun": "Macaristan",
    "aze": "Azerbaycan", "geo": "Gürcistan", "ukr": "Ukrayna", "rus": "Rusya",
    "pak": "Pakistan", "bgd": "Bangladeş", "idn": "Endonezya", "mys": "Malezya",
    "tha": "Tayland", "vnm": "Vietnam", "phl": "Filipinler", "zaf": "G. Afrika",
    "nga": "Nijerya", "ken": "Kenya", "irq": "Irak", "irn": "İran",
    "mar": "Fas", "dza": "Cezayir", "tun": "Tunus", "lby": "Libya",
}

DEVICE_NAMES = {"DESKTOP": "Masaüstü", "MOBILE": "Mobil", "TABLET": "Tablet"}


def _cache_get(key: str) -> Any | None:
    entry = _cache.get(key)
    if entry and (time.time() - entry["ts"]) < _CACHE_TTL:
        return entry["data"]
    return None


def _cache_set(key: str, data: Any) -> None:
    _cache[key] = {"ts": time.time(), "data": data}


def is_configured() -> bool:
    json_path = (settings.gsc_service_account_json or "").strip()
    return bool(json_path) and Path(json_path).is_file()


def get_site_url() -> str:
    return settings.canonical_site_url or "https://noryaai.com"


def _get_credentials():
    json_path = (settings.gsc_service_account_json or "").strip()
    if not json_path:
        return None
    try:
        from google.oauth2 import service_account
        path = Path(json_path)
        if not path.is_file():
            logger.warning("GSC service account JSON not found: %s", json_path)
            return None
        return service_account.Credentials.from_service_account_file(str(path), scopes=SCOPES)
    except Exception as e:
        logger.error("GSC credentials error: %s", e)
        return None


def _build_service(api: str = "webmasters", version: str = "v3"):
    creds = _get_credentials()
    if not creds:
        return None
    try:
        from googleapiclient.discovery import build
        return build(api, version, credentials=creds, cache_discovery=False)
    except Exception as e:
        logger.error("GSC service build error (%s/%s): %s", api, version, e)
        return None


def _query_analytics(body: dict) -> dict | None:
    svc = _build_service("webmasters", "v3")
    if not svc:
        return None
    try:
        return svc.searchanalytics().query(siteUrl=get_site_url(), body=body).execute()
    except Exception as e:
        logger.error("GSC searchanalytics error: %s", e)
        return None


def _date_range(days: int) -> tuple[str, str]:
    end = date.today() - timedelta(days=3)
    start = end - timedelta(days=days)
    return start.isoformat(), end.isoformat()


# ── public helpers ──────────────────────────────────────────────


def get_daily_performance(days: int = 28) -> dict | None:
    ck = f"daily_{days}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    start, end = _date_range(days)
    resp = _query_analytics({
        "startDate": start, "endDate": end,
        "dimensions": ["date"], "rowLimit": 25000,
    })
    if not resp:
        return None

    rows = resp.get("rows", [])
    result = {
        "dates": [r["keys"][0] for r in rows],
        "clicks": [r.get("clicks", 0) for r in rows],
        "impressions": [r.get("impressions", 0) for r in rows],
        "ctr": [round(r.get("ctr", 0) * 100, 2) for r in rows],
        "position": [round(r.get("position", 0), 1) for r in rows],
    }
    _cache_set(ck, result)
    return result


def get_top_queries(days: int = 28, limit: int = 50) -> list[dict] | None:
    ck = f"queries_{days}_{limit}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    start, end = _date_range(days)
    resp = _query_analytics({
        "startDate": start, "endDate": end,
        "dimensions": ["query"], "rowLimit": limit,
    })
    if not resp:
        return None

    result = [
        {
            "query": r["keys"][0],
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": round(r.get("ctr", 0) * 100, 2),
            "position": round(r.get("position", 0), 1),
        }
        for r in resp.get("rows", [])
    ]
    _cache_set(ck, result)
    return result


def get_top_pages(days: int = 28, limit: int = 50) -> list[dict] | None:
    ck = f"pages_{days}_{limit}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    start, end = _date_range(days)
    resp = _query_analytics({
        "startDate": start, "endDate": end,
        "dimensions": ["page"], "rowLimit": limit,
    })
    if not resp:
        return None

    result = [
        {
            "page": r["keys"][0],
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": round(r.get("ctr", 0) * 100, 2),
            "position": round(r.get("position", 0), 1),
        }
        for r in resp.get("rows", [])
    ]
    _cache_set(ck, result)
    return result


def get_performance_by_country(days: int = 28, limit: int = 20) -> list[dict] | None:
    ck = f"country_{days}_{limit}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    start, end = _date_range(days)
    resp = _query_analytics({
        "startDate": start, "endDate": end,
        "dimensions": ["country"], "rowLimit": limit,
    })
    if not resp:
        return None

    result = [
        {
            "country": r["keys"][0],
            "country_name": COUNTRY_NAMES.get(r["keys"][0].lower(), r["keys"][0].upper()),
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": round(r.get("ctr", 0) * 100, 2),
            "position": round(r.get("position", 0), 1),
        }
        for r in resp.get("rows", [])
    ]
    _cache_set(ck, result)
    return result


def get_performance_by_device(days: int = 28) -> list[dict] | None:
    ck = f"device_{days}"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    start, end = _date_range(days)
    resp = _query_analytics({
        "startDate": start, "endDate": end,
        "dimensions": ["device"], "rowLimit": 10,
    })
    if not resp:
        return None

    result = [
        {
            "device": r["keys"][0],
            "device_name": DEVICE_NAMES.get(r["keys"][0], r["keys"][0]),
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": round(r.get("ctr", 0) * 100, 2),
            "position": round(r.get("position", 0), 1),
        }
        for r in resp.get("rows", [])
    ]
    _cache_set(ck, result)
    return result


def get_sitemaps_status() -> list[dict] | None:
    ck = "sitemaps"
    cached = _cache_get(ck)
    if cached is not None:
        return cached

    svc = _build_service("webmasters", "v3")
    if not svc:
        return None

    try:
        resp = svc.sitemaps().list(siteUrl=get_site_url()).execute()
        result = [
            {
                "path": s.get("path", ""),
                "last_submitted": s.get("lastSubmitted", ""),
                "last_downloaded": s.get("lastDownloaded", ""),
                "is_pending": s.get("isPending", False),
                "warnings": s.get("warnings", 0),
                "errors": s.get("errors", 0),
                "contents": s.get("contents", []),
            }
            for s in resp.get("sitemap", [])
        ]
        _cache_set(ck, result)
        return result
    except Exception as e:
        logger.error("GSC sitemaps error: %s", e)
        return None


def inspect_url(url: str) -> dict | None:
    svc = _build_service("searchconsole", "v1")
    if not svc:
        return None

    try:
        resp = svc.urlInspection().index().inspect(body={
            "inspectionUrl": url,
            "siteUrl": get_site_url(),
        }).execute()

        result = resp.get("inspectionResult", {})
        idx = result.get("indexStatusResult", {})
        mobile = result.get("mobileUsabilityResult", {})
        rich = result.get("richResultsResult", {})

        return {
            "url": url,
            "verdict": idx.get("verdict", "UNKNOWN"),
            "coverage_state": idx.get("coverageState", ""),
            "indexing_state": idx.get("indexingState", ""),
            "last_crawl_time": idx.get("lastCrawlTime", ""),
            "page_fetch_state": idx.get("pageFetchState", ""),
            "robots_txt_state": idx.get("robotsTxtState", ""),
            "crawled_as": idx.get("crawledAs", ""),
            "referring_urls": idx.get("referringUrls", []),
            "sitemap_urls": idx.get("sitemap", []),
            "mobile_verdict": mobile.get("verdict", ""),
            "mobile_issues": mobile.get("issues", []),
            "rich_results_verdict": rich.get("verdict", ""),
            "rich_results_items": rich.get("detectedItems", []),
        }
    except Exception as e:
        logger.error("GSC URL inspection error: %s", e)
        return {"url": url, "error": str(e)}
