import hashlib
import json
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

UTC = timezone.utc


def stable_dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def make_cache_key(
    *,
    labs_norm: dict,
    lang: str,
    plan: str,
    model: str,
    sex: str | None = None,
    age_band: str | None = None,
    prompt_version: int = 1,
) -> str:
    payload = {
        "labs": labs_norm,
        "lang": lang,
        "plan": plan,
        "model": model,
        "sex": sex,
        "age_band": age_band,
        "v": prompt_version,
    }
    raw = stable_dumps(payload).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def now_iso() -> str:
    return datetime.now(UTC).isoformat()


def expires_iso(days: int) -> str:
    return (datetime.now(UTC) + timedelta(days=days)).isoformat()


def is_expired(expires_at: Optional[str]) -> bool:
    if not expires_at:
        return False
    return datetime.fromisoformat(expires_at.replace("Z", "+00:00")) <= datetime.now(UTC)
