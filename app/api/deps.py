from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session, select

from app.core.config import settings
from app.core.database import get_db
from app.core.security import decode_access_token, hash_password
from app.models import User

security = HTTPBearer(auto_error=False)

# Yerel test: development ortamında analiz için giriş zorunlu değil; token yoksa bu kullanıcı kullanılır.
DEV_GUEST_EMAIL = "dev@local.norya"


def get_current_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> int:
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Giriş yapmanız gerekiyor.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = decode_access_token(credentials.credentials)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz veya süresi dolmuş token.",
        )
    return int(payload["sub"])


def get_current_user(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
) -> User:
    user = db.get(User, user_id)
    if not user:
        # Token geçerli ama kullanıcı DB'de yok (örn. geçici veritabanı sıfırlandı) → oturumu geçersiz say
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Oturumunuz sona erdi veya geçersiz. Lütfen tekrar giriş yapın.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if getattr(user, "is_banned", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Hesabınız askıya alındı. Sorularınız için iletişim sayfasından bize ulaşın.",
        )
    return user


def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: Session = Depends(get_db),
) -> User | None:
    """Giriş yapılmışsa User döner, yoksa None. PayTR init gibi opsiyonel auth endpoint'leri için."""
    if not credentials:
        return None
    try:
        payload = decode_access_token(credentials.credentials)
        if not payload or "sub" not in payload:
            return None
        user_id = int(payload["sub"])
        user = db.get(User, user_id)
        if user and getattr(user, "is_banned", False):
            return None
        return user
    except Exception:
        return None


def _get_or_create_dev_guest(db: Session) -> User:
    """Development ortamında token yokken kullanılacak dev guest kullanıcıyı getir veya oluştur."""
    stmt = select(User).where(User.email == DEV_GUEST_EMAIL)
    user = db.exec(stmt).first()
    if user:
        return user
    user = User(
        email=DEV_GUEST_EMAIL,
        hashed_password=hash_password("dev-no-login"),
        full_name="Dev (yerel test)",
        plan="free",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_current_user_or_dev_guest(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    """Analiz endpoint'leri için: production'da giriş zorunlu; development'ta token yoksa dev guest kullanılır."""
    env = (getattr(settings, "environment", "") or "").strip().lower()
    if env == "production":
        if not credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Giriş yapmanız gerekiyor.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        payload = decode_access_token(credentials.credentials)
        if not payload or "sub" not in payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Geçersiz veya süresi dolmuş token.",
            )
        user_id = int(payload["sub"])
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Oturumunuz sona erdi veya geçersiz. Lütfen tekrar giriş yapın.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if getattr(user, "is_banned", False):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Hesabınız askıya alındı. Sorularınız için iletişim sayfasından bize ulaşın.",
            )
        return user
    # development: token varsa normal user, yoksa dev guest
    if credentials:
        try:
            payload = decode_access_token(credentials.credentials)
            if payload and "sub" in payload:
                user = db.get(User, int(payload["sub"]))
                if user and not getattr(user, "is_banned", False):
                    return user
        except Exception:
            pass
    return _get_or_create_dev_guest(db)
