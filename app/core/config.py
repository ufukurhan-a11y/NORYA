from pathlib import Path

from pydantic_settings import BaseSettings

# .env proje kökünde (norya/): app/core/config.py -> app/core -> app -> norya
_ROOT = Path(__file__).resolve().parent.parent.parent
_ENV_FILE = _ROOT / ".env"


class Settings(BaseSettings):
    openai_api_key: str = ""
    secret_key: str = "change-me-in-production"
    database_url: str = "sqlite:///./norya.db"
    # CORS: virgülle ayrılmış origin listesi; production'da https://alandiniz.com
    cors_origins: str = "*"
    # IP başına dakikada max istek (rate limit)
    rate_limit_per_minute: int = 30
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

    model_config = {
        "env_file": _ENV_FILE if _ENV_FILE.is_file() else ".env",
        "extra": "ignore",
    }


settings = Settings()
