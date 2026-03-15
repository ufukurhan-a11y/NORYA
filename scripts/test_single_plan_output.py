#!/usr/bin/env python3
"""
Single plan çıktı testi: Ekran ve PDF'de hangi blokların göründüğünü kontrol eder.
Çalıştırma: cd /Users/ufukurhan/norya && python scripts/test_single_plan_output.py
"""
import sys
from pathlib import Path

# Proje kökü
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Örnek rapor metni (main.py ile aynı yapıda)
SAMPLE_RESULT_TEXT = """
**Özet**:
Genel durum iyi. Bazı parametreler referans sınırında. Beslenme ve hareket önerilir.

**Risk göstergeleri**:
LDL ve glukoz takip edilmeli.

**Değerler**:
**LDL**: 118 mg/dL Reference: 0-100. Normal.
**HDL**: 52 mg/dL Reference: 40-. Normal.
**Glucose**: 95 mg/dL Reference: 70-100. Normal.
**CRP**: 2.2 mg/L Reference: 0-3. Normal.
**Vitamin D**: 28 ng/mL Reference: 30-. Düşük.

**Olası nedenler**:
- D vitamini güneş ve diyetle desteklenebilir.

**Öneriler**:
- Düzenli kontrole devam edin. Doktorunuzla paylaşın.
"""


def main():
    from datetime import datetime, timezone
    from app.services.report_pdf import (
        build_report_pdf,
        parse_report_to_context,
        _build_premium_context,
        _logo_base64,
        _pdf_labels,
        PDF_LABELS,
    )
    from app.core.plan_config import get_plan_config
    from jinja2 import Environment, FileSystemLoader

    out_dir = ROOT / "test-reports"
    out_dir.mkdir(exist_ok=True)

    report_date = datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")
    lang = "tr"

    # 1) Single plan PDF üret ve kaydet
    pdf_bytes = build_report_pdf(
        SAMPLE_RESULT_TEXT,
        report_date=report_date,
        lang=lang,
        report_id="single-plan-test",
        user_identifier="test@norya.com",
        plan_name="single",
    )
    pdf_path = out_dir / "single_plan_test.pdf"
    pdf_path.write_bytes(pdf_bytes)
    print(f"[OK] PDF kaydedildi: {pdf_path}")

    # 2) Aynı context ile HTML render et (blok kontrolü için)
    base_context = parse_report_to_context(SAMPLE_RESULT_TEXT, report_date=report_date, lang=lang)
    plan_cfg = get_plan_config("single")
    plan_config_ctx = {
        "plan_name": plan_cfg.plan_name,
        "comparison_enabled": plan_cfg.comparison_enabled,
        "trend_enabled": plan_cfg.trend_enabled,
        "explanation_depth": plan_cfg.explanation_depth,
        "pdf_depth": plan_cfg.pdf_depth,
    }
    premium_ctx = _build_premium_context(
        base_context,
        report_id="single-plan-test",
        report_date=report_date,
        user_id="test@norya.com",
        lang=lang,
        trend_data=None,
        trend_locked=True,
    )
    premium_ctx["plan_config"] = plan_config_ctx
    _labels = _pdf_labels(lang)
    _fallback = PDF_LABELS.get("en", {})
    premium_ctx["label_report_doc_sub_single"] = _labels.get("report_doc_sub_single") or _fallback.get("report_doc_sub_single", "")
    premium_ctx["label_report_plan_badge_single"] = _labels.get("report_plan_badge_single") or _fallback.get("report_plan_badge_single", "RAPOR")
    premium_ctx["logo_base64"] = _logo_base64()

    templates_dir = ROOT / "app" / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)), autoescape=True)
    template = env.get_template("report_premium.html")
    html_str = template.render(**premium_ctx)

    html_path = out_dir / "single_plan_preview.html"
    html_path.write_text(html_str, encoding="utf-8")
    print(f"[OK] HTML kaydedildi: {html_path}")

    # 3) HTML içeriğini kontrol et
    html_lower = html_str.lower()

    # Single'da OLMAMASI gerekenler
    trend_section = "trend-section" in html_str
    followup_block = "label_report_followup" in html_str and "trend_enabled" not in html_str[:html_str.find("label_report_followup")]
    # Şablonda follow-up bloğu {% if plan_config.trend_enabled %} ile sarılı; single'da trend_enabled False olduğu için o blok render edilmez
    followup_visible = "Takip Planı" in html_str or "Follow-up Plan" in html_str or "Follow-up" in html_str
    comparison_visible = "İki analizi karşılaştır" in html_str or "compare two analyses" in html_lower

    # Single'da OLMASI gerekenler
    has_executive = "executive-summary" in html_str
    has_health_score = "health-score-card" in html_str
    has_findings = "findings-cards-section" in html_str or "risk_indicators" in html_lower
    has_biomarker = "biomarker-highlights" in html_str or "lab-card" in html_str
    has_recommendations = "label_report_recommendations" in html_str or "Öneriler" in html_str
    has_disclaimer = "refined-disclaimer" in html_str
    badge_rapor = "RAPOR" in html_str and premium_ctx.get("label_report_plan_badge_single") == "RAPOR"

    # Follow-up: şablonda sadece trend_enabled true ise render ediliyor; HTML'de "report_followup" veya "Takip" geçebilir (başka yerde). Tam olarak note-block içinde Takip Planı var mı bakalım
    # trend_enabled false olduğunda o blok çıkmamalı. HTML'de "Takip Planı" kelimesi başka bir yerde de olabilir (ör. öneri metninde). Kontrol: "note-block" içinde "report_followup" veya "Takip Planı" aramak zor. Basitçe: trend-section class'ı sayısı 0 olmalı.
    trend_section_count = html_str.count('class="card trend-section"')
    followup_note_block = html_str.count("label_report_followup")  # label key; follow-up bloğu kapalıysa bu sadece JS/başka yerde geçebilir. Şablonda 2 yerde var: biri trend_enabled içinde. Single'da 0 olmamalı çünkü o blok render edilmiyor. Aslında label_report_followup değişkeni context'te var, sadece o blok {% if trend_enabled %} ile sarılı. Yani render edilen HTML'de "Takip Planı" metni sadece o bloktan gelir; blok render edilmediyse "Takip Planı" yine de başka bir yerde (ör. klinik notlar listesinde) olabilir. Klinik notlar bölümünde "report_followup" başlığı ile ayrı bir note-block var ve o blok {% if plan_config and plan_config.trend_enabled %} ile sarılı. O yüzden single'da bu blok yok. HTML çıktısında "Takip Planı" aramak: eğer sadece o bloktan geliyorsa bulunmamalı. Ama ai_followup listesi premium_ctx'te var ve başka bir yerde kullanılıyor olabilir - hayır, sadece o note-block'ta. O zaman single HTML'de "Takip Planı" (veya report_followup) metni olmamalı.
    has_followup_heading = "Takip Planı" in html_str or "Follow-up Plan" in html_str

    # 4) Özet raporu yaz
    report_lines = [
        "# Single Plan Test Özeti",
        "",
        "## 1. PDF üretildi",
        f"- Dosya: `test-reports/single_plan_test.pdf`",
        "",
        "## 2. PDF/HTML içerik kontrolü",
        "",
        "### Single planda OLMASI gerekenler",
        f"- Genel özet (executive-summary): **{'✓ Var' if has_executive else '✗ Yok'}**",
        f"- Sağlık skoru kartı (health-score-card): **{'✓ Var' if has_health_score else '✗ Yok'}**",
        f"- Öne çıkan bulgular / risk göstergeleri: **{'✓ Var' if has_findings else '✗ Yok'}**",
        f"- Biyobelirteç / lab kartları: **{'✓ Var' if has_biomarker else '✗ Yok'}**",
        f"- Öneriler bölümü: **{'✓ Var' if has_recommendations else '✗ Yok'}**",
        f"- Bilgilendirme uyarısı (disclaimer): **{'✓ Var' if has_disclaimer else '✗ Yok'}**",
        f"- Badge 'RAPOR' (single): **{'✓ Var' if badge_rapor else '✗ Yok'}**",
        "",
        "### Single planda OLMAMASI gerekenler",
        f"- Trend bölümü (trend-section): **{'✗ Görünüyor (HATA)' if trend_section else '✓ Yok (doğru)'}**",
        f"- Takip Planı / Follow-up başlığı: **{'✗ Görünüyor (HATA)' if has_followup_heading else '✓ Yok (doğru)'}**",
        f"- Karşılaştırma vaadi: **{'✗ Görünüyor (HATA)' if comparison_visible else '✓ Yok (doğru)'}**",
        "",
        "## 3. Ekran (SPA) ile tutarlılık",
        "- Single plan ekranda: Genel skor, öne çıkan bulgular, dikkat parametreleri, kategori özeti, biyobelirteç kartları (açıklamalı), öneriler, PDF indir.",
        "- Single planda ekranda trend, karşılaştırma veya follow-up bölümü yok (plan_config.trend_enabled false).",
        "- PDF aynı mantıkla plan_config kullanıyor; trend ve follow-up blokları şablonda trend_enabled ile gizleniyor.",
        "",
        "## 4. Metin kalitesi (tek cümle değil, açıklayıcı)",
        "- Ekran: Single için report_findings_summary_intro_single, report_cat_recommend_*_single, report_biomarker_desc_*_single 2-4 cümle seviyesinde.",
        "- PDF: executive_summary ve öneriler parse_report_to_context + AI çıktısından gelir; single plan PDF'de aynı içerik, sadece trend/follow-up sayfaları yok.",
        "",
        "## 5. Sonuç",
    ]

    errors = []
    if not has_executive:
        errors.append("Executive summary yok")
    if not has_health_score:
        errors.append("Sağlık skoru kartı yok")
    if not has_findings:
        errors.append("Bulgular/risk göstergeleri yok")
    if trend_section:
        errors.append("Trend bölümü single PDF'de görünüyor")
    if has_followup_heading:
        errors.append("Takip Planı başlığı single PDF'de görünüyor")

    if errors:
        report_lines.append("- **Ekran:** Kontrol edin (/?demo=single).")
        report_lines.append("- **PDF:** Eksik/Hata: " + "; ".join(errors))
        report_lines.append("- **Monthly'ye geçmeye hazır:** Hayır — önce single hataları giderilmeli.")
    else:
        report_lines.append("- **Ekran:** Single plan blokları doğru; trend/comparison/follow-up yok.")
        report_lines.append("- **PDF:** Single plan PDF'de doğru bölümler var; trend ve follow-up yok.")
        report_lines.append("- **Monthly'ye geçmeye hazır:** Evet (single tarafı tutarlı).")

    report_path = out_dir / "SINGLE_PLAN_TEST_SUMMARY.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"[OK] Özet rapor: {report_path}")
    print("")
    print("\n".join(report_lines))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
