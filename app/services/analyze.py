import base64

from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

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
}

def _language_instruction(lang: str | None) -> str:
    if not lang or lang not in REPORT_LANG_NAMES:
        return "Write the entire report in Turkish (Türkçe). Use only Turkish for all section titles and content."
    name = REPORT_LANG_NAMES[lang]
    return f"Write the entire report in {name}. Use only {name} for all section titles and content. Do not mix languages."

IMAGE_PROMPT_BASE = """This image contains blood test / lab results. Read the image and write a DETAILED report in the following structure:

1. **Summary** (or equivalent in the target language): 2-3 sentences overall assessment.
2. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** value unit. Reference: min-max unit. Normal/Low/High. Example: **Hemoglobin:** 14.2 g/dL. Reference: 12-16 g/dL. Normal.
3. **Possible causes** (or equivalent): If any value is out of range, briefly list possible causes.
4. **Recommendations** (or equivalent): Short tips on diet, lifestyle or when to see a doctor.

Use Markdown bold (**text**) for headings. If the image is unreadable or no lab result is visible, say so briefly."""

DETAILED_PROMPT_BASE = """Explain this blood test to the patient in clear, simple language. Write a DETAILED report with this structure:

1. **Summary** (or equivalent in the target language): 2-3 sentences overall assessment.
2. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** measured value unit. Reference: min-max unit. Normal/Low/High.
   Example line: **Hemoglobin (Hb):** 14.2 g/dL. Reference: 12-16 g/dL. Normal.
   Always include unit and reference range.
3. **Possible causes** (or equivalent): If any value is out of range, briefly list possible causes.
4. **Recommendations** (or equivalent): Short, practical tips on diet, lifestyle and when to see a doctor.

Explain medical terms in parentheses if needed. Use Markdown bold (**text**) for section titles."""


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
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content or ""


def analyze_blood_test_from_image(image_bytes: bytes, mime_type: str, lang: str | None = None) -> str:
    """Görsel (JPG/PNG) tahlil fotoğrafından doğrudan rapor üretir (OpenAI Vision)."""
    if not client or not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY tanımlı değil. .env dosyasına ekleyin.")
    lang_instruction = _language_instruction(lang)
    image_prompt = lang_instruction + "\n\n" + IMAGE_PROMPT_BASE
    b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    url = f"data:{mime_type};base64,{b64}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": image_prompt},
                    {"type": "image_url", "image_url": {"url": url}},
                ],
            }
        ],
    )
    return response.choices[0].message.content or "Görsel analiz edilemedi."
