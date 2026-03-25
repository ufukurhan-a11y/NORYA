from pathlib import Path
import sys

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import BaseSettings

# Marka adı: tüm sitede tek kaynak (title, OG, footer, schema). "NoryaAl" typo önlenir.
BRAND_NAME = "NoryaAI"

# .env proje kökünde (norya/): app/core/config.py -> app/core -> app -> norya
_ROOT = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = _ROOT / ".env"
# Config import edilir edilmez .env yüklensin (uvicorn cwd farklı olsa bile)
# Pytest sırasında test fixture'larının (özellikle DATABASE_URL) override'ını bozmamak için
# .env override davranışını kapatıyoruz.
_IS_PYTEST = "pytest" in sys.modules
load_dotenv(_ENV_FILE, override=not _IS_PYTEST)

# OpenAI anahtarının geçerli sayılması için (başında boşluk vb. olmaması)
OPENAI_KEY_PREFIX = "sk-"


class Settings(BaseSettings):
    openai_api_key: str = ""
    # Birden fazla anahtar: virgülle ayrılmış. Boşsa OPENAI_API_KEY kullanılır. Biri bozulunca/limit dolunca sıradakine geçilir.
    openai_api_keys: str = ""
    secret_key: str = "change-me-in-production"
    database_url: str = "sqlite:///./norya.db"
    # CORS: virgülle ayrılmış origin listesi; production'da https://alandiniz.com
    cors_origins: str = "*"
    # IP başına dakikada max istek (rate limit)
    rate_limit_per_minute: int = 60
    # Kayıt endpoint'i için ayrı limit (testte yüksek tutulabilir)
    rate_limit_register_per_minute: int = 3
    # PayTR (Türkiye sanal pos): iFrame API, önce ödeme alınır, bildirim URL ile hak tanınır
    paytr_merchant_id: str = ""
    paytr_merchant_key: str = ""
    paytr_merchant_salt: str = ""
    paytr_notification_url: str = ""   # Bildirim URL (PayTR buraya POST yapar), örn. https://siteniz.com/api/payment/callback
    paytr_ok_url: str = ""             # Başarılı ödeme sonrası müşteri yönlendirilecek
    paytr_fail_url: str = ""           # Hata/iptal sonrası yönlendirilecek
    paytr_currency: str = "EUR"        # Fiyat listesi para birimi (EUR); PayTR'ye TL göndermek için paytr_eur_to_try_rate kullanın
    paytr_eur_to_try_rate: float = 35.0  # EUR → TL kuru (örn. 35 = 1 EUR). >0 ise PayTR'ye TL ile ödeme gönderilir (mağazada EUR hesabı yoksa)
    paytr_amount_single: int = 1404   # Tek analiz (euro cent), 1404 = 14,04 € (KDV dahil)
    paytr_amount_monthly: int = 5400   # Aylık Pro (euro cent), 5400 = 54,00 € (KDV dahil)
    paytr_amount_yearly: int = 10692   # Yıllık Pro (euro cent), 10692 = 106,92 € (KDV dahil)
    paytr_test_mode: str = "0"         # Test için 1
    paytr_debug: bool = False          # True ise get-token'da debug_on=1; PayTR detaylı hata döner (sadece test için)
    admin_secret: str = ""             # Manuel hak tanıma (destek): POST /payment/grant için
    upload_max_mb: int = 10            # /analyze/upload için max dosya boyutu (MB)
    environment: str = "development"   # production: admin cookie Secure=True
    force_https_redirect: bool = True  # production'da HTTP istekleri HTTPS'e yönlendirilir (PayTR / güvenlik)
    # E-posta (şifre sıfırlama, doğrulama): SMTP
    smtp_host: str = ""
    smtp_port: int = 587
    smtp_user: str = ""
    smtp_password: str = ""
    smtp_from: str = "noreply@norya.com"
    smtp_from_name: str = "Norya"
    smtp_use_tls: bool = True
    # Şifre sıfırlama linkindeki site adresi (e-postadaki buton linki)
    frontend_url: str = "http://127.0.0.1:8000"
    # robots.txt Sitemap:/LLMs-Txt: mutlak URL (SEO; TestClient'ta bile canonical kalmalı). Staging için CANONICAL_SITE_URL.
    canonical_site_url: str = "https://noryaai.com"
    # QR doğrulama linki için backend adresi. Boşsa PDF isteğinin geldiği host kullanılır. Örn: https://api.norya.com
    backend_public_url: str = ""
    # PWA push bildirimleri (opsiyonel): VAPID public key (base64url). Boşsa push aboneliği alınmaz.
    vapid_public_key: str = ""
    vapid_private_key: str = ""  # Bildirim göndermek için (pywebpush ile kullanılır)
    # Google Analytics 4: Ölçüm kimliği (G-XXXXXXXXXX). Boşsa script eklenmez.
    ga_measurement_id: str = ""
    # Google Ads: Dönüşüm hesabı kimliği (AW-XXXXXXXXX). Boşsa gtag'a eklenmez.
    google_ads_conversion_id: str = "AW-18004536281"
    # Meta (Facebook) Pixel ID. Boşsa FB pixel yüklenmez.
    meta_pixel_id: str = ""
    # LinkedIn Insight Tag Partner ID. Boşsa LinkedIn script yüklenmez.
    linkedin_partner_id: str = ""
    # Google Ads: "Satın alma işlemi" dönüşüm etiketi. Hesap > Araçlar > Dönüşümler'deki etiketle birebir aynı olmalı.
    google_ads_conversion_label: str = "RF4SCL78oIYcENnXnYlD"
    # Google Search Console — HTML etiketi doğrulama: meta content değeri (Search Console ile birebir).
    google_site_verification: str = "i3QGzLVOYU64SpTMP62KQIf8soDOf6sCLKu-SMtPXHo"
    # WhatsApp iletişim: ülke kodu + numara, boşluksuz (örn. 905551234567). Boşsa varsayılan 905071703564 kullanılır.
    whatsapp_contact: str = "905071703564"
    # GİB e-Arşiv fatura (admin'den sipariş başına kesim)
    gib_earsiv_user: str = ""           # Vergi/TC no (10/11 hane)
    gib_earsiv_password: str = ""
    gib_earsiv_test_mode: str = "1"     # 1=test, 0=canlı
    invoice_company_title: str = ""     # Fatura ünvanı
    invoice_company_tax_office: str = ""
    invoice_company_address: str = ""
    invoice_company_city: str = ""
    invoice_company_email: str = ""
    invoice_eur_to_try_rate: float = 35.0  # 1 EUR = X TL (fatura tutarı TL)

    # Site genelinde gösterilen şirket bilgileri (footer, iletişim, PayTR uyumluluk)
    # ENV üzerinden özelleştirilebilir; boş bırakılırsa aşağıdaki varsayılanlar kullanılır.
    company_title: str = "NoryaAI"
    company_authorized_person: str = "Ufuk Urhan"
    company_tax_office: str = "Banaz"
    company_tax_number: str = "8940311420"
    company_address: str = "31 Ağustos Mahallesi, Tomurcuk Aysaş Mühendislik No:2 İç Kapı No:4, Banaz/Uşak, Türkiye"
    company_phone: str = "+90 507 170 35 64"
    company_support_email: str = "support@noryaai.com"
    company_contact_email: str = "info@noryaai.com"
    company_country: str = "Türkiye"

    # OpenAI bütçe takibi: satın alınan toplam kredi (USD). Dashboard'da kalan bakiye gösterilir.
    openai_budget_usd: float = 20.0

    # Google Search Console API: service account JSON dosya yolu. Boşsa SEO dashboard veri çekemez.
    gsc_service_account_json: str = ""

    # IndexNow (Bing/Yandex anında indexleme): 32 hex key. Boşsa IndexNow devre dışı.
    indexnow_key: str = ""

    # MinIO (S3 uyumlu): PDF raporları yüklenir, frontend buradan indirir
    minio_endpoint: str = ""           # örn. minio.example.com veya 127.0.0.1:9000
    minio_access_key: str = ""
    minio_secret_key: str = ""
    minio_bucket: str = "norya-pdf"   # bucket adı
    minio_secure: bool = True         # HTTPS
    minio_use_for_pdf: bool = False   # True ise PDF MinIO'ya yüklenir ve indirme oradan

    model_config = {
        "env_file": _ENV_FILE if _ENV_FILE.is_file() else ".env",
        "extra": "ignore",
    }

    @field_validator("openai_api_key", mode="before")
    @classmethod
    def strip_openai_key(cls, v: str | None) -> str:
        """Boşluk/yanlış kopya kaynaklı hataları azaltır."""
        return (v or "").strip()

    @field_validator("openai_api_keys", mode="before")
    @classmethod
    def strip_openai_keys(cls, v: str | None) -> str:
        return (v or "").strip()


settings = Settings()


def get_openai_keys() -> list[str]:
    """
    Geçerli OpenAI anahtarlarını döner (sk- ile başlayan, boşluksuz).
    OPENAI_API_KEYS varsa virgülle ayrılmış liste; yoksa OPENAI_API_KEY tek eleman.
    """
    keys_raw = (settings.openai_api_keys or "").strip()
    if keys_raw:
        keys = [k.strip() for k in keys_raw.split(",") if k.strip() and k.strip().startswith(OPENAI_KEY_PREFIX)]
        if keys:
            return keys
    single = (settings.openai_api_key or "").strip()
    if single and single.startswith(OPENAI_KEY_PREFIX):
        return [single]
    return []


def is_openai_configured() -> bool:
    """En az bir geçerli OpenAI anahtarı var mı?"""
    return len(get_openai_keys()) > 0
