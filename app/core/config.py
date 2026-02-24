from pathlib import Path

from pydantic_settings import BaseSettings

# .env proje kökünde (norya klasörü): app/core/config.py -> app -> norya
_ROOT = Path(__file__).resolve().parent.parent
_ENV_FILE = _ROOT / ".env"


class Settings(BaseSettings):
    openai_api_key: str = ""
    secret_key: str = "change-me-in-production"
    database_url: str = "sqlite:///./norya.db"

    model_config = {
        "env_file": _ENV_FILE if _ENV_FILE.is_file() else ".env",
        "extra": "ignore",
    }


settings = Settings()
