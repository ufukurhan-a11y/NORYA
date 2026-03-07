import hashlib
import hmac
from datetime import datetime, timedelta

import bcrypt
from jose import JWTError, jwt

from .config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 gün
MAX_BCRYPT_BYTES = 72  # bcrypt limiti


def hash_password(password: str) -> str:
    p = password.encode("utf-8")[:MAX_BCRYPT_BYTES]
    return bcrypt.hashpw(p, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    p = plain.encode("utf-8")[:MAX_BCRYPT_BYTES]
    return bcrypt.checkpw(p, hashed.encode("utf-8"))


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError:
        return None


# PDF indirme: canlıda proxy Authorization kesebildiği için URL'de tek kullanımlık token
PDF_TOKEN_EXPIRE_MINUTES = 5


def create_pdf_access_token(analysis_id: int, user_id: int) -> str:
    to_encode = {"p": "pdf", "aid": analysis_id, "uid": user_id}
    expire = datetime.utcnow() + timedelta(minutes=PDF_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)


def decode_pdf_access_token(token: str) -> tuple[int, int] | None:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        if payload.get("p") != "pdf":
            return None
        aid = payload.get("aid")
        uid = payload.get("uid")
        if aid is None or uid is None:
            return None
        return (int(aid), int(uid))
    except (JWTError, TypeError, ValueError):
        return None


# Rapor doğrulama (QR): tahmin edilemez signed token; DB'de token saklanmaz, doğrulama HMAC ile yapılır.
def create_report_verification_token(report_id: str, verification_code: str) -> str:
    """report_id + verification_code ile imzalı token üretir. QR URL'de kullanılır."""
    raw = f"{report_id}:{verification_code}"
    sig = hmac.new(
        (settings.secret_key or "norya-report-verify").encode("utf-8"),
        raw.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return sig


def verify_report_verification_token(report_id: str, verification_code: str, token: str) -> bool:
    """URL'den gelen token'ın report_id + verification_code ile eşleşip eşleşmediğini kontrol eder."""
    if not report_id or not verification_code or not token:
        return False
    expected = create_report_verification_token(report_id, verification_code)
    return hmac.compare_digest(expected, token)
