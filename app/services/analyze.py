import base64
import logging
import time

from fastapi import HTTPException
from openai import APIError, APIConnectionError, AuthenticationError, OpenAI, RateLimitError

from app.core.config import settings

logger = logging.getLogger(__name__)
OPENAI_TIMEOUT = 30.0
OPENAI_RETRY_WAIT = 1.5
OPENAI_RETRY_ONCE = (RateLimitError, APIConnectionError)

client = OpenAI(api_key=settings.openai_api_key, timeout=OPENAI_TIMEOUT) if settings.openai_api_key else None


def _openai_safe_call(create_fn):
    """OpenAI çağrısını timeout ile yapar; RateLimitError/APIConnectionError'da 1 kez 1.5 sn bekleyip tekrar dener."""
    try:
        return create_fn()
    except OPENAI_RETRY_ONCE as e:
        logger.warning("OpenAI retry after %s: %s", type(e).__name__, e)
        time.sleep(OPENAI_RETRY_WAIT)
        return create_fn()

# Rapor diline göre dil adı (modelin anlayacağı şekilde)
REPORT_LANG_NAMES: dict[str, str] = {
    "tr": "Turkish",
    "en": "English",
    "it": "Italian",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "ar": "Arabic",
    "hi": "Hindi",
    "el": "Greek",
    "cs": "Czech",
    "sr": "Serbian",
}

def _language_instruction(lang: str | None) -> str:
    if not lang or lang not in REPORT_LANG_NAMES:
        return "Write the entire report in Turkish (Türkçe). Use only Turkish for all section titles and content."
    name = REPORT_LANG_NAMES[lang]
    return (
        f"CRITICAL — Language: You MUST write the ENTIRE report ONLY in {name}. "
        f"Every section title and every sentence must be in {name}. "
        f"Do not use Turkish or English when the user language is {name}. "
        f"Section titles (Summary, Values, Risk indicators, etc.) must be written in {name} as well."
    )

IMAGE_PROMPT_BASE = """This image contains blood test / lab results. Read the image and write a DETAILED report in the following structure:

1. **Summary** (or equivalent in the target language): At least 10 sentences. Write a long, clear and simple overall assessment. Use short, understandable sentences. Explain what this test says about the patient's health in plain language—no jargon. The patient should feel they read a thorough explanation.
2. **Risk indicators** (or equivalent in target language, e.g. "Dikkat edilmesi gerekenler" / "Points d'attention"): List clearly which parameters are out of range or need attention. One short line per item. If all are normal, say "No values requiring special attention" (in target language).
3. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** value unit. Reference: min-max unit. Normal/Low/High. Example: **Hemoglobin:** 14.2 g/dL. Reference: 12-16 g/dL. Normal.
4. **Possible causes** (or equivalent): If any value is out of range, briefly list possible causes in simple language.
5. **Recommendations** (or equivalent): LONGER, practical section so the patient feels they got real value. Include in target language:
   - What to pay attention to (dikkat edilmesi gerekenler / things to watch).
   - What to eat less or avoid (az tüketilmesi / reduce or avoid).
   - What to do or improve (yapılması önerilenler / lifestyle, exercise, habits).
   - When to see a doctor (doktora ne zaman gidilmeli).
   Write 4-8 concrete, actionable lines. Use simple words.

Use Markdown bold (**text**) for section titles. If the image is unreadable or no lab result is visible, say so briefly."""

DETAILED_PROMPT_BASE = """Explain this blood test to the patient in clear, simple language. Write a DETAILED report so the patient feels the report is worth paying for. Use this structure:

1. **Summary** (or equivalent in the target language): At least 10 sentences. Write a long, clear and simple overall assessment. Use short, understandable sentences only. Plain language, no jargon. Explain in detail what these results mean for the patient. The patient should feel they read a thorough, easy-to-understand explanation.
2. **Risk indicators** (or equivalent, e.g. "Dikkat edilmesi gerekenler"): Clearly list which parameters are out of range or need attention. One short line per item. If all normal: say "No values requiring special attention" in target language.
3. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** measured value unit. Reference: min-max unit. Normal/Low/High.
   Example: **Hemoglobin (Hb):** 14.2 g/dL. Reference: 12-16 g/dL. Normal. Always include unit and reference range.
4. **Possible causes** (or equivalent): If any value is out of range, list possible causes in simple language.
5. **Recommendations** (or equivalent): LONGER, very practical section. The patient should feel "I know what to do". Include in target language:
   - What to pay attention to (dikkat edilmesi gerekenler).
   - What to eat less or avoid (az tüketilmesi gerekenler / şunlardan kaçının).
   - What to do or improve (yapmanız gerekenler: uyku, hareket, alışkanlıklar).
   - When to see a doctor (doktora ne zaman gitmeli).
   Write 5-10 concrete, actionable lines. Be specific (e.g. "reduce salt", "increase water", "check again in 3 months").

Explain medical terms in parentheses if needed. Use Markdown bold (**text**) for section titles only."""


def _raise_openai_http_error(exc: Exception) -> None:
    """OpenAI hatalarını uygun HTTP istisnalarına çevirir. (401 kullanıcı oturumu ile karışmasın diye API hatası 503.)"""
    if isinstance(exc, AuthenticationError):
        raise HTTPException(
            status_code=503,
            detail="AI erişimi başarısız: OPENAI_API_KEY .env içinde doğru tanımlı mı, billing açık mı kontrol edin.",
        ) from exc
    if isinstance(exc, RateLimitError):
        raise HTTPException(
            status_code=429,
            detail="AI yoğun: Lütfen biraz sonra tekrar deneyin.",
        ) from exc
    if isinstance(exc, APIConnectionError):
        raise HTTPException(
            status_code=503,
            detail="AI bağlantı sorunu: Ağ/servis geçici olarak erişilemiyor.",
        ) from exc
    if isinstance(exc, APIError):
        raise HTTPException(
            status_code=502,
            detail="AI servis hatası: Geçici sorun olabilir.",
        ) from exc
    raise HTTPException(status_code=500, detail="Beklenmeyen sunucu hatası.") from exc


def analyze_blood_test(text: str, detailed: bool = True, doctor_notes: str | None = None, lang: str | None = None) -> str:
    if not client or not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY tanımlı değil. .env dosyasına ekleyin.")
    lang_instruction = _language_instruction(lang)
    if not detailed:
        prompt = lang_instruction + "\n\nExplain this blood test in short, simple terms:\n" + text
    else:
        prompt = lang_instruction + "\n\n" + DETAILED_PROMPT_BASE + "\n\nLab data:\n" + text
        if doctor_notes and doctor_notes.strip():
            prompt += "\n\nPatient's extra note (doctor comment or additional info): " + doctor_notes.strip() + "\nTake this into account when interpreting."
    try:
        response = _openai_safe_call(lambda: client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        ))
        return response.choices[0].message.content or ""
    except (AuthenticationError, RateLimitError, APIConnectionError, APIError) as e:
        logger.exception("OpenAI API error in analyze_blood_test: %s", e)
        _raise_openai_http_error(e)
    except Exception as e:
        logger.exception("Unexpected error in analyze_blood_test: %s", e)
        _raise_openai_http_error(e)


def analyze_blood_test_from_image(image_bytes: bytes, mime_type: str, lang: str | None = None) -> str:
    """Görsel (JPG/PNG) tahlil fotoğrafından doğrudan rapor üretir (OpenAI Vision)."""
    if not client or not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY tanımlı değil. .env dosyasına ekleyin.")
    lang_instruction = _language_instruction(lang)
    image_prompt = lang_instruction + "\n\n" + IMAGE_PROMPT_BASE
    b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    url = f"data:{mime_type};base64,{b64}"
    system_msg = (
        "You are a medical report assistant. The user will send you ONE image containing blood test or lab results. "
        "You MUST look at the image, read the values and text in it, and produce a structured report. "
        "Do NOT say you cannot read or process images. You have vision capability. Always analyze the image and output the report in the requested language."
    )
    try:
        response = _openai_safe_call(lambda: client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": image_prompt},
                        {"type": "image_url", "image_url": {"url": url, "detail": "high"}},
                    ],
                },
            ],
        ))
        return response.choices[0].message.content or "Görsel analiz edilemedi."
    except (AuthenticationError, RateLimitError, APIConnectionError, APIError) as e:
        logger.exception("OpenAI API error in analyze_blood_test_from_image: %s", e)
        _raise_openai_http_error(e)
    except Exception as e:
        logger.exception("Unexpected error in analyze_blood_test_from_image: %s", e)
        _raise_openai_http_error(e)
