"""Enterprise dashboard dependency: kullanıcının aktif kurumunu belirle."""
from fastapi import Cookie, Depends, HTTPException, Request, status
from sqlmodel import Session, select

from app.core.database import get_db
from app.models import User
from app.models.institution import Institution, InstitutionMembership


def _get_current_user_from_cookie(request: Request, db: Session) -> User | None:
    """JWT token'ı cookie'den oku (enterprise dashboard browser-tabanlı)."""
    from app.core.security import decode_access_token
    token = request.cookies.get("access_token")
    if not token:
        auth = request.headers.get("authorization", "")
        if auth.startswith("Bearer "):
            token = auth[7:]
    if not token:
        return None
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        return None
    user = db.get(User, int(payload["sub"]))
    if user and getattr(user, "is_banned", False):
        return None
    return user


def require_enterprise_user(request: Request, db: Session = Depends(get_db)):
    """Aktif kurumsal üyeliği olan kullanıcıyı döndür. Yoksa login sayfasına yönlendir."""
    user = _get_current_user_from_cookie(request, db)
    if not user:
        from fastapi.responses import RedirectResponse
        return RedirectResponse(url="/giris?next=/enterprise/dashboard", status_code=303)

    inst_id_cookie = request.cookies.get("enterprise_inst_id")
    if inst_id_cookie:
        try:
            inst_id = int(inst_id_cookie)
            membership = db.exec(
                select(InstitutionMembership).where(
                    InstitutionMembership.user_id == user.id,
                    InstitutionMembership.institution_id == inst_id,
                    InstitutionMembership.is_active == True,
                )
            ).first()
            if membership:
                inst = db.get(Institution, inst_id)
                if inst and inst.is_active and inst.status != "suspended":
                    return {"user": user, "membership": membership, "institution": inst}
                if inst and (not inst.is_active or inst.status == "suspended"):
                    from fastapi.responses import HTMLResponse
                    return HTMLResponse(
                        _no_membership_page(user.email, suspended=True),
                        status_code=403,
                    )
        except (ValueError, TypeError):
            pass

    membership = db.exec(
        select(InstitutionMembership).where(
            InstitutionMembership.user_id == user.id,
            InstitutionMembership.is_active == True,
        )
    ).first()
    if not membership:
        from fastapi.responses import HTMLResponse
        return HTMLResponse(
            _no_membership_page(user.email),
            status_code=403,
        )
    inst = db.get(Institution, membership.institution_id)
    if not inst or not inst.is_active or inst.status == "suspended":
        from fastapi.responses import HTMLResponse
        return HTMLResponse(
            _no_membership_page(user.email, suspended=True),
            status_code=403,
        )
    return {"user": user, "membership": membership, "institution": inst}


def _no_membership_page(email: str, suspended: bool = False) -> str:
    title = "Kurum askıda" if suspended else "Kurumsal erişim bulunamadı"
    message = (
        "Kurumunuz şu anda askıya alınmış durumda. Lütfen kurum yöneticinizle iletişime geçin."
        if suspended
        else "Bu hesaba bağlı aktif bir kurumsal üyelik bulunamadı. Bir kuruma davet edilmeniz gerekmektedir."
    )
    return f"""<!DOCTYPE html>
<html lang="tr"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title} — NoryaAI</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/>
</head><body class="bg-[#f8f9fa] min-h-screen flex items-center justify-center p-6" style="font-family:Inter,sans-serif">
<div class="max-w-md w-full bg-white rounded-2xl shadow-lg p-8 text-center">
  <div class="w-16 h-16 rounded-2xl bg-[#006a69]/10 flex items-center justify-center mx-auto mb-6">
    <span class="material-symbols-outlined text-[#006a69]" style="font-size:36px">{'pause_circle' if suspended else 'domain_disabled'}</span>
  </div>
  <h1 style="font-family:Manrope,sans-serif" class="text-xl font-bold text-[#191c1d] mb-3">{title}</h1>
  <p class="text-sm text-[#3d4949] leading-relaxed mb-6">{message}</p>
  <p class="text-xs text-[#6d7a79] mb-6">Oturum: {email}</p>
  <div class="flex flex-col gap-3">
    <a href="/" class="block w-full py-3 rounded-xl text-sm font-semibold text-white bg-[#006a69] hover:brightness-105 transition-all">Ana sayfaya dön</a>
    <a href="mailto:enterprise@norya.ai" class="block w-full py-3 rounded-xl text-sm font-semibold text-[#006a69] border border-[#006a69]/20 hover:bg-[#006a69]/5 transition-all">Destek ile iletişime geç</a>
  </div>
</div>
</body></html>"""
