"""IP'den ülke kodu ve şehir çözümleme. ip-api.com kullanır (ücretsiz, dakikada 45 istek)."""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

# Önbellek: IP -> (country_code, city, expires). Basit in-memory cache.
_geo_cache: dict[str, tuple[str, str | None, float]] = {}
_CACHE_TTL = 3600.0  # 1 saat


def _now() -> float:
    import time
    return time.monotonic()


def get_geo_from_ip(ip: str | None) -> tuple[str | None, str | None]:
    """
    IP adresinden (ülke kodu, şehir) döner. Örn: ("TR", "Istanbul").
    Hata veya localhost'ta (None, None).
    """
    if not ip or ip in ("127.0.0.1", "::1", "localhost"):
        return (None, None)
    now = _now()
    if ip in _geo_cache:
        code, city, exp = _geo_cache[ip]
        if exp > now:
            return (code, city)
        del _geo_cache[ip]
    try:
        req = Request(
            f"http://ip-api.com/json/{ip}?fields=countryCode,city",
            method="GET",
        )
        with urlopen(req, timeout=2) as r:
            data = json.loads(r.read().decode())
            code = data.get("countryCode") or None
            city = (data.get("city") or "").strip() or None
            if code or city:
                _geo_cache[ip] = (code, city, now + _CACHE_TTL)
                return (code, city)
    except (URLError, OSError, ValueError, KeyError):
        pass
    return (None, None)


def get_country_from_ip(ip: str | None) -> str | None:
    """IP adresinden ülke kodu döner (TR, US vb.). Hata veya localhost'ta None."""
    country, _ = get_geo_from_ip(ip)
    return country
