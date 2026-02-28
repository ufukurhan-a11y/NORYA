from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings

# .env proje kökünde (norya/): app/core/config.py -> app/core -> app -> norya
_ROOT = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = _ROOT / ".env"

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
    paytr_currency: str = "EUR"        # Tahsilat para birimi: EUR (PayTR TL destekler; EUR için Stripe vb. kullanın)
    paytr_amount_single: int = 1300   # Tek analiz (euro cent), 1300 = 13,00 €
    paytr_amount_monthly: int = 5000   # Aylık Pro (euro cent), 5000 = 50,00 €
    paytr_amount_yearly: int = 9900   # Yıllık Pro (euro cent), 9900 = 99,00 €
    paytr_test_mode: str = "0"         # Test için 1
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
    # PWA push bildirimleri (opsiyonel): VAPID public key (base64url). Boşsa push aboneliği alınmaz.
    vapid_public_key: str = ""
    vapid_private_key: str = ""  # Bildirim göndermek için (pywebpush ile kullanılır)
    # Google Analytics 4: Ölçüm kimliği (G-XXXXXXXXXX). Boşsa script eklenmez.
    ga_measurement_id: str = ""
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
