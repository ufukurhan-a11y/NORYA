"""IP'den ülke kodu (TR, US vb.) çözümleme. ip-api.com kullanır (ücretsiz, dakikada 45 istek)."""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

# Önbellek: IP -> (country_code, expires). Basit in-memory cache.
_geo_cache: dict[str, tuple[str, float]] = {}
_CACHE_TTL = 3600.0  # 1 saat


def _now() -> float:
    import time
    return time.monotonic()


def get_country_from_ip(ip: str | None) -> str | None:
    """IP adresinden ülke kodu döner (TR, US vb.). Hata veya localhost'ta None."""
    if not ip or ip in ("127.0.0.1", "::1", "localhost"):
        return None
    now = _now()
    if ip in _geo_cache:
        code, exp = _geo_cache[ip]
        if exp > now:
            return code
        del _geo_cache[ip]
    try:
        req = Request(f"http://ip-api.com/json/{ip}?fields=countryCode", method="GET")
        with urlopen(req, timeout=2) as r:
            data = json.loads(r.read().decode())
            code = data.get("countryCode")
            if code:
                _geo_cache[ip] = (code, now + _CACHE_TTL)
                return code
    except (URLError, OSError, ValueError, KeyError):
        pass
    return None
