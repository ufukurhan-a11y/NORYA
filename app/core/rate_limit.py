"""IP bazlı rate limiting (SlowAPI); proxy (X-Forwarded-For) destekli."""
from fastapi import Request

from slowapi import Limiter
from slowapi.util import get_remote_address


def _get_client_ip(request: Request) -> str:
    """Proxy arkasında gerçek istemci IP (Render, Nginx)."""
    xff = request.headers.get("x-forwarded-for")
    if xff:
        return xff.split(",")[0].strip()
    if request.client and request.client.host:
        return request.client.host
    return "127.0.0.1"


limiter = Limiter(key_func=_get_client_ip)
