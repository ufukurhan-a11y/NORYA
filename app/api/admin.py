"""Admin API: sadece ADMIN_SECRET ile erişilir. Kullanıcılar, loglar, ödemeler, istatistikler."""
from datetime import datetime, timedelta
from pathlib import Path

from pydantic import BaseModel

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from fastapi.responses import HTMLResponse, Response
from sqlmodel import Session, select, func

from app.admin.deps import _admin_secret_constant_time_compare, require_admin_secret_or_cookie
from app.core.config import settings
from app.core.database import get_db
from app.models import AnalysisRecord, AuditLog, PaymentOrder, Presence, User
from app.services.analyze import analyze_blood_test
from app.services.report_pdf import build_report_pdf

router = APIRouter(prefix="/admin", tags=["admin"])

# Yüklenen orijinal belgeler (hastanın gönderdiği PDF/görsel) — main'deki UPLOADS_DIR ile aynı
_UPLOADS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "uploads"


def _get_admin_secret(
    x_admin_secret: str | None = Header(None, alias="X-Admin-Secret"),
    admin_secret: str | None = Query(None, description="Admin şifresi (URL'de veya header'da)"),
) -> str | None:
    return x_admin_secret or admin_secret


def _require_admin(secret: str | None = Depends(_get_admin_secret)) -> None:
    if not (settings.admin_secret or "").strip():
        raise HTTPException(status_code=503, detail="Admin paneli yapılandırılmamış (ADMIN_SECRET yok).")
    if not _admin_secret_constant_time_compare(secret, settings.admin_secret):
        raise HTTPException(status_code=403, detail="Yetkisiz.")


class AdminAnalyzeRequest(BaseModel):
    """Kontrol amaçlı: sadece metin analizi, kayıt yok."""
    text: str
    lang: str | None = "tr"


_ADMIN_HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Norya Admin</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 0; padding: 1rem; background: #0f172a; color: #e2e8f0; }
    h1 { font-size: 1.5rem; display: flex; align-items: center; gap: 10px; }
    .brand-logo { width: 56px; height: auto; max-height: 56px; object-fit: contain; flex-shrink: 0; background: #fff; }
    .login-box { max-width: 320px; margin: 2rem auto; padding: 1.5rem; background: #1e293b; border-radius: 12px; border: 1px solid #334155; }
    .login-box input { width: 100%; padding: 0.5rem; margin-bottom: 0.75rem; border: 1px solid #475569; border-radius: 6px; background: #0f172a; color: #e2e8f0; }
    .login-box button { width: 100%; padding: 0.6rem; background: #e07a5f; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600; }
    .login-box button:hover { background: #c9684a; }
    .dashboard { display: none; max-width: 1200px; margin: 0 auto; }
    .stats { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 2rem; }
    .stat { background: #1e293b; padding: 1rem; border-radius: 8px; border: 1px solid #334155; }
    .stat strong { display: block; font-size: 1.5rem; color: #e07a5f; }
    section { margin-bottom: 2rem; }
    section h2 { font-size: 1.1rem; margin-bottom: 0.5rem; color: #e2e8f0; }
    table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
    th, td { text-align: left; padding: 0.4rem 0.6rem; border-bottom: 1px solid #334155; }
    th { color: #94a3b8; }
    .err { color: #f87171; }
    .refresh { margin-left: 0.5rem; font-size: 0.85rem; padding: 0.25rem 0.5rem; background: #334155; color: #e2e8f0; border: none; border-radius: 4px; cursor: pointer; }
    .refresh:hover { background: #475569; }
    .health-link { font-size: 0.85rem; color: #e07a5f; margin-left: 1rem; }
    .health-ok { color: #22c55e; }
    .health-warn { color: #eab308; }
  </style>
</head>
<body>
  <div id="login" class="login-box">
    <h1><img src="/static/logo.png" alt="Norya AI" class="brand-logo" />Norya Admin</h1>
    <p>Admin şifresini girin (ADMIN_SECRET)</p>
    <input type="password" id="secret" placeholder="Admin şifresi" />
    <button type="button" onclick="enter()">Giriş</button>
    <p id="login-err" class="err" style="display:none;"></p>
  </div>
  <div id="dashboard" class="dashboard">
    <h1><img src="/static/logo.png" alt="Norya AI" class="brand-logo" />Norya Admin Panel</h1>
    <p style="color:#94a3b8;font-size:0.9rem;margin-top:0.25rem;"><a href="/health" target="_blank" class="health-link">Sistem durumu (health)</a> <span id="health-badge"></span></p>
    <div class="stats" id="stats"></div>
    <section>
      <h2>Son analizler <button class="refresh" onclick="loadAnalyses()">Yenile</button></h2>
      <div id="analyses-wrap"></div>
    </section>
    <section>
      <h2>Kullanıcılar <button class="refresh" onclick="loadUsers()">Yenile</button></h2>
      <div id="users-wrap"></div>
    </section>
    <section>
      <h2>Son loglar (login, register, analyze, payment) <button class="refresh" onclick="loadLogs()">Yenile</button></h2>
      <div id="logs-wrap"></div>
    </section>
    <section>
      <h2>Ödemeler <button class="refresh" onclick="loadPayments()">Yenile</button></h2>
      <div id="payments-wrap"></div>
    </section>
    <section>
      <h2>Kontrol amaçlı analiz</h2>
      <p style="color:#94a3b8;font-size:0.85rem;margin-bottom:0.5rem;">Metin gönder, sadece sonuç dönsün (kayıt yok, rapor yok).</p>
      <textarea id="control-analyze-text" rows="4" style="width:100%;max-width:600px;padding:0.5rem;border:1px solid #475569;border-radius:6px;background:#0f172a;color:#e2e8f0;font-family:inherit;margin-bottom:0.5rem;" placeholder="Örn: Glukoz 95 mg/dL, HbA1c 5.2%..."></textarea>
      <br /><button type="button" class="refresh" onclick="runControlAnalyze()">Analiz yap (kontrol)</button>
      <div id="control-analyze-result" style="margin-top:0.75rem;padding:0.75rem;background:#1e293b;border-radius:8px;border:1px solid #334155;white-space:pre-wrap;font-size:0.9rem;display:none;"></div>
    </section>
  </div>
  <script>
    function getSecret() { return document.getElementById('secret').value.trim() || sessionStorage.getItem('norya_admin_secret'); }
    function setSecret(s) { sessionStorage.setItem('norya_admin_secret', s); }
    function headers() { const s = getSecret(); return s ? { 'X-Admin-Secret': s } : {}; }
    function api(path) { return fetch(path, { headers: headers() }).then(r => { if (!r.ok) throw new Error(r.status + ' ' + r.statusText); return r.json(); }); }
    function enter() {
      const s = document.getElementById('secret').value.trim();
      if (!s) return;
      setSecret(s);
      api('/admin/stats').then(() => { document.getElementById('login').style.display='none'; document.getElementById('dashboard').style.display='block'; loadAll(); }).catch(e => { document.getElementById('login-err').textContent = e.message; document.getElementById('login-err').style.display='block'; });
    }
    function loadAll() { loadStats(); loadAnalyses(); loadUsers(); loadLogs(); loadPayments(); loadHealth(); }
    function loadHealth() {
      fetch('/health').then(r => r.json()).then(d => {
        var el = document.getElementById('health-badge');
        if (!el) return;
        el.innerHTML = d.status === 'ok' ? '<span class="health-ok">● OK</span>' + (d.openai_configured ? ' · OpenAI tanımlı' : ' <span class="health-warn">· OpenAI yok</span>') : '<span class="err">Hata</span>';
      }).catch(() => { var el = document.getElementById('health-badge'); if (el) el.innerHTML = '<span class="err">Health yok</span>'; });
    }
    function viewPdf(id) {
      var s = getSecret();
      if (!s) return;
      fetch('/admin/analyses/' + id + '/pdf', { headers: { 'X-Admin-Secret': s } })
        .then(function(r) { if (!r.ok) throw new Error(r.status); return r.blob(); })
        .then(function(blob) { var u = URL.createObjectURL(blob); window.open(u, '_blank'); })
        .catch(function(e) { alert('PDF açılamadı: ' + e.message); });
    }
    function viewOriginal(id) {
      var s = getSecret();
      if (!s) return;
      fetch('/admin/analyses/' + id + '/original', { headers: { 'X-Admin-Secret': s } })
        .then(function(r) { if (!r.ok) throw new Error(r.status); return r.blob(); })
        .then(function(blob) { var u = URL.createObjectURL(blob); window.open(u, '_blank'); })
        .catch(function(e) { alert('Orijinal belge açılamadı: ' + e.message); });
    }
    function loadAnalyses() {
      api('/admin/analyses?limit=50').then(arr => {
        if (arr.length === 0) { document.getElementById('analyses-wrap').innerHTML = '<p>Analiz yok.</p>'; return; }
        let html = '<table><tr><th>ID</th><th>Tarih</th><th>Kullanıcı (e-posta)</th><th>Kaynak</th><th>Giriş önizleme</th><th>Sonuç önizleme</th><th>PDF</th><th>Orijinal belge</th></tr>';
        arr.forEach(a => {
          var origBtn = a.has_original ? '<button type="button" class="refresh" onclick="viewOriginal('+a.id+')">Hastanın belgesi</button>' : '-';
          html += '<tr><td>'+a.id+'</td><td>'+(a.created_at||'-')+'</td><td>'+(a.user_email ? escape(a.user_email) : ('ID '+a.user_id))+'</td><td>'+escape(a.source||'')+'</td><td>'+(a.input_preview ? escape(a.input_preview.slice(0,40)) : '-')+'…</td><td>'+(a.result_preview ? escape(a.result_preview.slice(0,50)) : '-')+'…</td><td><button type="button" class="refresh" onclick="viewPdf('+a.id+')">Norya raporu</button></td><td>'+origBtn+'</td></tr>';
        });
        html += '</table>'; document.getElementById('analyses-wrap').innerHTML = html;
      }).catch(e => { document.getElementById('analyses-wrap').innerHTML = '<span class="err">'+e.message+'</span>'; });
    }
    function loadStats() {
      api('/admin/stats').then(d => {
        document.getElementById('stats').innerHTML = [
          ['Şu an sitede', d.active_now ?? 0],
          ['Toplam kullanıcı', d.total_users],
          ['Toplam analiz', d.total_analyses],
          ['Tamamlanan ödeme', d.total_payments_completed],
          ['Son 24h giriş', d.logins_last_24h],
          ['Son 24h benzersiz giriş', d.unique_users_logged_in_24h],
          ['Son 1h analiz', d.analyses_last_1h]
        ].map(([l,v]) => '<div class="stat"><span>'+l+'</span><strong>'+v+'</strong></div>').join('');
      }).catch(e => { document.getElementById('stats').innerHTML = '<span class="err">'+e.message+'</span>'; });
    }
    function loadUsers() {
      api('/admin/users?limit=200').then(arr => {
        if (arr.length === 0) { document.getElementById('users-wrap').innerHTML = '<p>Kullanıcı yok.</p>'; return; }
        let html = '<table><tr><th>ID</th><th>E-posta</th><th>Ad</th><th>Telefon</th><th>Ülke</th><th>Plan</th><th>Ek hak</th><th>Kayıt</th></tr>';
        arr.forEach(u => { html += '<tr><td>'+u.id+'</td><td>'+escape(u.email)+'</td><td>'+escape(u.full_name||'')+'</td><td>'+(u.phone?escape(u.phone):'-')+'</td><td>'+(u.country||'-')+'</td><td>'+u.plan+'</td><td>'+u.extra_credits+'</td><td>'+(u.created_at||'-')+'</td></tr>'; });
        html += '</table>'; document.getElementById('users-wrap').innerHTML = html;
      }).catch(e => { document.getElementById('users-wrap').innerHTML = '<span class="err">'+e.message+'</span>'; });
    }
    function loadLogs() {
      api('/admin/logs?limit=200').then(arr => {
        if (arr.length === 0) { document.getElementById('logs-wrap').innerHTML = '<p>Log yok.</p>'; return; }
        let html = '<table><tr><th>Tarih</th><th>Event</th><th>User</th><th>IP</th><th>Ülke</th></tr>';
        arr.forEach(l => { html += '<tr><td>'+(l.created_at||'-')+'</td><td>'+escape(l.event)+'</td><td>'+(l.user_email ? escape(l.user_email) : (l.user_id||'-'))+'</td><td>'+(l.ip||'-')+'</td><td>'+(l.country||'-')+'</td></tr>'; });
        html += '</table>'; document.getElementById('logs-wrap').innerHTML = html;
      }).catch(e => { document.getElementById('logs-wrap').innerHTML = '<span class="err">'+e.message+'</span>'; });
    }
    function loadPayments() {
      api('/admin/payments?limit=100').then(arr => {
        if (arr.length === 0) { document.getElementById('payments-wrap').innerHTML = '<p>Ödeme yok.</p>'; return; }
        let html = '<table><tr><th>Tarih</th><th>merchant_oid</th><th>E-posta</th><th>Ürün</th><th>Tutar (kr)</th><th>Durum</th></tr>';
        arr.forEach(p => { var amt = (p.amount_eur != null ? p.amount_eur.toFixed(2) + ' €' : (p.amount_kurus || 0)); html += '<tr><td>'+(p.created_at||'-')+'</td><td>'+escape(p.merchant_oid)+'</td><td>'+(p.user_email?escape(p.user_email):p.user_id)+'</td><td>'+p.product+'</td><td>'+amt+'</td><td>'+p.status+'</td></tr>'; });
        html += '</table>'; document.getElementById('payments-wrap').innerHTML = html;
      }).catch(e => { document.getElementById('payments-wrap').innerHTML = '<span class="err">'+e.message+'</span>'; });
    }
    function escape(s) { if (!s) return ''; const d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
    function runControlAnalyze() {
      var text = document.getElementById('control-analyze-text').value.trim();
      if (!text) { alert('Metin girin.'); return; }
      var el = document.getElementById('control-analyze-result'); el.style.display = 'block'; el.textContent = 'İşleniyor...';
      fetch('/admin/analyze', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Admin-Secret': getSecret() }, body: JSON.stringify({ text: text, lang: 'tr' }) })
        .then(function(r) { if (!r.ok) throw new Error(r.status + ' ' + r.statusText); return r.json(); })
        .then(function(d) { el.textContent = d.sonuc || '(boş sonuç)'; })
        .catch(function(e) { el.innerHTML = '<span class="err">' + escape(e.message) + '</span>'; });
    }
    if (sessionStorage.getItem('norya_admin_secret')) { document.getElementById('login').style.display='none'; document.getElementById('dashboard').style.display='block'; loadAll(); }
  </script>
</body>
</html>"""


def get_admin_html():
    """Admin panel HTML (main'den doğrudan route için kullanılır)."""
    return _ADMIN_HTML


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def admin_dashboard_page():
    """Admin panel giriş sayfası. Şifre ile /admin/stats vb. API'ler kullanılır. /admin ve /admin/ ikisi de çalışır."""
    return _ADMIN_HTML


@router.post("/analyze")
def admin_analyze_control(
    body: AdminAnalyzeRequest,
    _: None = Depends(_require_admin),
):
    """Kontrol amaçlı: metin gönder, sadece analiz sonucu dönsün. Kayıt yapılmaz, rapor üretilmez."""
    if not (body.text or "").strip():
        raise HTTPException(status_code=400, detail="Metin boş.")
    try:
        sonuc, _ = analyze_blood_test(body.text.strip(), detailed=True, lang=body.lang or "tr")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analiz hatası: {e!s}")
    return {"sonuc": sonuc}


@router.get("/stats")
def admin_stats(
    db: Session = Depends(get_db),
    _: None = Depends(_require_admin),
):
    """Özet istatistikler: toplam kullanıcı, analiz, ödeme; son 24h giriş; son 1h analiz (aktif kullanım proxy)."""
    now = datetime.utcnow()
    day_ago = now - timedelta(hours=24)
    hour_ago = now - timedelta(hours=1)
    active_threshold = now - timedelta(minutes=2)  # Son 2 dk heartbeat = şu an sitede

    total_users = db.exec(select(func.count(User.id))).one() or 0
    total_analyses = db.exec(select(func.count(AnalysisRecord.id))).one() or 0
    total_payments = db.exec(select(func.count(PaymentOrder.id)).where(PaymentOrder.status == "completed")).one() or 0

    logins_24h = db.exec(
        select(func.count(AuditLog.id)).where(AuditLog.event == "login").where(AuditLog.created_at >= day_ago)
    ).one() or 0
    analyses_1h = db.exec(
        select(func.count(AnalysisRecord.id)).where(AnalysisRecord.created_at >= hour_ago)
    ).one() or 0
    unique_logins_24h = (
        db.exec(
            select(func.count(func.distinct(AuditLog.user_id))).where(AuditLog.event == "login").where(AuditLog.created_at >= day_ago)
        ).one()
        or 0
    )
    active_now = (
        db.exec(select(func.count(Presence.id)).where(Presence.last_seen_at >= active_threshold)).one()
        or 0
    )

    return {
        "total_users": total_users,
        "total_analyses": total_analyses,
        "total_payments_completed": total_payments,
        "logins_last_24h": logins_24h,
        "unique_users_logged_in_24h": unique_logins_24h,
        "analyses_last_1h": analyses_1h,
        "active_now": active_now,
    }


@router.get("/analyses")
def admin_analyses(
    db: Session = Depends(get_db),
    _: None = Depends(_require_admin),
    limit: int = Query(50, le=200),
    offset: int = Query(0, ge=0),
):
    """Son analiz kayıtları: id, input_preview, result_preview, source, created_at."""
    stmt = (
        select(AnalysisRecord)
        .order_by(AnalysisRecord.id.desc())
        .offset(offset)
        .limit(limit)
    )
    rows = list(db.exec(stmt).all())
    user_ids = {r.user_id for r in rows}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email or ""
    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "user_email": users_map.get(r.user_id, ""),
            "input_preview": (r.input_text[:200] + "…") if (r.input_text and len(r.input_text) > 200) else (r.input_text or ""),
            "result_preview": (r.result_text[:200] + "…") if (r.result_text and len(r.result_text) > 200) else (r.result_text or ""),
            "source": getattr(r, "source", "") or "",
            "created_at": r.created_at.isoformat() if getattr(r, "created_at", None) else None,
            "has_original": bool(getattr(r, "original_stored_path", None)),
        }
        for r in rows
    ]


@router.get("/analyses/{analysis_id}/pdf", response_class=Response)
def admin_analysis_pdf(
    analysis_id: int,
    lang: str = Query("tr", description="Rapor dili: tr, en, de, fr, es, it, he, ar, hi, el, cs, sr"),
    db: Session = Depends(get_db),
    _: None = Depends(require_admin_secret_or_cookie),
):
    """Admin: İlgili analizin PDF raporunu döndürür (çok dilli başlık/etiketler)."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec:
        raise HTTPException(status_code=404, detail="Analiz bulunamadı.")
    report_date = None
    if getattr(rec, "created_at", None):
        dt = rec.created_at
        if hasattr(dt, "strftime"):
            report_date = dt.strftime("%d.%m.%Y %H:%M")
        else:
            report_date = str(dt)
    report_lang = (lang or "tr").strip().lower()[:5]
    try:
        pdf_bytes = build_report_pdf(
            result_text=rec.result_text or "",
            report_date=report_date,
            lang=report_lang,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF oluşturulamadı: {e!s}")
    filename = f"norya-rapor-{analysis_id}.pdf"
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )


@router.get("/analyses/{analysis_id}/original", response_class=Response)
def admin_analysis_original(
    analysis_id: int,
    db: Session = Depends(get_db),
    _: None = Depends(require_admin_secret_or_cookie),
):
    """Admin: Hastanın yüklediği orijinal belgeyi döndürür (PDF/görsel). Yanında 'PDF görüntüle' ile Norya raporu açılır."""
    rec = db.get(AnalysisRecord, analysis_id)
    if not rec or not getattr(rec, "original_stored_path", None):
        raise HTTPException(status_code=404, detail="Orijinal belge yok.")
    path = _UPLOADS_DIR / rec.original_stored_path
    if not path.is_file():
        raise HTTPException(status_code=404, detail="Dosya bulunamadı.")
    content = path.read_bytes()
    filename = getattr(rec, "original_filename", None) or f"orijinal-{analysis_id}"
    ext = path.suffix.lower()
    media_types = {
        ".pdf": "application/pdf",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }
    media_type = media_types.get(ext, "application/octet-stream")
    return Response(
        content=content,
        media_type=media_type,
        headers={"Content-Disposition": f'inline; filename="{filename}"'},
    )


@router.get("/users")
def admin_users(
    db: Session = Depends(get_db),
    _: None = Depends(_require_admin),
    limit: int = Query(200, le=500),
    offset: int = Query(0, ge=0),
):
    """Kullanıcı listesi: id, email, full_name, phone, country, plan, extra_credits, created_at."""
    stmt = select(User).order_by(User.id.desc()).offset(offset).limit(limit)
    users = list(db.exec(stmt).all())
    return [
        {
            "id": u.id,
            "email": u.email,
            "full_name": getattr(u, "full_name", "") or "",
            "phone": getattr(u, "phone", None) or None,
            "country": getattr(u, "country", None) or None,
            "plan": getattr(u, "plan", "free") or "free",
            "extra_credits": getattr(u, "extra_credits", 0) or 0,
            "created_at": (u.created_at.isoformat() if getattr(u, "created_at", None) else None),
        }
        for u in users
    ]


@router.get("/logs")
def admin_logs(
    db: Session = Depends(get_db),
    _: None = Depends(_require_admin),
    limit: int = Query(200, le=500),
    event: str | None = Query(None, description="Filtre: login, register, analyze, payment_*, payment_callback_error"),
):
    """Son audit logları: event, user_id, ip, created_at. user_id varsa email de döner."""
    stmt = select(AuditLog).order_by(AuditLog.id.desc()).limit(limit)
    if event:
        stmt = stmt.where(AuditLog.event == event)
    logs = list(db.exec(stmt).all())
    user_ids = {log.user_id for log in logs if log.user_id}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email
    return [
        {
            "id": log.id,
            "event": log.event,
            "user_id": log.user_id,
            "user_email": users_map.get(log.user_id) if log.user_id else None,
            "ip": log.ip,
            "country": getattr(log, "country", None) or None,
            "created_at": log.created_at.isoformat() if log.created_at else None,
        }
        for log in logs
    ]


@router.get("/payments")
def admin_payments(
    db: Session = Depends(get_db),
    _: None = Depends(_require_admin),
    limit: int = Query(100, le=300),
    status: str | None = Query(None, description="pending | completed | failed"),
):
    """Ödeme siparişleri: merchant_oid, user_id, email, product, amount_kurus, status, is_processed, created_at."""
    stmt = select(PaymentOrder).order_by(PaymentOrder.id.desc()).limit(limit)
    if status:
        stmt = stmt.where(PaymentOrder.status == status)
    orders = list(db.exec(stmt).all())
    user_ids = {o.user_id for o in orders}
    users_map = {}
    if user_ids:
        for u in db.exec(select(User).where(User.id.in_(user_ids))).all():
            users_map[u.id] = u.email
    return [
        {
            "id": o.id,
            "merchant_oid": o.merchant_oid,
            "user_id": o.user_id,
            "user_email": users_map.get(o.user_id),
            "product": o.product,
            "amount_kurus": o.amount_kurus,
            "amount_eur": (o.amount_kurus or 0) / 100,
            "currency": getattr(o, "currency", None) or "EUR",
            "status": o.status,
            "is_processed": getattr(o, "is_processed", False),
            "processed_at": o.processed_at.isoformat() if getattr(o, "processed_at", None) else None,
            "created_at": o.created_at.isoformat() if o.created_at else None,
        }
        for o in orders
    ]
