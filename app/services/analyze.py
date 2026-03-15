import base64
import logging
import re
import time

from fastapi import HTTPException
from openai import APIError, APIConnectionError, AuthenticationError, OpenAI, RateLimitError

from app.core.config import get_openai_keys, is_openai_configured
from app.services.lab_parser import parse_lab_text
from app.services.risk_engine import compute_risk

logger = logging.getLogger(__name__)
# Render cold start + OpenAI yanıt süresi için yeterli süre (görsel analiz uzun sürebilir)
OPENAI_TIMEOUT = 120.0
OPENAI_RETRY_WAIT = 2.5
OPENAI_RETRY_SECOND_WAIT = 5.0
OPENAI_RETRY_ONCE = (RateLimitError, APIConnectionError)
# APIConnectionError'da 2. deneme de başarısızsa bir kez daha dene (cold start / ağ gecikmesi)
OPENAI_RETRY_TWICE_FOR_CONNECTION = True

# Anahtar başına bir istemci (çoklu anahtar fallback için)
_openai_clients: dict[str, OpenAI] = {}

# Bir anahtar auth/rate limit verince diğerine geçilecek
OPENAI_FALLBACK_EXCEPTIONS = (AuthenticationError, RateLimitError)


def _get_client_for_key(key: str) -> OpenAI:
    """Verilen anahtar için OpenAI istemcisi döner (önbelleklenmiş)."""
    if key not in _openai_clients:
        _openai_clients[key] = OpenAI(api_key=key, timeout=OPENAI_TIMEOUT)
    return _openai_clients[key]


def _openai_create_with_fallback(create_fn):
    """
    create_fn(client) çağrısını yapar; AuthenticationError veya RateLimitError olursa
    sıradaki anahtarla tekrar dener. Tüm anahtarlar başarısızsa son hatayı fırlatır.
    """
    keys = get_openai_keys()
    if not keys:
        raise ValueError(
            "OPENAI_API_KEY tanımlı değil veya geçersiz. .env dosyasına OPENAI_API_KEY=sk-... veya OPENAI_API_KEYS=sk-1,sk-2 ekleyin."
        )
    last_exc: Exception | None = None
    for key in keys:
        try:
            client = _get_client_for_key(key)
            return create_fn(client)
        except OPENAI_FALLBACK_EXCEPTIONS as e:
            last_exc = e
            logger.warning("OpenAI anahtar atlandı (%s), sıradakine geçiliyor: %s", key[:12] + "...", e)
            continue
    if last_exc is not None:
        _raise_openai_http_error(last_exc)
    raise ValueError("Geçerli OpenAI anahtarı yok.")


def _openai_safe_call(create_fn):
    """OpenAI çağrısını timeout ile yapar; RateLimitError/APIConnectionError'da 1–2 kez bekleyip tekrar dener."""
    try:
        return create_fn()
    except OPENAI_RETRY_ONCE as e:
        logger.warning("OpenAI retry 1/2 after %s: %s", type(e).__name__, e)
        time.sleep(OPENAI_RETRY_WAIT)
        try:
            return create_fn()
        except APIConnectionError as e2:
            if OPENAI_RETRY_TWICE_FOR_CONNECTION:
                logger.warning("OpenAI retry 2/2 after APIConnectionError: %s", e2)
                time.sleep(OPENAI_RETRY_SECOND_WAIT)
                return create_fn()
            raise
        except RateLimitError:
            raise


def ping_openai() -> tuple[bool, float, str | None]:
    """
    Minimal OpenAI ping (tek token): /health/ai için. Çoklu anahtar varsa sırayla dener.
    Returns: (success, latency_ms, error_message_or_none)
    """
    t0 = time.perf_counter()
    keys = get_openai_keys()
    last_err: str | None = None
    for key in keys:
        try:
            client = _get_client_for_key(key)
            client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=1,
            )
            latency_ms = round((time.perf_counter() - t0) * 1000, 2)
            return (True, latency_ms, None)
        except Exception as e:
            last_err = str(e).strip()[:500] if str(e) else type(e).__name__
            if isinstance(e, OPENAI_FALLBACK_EXCEPTIONS):
                continue
            latency_ms = round((time.perf_counter() - t0) * 1000, 2)
            return (False, latency_ms, last_err)
    latency_ms = round((time.perf_counter() - t0) * 1000, 2)
    return (False, latency_ms, last_err or "Tüm anahtarlar denendi, erişim yok.")

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

IMAGE_PROMPT_BASE = """This image contains blood test / lab results. Read the image and write a DETAILED report in the following structure.

CRITICAL — Value vs reference (avoid wrong Summary/Risk/Values):
- Reference "min–max" (e.g. 90–230): if value < min → say LOW / below range; if value > max → say HIGH / above range; only if min ≤ value ≤ max → say Normal/within range.
- Reference "less than X" or "< X": if value ≥ X → say HIGH / above range (not normal); if value < X → say Normal.
- Reference "greater than X" or "> X": if value ≤ X → say LOW / below range; if value > X → say Normal.
Never say a value is "within" or "normal" when it is outside the reference. Never say "elevated" or "above" when the value is below the reference range.

1. **Summary** (or equivalent in the target language): At least 10 sentences. Write a long, clear and simple overall assessment. Use short, understandable sentences. Explain what this test says about the patient's health in plain language—no jargon. The patient should feel they read a thorough explanation. In the summary, describe each out-of-range parameter correctly: above reference = high/elevated; below reference = low/deficient.
2. **Risk indicators** (or equivalent in target language, e.g. "Dikkat edilmesi gerekenler" / "Points d'attention"): List clearly which parameters are out of range or need attention. One short line per item. If all are normal, say "No values requiring special attention" (in target language). For each item, state correctly whether the value is above or below the reference.
3. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** value unit. Reference: min-max unit. Normal/Low/High. Example: **Hemoglobin:** 14.2 g/dL. Reference: 12-16 g/dL. Normal. Always compare numerically: value < ref_min → Low; value > ref_max → High; else Normal.
4. **Possible causes** (or equivalent): If any value is out of range, briefly list possible causes in simple language.
5. **Recommendations** (or equivalent): LONGER, practical section so the patient feels they got real value. Include in target language:
   - What to pay attention to (dikkat edilmesi gerekenler / things to watch).
   - What to eat less or avoid (az tüketilmesi / reduce or avoid).
   - What to do or improve (yapılması önerilenler / lifestyle, exercise, habits).
   - When to see a doctor (doktora ne zaman gidilmeli).
   Write 4-8 concrete, actionable lines. Use simple words.
6. **Diet plan** (or equivalent in target language, e.g. "Diyet planı" / "Plan alimentaire"): Personalized nutrition based on the blood results. Include two clear sublists in the target language: (a) foods to eat more of / emphasize ("yenilmesi gerekenler"), and (b) foods to eat less of or avoid ("az tüketilmesi / yenilmemesi gerekenler"). Optionally add a simple 1-day or 3-day sample menu. Keep it practical and aligned with any deficiencies or risks (e.g. iron-rich foods if hemoglobin low, less salt if blood pressure/renal concern). Write in target language.
7. **Supplement recommendations** (or equivalent, e.g. "Takviye önerileri" / "Compléments recommandés"): Based on out-of-range values or deficiencies, suggest vitamins or minerals that may help (e.g. vitamin D, B12, iron, magnesium). For each: name, why it may be useful, and add "Consult your doctor for dosage and duration" (in target language). If all values are normal, suggest only general maintenance if appropriate, or state "No specific supplements suggested; a balanced diet is sufficient."
8. **Heart health** (or equivalent in target language, e.g. "Kalp sağlığı" / "Santé cardiovasculaire"): If the lab includes any cardiovascular-related parameters (cholesterol, LDL, HDL, triglycerides, glucose, HbA1c, CRP, homocysteine, troponin, BNP/NT-proBNP, etc.), write a short subsection (3–6 lines) in target language: what these results mean for heart/circulation risk; when to consider a cardiologist or repeat tests. If no such parameters are present, write one line: "This panel does not include specific cardiac markers; discuss with your doctor if you want a cardiovascular risk assessment."

Use Markdown bold (**text**) for section titles. If the image is unreadable or no lab result is visible, say so briefly."""

DETAILED_PROMPT_BASE = """Explain this blood test to the patient in clear, simple language. Write a DETAILED report so the patient feels the report is worth paying for. Use this structure.

CRITICAL — Value vs reference (you MUST get these right):
- Reference "min–max" (e.g. 90–230 µg/L): if value < min → say LOW / below range; if value > max → say HIGH / above range; only if min ≤ value ≤ max → Normal/within range.
- Reference "less than X" or "< X": if value ≥ X → say HIGH / above (not normal); if value < X → Normal.
- Reference "greater than X" or "> X": if value ≤ X → say LOW / below; if value > X → Normal.
Never say a value is "within" or "normal" when it is outside the reference. Never say "elevated" or "above" when the value is below the reference (e.g. 68 with ref 90–230 must be "low" / "below", not "elevated").

1. **Summary** (or equivalent in the target language): At least 10 sentences. Write a long, clear and simple overall assessment. Use short, understandable sentences only. Plain language, no jargon. Explain in detail what these results mean for the patient. For each parameter, state correctly: above reference = high/elevated; below reference = low/deficient; within = normal.
2. **Risk indicators** (or equivalent, e.g. "Dikkat edilmesi gerekenler"): Clearly list which parameters are out of range or need attention. One short line per item. If all normal: say "No values requiring special attention" in target language. For each out-of-range value, state whether it is above or below the reference.
3. **Values** (or equivalent): Each parameter on ONE line. Format: **Parameter name:** measured value unit. Reference: min-max unit. Normal/Low/High. Compare numerically: value < ref_min → Low; value > ref_max → High; else Normal.
   Example: **Hemoglobin (Hb):** 14.2 g/dL. Reference: 12-16 g/dL. Normal. Always include unit and reference range.
4. **Possible causes** (or equivalent): If any value is out of range, list possible causes in simple language.
5. **Recommendations** (or equivalent): LONGER, very practical section. The patient should feel "I know what to do". Include in target language:
   - What to pay attention to (dikkat edilmesi gerekenler).
   - What to eat less or avoid (az tüketilmesi gerekenler / şunlardan kaçının).
   - What to do or improve (yapmanız gerekenler: uyku, hareket, alışkanlıklar).
   - When to see a doctor (doktora ne zaman gitmeli).
   Write 5-10 concrete, actionable lines. Be specific (e.g. "reduce salt", "increase water", "check again in 3 months").
6. **Diet plan** (or equivalent in target language, e.g. "Diyet planı"): Personalized nutrition based on the blood results. Include two explicit sublists in the target language: (a) foods to eat more / emphasize ("yenilmesi gerekenler"), and (b) foods to eat less of or avoid ("az tüketilmesi / yenilmemesi gerekenler"). You may also add a simple 1-day or 3-day sample menu. Keep it practical and aligned with deficiencies/risks. Write in target language.
7. **Supplement recommendations** (or equivalent, e.g. "Takviye önerileri"): Based on out-of-range values or deficiencies, suggest vitamins/minerals that may help (e.g. vitamin D, B12, iron). For each: name, why it may be useful; add "Consult your doctor for dosage and duration" (in target language). If all normal, suggest only general maintenance or state that no specific supplements are needed.
8. **Heart health** (or equivalent in target language, e.g. "Kalp sağlığı"): If the lab includes cardiovascular-related parameters (cholesterol, LDL, HDL, triglycerides, glucose, HbA1c, CRP, homocysteine, troponin, BNP, etc.), write a short subsection (3–6 lines): what these results mean for heart/cardiovascular risk; when to see a cardiologist or repeat tests. If none are present, write one line saying this panel does not include specific cardiac markers and to discuss with a doctor if a cardiovascular check is desired.

Explain medical terms in parentheses if needed. Use Markdown bold (**text**) for section titles only."""

# AŞAMA-2: OpenAI sadece yorum (kısa, madde madde); uzun paragraf yok
AI_EXPLANATION_PROMPT = """Verilen labs_norm (normalize tahlil metni) ve risk_summary (kural tabanlı risk özeti) ile kısa yorum yaz.

Kurallar:
- Sadece madde madde yaz. Uzun paragraf yazma.
- Bölümler: (1) Özet — 3-5 madde; (2) Olası nedenler — varsa kısa maddeler; (3) Öneriler — 4-7 uygulanabilir madde.
- Dil: Tüm yanıtı SADECE hedef dilde yaz (başlıklar dahil).
- Teşhis önerisi veya kesin ifade kullanma. Bilgilendirme amaçlı olduğunu vurgula."""

# Single plan: kullanıcı tek seferlik analiz aldığında açıklama kalitesi premium olsun — kısa etiket değil, anlaşılır paragraf/madde
SINGLE_PLAN_EXPLANATION_PROMPT = """Verilen labs_norm ve risk_summary ile hastaya yönelik, anlaşılır ve güven veren bir yorum yaz. Bu rapor tek seferlik analiz paketi kullanıcısına sunulacak; kısa veya yüzeysel etiketler kullanma.

Zorunlu kurallar:
- Dil: Tüm yanıtı SADECE hedef dilde yaz (başlıklar dahil). Jargon veya korkutucu ifade kullanma. Teşhis koyma.
- Her bölüm gerçekten bilgilendirici olsun: "Normal.", "Stable.", "Monitor." gibi tek başına bırakma. Altında mutlaka 2–4 cümle veya eşdeğer maddelerle ne anlama geldiğini, neyle birlikte düşünülmesi gerektiğini ve neden takip edilebileceğini açıkla.
- Özet: En az 4–5 cümle (veya eşdeğer maddeler). Tahlilin genel tablosunu, hangi değerlerin referansta olduğunu, hangi alanlarda dikkat edilmesi gerektiğini sade dilde anlat. Kullanıcı "bu sonuç ne anlama geliyor?" sorusuna cevap almalı.
- Olası nedenler: Varsa her dışarıda kalan parametre için 1–2 cümle; tek kelime veya tek satır etiket yeterli değil. Olası nedenleri kısa ama anlamlı şekilde açıkla.
- Öneriler: 5–8 uygulanabilir madde. Beslenme, yaşam tarzı, ne zaman hekime gidilmeli konularında net ve somut ifadeler. Genel sözlerle şişirme; her madde gerçekten bilgilendirici olsun.
- Gereksiz tekrar veya doldurma cümleleri yazma. Kısa ama anlamlı, premium his veren bir rapor hedefleniyor."""


def ai_generate_explanation(
    risk_summary: dict,
    labs_norm: dict,
    lang: str | None,
    plan: str,
    doctor_notes: str | None = None,
) -> tuple[str, dict | None]:
    """
    Modele sadece labs_norm + risk_summary + plan + lang verir.
    Returns: (explanation_text, usage_dict). explanation = kısa, madde madde özet/neden/öneriler.
    Single plan için daha açıklayıcı, 4-5 cümle seviyesinde premium açıklama üretilir.
    """
    import json
    lang_instruction = _language_instruction(lang)
    # Token tasarrufu: labs metnini kısalt
    lab_text = (labs_norm.get("t") or "")[:1500]
    lab_note = (labs_norm.get("dn") or "")[:300] if labs_norm.get("dn") else ""
    payload = {
        "labs_norm_preview": lab_text,
        "doctor_notes": lab_note or None,
        "risk_summary": risk_summary,
        "plan": plan,
    }
    base_prompt = AI_EXPLANATION_PROMPT
    plan_lower = (plan or "").strip().lower()
    if plan_lower == "single":
        base_prompt = SINGLE_PLAN_EXPLANATION_PROMPT
    prompt = (
        lang_instruction + "\n\n" + base_prompt + "\n\n"
        "Input (JSON):\n" + json.dumps(payload, ensure_ascii=False, indent=0)
    )

    max_tokens = 2048 if plan_lower == "single" else 1024
    def _create(client: OpenAI):
        return _openai_safe_call(lambda: client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        ))

    try:
        response = _openai_create_with_fallback(_create)
        content = (response.choices[0].message.content or "").strip()
        usage = None
        if getattr(response, "usage", None):
            u = response.usage
            usage = {"prompt_tokens": getattr(u, "prompt_tokens", 0) or 0, "completion_tokens": getattr(u, "completion_tokens", 0) or 0}
        return content, usage
    except (AuthenticationError, RateLimitError, APIConnectionError, APIError) as e:
        logger.exception("OpenAI API error in ai_generate_explanation: %s", e)
        _raise_openai_http_error(e)
    except Exception as e:
        logger.exception("Unexpected error in ai_generate_explanation: %s", e)
        _raise_openai_http_error(e)


def _value_status(value: float, ref_low: float | None, ref_high: float | None) -> str:
    if ref_low is not None and value < ref_low:
        return "low"
    if ref_high is not None and value > ref_high:
        return "high"
    return "normal"


def build_tables(lab_values: list[dict]) -> list[dict]:
    """Lab değerlerinden tablo satırları: name, value, ref, status (normal/low/high)."""
    from app.services.risk_engine import REF_RANGES
    rows = []
    for lab in lab_values:
        name = lab.get("name")
        if not name:
            continue
        ref_low, ref_high = lab.get("ref_low"), lab.get("ref_high")
        if ref_low is None and ref_high is None:
            ref_low, ref_high = REF_RANGES.get(name, (None, None))
        st = _value_status(lab["value"], ref_low, ref_high)
        ref_str = ""
        if ref_low is not None and ref_high is not None:
            ref_str = f"{ref_low}-{ref_high}"
        elif ref_high is not None:
            ref_str = f"<{ref_high}"
        elif ref_low is not None:
            ref_str = f">{ref_low}"
        rows.append({
            "name": name,
            "value": lab["value"],
            "unit": lab.get("unit"),
            "ref": ref_str,
            "status": st,
        })
    return rows


# Sabit uyarı (AI'ya yükleme yok)
DISCLAIMER_TR = "Bu yorum teşhis değildir; bilgilendirme amaçlıdır. Sonuçları hekiminizle paylaşın."
DISCLAIMER_BY_LANG: dict[str, str] = {
    "tr": DISCLAIMER_TR,
    "en": "This interpretation is not a diagnosis; it is for information only. Share results with your doctor.",
    "it": "Questo commento non è una diagnosi; è solo informativo. Condividi i risultati con il tuo medico.",
    "es": "Esta interpretación no es un diagnóstico; es solo informativa. Comparta los resultados con su médico.",
    "fr": "Ce commentaire n'est pas un diagnostic; il est à titre informatif. Partagez les résultats avec votre médecin.",
    "de": "Diese Auswertung ist keine Diagnose; sie dient nur der Information. Teilen Sie die Ergebnisse Ihrem Arzt mit.",
}


def format_report_to_markdown(
    risk_summary: dict,
    explanation: str,
    tables: list[dict],
    meta: dict,
) -> str:
    """Rapor payload'ından sonuc (markdown) üretir; teşhis değildir uyarısı eklenir."""
    lang = meta.get("lang") or "tr"
    disclaimer = DISCLAIMER_BY_LANG.get(lang, DISCLAIMER_TR)
    titles = {
        "tr": ("Risk özeti", "Yorum", "Değerler", "Uyarı"),
        "en": ("Risk summary", "Interpretation", "Values", "Disclaimer"),
    }
    risk_label, interp_label, values_label, warn_label = titles.get(lang, titles["en"])
    overall = risk_summary.get("overall") or {}
    domains = risk_summary.get("domains") or {}
    lines = [
        f"## {risk_label}",
        f"- **Overall:** {overall.get('level', '')} (skor: {overall.get('score', 0)})",
    ]
    for dk, dv in domains.items():
        lines.append(f"- **{dk}:** {dv.get('level', '')} (skor: {dv.get('score', 0)}) — {', '.join(dv.get('reasons', []) or ['—'])}")
    lines.append("")
    lines.append(f"## {interp_label}")
    lines.append(explanation)
    lines.append("")
    lines.append(f"## {values_label}")
    for row in tables[:30]:
        ref = row.get("ref") or "—"
        st = row.get("status") or "normal"
        unit = (row.get("unit") or "")
        lines.append(f"- **{row.get('name')}:** {row.get('value')} {unit} (Ref: {ref}) — {st}")
    lines.append("")
    lines.append(f"## {warn_label}")
    lines.append(disclaimer)
    return "\n".join(lines)


def analyze_blood_test(
    text: str,
    detailed: bool = True,
    doctor_notes: str | None = None,
    lang: str | None = None,
    plan: str = "free",
    labs_norm: dict | None = None,
) -> tuple[dict, dict | None]:
    """
    İki aşamalı analiz: (1) Risk Engine -> risk_summary, (2) OpenAI -> explanation.
    Returns: (report_payload, usage). report_payload = { risk_summary, explanation, tables, meta, sonuc }.
    """
    lab_values = parse_lab_text(text)
    risk_summary = compute_risk(lab_values)
    if labs_norm is None:
        labs_norm = {"t": " ".join(text.split()).strip(), "dn": (doctor_notes or "").strip() or None}
    explanation, usage = ai_generate_explanation(risk_summary, labs_norm, lang, plan, doctor_notes)
    tables = build_tables(lab_values)
    meta = {"lang": lang or "tr", "plan": plan}
    sonuc = format_report_to_markdown(risk_summary, explanation, tables, meta)
    report_payload = {
        "risk_summary": risk_summary,
        "explanation": explanation,
        "tables": tables,
        "meta": meta,
        "sonuc": sonuc,
    }
    return report_payload, usage


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


def analyze_blood_test_from_image(image_bytes: bytes, mime_type: str, lang: str | None = None) -> tuple[str, dict | None]:
    """Görsel (JPG/PNG) tahlil fotoğrafından doğrudan rapor üretir (OpenAI Vision)."""
    lang_instruction = _language_instruction(lang)
    image_prompt = lang_instruction + "\n\n" + IMAGE_PROMPT_BASE
    b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    url = f"data:{mime_type};base64,{b64}"
    system_msg = (
        "You are a medical report assistant. The user will send you ONE image containing blood test or lab results. "
        "You MUST look at the image, read the values and text in it, and produce a structured report. "
        "Do NOT say you cannot read or process images. You have vision capability. Always analyze the image and output the report in the requested language."
    )
    def _create(client: OpenAI):
        return _openai_safe_call(lambda: client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": image_prompt},
                        {"type": "image_url", "image_url": {"url": url, "detail": "low"}},
                    ],
                },
            ],
            max_tokens=8192,
        ))

    try:
        response = _openai_create_with_fallback(_create)
        content = response.choices[0].message.content or "Görsel analiz edilemedi."
        usage = None
        if getattr(response, "usage", None):
            u = response.usage
            usage = {"prompt_tokens": getattr(u, "prompt_tokens", 0) or 0, "completion_tokens": getattr(u, "completion_tokens", 0) or 0}
        return content, usage
    except (AuthenticationError, RateLimitError, APIConnectionError, APIError) as e:
        logger.exception("OpenAI API error in analyze_blood_test_from_image: %s", e)
        _raise_openai_http_error(e)
    except Exception as e:
        logger.exception("Unexpected error in analyze_blood_test_from_image: %s", e)
        _raise_openai_http_error(e)
