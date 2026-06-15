from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import OpenAI, AuthenticationError, APIConnectionError, RateLimitError, APIError

load_dotenv()

_api_key = os.getenv("OPENAI_API_KEY", "").strip()
if not _api_key or not _api_key.startswith("sk-"):
    raise RuntimeError(
        "OPENAI_API_KEY .env dosyasında eksik veya geçersiz (sk- ile başlamalı)."
    )

client = OpenAI(api_key=_api_key)

app = FastAPI()


class AnalyzeRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {"durum": "hazır", "servis": "norya-api"}


@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Bu kan tahlili ifadesini hastaya anlaşılır şekilde açıkla: {req.text}"
                    ),
                }
            ],
            max_tokens=1024,
        )
        sonuc = response.choices[0].message.content or ""
        return {"sonuc": sonuc, "not": "Norya AI yorumladı."}
    except AuthenticationError as e:
        raise HTTPException(
            status_code=503,
            detail="AI erişimi başarısız: OPENAI_API_KEY geçersiz veya billing kapalı.",
        ) from e
    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail="AI yoğun: Lütfen biraz sonra tekrar deneyin.",
        ) from e
    except APIConnectionError as e:
        raise HTTPException(
            status_code=503,
            detail="AI bağlantı sorunu: Ağ/servis geçici olarak erişilemiyor.",
        ) from e
    except APIError as e:
        raise HTTPException(
            status_code=502,
            detail="AI servis hatası: Geçici sorun olabilir.",
        ) from e
