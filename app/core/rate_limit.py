"""IP bazlı rate limiting (SlowAPI); proxy (X-Forwarded-For) destekli."""
from slowapi import Limiter
from slowapi.util import get_remote_address


# Varsayılan global limit: IP başına 60 istek / dakika.
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["60/minute"],
)
