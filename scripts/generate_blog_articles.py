#!/usr/bin/env python3
"""
Otomatik blog makale + DALL-E 3 cover görsel üretimi.

Kullanım:
  python3 scripts/generate_blog_articles.py              # tüm parametreler, 9 dil
  python3 scripts/generate_blog_articles.py --test       # sadece HbA1c, sadece EN (test modu)
  python3 scripts/generate_blog_articles.py --param hba1c --langs en,tr,de
  python3 scripts/generate_blog_articles.py --no-image   # görsel üretme (hızlı test)

Her parametre için:
  1. GPT-4o ile 9 dilde makale içeriği üretir (sections formatı)
  2. DALL-E 3 ile premium medical cover görsel üretir
  3. SQLite DB'ye is_published=True olarak ekler
  4. Duplicate slug varsa atlar
"""

import argparse
import json
import os
import sqlite3
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# --- Config ---
ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "norya.db"
STATIC_BLOG_IMG = ROOT / "static" / "images" / "blog"
STATIC_BLOG_IMG.mkdir(parents=True, exist_ok=True)

# .env'den API key oku
from dotenv import load_dotenv
load_dotenv(ROOT / ".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

if not OPENAI_API_KEY:
    print("ERROR: OPENAI_API_KEY bulunamadı. .env dosyasını kontrol et.")
    sys.exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai paketi yüklü değil. pip install openai")
    sys.exit(1)

client = OpenAI(api_key=OPENAI_API_KEY)

# --- Kan parametreleri listesi ---
# Her parametre: id, ingilizce adı, DALL-E prompt için açıklama, kategori (her dilde)
PARAMETERS = [
    {
        "id": "hba1c",
        "name_en": "HbA1c (Glycated Hemoglobin)",
        "dalle_subject": "glycated hemoglobin HbA1c blood glucose diabetes monitoring",
        "categories": {
            "en": "Diabetes & Metabolic Health", "tr": "Diyabet ve Metabolik Sağlık",
            "de": "Diabetes & Stoffwechsel", "fr": "Diabète & Métabolisme",
            "it": "Diabete & Metabolismo", "es": "Diabetes & Metabolismo",
            "he": "סוכרת ובריאות מטבולית", "hi": "मधुमेह और चयापचय स्वास्थ्य",
            "ar": "السكري والصحة الأيضية",
        },
        "slugs": {
            "en": "hba1c-blood-test-meaning", "tr": "hba1c-kan-testi-anlami",
            "de": "hba1c-blutwert-bedeutung", "fr": "hba1c-signification-prise-de-sang",
            "it": "hba1c-esame-sangue-significato", "es": "hba1c-analisis-sangre-significado",
            "he": "hba1c-בדיקת-דם-משמעות", "hi": "hba1c-blood-test-matlab",
            "ar": "hba1c-تحليل-دم-المعنى",
        },
    },
    {
        "id": "tsh",
        "name_en": "TSH (Thyroid Stimulating Hormone)",
        "dalle_subject": "thyroid stimulating hormone TSH thyroid gland medical test",
        "categories": {
            "en": "Thyroid Health", "tr": "Tiroid Sağlığı",
            "de": "Schilddrüsengesundheit", "fr": "Santé thyroïdienne",
            "it": "Salute tiroidea", "es": "Salud tiroidea",
            "he": "בריאות בלוטת התריס", "hi": "थायरॉइड स्वास्थ्य",
            "ar": "صحة الغدة الدرقية",
        },
        "slugs": {
            "en": "tsh-thyroid-test-meaning", "tr": "tsh-tiroid-testi-anlami",
            "de": "tsh-schilddruese-wert-bedeutung", "fr": "tsh-hormone-thyroide-signification",
            "it": "tsh-ormone-tiroideo-significato", "es": "tsh-hormona-tiroides-significado",
            "he": "tsh-בדיקת-בלוטת-התריס-משמעות", "hi": "tsh-thyroid-test-matlab",
            "ar": "tsh-هرمون-الغدة-الدرقية-معنى",
        },
    },
    {
        "id": "ferritin",
        "name_en": "Ferritin (Iron Storage)",
        "dalle_subject": "ferritin iron storage protein blood test anemia",
        "categories": {
            "en": "Iron & Anemia", "tr": "Demir ve Anemi",
            "de": "Eisen & Anämie", "fr": "Fer & Anémie",
            "it": "Ferro & Anemia", "es": "Hierro & Anemia",
            "he": "ברזל ואנמיה", "hi": "आयरन और एनीमिया",
            "ar": "الحديد وفقر الدم",
        },
        "slugs": {
            "en": "ferritin-blood-test-meaning", "tr": "ferritin-kan-testi-anlami",
            "de": "ferritin-blutwert-bedeutung", "fr": "ferritine-prise-de-sang-signification",
            "it": "ferritina-esame-sangue-significato", "es": "ferritina-analisis-sangre-significado",
            "he": "פריטין-בדיקת-דם-משמעות", "hi": "ferritin-blood-test-matlab",
            "ar": "فيريتين-تحليل-دم-المعنى",
        },
    },
    {
        "id": "vitamin_d",
        "name_en": "Vitamin D (25-OH)",
        "dalle_subject": "vitamin D sunlight bone health immune system blood test",
        "categories": {
            "en": "Vitamins & Minerals", "tr": "Vitamin ve Mineraller",
            "de": "Vitamine & Mineralien", "fr": "Vitamines & Minéraux",
            "it": "Vitamine & Minerali", "es": "Vitaminas & Minerales",
            "he": "ויטמינים ומינרלים", "hi": "विटामिन और खनिज",
            "ar": "الفيتامينات والمعادن",
        },
        "slugs": {
            "en": "vitamin-d-blood-test-meaning", "tr": "d-vitamini-kan-testi-anlami",
            "de": "vitamin-d-blutwert-bedeutung", "fr": "vitamine-d-prise-de-sang-signification",
            "it": "vitamina-d-esame-sangue-significato", "es": "vitamina-d-analisis-sangre-significado",
            "he": "ויטמין-d-בדיקת-דם-משמעות", "hi": "vitamin-d-blood-test-matlab",
            "ar": "فيتامين-d-تحليل-دم-المعنى",
        },
    },
    {
        "id": "crp",
        "name_en": "CRP (C-Reactive Protein)",
        "dalle_subject": "C-reactive protein CRP inflammation marker blood test",
        "categories": {
            "en": "Inflammation & Immunity", "tr": "İnflamasyon ve Bağışıklık",
            "de": "Entzündung & Immunität", "fr": "Inflammation & Immunité",
            "it": "Infiammazione & Immunità", "es": "Inflamación & Inmunidad",
            "he": "דלקת ומערכת החיסון", "hi": "सूजन और प्रतिरक्षा",
            "ar": "الالتهاب والمناعة",
        },
        "slugs": {
            "en": "crp-blood-test-meaning", "tr": "crp-kan-testi-anlami",
            "de": "crp-blutwert-bedeutung", "fr": "crp-prise-de-sang-signification",
            "it": "crp-esame-sangue-significato", "es": "crp-analisis-sangre-significado",
            "he": "crp-בדיקת-דם-משמעות", "hi": "crp-blood-test-matlab",
            "ar": "crp-تحليل-دم-المعنى",
        },
    },
    {
        "id": "wbc",
        "name_en": "WBC (White Blood Cell Count)",
        "dalle_subject": "white blood cell WBC leukocyte immune defense microscope blood",
        "categories": {
            "en": "Complete Blood Count", "tr": "Tam Kan Sayımı",
            "de": "Blutbild", "fr": "Numération formule sanguine",
            "it": "Emocromo completo", "es": "Hemograma completo",
            "he": "ספירת דם מלאה", "hi": "पूर्ण रक्त गणना",
            "ar": "صورة الدم الكاملة",
        },
        "slugs": {
            "en": "wbc-white-blood-cell-meaning", "tr": "wbc-beyaz-kan-hucresi-anlami",
            "de": "wbc-leukozyten-bedeutung", "fr": "globules-blancs-wbc-signification",
            "it": "wbc-globuli-bianchi-significato", "es": "wbc-globulos-blancos-significado",
            "he": "wbc-תאי-דם-לבנים-משמעות", "hi": "wbc-white-blood-cell-matlab",
            "ar": "wbc-كريات-الدم-البيضاء-معنى",
        },
    },
    {
        "id": "creatinine",
        "name_en": "Creatinine (Kidney Function)",
        "dalle_subject": "creatinine kidney function renal health blood test laboratory",
        "categories": {
            "en": "Kidney Health", "tr": "Böbrek Sağlığı",
            "de": "Nierengesundheit", "fr": "Santé rénale",
            "it": "Salute renale", "es": "Salud renal",
            "he": "בריאות הכליות", "hi": "गुर्दे की सेहत",
            "ar": "صحة الكلى",
        },
        "slugs": {
            "en": "creatinine-blood-test-meaning", "tr": "kreatinin-kan-testi-anlami",
            "de": "kreatinin-blutwert-bedeutung", "fr": "creatinine-prise-de-sang-signification",
            "it": "creatinina-esame-sangue-significato", "es": "creatinina-analisis-sangre-significado",
            "he": "קראטינין-בדיקת-דם-משמעות", "hi": "creatinine-blood-test-matlab",
            "ar": "كرياتينين-تحليل-دم-المعنى",
        },
    },
    {
        "id": "alt",
        "name_en": "ALT (Alanine Aminotransferase / Liver Enzyme)",
        "dalle_subject": "ALT liver enzyme hepatic function blood test alanine aminotransferase",
        "categories": {
            "en": "Liver Health", "tr": "Karaciğer Sağlığı",
            "de": "Lebergesundheit", "fr": "Santé hépatique",
            "it": "Salute epatica", "es": "Salud hepática",
            "he": "בריאות הכבד", "hi": "लीवर स्वास्थ्य",
            "ar": "صحة الكبد",
        },
        "slugs": {
            "en": "alt-liver-enzyme-meaning", "tr": "alt-karaciger-enzimi-anlami",
            "de": "alt-leberenzym-bedeutung", "fr": "alt-enzyme-hepatique-signification",
            "it": "alt-enzima-epatico-significato", "es": "alt-enzima-hepatico-significado",
            "he": "alt-אנזים-כבד-משמעות", "hi": "alt-liver-enzyme-matlab",
            "ar": "alt-انزيم-الكبد-معنى",
        },
    },
    {
        "id": "glucose",
        "name_en": "Fasting Blood Glucose",
        "dalle_subject": "fasting blood glucose sugar level diabetes blood test laboratory",
        "categories": {
            "en": "Diabetes & Metabolic Health", "tr": "Diyabet ve Metabolik Sağlık",
            "de": "Diabetes & Stoffwechsel", "fr": "Diabète & Métabolisme",
            "it": "Diabete & Metabolismo", "es": "Diabetes & Metabolismo",
            "he": "סוכרת ובריאות מטבולית", "hi": "मधुमेह और चयापचय स्वास्थ्य",
            "ar": "السكري والصحة الأيضية",
        },
        "slugs": {
            "en": "fasting-glucose-blood-test-meaning", "tr": "aclik-kan-sekeri-anlami",
            "de": "nuchternglukose-blutwert-bedeutung", "fr": "glycemie-jeun-signification",
            "it": "glicemia-digiuno-significato", "es": "glucosa-ayunas-significado",
            "he": "גלוקוז-צום-בדיקת-דם-משמעות", "hi": "fasting-glucose-blood-test-matlab",
            "ar": "جلوكوز-صيام-تحليل-دم-معنى",
        },
    },
    {
        "id": "vitamin_b12",
        "name_en": "Vitamin B12 (Cobalamin)",
        "dalle_subject": "vitamin B12 cobalamin nerve health energy blood test deficiency",
        "categories": {
            "en": "Vitamins & Minerals", "tr": "Vitamin ve Mineraller",
            "de": "Vitamine & Mineralien", "fr": "Vitamines & Minéraux",
            "it": "Vitamine & Minerali", "es": "Vitaminas & Minerales",
            "he": "ויטמינים ומינרלים", "hi": "विटामिन और खनिज",
            "ar": "الفيتامينات والمعادن",
        },
        "slugs": {
            "en": "vitamin-b12-blood-test-meaning", "tr": "b12-vitamini-kan-testi-anlami",
            "de": "vitamin-b12-blutwert-bedeutung", "fr": "vitamine-b12-prise-de-sang-signification",
            "it": "vitamina-b12-esame-sangue-significato", "es": "vitamina-b12-analisis-sangre-significado",
            "he": "ויטמין-b12-בדיקת-דם-משמעות", "hi": "vitamin-b12-blood-test-matlab",
            "ar": "فيتامين-b12-تحليل-دم-المعنى",
        },
    },
]

LANGS = ["en", "tr", "de", "fr", "it", "es", "he", "hi", "ar"]

LANG_NAMES = {
    "en": "English", "tr": "Turkish", "de": "German", "fr": "French",
    "it": "Italian", "es": "Spanish", "he": "Hebrew", "hi": "Hindi", "ar": "Arabic",
}

# --- DB helpers ---

def db_slug_exists(conn: sqlite3.Connection, slug: str, lang: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM blog_posts WHERE slug=? AND lang=?", (slug, lang))
    return cur.fetchone() is not None


def db_insert_post(conn: sqlite3.Connection, *, slug: str, lang: str, title: str,
                   meta_title: str, meta_description: str, content_json: str,
                   cover_image: str, category: str, reading_time: int) -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO blog_posts
           (slug, lang, title, meta_title, meta_description, content_json,
            cover_image, category, author_name, is_published, is_featured,
            reading_time_minutes, created_at, published_at)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (slug, lang, title, meta_title, meta_description, content_json,
         cover_image, category, "Norya Editorial Team", True, False,
         reading_time, now, now),
    )
    conn.commit()
    return cur.lastrowid


# --- DALL-E 3 görsel üretimi ---

def generate_cover_image(param_id: str, subject: str) -> str:
    """
    DALL-E 3 ile premium medical cover görsel üretir.
    Dönen değer: static path (örn. /static/images/blog/hba1c-cover.jpg)
    """
    img_filename = f"{param_id}-cover.png"
    img_path = STATIC_BLOG_IMG / img_filename
    static_url = f"/static/images/blog/{img_filename}"

    if img_path.exists():
        print(f"  [IMAGE] Zaten var, atlanıyor: {img_path}")
        return static_url

    prompt = (
        f"Premium medical editorial illustration for a health blog article about {subject}. "
        "Style: clean, modern, clinical yet approachable. "
        "Color palette: deep teal (#0d9488) and white with subtle gradients. "
        "Show microscopic or molecular visualization with a professional medical aesthetic. "
        "No text, no labels, no watermarks. "
        "Ultra-high quality, suitable for a premium health SaaS platform. "
        "Wide format, horizontal composition."
    )

    print(f"  [IMAGE] gpt-image-1 ile görsel üretiliyor: {param_id}...")
    try:
        import base64
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1536x1024",
            quality="medium",
            n=1,
        )
        # gpt-image-1 b64_json döner
        b64_data = response.data[0].b64_json
        if b64_data:
            img_bytes = base64.b64decode(b64_data)
            with open(img_path, "wb") as f:
                f.write(img_bytes)
            print(f"  [IMAGE] Kaydedildi: {img_path}")
            return static_url
        # Fallback: URL varsa indir
        image_url = getattr(response.data[0], "url", None)
        if image_url:
            urllib.request.urlretrieve(image_url, img_path)
            print(f"  [IMAGE] Kaydedildi (URL): {img_path}")
            return static_url
        raise ValueError("Görsel verisi boş döndü")
    except Exception as e:
        print(f"  [IMAGE] HATA: {e} — varsayılan cover kullanılıyor")
        return f"/static/images/blog/{param_id}-hero.jpg"


# --- GPT-4o makale üretimi ---

ARTICLE_SYSTEM_PROMPT = """You are a medical content writer for NoryaAI, a premium AI-powered blood test analysis platform.
Write authoritative, evidence-based, SEO-optimized blog articles about blood test parameters.
Follow these rules strictly:
- Write in the requested language
- Use clinical accuracy but accessible language
- Include specific reference ranges, causes, symptoms, and evidence-based recommendations
- Each section must have substantial, unique content (minimum 200 words per section)
- Use HTML formatting: <p>, <ul>, <li>, <strong>, <table> tags where appropriate
- Include a CTA section at the end mentioning Norya AI
- Medical disclaimer: always note results should be discussed with a doctor
- Do NOT use markdown — only HTML within body_html fields
- Return ONLY valid JSON, no extra text"""


def generate_article_content(param: dict, lang: str) -> dict | None:
    """
    GPT-4o ile tek bir dil için makale içeriği üretir.
    Dönen dict: {title, meta_title, meta_description, sections: [...]}
    """
    lang_name = LANG_NAMES[lang]
    param_name = param["name_en"]
    slug = param["slugs"][lang]
    category = param["categories"][lang]

    prompt = f"""Write a comprehensive, SEO-optimized blog article about "{param_name}" blood test in {lang_name}.

Requirements:
- Language: {lang_name} (native quality, not translated)
- Topic: {param_name} — what it measures, normal ranges, causes of abnormal values, what to do
- Slug: {slug}
- Category: {category}
- Reading time: ~8-10 minutes

Return ONLY this exact JSON structure (no markdown, no extra text):
{{
  "title": "<H1 title in {lang_name}, compelling and SEO-friendly>",
  "meta_title": "<SEO meta title, under 60 chars, in {lang_name}>",
  "meta_description": "<SEO meta description, 140-160 chars, in {lang_name}>",
  "sections": [
    {{
      "id": "intro",
      "level": 2,
      "heading": "<Section heading in {lang_name}>",
      "body_html": "<Rich HTML content, minimum 200 words>"
    }},
    {{
      "id": "what-it-measures",
      "level": 2,
      "heading": "<Section heading>",
      "body_html": "<Content with explanation of what the test measures>"
    }},
    {{
      "id": "reference-ranges",
      "level": 2,
      "heading": "<Section heading>",
      "body_html": "<HTML table with normal/borderline/high/low ranges and clinical meaning>"
    }},
    {{
      "id": "causes",
      "level": 2,
      "heading": "<Section heading>",
      "body_html": "<Causes of high and low values>"
    }},
    {{
      "id": "symptoms",
      "level": 2,
      "heading": "<Section heading>",
      "body_html": "<Symptoms and clinical presentation>"
    }},
    {{
      "id": "what-to-do",
      "level": 2,
      "heading": "<Section heading>",
      "body_html": "<Evidence-based recommendations, lifestyle, when to see a doctor>"
    }},
    {{
      "id": "norya-cta",
      "level": 2,
      "heading": "<Section heading about analyzing with AI>",
      "body_html": "<CTA section mentioning NoryaAI blood test analyzer, in a styled div with teal background>"
    }}
  ]
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": ARTICLE_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=4000,
            temperature=0.7,
            response_format={"type": "json_object"},
        )
        content = response.choices[0].message.content
        data = json.loads(content)
        return data
    except json.JSONDecodeError as e:
        print(f"  [GPT] JSON parse hatası ({lang}): {e}")
        return None
    except Exception as e:
        print(f"  [GPT] HATA ({lang}): {e}")
        return None


# --- Ana işlem ---

def process_parameter(param: dict, langs: list[str], conn: sqlite3.Connection,
                       generate_image: bool = True) -> dict:
    """Tek bir parametre için tüm dillerde makale üretir ve DB'ye ekler."""
    stats = {"created": 0, "skipped": 0, "errors": 0}
    param_id = param["id"]
    print(f"\n{'='*60}")
    print(f"PARAMETRE: {param['name_en']} ({param_id})")
    print(f"{'='*60}")

    # Cover görsel (bir kez, parametre başına)
    cover_url = "/static/images/blog/default-blood-test-hero.jpg"
    if generate_image:
        cover_url = generate_cover_image(param_id, param["dalle_subject"])

    # Her dil için makale üret
    for lang in langs:
        slug = param["slugs"][lang]
        print(f"\n  [{lang.upper()}] {slug}")

        # Duplicate kontrolü
        if db_slug_exists(conn, slug, lang):
            print(f"  [{lang.upper()}] ATLANDI — slug zaten DB'de var")
            stats["skipped"] += 1
            continue

        # GPT-4o ile içerik üret
        print(f"  [{lang.upper()}] GPT-4o ile içerik üretiliyor...")
        article = generate_article_content(param, lang)
        if not article:
            print(f"  [{lang.upper()}] HATA — içerik üretilemedi")
            stats["errors"] += 1
            continue

        # Sections kontrolü
        sections = article.get("sections", [])
        if not sections:
            print(f"  [{lang.upper()}] HATA — sections boş")
            stats["errors"] += 1
            continue

        # DB'ye ekle
        try:
            post_id = db_insert_post(
                conn,
                slug=slug,
                lang=lang,
                title=article.get("title", param["name_en"]),
                meta_title=article.get("meta_title", ""),
                meta_description=article.get("meta_description", ""),
                content_json=json.dumps(sections, ensure_ascii=False),
                cover_image=cover_url,
                category=param["categories"][lang],
                reading_time=9,
            )
            print(f"  [{lang.upper()}] ✓ DB'ye eklendi — id={post_id}, slug={slug}")
            stats["created"] += 1
        except sqlite3.IntegrityError as e:
            print(f"  [{lang.upper()}] DB HATA: {e}")
            stats["errors"] += 1

        # Rate limit önlemi
        time.sleep(0.5)

    return stats


def main():
    parser = argparse.ArgumentParser(description="Blog makale + DALL-E cover üretim scripti")
    parser.add_argument("--test", action="store_true", help="Sadece HbA1c EN (hızlı test)")
    parser.add_argument("--param", type=str, help="Belirli parametre id (örn: hba1c,tsh)")
    parser.add_argument("--langs", type=str, help="Belirli diller (örn: en,tr,de)")
    parser.add_argument("--no-image", action="store_true", help="DALL-E görsel üretme")
    args = parser.parse_args()

    # Dil ve parametre filtresi
    langs = LANGS
    params = PARAMETERS

    if args.test:
        langs = ["en"]
        params = [p for p in PARAMETERS if p["id"] == "hba1c"]
        print("TEST MODU: Sadece HbA1c EN")

    if args.langs:
        langs = [l.strip() for l in args.langs.split(",") if l.strip() in LANGS]
        print(f"Diller: {langs}")

    if args.param:
        param_ids = [p.strip() for p in args.param.split(",")]
        params = [p for p in PARAMETERS if p["id"] in param_ids]
        if not params:
            print(f"HATA: Parametre bulunamadı: {args.param}")
            sys.exit(1)
        print(f"Parametreler: {[p['id'] for p in params]}")

    generate_image = not args.no_image

    print(f"\n{'*'*60}")
    print(f"BAŞLIYOR: {len(params)} parametre × {len(langs)} dil = {len(params)*len(langs)} makale")
    print(f"Görsel üretimi: {'AÇIK (DALL-E 3)' if generate_image else 'KAPALI'}")
    print(f"DB: {DB_PATH}")
    print(f"{'*'*60}")

    conn = sqlite3.connect(DB_PATH)
    total_stats = {"created": 0, "skipped": 0, "errors": 0}

    for param in params:
        stats = process_parameter(param, langs, conn, generate_image=generate_image)
        for k in total_stats:
            total_stats[k] += stats[k]

    conn.close()

    print(f"\n{'='*60}")
    print(f"TAMAMLANDI")
    print(f"  Oluşturulan: {total_stats['created']}")
    print(f"  Atlanan (duplicate): {total_stats['skipped']}")
    print(f"  Hatalar: {total_stats['errors']}")
    print(f"{'='*60}")
    if total_stats["created"] > 0:
        print("\nSonraki adım: git add + commit + push → Render deploy")


if __name__ == "__main__":
    main()
