"""Admin: Fatura ve gider linkleri — PayTR, Render, Cursor, OpenAI, Cloudflare tek sayfadan."""
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from app.core.templating import Jinja2Templates

from app.admin.deps import require_admin_cookie

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Fatura / ödeme geçmişi sayfaları (dış linkler)
BILLING_LINKS = [
    {
        "name": "PayTR",
        "url": "https://www.paytr.com",
        "description": "Üye paneli → İşlemler / Raporlar. Tahsilat raporu, işlem listesi.",
        "icon": "💳",
    },
    {
        "name": "Render",
        "url": "https://dashboard.render.com/billing",
        "description": "Billing → Invoices / Usage. Fatura indir.",
        "icon": "☁️",
    },
    {
        "name": "Cursor",
        "url": "https://cursor.com/settings",
        "description": "Subscription / Billing veya e-posta faturaları.",
        "icon": "⌨️",
    },
    {
        "name": "OpenAI (ChatGPT API)",
        "url": "https://platform.openai.com/account/billing",
        "description": "API kullanımı, kredi, faturalar.",
        "icon": "🤖",
    },
    {
        "name": "Cloudflare",
        "url": "https://dash.cloudflare.com/?to=/:account/billing",
        "description": "Billing & Usage. Faturalar, kullanım özeti.",
        "icon": "🛡️",
    },
    {
        "name": "Google (Analytics & Ads)",
        "url": "https://ads.google.com/aw/billing",
        "description": "Google Ads faturaları. Analytics ücretsiz; Ads kullanım varsa buradan.",
        "icon": "📊",
    },
    {
        "name": "GİB e-Arşiv",
        "url": "https://earsivportal.efatura.gov.tr",
        "description": "E-arşiv fatura girişi, GİB portal. Admin’den kesilen faturalar bu sistemde.",
        "icon": "📑",
    },
    {
        "name": "Domain (alan adı)",
        "url": "https://www.cloudflare.com/products/registrar/",
        "description": "Alan adı (noryaai.com) hangi firmadaysa: Cloudflare, Namecheap, GoDaddy vb. Fatura orada.",
        "icon": "🌐",
    },
    {
        "name": "E-posta servisi (SMTP)",
        "url": "https://resend.com/billing",
        "description": "Şifre sıfırlama mailleri için kullandığınız servis: Gmail, SendGrid, Resend, Mailgun vb.",
        "icon": "✉️",
    },
]

# Aklınıza gelebilecek diğer servisler (sayfada liste olarak gösterilir)
OTHER_BILLING_HINTS = [
    "GitHub (Copilot / Team) — github.com/settings/billing",
    "Sentry (hata takibi) — sentry.io/settings/billing",
    "Vercel / Netlify — frontend host ise",
    "1Password / LastPass — ekip şifre yöneticisi",
    "Notion / Slack — ekip araçları",
    "Figma — tasarım aboneliği",
    "Bankalar — PayTR tahsilat hesabı, kredi kartı ödemeleri",
]


@router.get("", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
def billing_links_page(request: Request, _=Depends(require_admin_cookie)):
    """Fatura ve gider linkleri — tüm servislere tek sayfadan erişim."""
    return templates.TemplateResponse(
        "admin/billing_links.html",
        {"request": request, "links": BILLING_LINKS, "other_hints": OTHER_BILLING_HINTS},
    )
