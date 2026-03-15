"""
Premium tıbbi PDF raporu: result_text (AI çıktısı) → parse → Jinja2 → WeasyPrint → PDF bytes.
"""
import base64
import math
import re
from datetime import datetime, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from app.charts import overall_score_svg_base64, range_bar_svg_base64, simple_value_bar_svg_base64
from app.services.risk_engine import compute_risk


def _gauge_arc_end(score: int) -> tuple[float, float]:
    """Yarım daire gauge: score 0-100 → arc bitiş noktası (viewBox 0 0 200 100, merkez 100,100, r=90)."""
    score = max(0, min(100, score))
    # 0 → (10,100), 100 → (190,100). Açı: 180° - 180*(score/100)
    angle_rad = math.pi * (1 - score / 100.0)
    x = 100 - 90 * math.cos(angle_rad)
    y = 100 - 90 * math.sin(angle_rad)
    return (round(x, 2), round(y, 2))


def _gauge_svg(score: int, fill_class: str) -> str:
    """Yarım daire risk gauge SVG: stroke-dasharray ile fill (score 0-100 → angle 0..180)."""
    score = max(0, min(100, score))
    # Yarı çember uzunluğu: π * r = π * 90
    arc_len = math.pi * 90
    dash_len = arc_len * (score / 100.0)
    # Görünen kısım = dash_len; dashoffset = arc_len - dash_len ile path başından itibaren doldur
    offset = arc_len - dash_len
    return f'''<svg class="gauge-svg" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <path class="gauge-bg" d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke="#e5e7eb" stroke-width="12" stroke-linecap="round"/>
  <path class="gauge-fill {fill_class}" d="M10 100 A90 90 0 0 1 190 100" fill="none" stroke-width="12" stroke-linecap="round" stroke-dasharray="{dash_len:.2f} {arc_len * 2:.2f}" stroke-dashoffset="0"/>
  <text class="gauge-score" x="100" y="72" text-anchor="middle" font-size="20" font-weight="700">{score}</text>
</svg>'''

# Şablon dizini: app/templates (package içinden çalışırken app/templates)
_TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
_PROJECT_ROOT = _TEMPLATES_DIR.parent.parent  # norya/ (static/logo.png burada)
_ENV = Environment(loader=FileSystemLoader(str(_TEMPLATES_DIR)), autoescape=True)

# Rapor ikonu: Tüm PDF raporlarında kullanılan tek ikon (Norya N ikonu — dikkat çekecek kadar, çok büyük değil)
_REPORT_ICON_PATH = _PROJECT_ROOT / "static" / "norya_report_icon.png"
_LOGO_BASE64_CACHE: str | None = None


def _logo_base64() -> str:
    """Rapor header'ında kullanılan Norya ikonunu base64 döndürür (WeasyPrint uyumlu). Öncelik: norya_report_icon.png."""
    global _LOGO_BASE64_CACHE
    if _LOGO_BASE64_CACHE is not None:
        return _LOGO_BASE64_CACHE
    for candidate in (
        _REPORT_ICON_PATH,
        _PROJECT_ROOT / "static" / "norya_report_icon.png",
        Path.cwd() / "static" / "norya_report_icon.png",
        _PROJECT_ROOT / "static" / "norya_logo_transparent_trim.png",
        Path.cwd() / "static" / "norya_logo_transparent_trim.png",
    ):
        try:
            if candidate and getattr(candidate, "exists", None) and candidate.exists():
                _LOGO_BASE64_CACHE = base64.b64encode(candidate.read_bytes()).decode("ascii")
                return _LOGO_BASE64_CACHE
        except Exception:
            continue
    _LOGO_BASE64_CACHE = ""
    return _LOGO_BASE64_CACHE

# Yaygın parametreler için varsayılan referans aralıkları (kan şekeri, lipid vb.) — raporda ref yoksa kullanılır
DEFAULT_REF_RANGES: dict[str, str] = {
    "glucose": "70–100 mg/dL",
    "glukoz": "70–100 mg/dL",
    "açlık glukoz": "70–100 mg/dL",
    "fasting glucose": "70–100 mg/dL",
    "hba1c": "%5.7–6.4 (prediabetes), &lt;5.7% normal",
    "hb a1c": "%5.7–6.4 (prediabetes), &lt;5.7% normal",
    "ldl": "&lt;100 mg/dL optimal",
    "hdl": "&gt;40 mg/dL (M), &gt;50 mg/dL (F)",
    "triglyceride": "&lt;150 mg/dL",
    "trigliserid": "&lt;150 mg/dL",
    "cholesterol": "&lt;200 mg/dL",
    "kolesterol": "&lt;200 mg/dL",
    "crp": "&lt;3 mg/L",
    "c-reaktif": "&lt;3 mg/L",
    "alt": "7–56 U/L",
    "ast": "10–40 U/L",
    "creatinine": "0.7–1.3 mg/dL (M), 0.6–1.1 (F)",
    "kreatinin": "0.7–1.3 mg/dL (M), 0.6–1.1 (F)",
    "urea": "15–40 mg/dL",
    "üre": "15–40 mg/dL",
    "egfr": "&gt;90 mL/min/1.73 m²",
    "ferritin": "12–150 ng/mL (F), 12–300 (M)",
    "demir": "60–170 µg/dL",
    "iron": "60–170 µg/dL",
    "tsh": "0.4–4.0 mIU/L",
    "ft3": "2.3–4.2 pg/mL",
    "ft4": "0.8–1.8 ng/dL",
    "vitamin d": "30–100 ng/mL",
    "d vitamini": "30–100 ng/mL",
    "b12": "200–900 pg/mL",
    "wbc": "4.5–11.0 K/µL",
    "rbc": "4.5–5.5 M/µL (M), 4.0–5.0 (F)",
    "hgb": "13.5–17.5 g/dL (M), 12.0–15.5 (F)",
    "hemoglobin": "13.5–17.5 g/dL (M), 12.0–15.5 (F)",
    "hct": "38.8–50% (M), 34.9–44.5% (F)",
    "plt": "150–400 K/µL",
    "mcv": "80–100 fL",
    "rdw": "11.5–14.5%",
}

# PDF şablonu çok dilli etiketler (rapor dili: TR/EN/DE/FR/ES/IT vb.)
PDF_LABELS: dict[str, dict[str, str]] = {
    "tr": {
        "title": "Norya Analiz Raporu",
        "subtitle": "Kan Tahlili Analiz Raporu — Laboratuvar Sonuçları Yorumu",
        "report_date_label": "Rapor Tarihi",
        "summary_heading": "Özet",
        "biomarkers_heading": "Değerler ve referans aralıkları",
        "param": "Parametre",
        "result": "Sonuç",
        "unit": "Birim",
        "ref_range": "Referans Aralığı",
        "status": "Durum",
        "possible_causes_heading": "Olası Nedenler",
        "recommendations_heading": "Öneriler",
        "footer_note": "Norya ile oluşturulmuştur. Teşhis yerine geçmez; hekiminize danışın.",
        "page_footer": "Bu rapor bilgilendirme amaçlıdır. Tıbbi karar için hekime danışın. — Norya",
        "emr_ehr_note": "EMR/EHR uyumlu — Bu rapor hastane veya hekim bilgi sistemlerine (EMR/EHR) yüklenebilir formattadır.",
        "risk_default_attention": "Dikkat edilmesi gereken parametreler olabilir; önerileri okuyup hekiminizle paylaşın.",
        "risk_default_normal": "Değerler referans aralığında. Özet ve öneriler aşağıda.",
        "risk_indicators_heading": "Risk İşaretleri",
        "report_cat_recommend_ok": "Değerler uygun aralıkta. Sağlığınızı korumak için düzenli takip ve yaşam tarzı önerilerine uymanız yararlı olabilir.",
        "report_cat_recommend_mid": "Takip ve yaşam tarzı (beslenme, hareket) için hekiminizle görüşmeniz önerilir.",
        "report_cat_recommend_risk": "Bu parametreler için hekiminizle görüşmeniz ve gerekirse ek tetkik planlamanız önerilir.",
        "overall_status_heading": "Genel durum",
        "overall_chart_title": "Genel durum (0–100)",
        "overall_badge_normal": "Normal",
        "overall_badge_attention": "Sınır",
        "overall_badge_high": "Riskli",
        "overall_chart_legend": "Yeşil = Normal · Turuncu = Sınır · Kırmızı = Riskli (skor 0–100)",
        "intro_heading": "Bu rapor hakkında",
        "intro_p1": "Bu rapor, laboratuvar sonuçlarınızın anlaşılır bir ön değerlendirmesidir ve yalnızca bilgilendirme amaçlıdır. Aşağıda özet, parametre değerleri, referans aralıkları ve genel öneriler yer alır. Rapor teşhis koymaz; tıbbi karar yerine geçmez. Sonuçlarınızı mutlaka bir hekim ile görüşmeniz önerilir. Tıbbi kararlar ve tedavi planı için hekiminize danışın.",
        "intro_p2": "Norya, kan tahlili sonuçlarınızı sade dilde yorumlamanıza yardımcı olan bir araçtır. Elde ettiğiniz özet ve öneriler genel sağlık farkındalığınızı artırmak içindir. Herhangi bir parametre referans dışındaysa veya endişeniz varsa hekiminize başvurun. Düzenli takip ve yaşam tarzı önerileri hekiminizle birlikte planlanmalıdır. Bu rapor, hekim muayenesi veya tanı yerine kullanılmamalıdır.",
        "how_to_read_heading": "Parametreler nasıl okunur?",
        "how_to_read_body": "Her parametre için \"Sonuç\" satırında laboratuvar değeriniz, \"Ref\" satırında ise o test için kabul edilen referans aralığı verilir. Yeşil renk, değerin referans aralığında (normal) olduğunu gösterir. Turuncu, sınırda veya takip gerektiren durumu ifade eder. Kırmızı, referans dışı (düşük veya yüksek) ve hekim değerlendirmesi önerilen durumu gösterir. Tüm sonuçları hekiminizle paylaşarak birlikte yorumlamanız önemlidir.",
        "doctor_title": "Norya — Doktoruma Götür",
        "doctor_subtitle": "Kan Tahlili Özeti — Hekime iletilmek üzere hazırlanmıştır",
        "doctor_banner_text": "Bu rapor, hastanın hekimi ile paylaşması amacıyla Norya tarafından oluşturulmuştur. Eğitim amaçlı bilgilendirme niteliğindedir. Tıbbi karar ve tedavi için hekim değerlendirmesi gerekir.",
        "doctor_page_footer": "Hekime iletilmek üzere hazırlanmıştır. Tıbbi karar için hekim değerlendirmesi gerekir. — Norya",
        "doctor_footer_note": "Bu rapor Norya laboratuvar sonuçları yorumlama hizmeti ile oluşturulmuştur. Teşhis veya tedavi yerine geçmez. Tıbbi kararlar için hekim değerlendirmesi gerekir.",
        "report_header_title": "Kan Tahlili Analiz Raporu",
        "report_header_subtitle": "Yapay zeka destekli ön değerlendirme",
        "report_header_subtitle_short": "Klinik karar yerine geçmez",
        "report_id_label": "Rapor No",
        "info_patient_heading": "Kişi",
        "info_analysis_heading": "Analiz",
        "footer_disclaimer": "Bu rapor bilgilendirme amaçlıdır. Doktorunuza danışın.",
        "medical_disclaimer_1": "Bu rapor bilgilendirme amaçlıdır; teşhis veya tedavi yerine geçmez. Sağlık kararları için hekiminize başvurun.",
        "medical_disclaimer_2": "Norya AI bir tıbbi teşhis sistemi değildir.",
        "report_summary": "Özet",
        "report_findings": "Bulgular",
        "report_recommendations": "Öneriler",
        "report_causes": "Olası Nedenler",
        "report_followup": "Takip Planı",
        "report_doctor_note": "Doktora Not",
        "report_clinical_notes": "Klinik Notlar",
        "report_risk_summary": "Risk Özeti",
        "report_health_score": "Genel Sağlık Skoru",
        "report_risk_indicator": "Risk Göstergesi",
        "report_trend_analysis": "Trend Analizi",
        "report_trend_more_needed": "Trend için daha fazla analiz gerekli.",
        "report_band_low": "Düşük",
        "report_band_mid": "Orta",
        "report_band_high": "İyi",
        "report_findings_highlight": "Öne Çıkan Bulgular",
        "report_test_results": "Test Sonuçları",
        "report_test": "Test",
        "report_result": "Sonuç",
        "report_reference": "Referans",
        "report_common_refs": "Yaygın referans aralıkları (bilgi)",
        "report_status": "Durum",
        "report_alert_title": "Bilgilendirme amaçlıdır.",
        "report_alert_body": "Bu rapor tıbbi teşhis veya tedavi yerine geçmez. Sağlık kararlarınız için hekiminize başvurunuz.",
        "report_footer": "Norya • Bilgilendirme amaçlıdır • support@noryaai.com",
        "report_brand_sub": "Ön Değerlendirme Raporu",
        "report_doc_title": "Kan Tahlili Analiz Raporu",
        "report_doc_sub": "Sağlık durumunuzun ön değerlendirmesi; teşhis yerine geçmez, bilgilendirme amaçlıdır.",
        "report_rid_label": "Rapor No",
        "report_user_label": "Kullanıcı",
        "report_date_label_short": "Tarih",
        "report_lang_label": "Dil",
        "report_verify_code": "Doğrulama",
        "report_verification_title": "Rapor Doğrulama",
        "report_verification_scan_hint": "Orijinallik için QR ile tarayın veya kodu doğrulama sayfasında girin.",
        "report_page_title": "Norya Klinik Rapor",
        "report_share_note": "Bu raporu hekiminizle paylaşabilir, gerekli görülürse ek tetkik veya takip planı birlikte oluşturabilirsiniz.",
        "report_health_score_title": "Genel Sağlık Skoru",
        "report_risk_indicator_title": "Risk Göstergesi",
        "report_trend_title": "Trend Analizi",
        "report_trend_need_more": "Trend için daha fazla analiz gerekli.",
        "report_upgrade": "Premium'a Geç",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Bilgilendirme amaçlıdır.",
        "report_disclaimer_text": "Teşhis veya tedavi yerine geçmez; sağlık kararları için hekiminize başvurun.",
        "report_trend_locked": "Trend analizi abonelik ile açılır.",
        "report_category_scores": "Kategori skorları",
        "report_risk_distribution": "Risk dağılımı",
        "report_radar_balance": "Biyobelirteç dengesi",
        "report_top_attention": "Öne çıkan dikkat alanları",
        "report_dist_normal": "Normal (referans aralığında)",
        "report_dist_borderline": "Sınırda (takip önerilir)",
        "report_dist_attention": "Dikkat (hekim değerlendirmesi önerilir)",
        "report_executive_summary": "Genel Sağlık Özeti — Laboratuvar sonuçlarınızın kısa değerlendirmesi",
        "report_summary_tiles": "Özet — Skor ve risk düzeyi",
        "report_biomarker_highlights": "Biyobelirteç Özeti — Öne çıkan kan değerleri",
        "report_risk_indicators": "Risk Göstergeleri — Takip edilmesi önerilen parametreler",
        "report_key_areas": "Takip Edilecek Alanlar — Sağlık açısından öncelikli konular",
        "report_foods_to_favor": "Tercih Edilebilecek Gıdalar",
        "report_foods_to_limit": "Sınırlanabilecek Gıdalar",
        "report_foods_eat_heading": "Yenilmesi Gerekenler",
        "report_foods_avoid_heading": "Yenilmemesi Gerekenler",
        "report_lifestyle": "Yaşam Tarzı Önerileri",
        "report_doctor_discussion": "Hekim Görüşmesi Notları",
        "report_tile_overall_score": "Genel Skor",
        "report_tile_risk_level": "Risk Düzeyi",
        "report_tile_bio_age": "Biyolojik Yaş",
        "report_tile_priority": "Öncelik",
        "report_priority_general": "Genel iyilik hali ve düzenli takip",
        "report_food_favor_default": "Dengeli beslenme; sebze ve meyveler lif ve vitaminlerle genel sağlığı destekleyebilir. Tam tahıllar ve baklagiller de kalp ve sindirim sağlığı için faydalıdır.",
        "report_food_limit_default": "İşlenmiş gıdalar ve aşırı şeker sınırlanabilir; bu tür besinler kan şekeri ve kilo dengesini olumsuz etkileyebilir.",
        "report_lifestyle_sleep": "Yeterli uyku (günde 7–8 saat) hem toparlanmayı hem de bağışıklık ve ruh halini destekler.",
        "report_lifestyle_movement": "Düzenli hareket kalp damar sağlığı, kan şekeri dengesi ve genel iyilik hali için önerilir.",
        "report_lifestyle_followup": "Takip süresini ve gerekirse tekrarlanan tahlilleri hekiminizle görüşün.",
        "report_movement_default": "Haftada en az 150 dakika orta tempolu hareket (yürüyüş, yüzme, bisiklet) kalp sağlığı ve kilo yönetimi için önerilir.",
        "report_stress_default": "Stres azaltma: nefes egzersizleri, kısa molalar ve düzenli uyku hem ruh hem beden sağlığını destekler.",
        "report_sleep_default": "Günde 7–8 saat uyku önerilir; uyku hijyenine (karanlık oda, düzenli saat) dikkat edin.",
        "report_hydration_default": "Günde yaklaşık 1,5–2 litre sıvı tüketimi böbrek fonksiyonları ve genel metabolizma için önerilir.",
        "report_doctor_note_1": "Bu raporu hekiminizle paylaşarak laboratuvar sonuçlarınızı birlikte yorumlayabilirsiniz.",
        "report_doctor_note_2": "Belirti, şikâyet veya endişeleriniz varsa mutlaka hekim tarafından değerlendirilmelidir.",
        "report_risk_factors": "Risk Faktörleri",
        "report_risk_factors_line_1": "Kardiyovasküler veya metabolik faktörlere işaret edebilir; hekiminizle görüşün.",
        "report_risk_factors_line_2": "Yaşam tarzı ve beslenme genel iyilik halini destekleyebilir.",
        "report_refined_disclaimer": "Bu rapor yalnızca bilgilendirme amaçlıdır; teşhis veya tedavi sunmaz. Sağlık durumunuzla ilgili kararlar ve tedavi seçenekleri için hekiminize başvurun.",
        "report_doc_sub_single": "Tek analiz raporu — Özet, değerler ve öneriler; teşhis yerine geçmez, bilgilendirme amaçlıdır.",
        "report_plan_badge_single": "RAPOR",
        "report_trend_placeholder": "Trend, zamanla daha fazla raporla kullanılabilir hale gelir.",
        "report_comparison_title": "Önceki analizle karşılaştırma",
        "report_what_changed_title": "Neler değişti?",
        "report_comparison_no_previous": "Henüz önceki analiz yok. Bir sonraki raporunuzda bu bölüm karşılaştırma ile doldurulacaktır.",
        "report_what_changed_no_data": "Değişim özeti, bir sonraki raporunuzdan itibaren karşılaştırma verisiyle birlikte görünecektir.",
        "report_why_it_matters": "Neden önemli",
        "report_monitoring_focus": "Takip odağı",
        "report_domain_cardio": "Kardiyovasküler",
        "report_domain_metabolic": "Metabolik",
        "report_domain_vitamin": "Vitamin",
        "report_domain_inflammation": "Enflamasyon",
        "report_health_age_title": "Biyolojik Yaş Tahmini",
        "report_movement_heading": "Hareket ve Egzersiz",
        "report_stress_heading": "Stres Yönetimi",
        "report_sleep_heading": "Uyku ve Dinlenme",
        "report_hydration_heading": "Sıvı Tüketimi",
        "report_cat_hemogram": "Hemogram",
        "report_cat_crp": "CRP (Enflamasyon)",
        "report_cat_glucose": "Glukoz",
        "report_cat_lipids": "Lipidler (LDL / HDL / Trigliserid)",
        "report_cat_liver": "Karaciğer (ALT / AST)",
        "report_cat_kidney": "Böbrek (Üre / Kreatinin)",
        "report_cat_iron": "Demir / Ferritin",
        "report_cat_thyroid": "Tiroid (TSH / FT3 / FT4)",
        "report_cat_other": "Diğer Değerler",
        "report_attention_do": "Neye dikkat etmeli",
        "report_attention_avoid": "Neye dikkat etmemeli",
    },
    "en": {
        "title": "Norya Analysis Report",
        "subtitle": "Blood Test Analysis Report — AI-Assisted Interpretation",
        "report_date_label": "Report Date",
        "summary_heading": "Summary",
        "biomarkers_heading": "Biomarkers and Reference Ranges",
        "param": "Parameter",
        "result": "Result",
        "unit": "Unit",
        "ref_range": "Reference Range",
        "status": "Status",
        "possible_causes_heading": "Possible Causes",
        "recommendations_heading": "Recommendations",
        "footer_note": "This report was generated by Norya AI interpretation. It is not a diagnosis or treatment. Always consult a healthcare professional for medical decisions.",
        "page_footer": "This report is for information only. Consult a doctor for medical decisions. — Norya",
        "emr_ehr_note": "EMR/EHR compatible — This report can be uploaded to hospital or clinician information systems (EMR/EHR).",
        "risk_default_attention": "Some values may need attention; read the recommendations and share your results with your doctor.",
        "risk_default_normal": "All values are within reference range. Summary and health recommendations below; regular follow-up is a good habit.",
        "risk_indicators_heading": "Risk Indicators",
        "report_cat_recommend_ok": "Values are in a healthy range. Following lifestyle advice and regular check-ups can help you stay well.",
        "report_cat_recommend_mid": "Discuss follow-up and lifestyle (diet, activity) with your doctor.",
        "report_cat_recommend_risk": "Discuss these parameters with your doctor and consider further tests if needed.",
        "overall_status_heading": "Overall status",
        "overall_chart_title": "Overall status (0–100)",
        "overall_badge_normal": "Normal",
        "overall_badge_attention": "Borderline",
        "overall_badge_high": "At risk",
        "overall_chart_legend": "Green = Normal | Orange = Borderline | Red = At risk (score 0–100 by reference range fit)",
        "intro_heading": "About this report",
        "intro_p1": "This report is an AI-assisted preliminary interpretation of your blood test results. It includes a summary, parameter values with reference ranges, and general recommendations. It does not provide a diagnosis and is for information only.",
        "intro_p2": "Always discuss your results with a healthcare provider. Consult your doctor for medical decisions and treatment plans.",
        "how_to_read_heading": "How to read the parameters",
        "how_to_read_body": "For each parameter, the \"Result\" column shows your lab value and \"Reference range\" shows the normal range for that test. Green = Normal (within range), orange = Borderline, red = Outside range (low or high). The charts show where your value sits relative to the reference range.",
        "doctor_title": "Norya — Take to My Doctor",
        "doctor_subtitle": "Blood Test Summary — Prepared for sharing with your doctor",
        "doctor_banner_text": "This report was generated by Norya for the patient to share with their doctor. It is for educational information only. Medical decisions and treatment require physician evaluation.",
        "doctor_page_footer": "Prepared for sharing with your doctor. Medical decisions require physician evaluation. — Norya",
        "doctor_footer_note": "This report was generated by Norya AI. It does not replace diagnosis or treatment. Medical decisions require physician evaluation.",
        "report_header_title": "Blood Test Analysis Report",
        "report_header_subtitle": "AI-assisted preliminary assessment",
        "report_header_subtitle_short": "Does not replace clinical decision",
        "report_id_label": "Report No.",
        "info_patient_heading": "Patient",
        "info_analysis_heading": "Analysis",
        "footer_disclaimer": "This report is for information only. Consult your doctor.",
        "medical_disclaimer_1": "This report is for AI-assisted preliminary assessment only. It does not replace medical diagnosis or treatment. Please consult your doctor for decisions regarding your health.",
        "medical_disclaimer_2": "Norya AI is not a medical diagnosis system.",
        "report_summary": "Summary",
        "report_findings": "Findings",
        "report_recommendations": "Recommendations",
        "report_causes": "Possible Causes",
        "report_followup": "Follow-up Plan",
        "report_doctor_note": "Note for Doctor",
        "report_clinical_notes": "Clinical Notes",
        "report_risk_summary": "Risk Summary",
        "report_health_score": "Overall Health Score",
        "report_risk_indicator": "Risk Indicator",
        "report_trend_analysis": "Trend Analysis",
        "report_trend_more_needed": "More analyses needed for trend.",
        "report_band_low": "Low",
        "report_band_mid": "Moderate",
        "report_band_high": "Good",
        "report_findings_highlight": "Key Findings",
        "report_test_results": "Test Results",
        "report_test": "Test",
        "report_result": "Result",
        "report_reference": "Reference",
        "report_common_refs": "Common reference ranges (info)",
        "report_status": "Status",
        "report_alert_title": "For information only.",
        "report_alert_body": "This report does not replace medical diagnosis or treatment. Consult your doctor for health decisions.",
        "report_footer": "Norya • For information only • support@noryaai.com",
        "report_brand_sub": "Clinical Report",
        "report_doc_title": "Blood Test Analysis Report",
        "report_doc_sub": "A preliminary view of your health status; it does not replace a diagnosis and is for information only.",
        "report_rid_label": "Report No",
        "report_user_label": "User",
        "report_date_label_short": "Date",
        "report_lang_label": "Language",
        "report_verify_code": "Verification",
        "report_verification_title": "Report Verification",
        "report_verification_scan_hint": "Scan QR or enter the code on the verification page to confirm authenticity.",
        "report_page_title": "Norya Clinical Report",
        "report_share_note": "You can share this report with your doctor and plan further tests or follow-up together if needed.",
        "report_health_score_title": "Overall Health Score",
        "report_risk_indicator_title": "Risk Indicator",
        "report_trend_title": "Trend Analysis",
        "report_trend_need_more": "More analyses needed for trend.",
        "report_upgrade": "Upgrade to Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "For information only.",
        "report_disclaimer_text": "This report does not replace medical diagnosis or treatment. Consult your doctor for health decisions.",
        "report_trend_locked": "Trend analysis is available with subscription.",
        "report_category_scores": "Category scores",
        "report_risk_distribution": "Risk distribution",
        "report_radar_balance": "Biomarker balance",
        "report_top_attention": "Top attention areas",
        "report_dist_normal": "Normal (within reference range)",
        "report_dist_borderline": "Borderline (follow-up recommended)",
        "report_dist_attention": "Attention (physician evaluation recommended)",
        "report_executive_summary": "Health Summary — A brief interpretation of your lab results",
        "report_summary_tiles": "Summary — Score and risk level",
        "report_biomarker_highlights": "Biomarker Highlights — Key blood values",
        "report_risk_indicators": "Risk Indicators — Parameters worth monitoring",
        "report_risk_factors": "Risk Factors",
        "report_risk_factors_line_1": "May indicate cardiovascular or metabolic factors. Discuss with your clinician.",
        "report_risk_factors_line_2": "Lifestyle and diet may support overall wellness.",
        "report_key_areas": "Key Areas to Watch — Health priorities",
        "report_foods_to_favor": "Foods to Favor",
        "report_foods_to_limit": "Foods to Limit",
        "report_foods_eat_heading": "Foods to Include",
        "report_foods_avoid_heading": "Foods to Avoid",
        "report_movement_heading": "Movement & Exercise",
        "report_stress_heading": "Stress Management",
        "report_sleep_heading": "Sleep & Rest",
        "report_hydration_heading": "Hydration",
        "report_cat_hemogram": "Hemogram",
        "report_cat_crp": "CRP (Inflammation)",
        "report_cat_glucose": "Glucose",
        "report_cat_lipids": "Lipids (LDL / HDL / Triglycerides)",
        "report_cat_liver": "Liver (ALT / AST)",
        "report_cat_kidney": "Kidney (Urea / Creatinine)",
        "report_cat_iron": "Iron / Ferritin",
        "report_cat_thyroid": "Thyroid (TSH / FT3 / FT4)",
        "report_cat_other": "Other Values",
        "report_attention_do": "What to pay attention to",
        "report_attention_avoid": "What to avoid",
        "report_lifestyle": "Lifestyle Support",
        "report_doctor_discussion": "Doctor Discussion Notes",
        "report_tile_overall_score": "Overall Score",
        "report_tile_risk_level": "Risk Level",
        "report_tile_bio_age": "Biological Age",
        "report_tile_priority": "Priority Focus",
        "report_priority_general": "General wellness and regular follow-up",
        "report_food_favor_default": "Balanced diet; vegetables and fruits provide fibre and vitamins that support general health. Whole grains and legumes are also beneficial for heart and digestive health.",
        "report_food_limit_default": "Processed foods and excess sugar may be worth limiting; they can affect blood sugar and weight balance.",
        "report_movement_default": "At least 150 minutes of moderate activity per week (walking, swimming, cycling) is recommended for heart health and weight management.",
        "report_stress_default": "Stress reduction: breathing exercises, short breaks and regular sleep support both mental and physical health.",
        "report_sleep_default": "7–8 hours of sleep per night is recommended; pay attention to sleep hygiene (dark room, consistent schedule).",
        "report_hydration_default": "About 1.5–2 litres of fluid per day is recommended for kidney function and metabolism.",
        "report_lifestyle_sleep": "Adequate sleep (7–8 hours) supports recovery, immunity and mood.",
        "report_lifestyle_movement": "Regular movement is recommended for cardiovascular health, blood sugar balance and general wellness.",
        "report_lifestyle_followup": "Discuss follow-up timing and any repeat tests with your doctor.",
        "report_doctor_note_1": "Share this report with your doctor so you can interpret your lab results together.",
        "report_doctor_note_2": "Any symptoms, concerns or questions should be evaluated by a physician.",
        "report_refined_disclaimer": "This report is for informational use only; it does not provide a diagnosis or treatment. For decisions about your health and treatment options, consult your doctor.",
        "report_doc_sub_single": "Single analysis report — Summary, values and recommendations; for information only, not a substitute for diagnosis.",
        "report_plan_badge_single": "REPORT",
        "report_trend_placeholder": "Trend becomes available with more reports over time.",
        "report_comparison_title": "Compare with previous analysis",
        "report_what_changed_title": "What changed?",
        "report_comparison_no_previous": "No previous analysis yet. After your next report, this section will show a comparison.",
        "report_what_changed_no_data": "Change summary will appear after your next report when comparison data is available.",
        "report_why_it_matters": "Why it matters",
        "report_monitoring_focus": "Monitoring focus",
        "report_domain_cardio": "Cardiovascular",
        "report_domain_metabolic": "Metabolic",
        "report_domain_vitamin": "Vitamin",
        "report_domain_inflammation": "Inflammation",
        "report_health_age_title": "Biological age estimate",
    },
    "de": {
        "title": "Norya Analysebericht",
        "subtitle": "Blutbild-Analyse — KI-gestützte Auswertung",
        "report_date_label": "Berichtsdatum",
        "summary_heading": "Zusammenfassung",
        "biomarkers_heading": "Biomarker und Referenzbereiche",
        "param": "Parameter",
        "result": "Ergebnis",
        "unit": "Einheit",
        "ref_range": "Referenzbereich",
        "status": "Status",
        "possible_causes_heading": "Mögliche Ursachen",
        "recommendations_heading": "Empfehlungen",
        "footer_note": "Dieser Bericht wurde von Norya KI erstellt. Er ersetzt keine Diagnose oder Behandlung. Konsultieren Sie einen Arzt.",
        "page_footer": "Dieser Bericht dient nur zur Information. Arzt konsultieren. — Norya",
        "emr_ehr_note": "EMR/EHR-kompatibel — Dieser Bericht kann in Klinik- oder Arztinformationssysteme hochgeladen werden.",
        "risk_default_attention": "Einige Werte erfordern möglicherweise Beachtung. Siehe Empfehlungen und ggf. Arzt konsultieren.",
        "risk_default_normal": "Alle Werte im Referenzbereich. Zusammenfassung und Empfehlungen unten.",
        "overall_status_heading": "Gesamtstatus",
        "overall_chart_title": "Gesamtstatus (0–100)",
        "overall_badge_normal": "Normal",
        "overall_badge_attention": "Grenzwertig",
        "overall_badge_high": "Risiko",
        "overall_chart_legend": "Grün = Normal | Orange = Grenzwertig | Rot = Risiko (Score 0–100 basierend auf dem Referenzbereich)",
        "intro_heading": "Über diesen Bericht",
        "intro_p1": "Dieser Bericht ist eine KI-gestützte Auswertung Ihrer Blutwerte mit Zusammenfassung, Parametern und Empfehlungen. Er dient nur zur Information und ersetzt keine Diagnose.",
        "intro_p2": "Besprechen Sie Ihre Ergebnisse mit einem Arzt. Konsultieren Sie Ihren Arzt für medizinische Entscheidungen.",
        "how_to_read_heading": "Wie liest man die Parameter?",
        "how_to_read_body": "„Ergebnis“ zeigt Ihren Laborwert, „Referenzbereich“ den Normalbereich. Grün = Normal, Orange = Grenzwertig, Rot = Außerhalb des Bereichs. Die Grafik zeigt die Position Ihres Werts.",
        "doctor_title": "Norya — Für meinen Arzt",
        "doctor_subtitle": "Blutbild-Zusammenfassung — Zur Weitergabe an den Arzt",
        "doctor_banner_text": "Dieser Bericht wurde von Norya für die Weitergabe an den behandelnden Arzt erstellt. Nur zur Information. Medizinische Entscheidungen erfordern ärztliche Bewertung.",
        "doctor_page_footer": "Zur Weitergabe an den Arzt. Ärztliche Bewertung erforderlich. — Norya",
        "doctor_footer_note": "Dieser Bericht wurde von Norya erstellt. Er ersetzt keine Diagnose oder Behandlung. Ärztliche Bewertung erforderlich.",
        "medical_disclaimer_1": "Dieser Bericht ist eine KI-gestützte, vorläufige Einschätzung. Er ersetzt keine medizinische Diagnose oder Behandlung. Für Entscheidungen zu Ihrer Gesundheit wenden Sie sich bitte an Ihren Arzt.",
        "medical_disclaimer_2": "Norya AI ist kein medizinisches Diagnosesystem.",
        "report_summary": "Zusammenfassung",
        "report_findings": "Befunde",
        "report_recommendations": "Empfehlungen",
        "report_causes": "Mögliche Ursachen",
        "report_followup": "Verlaufskontrolle",
        "report_doctor_note": "Notiz für den Arzt",
        "report_clinical_notes": "Klinische Notizen",
        "report_risk_summary": "Risikoübersicht",
        "report_health_score": "Gesundheitspunktzahl",
        "report_risk_indicator": "Risikoanzeige",
        "report_trend_analysis": "Trendanalyse",
        "report_trend_more_needed": "Für den Trend sind weitere Analysen nötig.",
        "report_band_low": "Niedrig",
        "report_band_mid": "Mittel",
        "report_band_high": "Gut",
        "report_findings_highlight": "Wichtige Befunde",
        "report_test_results": "Testergebnisse",
        "report_test": "Test",
        "report_result": "Ergebnis",
        "report_reference": "Referenz",
        "report_status": "Status",
        "report_alert_title": "Nur zur Information.",
        "report_alert_body": "Dieser Bericht ersetzt keine Diagnose oder Behandlung. Konsultieren Sie Ihren Arzt.",
        "report_footer": "Norya • Nur zur Information • support@noryaai.com",
        "report_brand_sub": "Klinischer Bericht",
        "report_doc_title": "Blutbild-Analysebericht",
        "report_doc_sub": "Informationsorientiertes klinisches Berichtsformat",
        "report_rid_label": "Bericht-Nr",
        "report_user_label": "Benutzer",
        "report_date_label_short": "Datum",
        "report_lang_label": "Sprache",
        "report_verify_code": "Verifizierung",
        "report_page_title": "Norya Klinischer Bericht",
        "report_share_note": "Sie können diesen Bericht mit Ihrem Arzt teilen und bei Bedarf weitere Untersuchungen planen.",
        "report_health_score_title": "Gesundheitspunktzahl",
        "report_risk_indicator_title": "Risikoanzeige",
        "report_trend_title": "Trendanalyse",
        "report_trend_need_more": "Für den Trend sind weitere Analysen nötig.",
        "report_upgrade": "Auf Premium wechseln",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Nur zur Information.",
        "report_disclaimer_text": "Dieser Bericht ersetzt keine Diagnose oder Behandlung. Konsultieren Sie Ihren Arzt.",
        "report_trend_locked": "Trendanalyse mit Abonnement verfügbar.",
        "report_domain_cardio": "Kardiovaskulär",
        "report_domain_metabolic": "Stoffwechsel",
        "report_domain_vitamin": "Vitamin",
        "report_domain_inflammation": "Entzündung",
        "report_comparison_title": "Vergleich mit vorheriger Analyse",
        "report_what_changed_title": "Was hat sich geändert?",
        "report_comparison_no_previous": "Noch keine vorherige Analyse. Nach Ihrem nächsten Bericht wird hier der Vergleich angezeigt.",
        "report_what_changed_no_data": "Die Änderungsübersicht erscheint nach Ihrem nächsten Bericht, sobald Vergleichsdaten vorliegen.",
        "report_risk_factors": "Risikofaktoren",
        "report_risk_factors_line_1": "Kann auf kardiovaskuläre oder metabolische Faktoren hinweisen. Mit dem Arzt besprechen.",
        "report_risk_factors_line_2": "Lebensstil und Ernährung können das allgemeine Wohlbefinden unterstützen.",
    },
    "fr": {
        "title": "Rapport d'analyse Norya",
        "subtitle": "Rapport d'analyse sanguine — Interprétation par IA",
        "report_date_label": "Date du rapport",
        "summary_heading": "Résumé",
        "biomarkers_heading": "Biomarqueurs et intervalles de référence",
        "param": "Paramètre",
        "result": "Résultat",
        "unit": "Unité",
        "ref_range": "Intervalle de référence",
        "status": "Statut",
        "possible_causes_heading": "Causes possibles",
        "recommendations_heading": "Recommandations",
        "footer_note": "Ce rapport a été généré par Norya. Il ne remplace pas un diagnostic ou un traitement. Consultez un professionnel de santé.",
        "page_footer": "Ce rapport est à titre informatif. Consultez un médecin. — Norya",
        "emr_ehr_note": "Compatible EMR/EHR — Ce rapport peut être importé dans les systèmes d'information hospitaliers ou médicaux.",
        "risk_default_attention": "Certaines valeurs peuvent nécessiter une attention. Voir les recommandations et consulter un médecin si besoin.",
        "risk_default_normal": "Toutes les valeurs sont dans les normes. Résumé et recommandations ci-dessous.",
        "overall_status_heading": "État général",
        "overall_chart_title": "État général (0–100)",
        "overall_badge_normal": "Normal",
        "overall_badge_attention": "Limite",
        "overall_badge_high": "Risque",
        "overall_chart_legend": "Vert = Normal | Orange = Limite | Rouge = À risque (score 0–100 selon l'adéquation à l'intervalle de référence)",
        "intro_heading": "À propos de ce rapport",
        "intro_p1": "Ce rapport est une interprétation préliminaire de vos résultats d'analyse sanguine. Il contient un résumé, les paramètres et des recommandations. Il est informatif et ne constitue pas un diagnostic.",
        "intro_p2": "Consultez toujours un professionnel de santé pour vos résultats et décisions médicales.",
        "how_to_read_heading": "Comment lire les paramètres",
        "how_to_read_body": "« Résultat » indique votre valeur, « Intervalle de référence » la norme. Vert = Normal, orange = Limite, rouge = Hors norme. Les graphiques montrent la position par rapport à la norme.",
        "doctor_title": "Norya — À montrer à mon médecin",
        "doctor_subtitle": "Résumé d'analyse sanguine — À transmettre au médecin",
        "doctor_banner_text": "Ce rapport a été généré par Norya pour être partagé avec le médecin. À titre informatif. Les décisions médicales nécessitent l'évaluation du médecin.",
        "doctor_page_footer": "À transmettre au médecin. Évaluation médicale requise. — Norya",
        "doctor_footer_note": "Ce rapport a été généré par Norya. Il ne remplace pas un diagnostic ou un traitement. Évaluation médicale requise.",
        "medical_disclaimer_1": "Ce rapport est une évaluation préliminaire assistée par IA. Il ne remplace pas un diagnostic ou un traitement médical. Pour toute décision concernant votre santé, consultez votre médecin.",
        "medical_disclaimer_2": "Norya AI n'est pas un système de diagnostic médical.",
        "report_summary": "Résumé",
        "report_findings": "Constatations",
        "report_recommendations": "Recommandations",
        "report_causes": "Causes possibles",
        "report_followup": "Suivi",
        "report_doctor_note": "Note pour le médecin",
        "report_clinical_notes": "Notes cliniques",
        "report_risk_summary": "Résumé des risques",
        "report_health_score": "Score de santé général",
        "report_risk_indicator": "Indicateur de risque",
        "report_trend_analysis": "Analyse de tendance",
        "report_trend_more_needed": "Plus d'analyses nécessaires pour la tendance.",
        "report_band_low": "Faible",
        "report_band_mid": "Modéré",
        "report_band_high": "Bon",
        "report_findings_highlight": "Constats principaux",
        "report_test_results": "Résultats des analyses",
        "report_test": "Test",
        "report_result": "Résultat",
        "report_reference": "Référence",
        "report_status": "Statut",
        "report_alert_title": "À titre informatif uniquement.",
        "report_alert_body": "Ce rapport ne remplace pas un diagnostic ou un traitement. Consultez votre médecin.",
        "report_footer": "Norya • À titre informatif • support@noryaai.com",
        "report_brand_sub": "Rapport clinique",
        "report_doc_title": "Rapport d'analyse sanguine",
        "report_doc_sub": "Format de rapport clinique à titre informatif",
        "report_rid_label": "N° rapport",
        "report_user_label": "Utilisateur",
        "report_date_label_short": "Date",
        "report_lang_label": "Langue",
        "report_verify_code": "Vérification",
        "report_page_title": "Rapport clinique Norya",
        "report_share_note": "Vous pouvez partager ce rapport avec votre médecin et planifier un suivi si nécessaire.",
        "report_health_score_title": "Score de santé général",
        "report_risk_indicator_title": "Indicateur de risque",
        "report_trend_title": "Analyse de tendance",
        "report_trend_need_more": "Plus d'analyses nécessaires pour la tendance.",
        "report_upgrade": "Passer à Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "À titre informatif uniquement.",
        "report_disclaimer_text": "Ce rapport ne remplace pas un diagnostic ou un traitement. Consultez votre médecin.",
        "report_trend_locked": "L'analyse de tendance est disponible avec l'abonnement.",
        "report_domain_cardio": "Cardiovasculaire",
        "report_domain_metabolic": "Métabolique",
        "report_domain_vitamin": "Vitamine",
        "report_domain_inflammation": "Inflammation",
        "report_comparison_title": "Comparer à l'analyse précédente",
        "report_what_changed_title": "Ce qui a changé",
        "report_comparison_no_previous": "Pas encore d'analyse précédente. Après votre prochain rapport, cette section affichera la comparaison.",
        "report_what_changed_no_data": "Le résumé des changements apparaîtra après votre prochain rapport lorsque les données de comparaison seront disponibles.",
        "report_risk_factors": "Facteurs de risque",
        "report_risk_factors_line_1": "Peut indiquer des facteurs cardiovasculaires ou métaboliques. À discuter avec votre médecin.",
        "report_risk_factors_line_2": "Le mode de vie et l'alimentation peuvent favoriser le bien-être général.",
    },
    "es": {
        "title": "Informe de análisis Norya",
        "subtitle": "Informe de análisis de sangre — Interpretación con IA",
        "report_date_label": "Fecha del informe",
        "summary_heading": "Resumen",
        "biomarkers_heading": "Biomarcadores e intervalos de referencia",
        "param": "Parámetro",
        "result": "Resultado",
        "unit": "Unidad",
        "ref_range": "Intervalo de referencia",
        "status": "Estado",
        "possible_causes_heading": "Posibles causas",
        "recommendations_heading": "Recomendaciones",
        "footer_note": "Este informe fue generado por Norya. No sustituye un diagnóstico o tratamiento. Consulte a un profesional sanitario.",
        "page_footer": "Este informe es solo informativo. Consulte a un médico. — Norya",
        "emr_ehr_note": "Compatible EMR/EHR — Este informe puede cargarse en sistemas de información hospitalarios o clínicos.",
        "risk_default_attention": "Algunos valores pueden requerir atención. Véase recomendaciones y consulte a un médico si es necesario.",
        "risk_default_normal": "Todos los valores están dentro del rango de referencia. Resumen y recomendaciones a continuación.",
        "overall_status_heading": "Estado general",
        "overall_chart_title": "Estado general (0–100)",
        "overall_badge_normal": "Normal",
        "overall_badge_attention": "Límite",
        "overall_badge_high": "Riesgo",
        "overall_chart_legend": "Verde = Normal | Naranja = Límite | Rojo = De riesgo (puntuación 0–100 según el ajuste al rango de referencia)",
        "intro_heading": "Sobre este informe",
        "intro_p1": "Este informe es una interpretación preliminar de sus análisis de sangre. Incluye resumen, parámetros y recomendaciones. Es solo informativo y no sustituye un diagnóstico.",
        "intro_p2": "Consulte siempre a un profesional sanitario sobre sus resultados y decisiones médicas.",
        "how_to_read_heading": "Cómo leer los parámetros",
        "how_to_read_body": "«Resultado» muestra su valor; «Intervalo de referencia» muestra la norma. Verde = Normal, naranja = Límite, rojo = Fuera de rango. Los gráficos muestran la posición respecto a la norma.",
        "doctor_title": "Norya — Para mi médico",
        "doctor_subtitle": "Resumen de análisis — Para compartir con su médico",
        "doctor_banner_text": "Este informe fue generado por Norya para compartir con el médico. Solo informativo. Las decisiones médicas requieren evaluación del médico.",
        "doctor_page_footer": "Para compartir con el médico. Se requiere evaluación médica. — Norya",
        "doctor_footer_note": "Este informe fue generado por Norya. No sustituye diagnóstico ni tratamiento. Se requiere evaluación médica.",
        "medical_disclaimer_1": "Este informe es una evaluación preliminar asistida por IA. No sustituye un diagnóstico ni un tratamiento médico. Para decisiones sobre su salud, consulte siempre a su médico.",
        "medical_disclaimer_2": "Norya AI no es un sistema de diagnóstico médico.",
        "report_health_score_title": "Puntuación de salud general",
        "report_risk_indicator_title": "Indicador de riesgo",
        "report_trend_title": "Análisis de tendencia",
        "report_trend_need_more": "Se necesitan más análisis para la tendencia.",
        "report_upgrade": "Pasar a Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Solo informativo.",
        "report_disclaimer_text": "Este informe no sustituye el diagnóstico o tratamiento. Consulte a su médico.",
        "report_trend_locked": "El análisis de tendencias está disponible con la suscripción.",
        "report_domain_cardio": "Cardiovascular",
        "report_domain_metabolic": "Metabólico",
        "report_domain_vitamin": "Vitamina",
        "report_domain_inflammation": "Inflamación",
        "report_comparison_title": "Comparar con el análisis anterior",
        "report_what_changed_title": "Qué ha cambiado",
        "report_comparison_no_previous": "Aún no hay análisis anterior. Tras su próximo informe se mostrará aquí la comparación.",
        "report_what_changed_no_data": "El resumen de cambios aparecerá tras su próximo informe cuando haya datos de comparación.",
        "report_risk_factors": "Factores de riesgo",
        "report_risk_factors_line_1": "Puede indicar factores cardiovasculares o metabólicos. Consulte con su médico.",
        "report_risk_factors_line_2": "El estilo de vida y la dieta pueden favorecer el bienestar general.",
    },
    "it": {
        "title": "Report di analisi Norya",
        "subtitle": "Report analisi del sangue — Interpretazione con IA",
        "report_date_label": "Data del report",
        "summary_heading": "Riassunto",
        "biomarkers_heading": "Biomarcatori e intervalli di riferimento",
        "param": "Parametro",
        "result": "Risultato",
        "unit": "Unità",
        "ref_range": "Intervallo di riferimento",
        "status": "Stato",
        "possible_causes_heading": "Possibili cause",
        "recommendations_heading": "Raccomandazioni",
        "footer_note": "Questo report è stato generato da Norya. Non sostituisce diagnosi o trattamento. Consultare un medico.",
        "page_footer": "Questo report è a scopo informativo. Consultare un medico. — Norya",
        "emr_ehr_note": "Compatibile EMR/EHR — Questo report può essere caricato nei sistemi informativi ospedalieri o clinici.",
        "risk_default_attention": "Alcuni valori potrebbero richiedere attenzione. Vedi raccomandazioni e consulta un medico se necessario.",
        "risk_default_normal": "Tutti i valori sono nell'intervallo di riferimento. Riassunto e raccomandazioni sotto.",
        "overall_status_heading": "Stato generale",
        "overall_chart_title": "Stato generale (0–100)",
        "overall_badge_normal": "Normale",
        "overall_badge_attention": "Limite",
        "overall_badge_high": "Rischio",
        "overall_chart_legend": "Verde = Normale | Arancione = Limite | Rosso = A rischio (punteggio 0–100 in base all'intervallo di riferimento)",
        "intro_heading": "Informazioni su questo report",
        "intro_p1": "Questo report è un'interpretazione preliminare dei risultati delle analisi del sangue. Include riassunto, parametri e raccomandazioni. È solo informativo e non costituisce una diagnosi.",
        "intro_p2": "Consultare sempre un medico per i risultati e le decisioni mediche.",
        "how_to_read_heading": "Come leggere i parametri",
        "how_to_read_body": "«Risultato» indica il valore; «Intervallo di riferimento» indica la norma. Verde = Normale, arancione = Limite, rosso = Fuori range. I grafici mostrano la posizione rispetto alla norma.",
        "doctor_title": "Norya — Da portare al medico",
        "doctor_subtitle": "Riepilogo analisi del sangue — Da condividere con il medico",
        "doctor_banner_text": "Questo report è stato generato da Norya per la condivisione con il medico. Solo informativo. Le decisioni mediche richiedono valutazione del medico.",
        "doctor_page_footer": "Da condividere con il medico. Valutazione medica richiesta. — Norya",
        "doctor_footer_note": "Questo report è stato generato da Norya. Non sostituisce diagnosi o trattamento. Valutazione medica richiesta.",
        "medical_disclaimer_1": "Questo report è una valutazione preliminare assistita dall'IA. Non sostituisce una diagnosi o un trattamento medico. Per le decisioni sulla tua salute, consulta il tuo medico.",
        "medical_disclaimer_2": "Norya AI non è un sistema di diagnosi medica.",
        "report_health_score_title": "Punteggio salute generale",
        "report_risk_indicator_title": "Indicatore di rischio",
        "report_trend_title": "Analisi di tendenza",
        "report_trend_need_more": "Sono necessarie più analisi per la tendenza.",
        "report_upgrade": "Passa a Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Solo a scopo informativo.",
        "report_disclaimer_text": "Questo report non sostituisce diagnosi o trattamento. Consultare il medico.",
        "report_trend_locked": "L'analisi di tendenza è disponibile con l'abbonamento.",
        "report_domain_cardio": "Cardiovascolare",
        "report_domain_metabolic": "Metabolico",
        "report_domain_vitamin": "Vitamina",
        "report_domain_inflammation": "Infiammazione",
        "report_comparison_title": "Confronta con l'analisi precedente",
        "report_what_changed_title": "Cosa è cambiato",
        "report_comparison_no_previous": "Non c'è ancora un'analisi precedente. Dopo il prossimo report questa sezione mostrerà il confronto.",
        "report_what_changed_no_data": "Il riepilogo delle modifiche apparirà dopo il prossimo report quando i dati di confronto saranno disponibili.",
        "report_risk_factors": "Fattori di rischio",
        "report_risk_factors_line_1": "Può indicare fattori cardiovascolari o metabolici. Da discutere con il medico.",
        "report_risk_factors_line_2": "Stile di vita e alimentazione possono favorire il benessere generale.",
    },
    "he": {
        "title": "דוח ניתוח Norya",
        "subtitle": "דוח בדיקת דם — פרשנות מבוססת בינה מלאכותית",
        "report_date_label": "תאריך הדוח",
        "summary_heading": "סיכום",
        "biomarkers_heading": "סמנים ו טווחי ייחוס",
        "param": "פרמטר",
        "result": "תוצאה",
        "unit": "יחידה",
        "ref_range": "טווח ייחוס",
        "status": "סטטוס",
        "possible_causes_heading": "סיבות אפשריות",
        "recommendations_heading": "המלצות",
        "footer_note": "דוח זה נוצר על ידי Norya. אינו מחליף אבחנה או טיפול. יש להתייעץ עם רופא.",
        "page_footer": "דוח זה למידע בלבד. יש להתייעץ עם רופא. — Norya",
        "risk_default_attention": "ייתכן שחלק מהערכים דורשים תשומת לב. ראה המלצות והתייעץ עם רופא.",
        "risk_default_normal": "כל הערכים בטווח הייחוס. סיכום והמלצות להלן.",
        "overall_status_heading": "מצב כללי",
        "overall_chart_title": "מצב כללי (0–100)",
        "overall_badge_normal": "תקין",
        "overall_badge_attention": "גבולי",
        "overall_badge_high": "בסיכון",
        "overall_chart_legend": "ירוק = תקין | כתום = גבולי | אדום = בסיכון (ציון 0–100 על פי התאמה לטווח הייחוס)",
        "intro_heading": "אודות הדוח",
        "intro_p1": "דוח זה הוא פרשנות מקדימה מבוססת בינה מלאכותית של תוצאות בדיקת הדם. הוא כולל סיכום, ערכי פרמטרים והמלצות. הוא למטרות מידע בלבד ואינו מהווה אבחנה.",
        "intro_p2": "יש לדון בתוצאות עם רופא. יש להתייעץ עם רופא לגבי החלטות רפואיות.",
        "how_to_read_heading": "כיצד לקרוא את הפרמטרים",
        "how_to_read_body": "„תוצאה“ מציגה את הערך; „טווח ייחוס“ מציג את הנורמה. ירוק = תקין, כתום = גבולי, אדום = מחוץ לטווח. הגרפים מציגים את מיקום הערך ביחס לטווח.",
        "doctor_title": "Norya — להראות לרופא",
        "doctor_subtitle": "סיכום בדיקת דם — להעברה לרופא",
        "doctor_banner_text": "דוח זה נוצר על ידי Norya לשיתוף עם הרופא. למידע בלבד. החלטות רפואיות דורשות הערכת רופא.",
        "doctor_page_footer": "להעברה לרופא. נדרשת הערכת רופא. — Norya",
        "doctor_footer_note": "דוח זה נוצר על ידי Norya. אינו מחליף אבחנה או טיפול. נדרשת הערכת רופא.",
        "medical_disclaimer_1": "דוח זה הוא הערכה מקדימה המבוססת על בינה מלאכותית. הוא אינו מחליף אבחנה או טיפול רפואי. להחלטות לגבי בריאותך, התייעץ עם הרופא שלך.",
        "medical_disclaimer_2": "Norya AI אינו מערכת לאבחון רפואי.",
        "report_health_score_title": "ציון בריאות כללי",
        "report_risk_indicator_title": "מדד סיכון",
        "report_trend_title": "ניתוח מגמה",
        "report_trend_need_more": "נדרשות בדיקות נוספות למגמה.",
        "report_upgrade": "שדרוג לפרימיום",
        "report_premium_badge": "פרימיום",
        "report_disclaimer_title": "למטרות מידע בלבד.",
        "report_disclaimer_text": "דוח זה אינו מחליף אבחנה או טיפול. יש להתייעץ עם רופא.",
        "report_trend_locked": "ניתוח מגמה זמין במנוי.",
        "report_domain_cardio": "קרדיווסקולרי",
        "report_domain_metabolic": "מטבולי",
        "report_domain_vitamin": "ויטמין",
        "report_domain_inflammation": "דלקת",
        "report_comparison_title": "השוואה לניתוח הקודם",
        "report_what_changed_title": "מה השתנה?",
        "report_comparison_no_previous": "עדיין אין ניתוח קודם. לאחר הדוח הבא יוצג כאן ההשוואה.",
        "report_what_changed_no_data": "סיכום השינויים יופיע לאחר הדוח הבא כאשר נתוני ההשוואה זמינים.",
        "report_risk_factors": "גורמי סיכון",
        "report_risk_factors_line_1": "עלול להצביע על גורמי סיכון קרדיווסקולריים או מטבוליים. יש להתייעץ עם הרופא.",
        "report_risk_factors_line_2": "אורח חיים ותזונה יכולים לתמוך בבריאות הכללית.",
    },
    "ar": {
        "title": "تقرير تحليل Norya",
        "subtitle": "تقرير تحليل الدم — تفسير بالذكاء الاصطناعي",
        "report_date_label": "تاريخ التقرير",
        "summary_heading": "ملخص",
        "biomarkers_heading": "العلامات الحيوية ونطاقات المرجع",
        "param": "المعامل",
        "result": "النتيجة",
        "unit": "الوحدة",
        "ref_range": "النطاق المرجعي",
        "status": "الحالة",
        "possible_causes_heading": "الأسباب المحتملة",
        "recommendations_heading": "التوصيات",
        "footer_note": "تم إنشاء هذا التقرير بواسطة Norya. لا يحل محل التشخيص أو العلاج. استشر طبيباً.",
        "page_footer": "هذا التقرير للمعلومات فقط. استشر طبيباً. — Norya",
        "risk_default_attention": "قد تتطلب بعض القيم الانتباه. راجع التوصيات واستشر طبيباً إذا لزم الأمر.",
        "risk_default_normal": "جميع القيم ضمن النطاق المرجعي. الملخص والتوصيات أدناه.",
        "overall_status_heading": "الحالة العامة",
        "overall_chart_title": "الحالة العامة (0–100)",
        "overall_badge_normal": "طبيعي",
        "overall_badge_attention": "حدي",
        "overall_badge_high": "معرض للخطر",
        "overall_chart_legend": "أخضر = طبيعي | برتقالي = حدي | أحمر = خطِر (درجة 0–100 حسب التوافق مع النطاق المرجعي)",
        "intro_heading": "حول هذا التقرير",
        "intro_p1": "هذا التقرير تفسير أولي بمساعدة الذكاء الاصطناعي لنتائج تحليل الدم. يتضمن ملخصاً والقيم والتوصيات. إنه للمعلومات فقط ولا يشكل تشخيصاً.",
        "intro_p2": "استشر طبيباً دائماً بشأن نتائجك والقرارات الطبية.",
        "how_to_read_heading": "كيف تقرأ المعاملات",
        "how_to_read_body": "«النتيجة» تعرض قيمتك؛ «النطاق المرجعي» يعرض المعيار. أخضر = طبيعي، برتقالي = حدي، أحمر = خارج النطاق. الرسوم توضح موقع القيمة بالنسبة للنطاق.",
        "doctor_title": "Norya — للمشاركة مع الطبيب",
        "doctor_subtitle": "ملخص تحليل الدم — للإرسال إلى الطبيب",
        "doctor_banner_text": "تم إنشاء هذا التقرير بواسطة Norya لمشاركته مع الطبيب. للمعلومات فقط. القرارات الطبية تتطلب تقييم الطبيب.",
        "doctor_page_footer": "للإرسال إلى الطبيب. تقييم الطبيب مطلوب. — Norya",
        "doctor_footer_note": "تم إنشاء هذا التقرير بواسطة Norya. لا يحل محل التشخيص أو العلاج. تقييم الطبيب مطلوب.",
        "medical_disclaimer_1": "هذا التقرير تقييم أولي بمساعدة الذكاء الاصطناعي. لا يحل محل التشخيص أو العلاج الطبي. لاتخاذ قرارات تتعلق بصحتك، استشر طبيبك.",
        "medical_disclaimer_2": "Norya AI ليست نظاماً للتشخيص الطبي.",
        "report_health_score_title": "درجة الصحة العامة",
        "report_risk_indicator_title": "مؤشر المخاطر",
        "report_trend_title": "تحليل الاتجاه",
        "report_trend_need_more": "المزيد من التحليلات مطلوبة للاتجاه.",
        "report_upgrade": "الترقية إلى بريميوم",
        "report_premium_badge": "بريميوم",
        "report_disclaimer_title": "للمعلومات فقط.",
        "report_disclaimer_text": "هذا التقرير لا يحل محل التشخيص أو العلاج. استشر طبيبك.",
        "report_trend_locked": "تحليل الاتجاه متاح مع الاشتراك.",
        "report_domain_cardio": "قلبي وعائي",
        "report_domain_metabolic": "أيضي",
        "report_domain_vitamin": "فيتامين",
        "report_domain_inflammation": "التهاب",
        "report_comparison_title": "المقارنة مع التحليل السابق",
        "report_what_changed_title": "ما الذي تغيّر؟",
        "report_comparison_no_previous": "لا يوجد تحليل سابق بعد. بعد تقريرك التالي ستُعرض المقارنة في هذا القسم.",
        "report_what_changed_no_data": "ملخص التغيّر سيظهر بعد تقريرك التالي عندما تتوفر بيانات المقارنة.",
        "report_risk_factors": "عوامل الخطر",
        "report_risk_factors_line_1": "قد يشير إلى عوامل قلبية أو استقلابية. ناقش مع طبيبك.",
        "report_risk_factors_line_2": "نمط الحياة والنظام الغذائي قد يدعمان الصحة العامة.",
    },
    "hi": {
        "title": "Norya विश्लेषण रिपोर्ट",
        "subtitle": "रक्त परीक्षण विश्लेषण रिपोर्ट — AI-सहायक व्याख्या",
        "report_date_label": "रिपोर्ट तारीख",
        "summary_heading": "सारांश",
        "biomarkers_heading": "बायोमार्कर और संदर्भ सीमा",
        "param": "पैरामीटर",
        "result": "परिणाम",
        "unit": "इकाई",
        "ref_range": "संदर्भ सीमा",
        "status": "स्थिति",
        "possible_causes_heading": "संभावित कारण",
        "recommendations_heading": "सिफारिशें",
        "footer_note": "यह रिपोर्ट Norya द्वारा जनित है। यह निदान या उपचार का विकल्प नहीं है। चिकित्सक से परामर्श लें।",
        "page_footer": "यह रिपोर्ट केवल सूचना के लिए है। चिकित्सक से परामर्श करें। — Norya",
        "risk_default_attention": "कुछ मानों पर ध्यान देना पड़ सकता है। सिफारिशें देखें और चिकित्सक से परामर्श करें।",
        "risk_default_normal": "सभी मान संदर्भ सीमा में हैं। सारांश और सिफारिशें नीचे।",
        "overall_status_heading": "कुल स्थिति",
        "overall_chart_title": "कुल स्थिति (0–100)",
        "overall_badge_normal": "सामान्य",
        "overall_badge_attention": "सीमावर्ती",
        "overall_badge_high": "जोखिम",
        "overall_chart_legend": "हरा = सामान्य | नारंगी = सीमावर्ती | लाल = जोखिम (स्कोर 0–100, संदर्भ सीमा के अनुरूपता के अनुसार)",
        "intro_heading": "इस रिपोर्ट के बारे में",
        "intro_p1": "यह रिपोर्ट रक्त परीक्षण परिणामों की AI-सहायक प्रारंभिक व्याख्या है। इसमें सारांश, पैरामीटर और सिफारिशें हैं। यह केवल सूचनार्थ है और निदान नहीं है।",
        "intro_p2": "अपने परिणाम और चिकित्सा निर्णय के लिए हमेशा चिकित्सक से परामर्श लें।",
        "how_to_read_heading": "पैरामीटर कैसे पढ़ें",
        "how_to_read_body": "«परिणाम» आपका मान दिखाता है; «संदर्भ सीमा» मानक दिखाती है। हरा = सामान्य, नारंगी = सीमा, लाल = सीमा के बाहर। ग्राफ़ मान की स्थिति दिखाते हैं।",
        "doctor_title": "Norya — डॉक्टर को दिखाने के लिए",
        "doctor_subtitle": "रक्त परीक्षण सारांश — डॉक्टर के साथ साझा करने के लिए",
        "doctor_banner_text": "यह रिपोर्ट Norya द्वारा डॉक्टर के साथ साझा करने के लिए बनाई गई। केवल सूचना के लिए। चिकित्सा निर्णय के लिए चिकित्सक मूल्यांकन आवश्यक।",
        "doctor_page_footer": "डॉक्टर के साथ साझा करने के लिए। चिकित्सक मूल्यांकन आवश्यक। — Norya",
        "doctor_footer_note": "यह रिपोर्ट Norya द्वारा बनाई गई। निदान या उपचार का विकल्प नहीं। चिकित्सक मूल्यांकन आवश्यक।",
        "medical_disclaimer_1": "यह रिपोर्ट AI-सहायक प्रारंभिक मूल्यांकन है। यह किसी भी चिकित्सीय निदान या उपचार का स्थानापन्न नहीं है। अपने स्वास्थ्य से जुड़े निर्णयों के लिए हमेशा अपने डॉक्टर से परामर्श करें।",
        "medical_disclaimer_2": "Norya AI कोई चिकित्सीय निदान प्रणाली नहीं है।",
        "report_health_score_title": "समग्र स्वास्थ्य स्कोर",
        "report_risk_indicator_title": "जोखिम संकेतक",
        "report_trend_title": "ट्रेंड विश्लेषण",
        "report_trend_need_more": "ट्रेंड के लिए और विश्लेषण आवश्यक।",
        "report_upgrade": "प्रीमियम में अपग्रेड करें",
        "report_premium_badge": "प्रीमियम",
        "report_disclaimer_title": "केवल सूचना के लिए।",
        "report_disclaimer_text": "यह रिपोर्ट निदान या उपचार का विकल्प नहीं है। डॉक्टर से सलाह लें।",
        "report_trend_locked": "ट्रेंड विश्लेषण सदस्यता के साथ उपलब्ध है।",
        "report_domain_cardio": "हृदय संबंधी",
        "report_domain_metabolic": "चयापचय",
        "report_domain_vitamin": "विटामिन",
        "report_domain_inflammation": "सूजन",
        "report_comparison_title": "पिछले विश्लेषण से तुलना",
        "report_what_changed_title": "क्या बदला?",
        "report_comparison_no_previous": "अभी कोई पिछला विश्लेषण नहीं। अगली रिपोर्ट के बाद यह सेक्शन तुलना दिखाएगा।",
        "report_what_changed_no_data": "बदलाव सारांश आपकी अगली रिपोर्ट के बाद दिखेगा जब तुलना डेटा उपलब्ध हो।",
        "report_risk_factors": "जोखिम कारक",
        "report_risk_factors_line_1": "हृदय या चयापचय कारकों की ओर इशारा कर सकता है। चिकित्सक से चर्चा करें।",
        "report_risk_factors_line_2": "जीवनशैली और आहार समग्र सेहत को सहायता दे सकते हैं।",
    },
    "el": {
        "title": "Αναφορά ανάλυσης Norya",
        "subtitle": "Αναφορά αίματος — Ερμηνεία με AI",
        "report_date_label": "Ημερομηνία αναφοράς",
        "summary_heading": "Περίληψη",
        "biomarkers_heading": "Βιοδείκτες και εύρη αναφοράς",
        "param": "Παράμετρος",
        "result": "Αποτέλεσμα",
        "unit": "Μονάδα",
        "ref_range": "Εύρος αναφοράς",
        "status": "Κατάσταση",
        "possible_causes_heading": "Πιθανές αιτίες",
        "recommendations_heading": "Συστάσεις",
        "footer_note": "Αυτή η αναφορά δημιουργήθηκε από το Norya. Δεν αντικαθιστά διάγνωση ή θεραπεία. Συμβουλευτείτε γιατρό.",
        "page_footer": "Αυτή η αναφορά είναι μόνο για πληροφόρηση. Συμβουλευτείτε γιατρό. — Norya",
        "risk_default_attention": "Ορισμένες τιμές μπορεί να απαιτούν προσοχή. Δείτε συστάσεις και συμβουλευτείτε γιατρό.",
        "risk_default_normal": "Όλες οι τιμές εντός εύρους αναφοράς. Περίληψη και συστάσεις παρακάτω.",
        "overall_status_heading": "Γενική κατάσταση",
        "overall_chart_title": "Γενική κατάσταση (0–100)",
        "overall_badge_normal": "Φυσιολογικό",
        "overall_badge_attention": "Οριακό",
        "overall_badge_high": "Κίνδυνος",
        "overall_chart_legend": "Πράσινο = Φυσιολογικό | Πορτοκαλί = Οριακό | Κόκκινο = Επικίνδυνο (σκορ 0–100 ανάλογα με το εύρος αναφοράς)",
        "intro_heading": "Σχετικά με αυτή την αναφορά",
        "intro_p1": "Αυτή η αναφορά είναι προκαταρκτική ερμηνεία με AI των αποτελεσμάτων αίματος. Περιλαμβάνει περίληψη, παραμέτρους και συστάσεις. Είναι μόνο για πληροφόρηση και δεν αντικαθιστά διάγνωση.",
        "intro_p2": "Συμβουλευτείτε πάντα γιατρό για τα αποτελέσματα και τις ιατρικές αποφάσεις.",
        "how_to_read_heading": "Πώς να διαβάσετε τις παραμέτρους",
        "how_to_read_body": "«Αποτέλεσμα» δείχνει την τιμή· «Εύρος αναφοράς» δείχνει το κανονικό. Πράσινο = Φυσιολογικό, πορτοκαλί = Οριακό, κόκκινο = Εκτός εύρους. Τα γραφήματα δείχνουν τη θέση της τιμής.",
        "doctor_title": "Norya — Για τον γιατρό μου",
        "doctor_subtitle": "Σύνοψη αίματος — Για κοινοποίηση στον γιατρό",
        "doctor_banner_text": "Αυτή η αναφορά δημιουργήθηκε από το Norya για κοινοποίηση με τον γιατρό. Μόνο για πληροφόρηση. Οι ιατρικές αποφάσεις απαιτούν αξιολόγηση από γιατρό.",
        "doctor_page_footer": "Για κοινοποίηση στον γιατρό. Απαιτείται αξιολόγηση από γιατρό. — Norya",
        "doctor_footer_note": "Αυτή η αναφορά δημιουργήθηκε από το Norya. Δεν αντικαθιστά διάγνωση ή θεραπεία. Απαιτείται αξιολόγηση από γιατρό.",
        "medical_disclaimer_1": "Αυτή η αναφορά είναι προκαταρκτική εκτίμηση με τη βοήθεια AI. Δεν αντικαθιστά ιατρική διάγνωση ή θεραπεία. Για αποφάσεις σχετικά με την υγεία σας, συμβουλευτείτε τον γιατρό σας.",
        "medical_disclaimer_2": "Το Norya AI δεν είναι σύστημα ιατρικής διάγνωσης.",
        "report_health_score_title": "Γενική βαθμολογία υγείας",
        "report_risk_indicator_title": "Δείκτης κινδύνου",
        "report_trend_title": "Ανάλυση τάσης",
        "report_trend_need_more": "Απαιτούνται περισσότερες αναλύσεις για την τάση.",
        "report_upgrade": "Αναβάθμιση σε Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Μόνο για ενημέρωση.",
        "report_disclaimer_text": "Αυτή η αναφορά δεν αντικαθιστά τη διάγνωση ή τη θεραπεία. Συμβουλευτείτε το γιατρό σας.",
        "report_trend_locked": "Η ανάλυση τάσης διατίθεται με συνδρομή.",
        "report_domain_cardio": "Καρδιαγγειακό",
        "report_domain_metabolic": "Μεταβολικό",
        "report_domain_vitamin": "Βιταμίνη",
        "report_domain_inflammation": "Φλεγμονή",
    },
    "cs": {
        "title": "Norya zpráva z analýzy",
        "subtitle": "Zpráva z krevního testu — Interpretace s AI",
        "report_date_label": "Datum zprávy",
        "summary_heading": "Shrnutí",
        "biomarkers_heading": "Biomarkery a referenční rozsahy",
        "param": "Parametr",
        "result": "Výsledek",
        "unit": "Jednotka",
        "ref_range": "Referenční rozsah",
        "status": "Stav",
        "possible_causes_heading": "Možné příčiny",
        "recommendations_heading": "Doporučení",
        "footer_note": "Tuto zprávu vygeneroval Norya. Nenahrazuje diagnózu ani léčbu. Konzultujte lékaře.",
        "page_footer": "Tato zpráva je pouze informativní. Konzultujte lékaře. — Norya",
        "risk_default_attention": "Některé hodnoty mohou vyžadovat pozornost. Viz doporučení a konzultujte lékaře.",
        "risk_default_normal": "Všechny hodnoty v referenčním rozsahu. Shrnutí a doporučení níže.",
        "overall_status_heading": "Celkový stav",
        "overall_chart_title": "Celkový stav (0–100)",
        "overall_badge_normal": "Normální",
        "overall_badge_attention": "Hraniční",
        "overall_badge_high": "Rizikové",
        "overall_chart_legend": "Zelená = Normální | Oranžová = Hraniční | Červená = Rizikové (skóre 0–100 podle souladu s referenčním rozsahem)",
        "intro_heading": "O této zprávě",
        "intro_p1": "Tato zpráva je předběžné AI vyhodnocení výsledků krevních testů. Obsahuje shrnutí, parametry a doporučení. Je pouze informativní a nenahrazuje diagnózu.",
        "intro_p2": "Vždy konzultujte s lékařem své výsledky a lékařská rozhodnutí.",
        "how_to_read_heading": "Jak číst parametry",
        "how_to_read_body": "„Výsledek“ ukazuje vaši hodnotu; „Referenční rozsah“ ukazuje normu. Zelená = Normální, oranžová = Mezní, červená = Mimo rozsah. Grafy ukazují polohu hodnoty.",
        "doctor_title": "Norya — K lékaři",
        "doctor_subtitle": "Shrnutí krevního testu — Pro sdílení s lékařem",
        "doctor_banner_text": "Tuto zprávu vygeneroval Norya pro sdílení s lékařem. Pouze informativní. Lékařská rozhodnutí vyžadují posouzení lékařem.",
        "doctor_page_footer": "Pro sdílení s lékařem. Vyžaduje se posouzení lékařem. — Norya",
        "doctor_footer_note": "Tuto zprávu vygeneroval Norya. Nenahrazuje diagnózu ani léčbu. Vyžaduje se posouzení lékařem.",
        "medical_disclaimer_1": "Tato zpráva je předběžné vyhodnocení s pomocí AI. Nenahrazuje lékařskou diagnózu ani léčbu. Pro rozhodnutí o svém zdraví se poraďte se svým lékařem.",
        "medical_disclaimer_2": "Norya AI není systém lékařské diagnostiky.",
        "report_health_score_title": "Celkové skóre zdraví",
        "report_risk_indicator_title": "Ukazatel rizika",
        "report_trend_title": "Trendová analýza",
        "report_trend_need_more": "Pro trend je zapotřebí více analýz.",
        "report_upgrade": "Přejít na Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Pouze pro informaci.",
        "report_disclaimer_text": "Tato zpráva nenahrazuje diagnózu ani léčbu. Konzultujte s lékařem.",
        "report_trend_locked": "Analýza trendu je k dispozici s předplatným.",
        "report_domain_cardio": "Kardiovaskulární",
        "report_domain_metabolic": "Metabolický",
        "report_domain_vitamin": "Vitamin",
        "report_domain_inflammation": "Zánět",
    },
    "sr": {
        "title": "Norya izveštaj analize",
        "subtitle": "Izveštaj krvne analize — AI tumačenje",
        "report_date_label": "Datum izveštaja",
        "summary_heading": "Rezime",
        "biomarkers_heading": "Biomarkeri i referentni opsezi",
        "param": "Parametar",
        "result": "Rezultat",
        "unit": "Jedinica",
        "ref_range": "Referentni opseg",
        "status": "Status",
        "possible_causes_heading": "Mogući uzroci",
        "recommendations_heading": "Preporuke",
        "footer_note": "Ovaj izveštaj je generisao Norya. Ne zamenjuje dijagnozu ili lečenje. Konsultujte lekara.",
        "page_footer": "Ovaj izveštaj je samo informativan. Konsultujte lekara. — Norya",
        "risk_default_attention": "Neke vrednosti mogu zahtevati pažnju. Pogledajte preporuke i konsultujte lekara.",
        "risk_default_normal": "Sve vrednosti u referentnom opsegu. Rezime i preporuke ispod.",
        "overall_status_heading": "Opšte stanje",
        "overall_chart_title": "Opšte stanje (0–100)",
        "overall_badge_normal": "Normalno",
        "overall_badge_attention": "Granično",
        "overall_badge_high": "Rizično",
        "overall_chart_legend": "Zeleno = Normalno | Narandžasto = Granično | Crveno = Rizično (skor 0–100 u odnosu na referentni opseg)",
        "intro_heading": "O ovom izveštaju",
        "intro_p1": "Ovaj izveštaj je AI tumačenje rezultata krvne analize. Uključuje rezime, parametre i preporuke. Samo je informativan i ne zamenjuje dijagnozu.",
        "intro_p2": "Uvek konsultujte lekara za rezultate i medicinske odluke.",
        "how_to_read_heading": "Kako čitati parametre",
        "how_to_read_body": "„Rezultat“ pokazuje vašu vrednost; „Referentni opseg“ pokazuje normu. Zeleno = Normalno, narandžasto = Granično, crveno = Van opsega. Grafici pokazuju položaj vrednosti.",
        "doctor_title": "Norya — Za lekara",
        "doctor_subtitle": "Rezime krvne analize — Za deljenje sa lekarom",
        "doctor_banner_text": "Ovaj izveštaj je generisao Norya za deljenje sa lekarom. Samo informativno. Medicinske odluke zahtevaju procenu lekara.",
        "doctor_page_footer": "Za deljenje sa lekarom. Potrebna procena lekara. — Norya",
        "doctor_footer_note": "Ovaj izveštaj je generisao Norya. Ne zamenjuje dijagnozu ili lečenje. Potrebna procena lekara.",
        "medical_disclaimer_1": "Ovaj izveštaj je preliminarna procena uz pomoć AI. Ne zamenjuje medicinsku dijagnozu ili lečenje. Za odluke o svom zdravlju konsultujte lekara.",
        "medical_disclaimer_2": "Norya AI nije sistem za medicinsku dijagnostiku.",
        "report_health_score_title": "Opšte zdravstveno stanje",
        "report_risk_indicator_title": "Pokazatelj rizika",
        "report_trend_title": "Analiza trenda",
        "report_trend_need_more": "Potrebne su dodatne analize za trend.",
        "report_upgrade": "Nadogradnja na Premium",
        "report_premium_badge": "Premium",
        "report_disclaimer_title": "Samo u informativne svrhe.",
        "report_disclaimer_text": "Ovaj izveštaj ne zamenjuje dijagnozu ili lečenje. Posavetujte se sa lekarom.",
        "report_trend_locked": "Analiza trenda dostupna je uz pretplatu.",
        "report_domain_cardio": "Kardiovaskularni",
        "report_domain_metabolic": "Metabolički",
        "report_domain_vitamin": "Vitamin",
        "report_domain_inflammation": "Upala",
    },
}


def _pdf_labels(lang: str) -> dict[str, str]:
    """Rapor diline göre PDF etiketleri; bilinmeyen dil için İngilizce."""
    return PDF_LABELS.get(lang, PDF_LABELS.get("en", PDF_LABELS["tr"]))


def _strip_ai_from_text(text: str) -> str:
    """PDF'de AI/yapay zeka/model kelimeleri görünmesin (bilgilendirme amaçlı metin)."""
    if not text or not text.strip():
        return text
    patterns = [
        r"\bAI\b",
        r"\bA\.I\.\b",
        r"\byapay\s+zeka\b",
        r"\byapay\s+zekâ\b",
        r"\bYapay\s+[Zz]eka\b",
        r"\bmodel\s+(ile|tarafından|destekli)\b",
        r"\bAI[- ]assisted\b",
        r"\bAI[- ]destekli\b",
        r"\bartificial\s+intelligence\b",
    ]
    out = text
    for p in patterns:
        out = re.sub(p, " ", out, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", out).strip()


# Bölüm başlıkları (Türkçe / İngilizce / yaygın varyantlar)
SECTION_PATTERNS = [
    (r"\*\*Summary\*\*", "summary"),
    (r"\*\*Özet\*\*", "summary"),
    (r"\*\*Risk indicators?\*\*", "risk_indicators"),
    (r"\*\*Dikkat edilmesi gerekenler\*\*", "risk_indicators"),
    (r"\*\*Values?\*\*", "values"),
    (r"\*\*Değerler\*\*", "values"),
    (r"\*\*Parametreler\*\*", "values"),
    (r"\*\*Test sonuçları?\*\*", "values"),
    (r"\*\*Sonuçlar\*\*", "values"),
    (r"\*\*Lab results?\*\*", "values"),
    (r"\*\*Laboratuvar sonuçları?\*\*", "values"),
    (r"\*\*Laboratory results?\*\*", "values"),
    (r"\*\*Kan değerleri\*\*", "values"),
    (r"\*\*Blood (test )?results?\*\*", "values"),
    (r"\*\*Possible causes?\*\*", "possible_causes"),
    (r"\*\*Olası nedenler\*\*", "possible_causes"),
    (r"\*\*Recommendations?\*\*", "recommendations"),
    (r"\*\*Öneriler\*\*", "recommendations"),
]

# Values bloğundaki satır: **Parametre adı:** değer birim. Reference: ... Normal/Low/High (sonunda nokta olabilir)
BIOMARKER_LINE = re.compile(
    r"\*\*([^*]+)\*?\s*:\s*([^\n]+?)\s*\.\s*"
    r"(?:Reference:\s*([^\n]+?)\s*\.\s*)?"
    r"(Normal|Low|High|Borderline|Düşük|Yüksek|Sınırda|Sınır)\s*\.?\s*$",
    re.IGNORECASE,
)
# Daha esnek: Reference ve/veya status ayrı satırda veya noktasız olabilir
BIOMARKER_LINE_RELAXED = re.compile(
    r"\*\*([^*]+)\*?\s*:\s*([^\n]+?)(?:\s*\.\s*)?"
    r"(?:\s*Reference:\s*([^\n]+?)(?:\s*\.\s*)?)?"
    r"(?:\s+(Normal|Low|High|Borderline|Düşük|Yüksek|Sınırda|Sınır))?\s*$",
    re.IGNORECASE,
)


def _is_section_header(line: str) -> bool:
    """Satır sadece bölüm başlığı mı (Summary, Risk, Values, Diyet, Takviye, Kalp, ...) kontrol et.
    **Parametre adı:** değer. Reference: ... Normal. gibi Values içindeki satırları bölüm başlığı sayma."""
    if not line or not line.strip().startswith("**"):
        return False
    stripped = line.strip()
    match = re.match(r"^\*\*([^*]+)\*\*\s*:?\s*(.*)$", stripped)
    if not match:
        return False
    title, rest = match.group(1).strip(), (match.group(2) or "").strip()
    # Values bölümündeki parametre satırı: "14.2 g/dL. Reference: 12-16 g/dL. Normal" — bölüm başlığı DEĞİL
    if re.search(r"Reference\s*:\s*|Ref\s*:\s*", rest, re.IGNORECASE) or re.search(
        r"\b(Normal|Low|High|Borderline|Düşük|Yüksek|Sınırda|Sınır)\s*\.?\s*$", rest, re.IGNORECASE
    ):
        return False
    known = (
        "summary", "özet", "risk indicators", "risk indicator", "dikkat edilmesi gerekenler",
        "values", "value", "değerler", "parametreler", "possible causes", "possible cause",
        "olası nedenler", "recommendations", "recommendation", "öneriler",
        "diet plan", "diyet planı", "plan alimentaire", "supplement", "takviye", "heart", "kalp",
    )
    if title.lower() in known:
        return True
    if any(k in title.lower() for k in ("summary", "özet", "risk", "dikkat", "value", "değer", "parametre", "cause", "neden", "recommendation", "öneri", "diet", "diyet", "supplement", "takviye", "heart", "kalp", "alimentaire")):
        return len(rest) < 120
    # Diyet, Takviye, Kalp gibi kısa başlıklar (parametre satırı değilse)
    if len(rest) < 120:
        return True
    return False


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Metni **Bölüm başlığı** bloklarına göre böl; (başlık, içerik) listesi döndür."""
    if not (text or text.strip()):
        return []
    lines = text.split("\n")
    result: list[tuple[str, str]] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in lines:
        if _is_section_header(line):
            if current_title is not None:
                result.append((current_title, "\n".join(current_body).strip()))
            match = re.match(r"^\s*\*\*([^*]+)\*\*\s*:?\s*(.*)$", line.strip())
            if match:
                current_title = match.group(1).strip()
                rest = (match.group(2) or "").strip()
                current_body = [rest] if rest else []
            else:
                current_title = re.sub(r"^\*\*|\*\*\s*:?\s*$", "", line.strip()).strip()
                current_body = []
        else:
            if current_title is not None:
                current_body.append(line)
    if current_title is not None:
        result.append((current_title, "\n".join(current_body).strip()))
    return result


def _map_section_key(title: str) -> str | None:
    """Bölüm başlığını summary/risk_indicators/values/possible_causes/recommendations ile eşle."""
    title_lower = title.strip().lower()
    for pattern, key in SECTION_PATTERNS:
        if re.search(pattern, title, re.IGNORECASE):
            return key
    if "summary" in title_lower or "özet" in title_lower:
        return "summary"
    if "risk" in title_lower or "dikkat" in title_lower:
        return "risk_indicators"
    if any(x in title_lower for x in ("value", "değer", "parametre", "sonuç", "result", "lab", "laboratuvar", "test sonuç", "kan değer")):
        return "values"
    if "cause" in title_lower or "neden" in title_lower:
        return "possible_causes"
    if "recommendation" in title_lower or "öneri" in title_lower:
        return "recommendations"
    return None


def _normalize_status(s: str) -> str:
    """Normal/Low/High/Borderline → normal, low, high, border."""
    if not s:
        return "normal"
    s = s.strip().lower()
    if s in ("normal", "normale"):
        return "normal"
    if s in ("low", "düşük", "basso", "baja"):
        return "low"
    if s in ("high", "yüksek", "alto", "alta"):
        return "high"
    if "border" in s or "sınır" in s:
        return "border"
    return "normal"


def _status_label(status: str) -> str:
    """Web raporu ile aynı: Normal / Sınır / Riskli (grafik ve tablo için)."""
    tr = {"normal": "Normal", "low": "Riskli", "high": "Riskli", "border": "Sınır"}
    return tr.get(status, status)


def _split_value_unit(raw: str) -> tuple[str, str | None]:
    """Örn. '14.2 g/dL' -> ('14.2', 'g/dL'); '120' -> ('120', None)."""
    raw = (raw or "").strip()
    if not raw:
        return ("—", None)
    parts = raw.split(None, 1)
    value = parts[0] if parts else "—"
    unit = parts[1] if len(parts) > 1 else None
    return (value, unit)


# Referans metninden min-max sayıları: "12-16 g/dL", "0.27-4.2 mIU/L" -> (12, 16) veya (0.27, 4.2)
_REF_NUMBERS = re.compile(r"(\d+(?:[.,]\d+)?)")


def _parse_reference_range(reference: str | None) -> tuple[float, float] | None:
    """Referans aralığı string'inden (ref_min, ref_max) döndürür."""
    if not reference or not reference.strip():
        return None
    numbers = _REF_NUMBERS.findall(reference.strip().replace(",", "."))
    if len(numbers) < 2:
        return None
    try:
        low = float(numbers[0])
        high = float(numbers[1])
        if low > high:
            low, high = high, low
        return (low, high)
    except ValueError:
        return None


def _value_to_float(value_str: str) -> float | None:
    """Gösterim değerini sayıya çevirir: '14.2', '<5', '>20' -> float veya None."""
    if not value_str or value_str == "—":
        return None
    s = (value_str.strip().replace(",", ".").replace(" ", "")
         .lstrip("<>≤≥"))
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _enrich_biomarker_chart(row: dict) -> None:
    """Biomarker satırına chart_svg_base64 ekler: referans varsa range bar, yoksa basit değer çubuğu (tüm sonuçlara grafik)."""
    ref = _parse_reference_range(row.get("reference"))
    value_float = _value_to_float(row.get("value") or "")
    if value_float is None:
        row["chart_svg_base64"] = None
        row["display_min"] = None
        row["display_max"] = None
        return
    status = row.get("status") or "normal"
    status_label = row.get("status_label")
    if ref is not None:
        ref_min, ref_max = ref
        if ref_max > ref_min:
            span = ref_max - ref_min
            padding = max(span * 0.3, span * 0.1) if span > 0 else 1.0
            display_min = min(ref_min, value_float) - padding
            display_max = max(ref_max, value_float) + padding
            b64 = range_bar_svg_base64(
                name=row["name"],
                value=value_float,
                unit=row.get("unit") or "",
                ref_min=ref_min,
                ref_max=ref_max,
                status=status,
                display_min=display_min,
                display_max=display_max,
                status_label=status_label,
            )
            row["chart_svg_base64"] = b64
            row["display_min"] = display_min
            row["display_max"] = display_max
            return
    b64 = simple_value_bar_svg_base64(
        name=row["name"],
        value=value_float,
        unit=row.get("unit") or "",
        status=status,
        status_label=status_label,
    )
    row["chart_svg_base64"] = b64
    row["display_min"] = None
    row["display_max"] = None


def parse_biomarkers(values_block: str) -> list[dict]:
    """Values bölümünden parametre satırlarını parse et. Tüm **Parametre:** değer satırları ve benzeri formatlar alınır."""
    rows: list[dict] = []
    seen_names: set[str] = set()
    for raw_line in (values_block or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # Madde işareti veya tire ile başlayan satırları da oku ( - **LDL**: ... veya • **LDL**: ... )
        if line.startswith("-") or line.startswith("•") or line.startswith("*"):
            line = line.lstrip("-•*").strip()
        if not line:
            continue
        # Önce **Parametre:** değer. Reference: ... Normal/Low/High formatı
        m = BIOMARKER_LINE.search(line) or BIOMARKER_LINE_RELAXED.search(line)
        if m:
            name = m.group(1).strip()
            value_str = (m.group(2) or "").strip()
            if value_str.startswith("**"):
                value_str = value_str.lstrip("*").strip()
            reference = (m.group(3) or "").strip() or None
            status = _normalize_status(m.group(4) or "")
            value, unit = _split_value_unit(value_str)
            key = name.lower()
            if key not in seen_names:
                seen_names.add(key)
                rows.append({
                    "name": name,
                    "value": value,
                    "unit": unit,
                    "reference": reference,
                    "status": status,
                    "status_label": _status_label(status),
                })
            continue
        # **Parametre:** değer (reference/status yok)
        simple = re.match(r"\*\*([^*]+)\*?\s*:\s*(.+)", line)
        if simple:
            name = simple.group(1).strip()
            value, unit = _split_value_unit(simple.group(2))
            key = name.lower()
            if key not in seen_names:
                seen_names.add(key)
                rows.append({
                    "name": name,
                    "value": value,
                    "unit": unit,
                    "reference": None,
                    "status": "normal",
                    "status_label": "—",
                })
            continue
        # Parametre adı: değer birim (yıldızsız satır; Reference: veya Normal/Düşük/Yüksek varsa status çıkar)
        plain = re.match(r"^([A-Za-z0-9ığüşöçİĞÜŞÖÇ\s\-/]+)\s*:\s*(.+)", line)
        if plain:
            name = plain.group(1).strip()
            if len(name) < 2 or len(name) > 80:
                continue
            rest = plain.group(2).strip()
            ref_match = re.search(r"\b(?:Reference|Ref\.?)\s*:\s*([^.]+?)(?:\.\s*(Normal|Low|High|Borderline|Düşük|Yüksek|Sınırda|Sınır))?\s*\.?\s*$", rest, re.IGNORECASE)
            reference = None
            status = "normal"
            value_str = rest
            if ref_match:
                reference = ref_match.group(1).strip() or None
                if ref_match.lastindex >= 2 and ref_match.group(2):
                    status = _normalize_status(ref_match.group(2))
                value_str = rest[: ref_match.start()].strip().rstrip(".,")
            value, unit = _split_value_unit(value_str)
            key = name.lower()
            if key not in seen_names:
                seen_names.add(key)
                rows.append({
                    "name": name,
                    "value": value,
                    "unit": unit,
                    "reference": reference,
                    "status": status,
                    "status_label": _status_label(status),
                })
    return rows


def _values_section_from_result_text(result_text: str) -> str:
    """result_text'ten 'values' bölümünü döndürür (trend için)."""
    sections_list = _split_sections(result_text or "")
    for title, body in sections_list:
        key = _map_section_key(title)
        if key == "values":
            return body
    return ""


def _extract_numeric_value(v: str) -> float | None:
    """'120', '14.2', '—' -> 120.0, 14.2, None."""
    if not v or v == "—" or v == "-":
        return None
    s = (v or "").strip().replace(",", ".")
    try:
        return float(re.sub(r"[^\d.]", "", s) or 0)
    except (ValueError, TypeError):
        return None


def extract_trend_from_results(entries: list[tuple[str, str]]) -> dict | None:
    """
    Son N analiz (date_str, result_text) listesinden LDL, Glucose, CRP trend verisi çıkarır.
    Returns: { "dates": [d1,d2,d3], "ldl": [v1,v2,v3], "glucose": [...], "crp": [...] } veya None.
    """
    if not entries:
        return None
    dates: list[str] = []
    ldl_list: list[float | None] = []
    glucose_list: list[float | None] = []
    crp_list: list[float | None] = []
    name_aliases = {
        "ldl": ("ldl", "ldl kolesterol", "ldl-c"),
        "glucose": ("glucose", "glukoz", "glikoz", "kan şekeri", "blood glucose", "fasting glucose"),
        "crp": ("crp", "c-reaktif", "c reactive", "hs-crp", "crp (yüksek duyarlı)"),
    }
    for date_str, result_text in entries[:3]:
        values_block = _values_section_from_result_text(result_text)
        biomarkers = parse_biomarkers(values_block)
        by_key: dict[str, float | None] = {}
        for row in biomarkers:
            name = (row.get("name") or "").strip().lower()
            val = _extract_numeric_value(str(row.get("value") or ""))
            for key, aliases in name_aliases.items():
                if any(a in name for a in aliases):
                    by_key[key] = val
                    break
        dates.append(date_str)
        ldl_list.append(by_key.get("ldl"))
        glucose_list.append(by_key.get("glucose"))
        crp_list.append(by_key.get("crp"))
    has_any = any(ldl_list) or any(glucose_list) or any(crp_list)
    if not has_any:
        return None
    return {
        "dates": dates,
        "ldl": ldl_list,
        "glucose": glucose_list,
        "crp": crp_list,
    }


def _shorten_causes_to_few_words(text: str, min_words: int = 3, max_words: int = 5) -> str:
    """Her satırı en az min_words, en fazla max_words kelime olacak şekilde kısalt (standart PDF: 3-4 kelime)."""
    if not (text or "").strip():
        return text or ""
    lines: list[str] = []
    for line in (text or "").strip().splitlines():
        line = line.strip()
        if not line:
            continue
        # Madde işaretini kaldır: - veya * ile başlayan
        if line.startswith("-") or line.startswith("*") or line.startswith("•"):
            line = line.lstrip("-*•").strip()
        words = line.split()
        if not words:
            continue
        # En az min_words, en fazla max_words kelime (tercihen 3-4 kelime)
        n = min(max_words, len(words))
        if n < min_words and len(words) >= min_words:
            n = min_words
        short = " ".join(words[:n])
        lines.append(short)
    return "\n".join(lines) if lines else (text or "").strip()


def parse_report_to_context(
    result_text: str,
    report_date: str | None = None,
    lang: str = "tr",
) -> dict:
    """
    AI result_text'i bölümlere ayırıp PDF şablonu için context sözlüğü üretir.
    """
    report_date = report_date or datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")
    sections_list = _split_sections(result_text or "")
    data: dict = {
        "summary": "",
        "risk_indicators": "",
        "values": "",
        "possible_causes": "",
        "recommendations": "",
        "raw_sections": [],
    }
    for title, body in sections_list:
        key = _map_section_key(title)
        if key and key in data and isinstance(data[key], str):
            data[key] = body
        elif key is None:
            data["raw_sections"].append({"title": title, "body": body})

    biomarkers = parse_biomarkers(data["values"])
    # Değerler bölümü boşsa veya az parametre varsa, diğer bölümlerde (raw_sections) parametre satırlarını ara
    if len(biomarkers) < 3 and data["raw_sections"]:
        seen = {(r.get("name") or "").strip().lower() for r in biomarkers}
        for raw in data["raw_sections"]:
            body = (raw.get("body") or "").strip()
            if not body or len(body) < 20:
                continue
            title_lower = (raw.get("title") or "").strip().lower()
            if not any(x in title_lower for x in ("değer", "value", "parametre", "sonuç", "result", "lab", "test")):
                continue
            extra = parse_biomarkers(body)
            for row in extra:
                key = (row.get("name") or "").strip().lower()
                if key and key not in seen:
                    seen.add(key)
                    biomarkers.append(row)
    for row in biomarkers:
        _enrich_biomarker_chart(row)
    risk_level = "none"
    risk_message = ""
    if data["risk_indicators"]:
        risk_message = data["risk_indicators"].strip()
        risk_lower = risk_message.lower()
        if any(
            x in risk_lower
            for x in ("yüksek risk", "acil", "doktora", "hemen", "high risk", "urgent")
        ):
            risk_level = "high"
        elif any(
            x in risk_lower
            for x in ("dikkat", "attention", "sınır", "borderline", "kontrol")
        ) or any(b.get("status") in ("low", "high", "border") for b in biomarkers):
            risk_level = "attention"
        else:
            risk_level = "normal"

    labels = _pdf_labels(lang)
    if not risk_message and biomarkers:
        has_abnormal = any(b.get("status") in ("low", "high", "border") for b in biomarkers)
        risk_message = (
            labels["risk_default_attention"]
            if has_abnormal
            else labels["risk_default_normal"]
        )

    # Genel durum skoru 0–100: normal parametre oranı; risk_level ile aynı renk mantığı (dışarıdaki yeşil/turuncu/kırmızı)
    total = len(biomarkers)
    normal_count = sum(1 for b in biomarkers if b.get("status") == "normal")
    overall_score = round(100 * normal_count / total) if total else 100
    overall_score = max(0, min(100, overall_score))
    chart_status = risk_level if risk_level != "none" else "normal"
    chart_title = labels.get("overall_chart_title", "Genel durum (0–100)")
    badge_label = labels.get(f"overall_badge_{chart_status}") or {"normal": "Normal", "attention": "Sınır", "high": "Riskli"}.get(chart_status, "Normal")
    overall_chart_svg = overall_score_svg_base64(
        score=overall_score,
        status=chart_status,
        title=chart_title,
        badge_label=badge_label,
        include_title=False,  # Şablonda zaten "Genel durum" + legend var; SVG sadece bar
    )

    # Standart PDF: olası nedenler ve öneriler her satır en az 3, en fazla 5 kelime
    possible_causes_short = _shorten_causes_to_few_words(data["possible_causes"], min_words=3, max_words=5)
    recommendations_short = _shorten_causes_to_few_words(data["recommendations"], min_words=3, max_words=5)

    out = {
        "title": labels["title"],
        "lang": lang,
        "report_date": report_date,
        "summary": data["summary"],
        "risk_level": risk_level,
        "risk_message": risk_message,
        "biomarkers": biomarkers,
        "possible_causes": possible_causes_short,
        "recommendations": recommendations_short,
        "raw_sections": data["raw_sections"],
        "overall_score": overall_score,
        "overall_chart_svg_base64": overall_chart_svg,
    }
    out.update(labels)
    return out


def render_pdf(context: dict) -> bytes:
    """Jinja2 şablonunu render edip WeasyPrint ile PDF üretir (lazy import: WeasyPrint sistem kütüphaneleri sunucu başlarken gerekmez)."""
    from weasyprint import HTML
    context = dict(context)
    context["logo_base64"] = _logo_base64()
    template = _ENV.get_template("report_pdf.html")
    html_str = template.render(**context)
    html_doc = HTML(string=html_str, base_url=str(_PROJECT_ROOT))
    pdf_bytes = html_doc.write_pdf()
    return pdf_bytes


# Premium plan: klinik rapor şablonu (AI kelimesi yok, kurumsal görünüm)


def _trend_svg(trend_data: dict) -> str:
    """Trend verisi (dates, ldl, glucose, crp) ile mini bar chart SVG. 3 tarih, her satırda 3 bar (LDL/Glucose/CRP)."""
    dates = trend_data.get("dates") or []
    ldl = trend_data.get("ldl") or []
    glucose = trend_data.get("glucose") or []
    crp = trend_data.get("crp") or []
    n = min(3, len(dates))
    if n == 0:
        return ""
    all_vals = [v for v in (ldl + glucose + crp) if v is not None and not (isinstance(v, float) and (v != v))]
    max_val = max(all_vals) if all_vals else 1
    if max_val <= 0:
        max_val = 1
    w, h = 240, 58
    bar_h = 10
    gap = 4
    row_h = bar_h + gap
    bar_max_w = 45
    x0 = 58
    out: list[str] = [
        f'<svg class="trend-svg" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
    ]
    for i in range(n):
        y = 8 + i * row_h
        date_str = (dates[i] or "")[:10]
        out.append(f'<text x="0" y="{y + bar_h - 2}" font-size="9" fill="#64748b">{date_str}</text>')
        ldl_w = (ldl[i] or 0) / max_val * bar_max_w if i < len(ldl) and ldl[i] is not None else 0
        glu_w = (glucose[i] or 0) / max_val * bar_max_w if i < len(glucose) and glucose[i] is not None else 0
        crp_w = (crp[i] or 0) / max_val * bar_max_w if i < len(crp) and crp[i] is not None else 0
        out.append(f'<rect x="{x0}" y="{y}" width="{max(2, ldl_w)}" height="{bar_h}" rx="2" fill="#3b82f6"/>')
        out.append(f'<rect x="{x0 + bar_max_w + 2}" y="{y}" width="{max(2, glu_w)}" height="{bar_h}" rx="2" fill="#0EA5A4"/>')
        out.append(f'<rect x="{x0 + (bar_max_w + 2) * 2}" y="{y}" width="{max(2, crp_w)}" height="{bar_h}" rx="2" fill="#f59e0b"/>')
    out.append("</svg>")
    return "\n".join(out)


# Outline icons (Feather-style, 24x24, stroke only) for report sections — web + PDF
REPORT_ICONS: dict[str, str] = {
    "file-text": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
    "activity": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    "grid": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "bar-chart-2": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    "alert-circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    "eye": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>',
    "apple": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c4-4 8-6.5 8-11a5 5 0 0 0-10 0c0 4.5 4 7 8 11z"/><path d="M12 11c0-2 1.5-4 4-4"/></svg>',
    "minus-circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="8" y1="12" x2="16" y2="12"/></svg>',
    "heart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    "trending-up": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    "message-circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    "info": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>',
    "gauge": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "target": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
}


def _report_icon(name: str) -> str:
    """Return inline SVG for report section icon (safe for HTML/PDF)."""
    return REPORT_ICONS.get(name, REPORT_ICONS["info"])


def _radar_svg(domains: dict) -> str:
    """Four-axis radar chart from domain scores (cardio, metabolic, inflammation, vitamin). viewBox 0 0 200 200."""
    order = ("cardio", "metabolic", "inflammation", "vitamin")
    scores = [max(0, min(100, (domains.get(d) or {}).get("score", 50))) for d in order]
    cx, cy, r = 100.0, 100.0, 72.0
    points = []
    for i, s in enumerate(scores):
        angle = (i * 90 - 90) * math.pi / 180
        x = cx + r * (s / 100.0) * math.cos(angle)
        y = cy + r * (s / 100.0) * math.sin(angle)
        points.append(f"{x:.2f},{y:.2f}")
    poly = " ".join(points)
    axes = []
    for i in range(4):
        a = (i * 90 - 90) * math.pi / 180
        x2 = cx + r * math.cos(a)
        y2 = cy + r * math.sin(a)
        axes.append(f'<line x1="{cx}" y1="{cy}" x2="{x2}" y2="{y2}" class="report-radar-axis" stroke="#cbd5e1" stroke-width="1"/>')
    return f'''<svg class="report-radar-svg" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#e2e8f0" stroke-width="1"/>
  {"".join(axes)}
  <polygon points="{poly}" fill="rgba(14,165,164,0.12)" stroke="none"/>
  <polygon points="{poly}" fill="none" stroke="#0EA5A4" stroke-width="1.5"/>
</svg>'''


def _biomarkers_to_lab_values(biomarkers: list[dict]) -> list[dict]:
    """PDF'den parse edilen biomarkers → risk_engine.compute_risk beklediği lab_values (name, value, ref_low, ref_high)."""
    canonical = {
        "ldl": "LDL", "ldl kolesterol": "LDL", "ldl-c": "LDL", "hdl": "HDL", "trigliserid": "Triglycerides",
        "triglycerides": "Triglycerides", "tg": "Triglycerides", "total kolesterol": "Total cholesterol",
        "glukoz": "Glucose", "glucose": "Glucose", "açlık glukoz": "Glucose", "hba1c": "HbA1c", "crp": "CRP",
        "c-reaktif": "CRP", "homosistein": "Homocysteine", "alt": "ALT", "ast": "AST", "ggt": "GGT",
        "kreatinin": "Creatinine", "creatinine": "Creatinine", "egfr": "eGFR", "vitamin d": "Vitamin D",
        "d vitamini": "Vitamin D", "b12": "B12", "folat": "Folate", "ferritin": "Ferritin", "demir": "Iron",
        "iron": "Iron", "hb": "Hb", "hemoglobin": "Hb", "tsh": "TSH",
    }
    out: list[dict] = []
    for row in biomarkers:
        name_raw = (row.get("name") or "").strip()
        if not name_raw:
            continue
        key = name_raw.lower()
        param = next((canonical[alias] for alias in canonical if alias in key or key in alias), name_raw)
        val = _value_to_float(str(row.get("value") or ""))
        if val is None:
            continue
        ref = _parse_reference_range(row.get("reference"))
        ref_low, ref_high = (ref[0], ref[1]) if ref else (None, None)
        out.append({"name": param, "value": val, "ref_low": ref_low, "ref_high": ref_high})
    return out


def _build_premium_context(
    base_context: dict,
    report_id: str,
    report_date: str,
    user_id: str,
    lang: str,
    trend_data: dict | None = None,
    trend_locked: bool = False,
) -> dict:
    """Parse edilmiş context'ten premium template için risk_cards, findings, lab_rows, clinical_notes, recommendations üretir."""
    risk_level = base_context.get("risk_level") or "normal"
    overall_score = base_context.get("overall_score") or 100
    biomarkers = base_context.get("biomarkers") or []
    # Domain skorları: biomarkers'tan risk_engine ile hesapla (gerçekçi skorlar)
    risk_cards: list[dict] = []
    lab_values = _biomarkers_to_lab_values(biomarkers)
    if lab_values:
        try:
            risk_summary = compute_risk(lab_values)
            overall = risk_summary.get("overall") or {}
            overall_score = overall.get("score", overall_score)
            domains = risk_summary.get("domains") or {}
            domain_order = ("cardio", "metabolic", "vitamin", "inflammation")
            level_map = {"low": "low", "mid": "mid", "high": "high"}
            label_map = {"low": "Normal", "mid": "Sınır", "high": "Riskli"} if lang == "tr" else {"low": "Normal", "mid": "Borderline", "high": "At risk"}
            labels = _pdf_labels(lang)
            name_keys = ("report_domain_cardio", "report_domain_metabolic", "report_domain_vitamin", "report_domain_inflammation")
            for i, dk in enumerate(domain_order):
                d = domains.get(dk, {})
                score = d.get("score", 50)
                lev = level_map.get(d.get("level", "mid"), "mid")
                risk_cards.append({
                    "name": labels.get(name_keys[i], name_keys[i]),
                    "score": score,
                    "label": label_map.get(lev, "Normal"),
                    "level": lev,
                })
        except Exception:
            pass
    if not risk_cards:
        level_map = {"normal": "low", "attention": "mid", "high": "high", "none": "low"}
        level = level_map.get(risk_level, "low")
        label_map = {"normal": "Normal", "attention": "Sınır", "high": "Riskli", "none": "Normal"} if lang == "tr" else {"normal": "Normal", "attention": "Borderline", "high": "At risk", "none": "Normal"}
        label = label_map.get(risk_level, "Normal")
        labels = _pdf_labels(lang)
        name_keys = ("report_domain_cardio", "report_domain_metabolic", "report_domain_vitamin", "report_domain_inflammation")
        risk_cards = [
            {"name": labels.get(name_keys[i], name_keys[i]), "score": overall_score, "label": label, "level": level}
            for i in range(4)
        ]

    # Risk distribution and top attention from risk_summary.highlights (when available)
    risk_distribution = {"normal": 0, "borderline": 0, "attention": 0}
    top_attention: list[dict] = []
    radar_svg = ""
    if lab_values:
        try:
            risk_summary = compute_risk(lab_values)
            domains = risk_summary.get("domains") or {}
            highlights = risk_summary.get("highlights") or []
            for h in highlights:
                lev = (h.get("level") or "").lower()
                if lev == "low":
                    risk_distribution["normal"] += 1
                elif lev == "mid":
                    risk_distribution["borderline"] += 1
                else:
                    risk_distribution["attention"] += 1
            if not highlights:
                risk_distribution["normal"] = 1
            for h in highlights:
                if len(top_attention) >= 5:
                    break
                lev = (h.get("level") or "").lower()
                if lev in ("mid", "high"):
                    top_attention.append({"test": h.get("test") or "—", "action": h.get("action") or ""})
            radar_svg = _radar_svg(domains)
        except Exception:
            pass
    if not radar_svg and risk_cards:
        domains_fallback = {dk: {"score": c.get("score", 50)} for dk, c in zip(("cardio", "metabolic", "inflammation", "vitamin"), risk_cards)}
        radar_svg = _radar_svg(domains_fallback)
    total_dist = risk_distribution["normal"] + risk_distribution["borderline"] + risk_distribution["attention"]
    if total_dist == 0:
        total_dist = 1
    dist_pct = {
        "normal_pct": 100 * risk_distribution["normal"] / total_dist,
        "borderline_pct": 100 * risk_distribution["borderline"] / total_dist,
        "attention_pct": 100 * risk_distribution["attention"] / total_dist,
    }
    top_attention = top_attention[:10]

    _labels = _pdf_labels(lang)
    _fallback_en = PDF_LABELS.get("en", {})

    def _t_early(key: str, default: str = "") -> str:
        return (_labels.get(key) or _fallback_en.get(key) or default)

    # Biomarker category mapping for grouped highlights (Metabolic, Cardiovascular, Liver, Inflammation, Iron/Nutrients, Vitamins)
    BIOMARKER_GROUP: dict[str, tuple[str, ...]] = {
        "Metabolic": ("Glucose", "HbA1c", "Creatinine", "eGFR"),
        "Cardiovascular": ("LDL", "HDL", "Triglycerides", "Total cholesterol", "CRP", "Homocysteine"),
        "Liver": ("ALT", "AST", "GGT"),
        "Inflammation": ("CRP", "Homocysteine"),
        "Iron/Nutrients": ("Ferritin", "Iron", "Hb", "Hemoglobin"),
        "Vitamins": ("Vitamin D", "B12", "Folate"),
    }
    def _status_class_early(s: str) -> str:
        s = (s or "").strip().lower()
        if s == "normal":
            return "normal"
        if s in ("border", "mid", "sınır", "borderline"):
            return "border"
        return "risk"

    biomarker_highlights: dict[str, list[dict]] = {k: [] for k in BIOMARKER_GROUP}
    for row in (base_context.get("biomarkers") or []):
        name = (row.get("name") or "").strip()
        if not name:
            continue
        for group, params in BIOMARKER_GROUP.items():
            if any(p.lower() in name.lower() or name.lower() in p.lower() for p in params):
                biomarker_highlights[group].append({
                    "name": name,
                    "value": row.get("value") or "—",
                    "unit": row.get("unit"),
                    "ref": row.get("reference"),
                    "status": row.get("status_label") or "—",
                    "status_class": _status_class_early(row.get("status") or "normal"),
                })
                break

    # Executive summary: first 2–4 sentences from summary
    summary_txt = (base_context.get("summary") or "").strip()
    executive_sentences = [
        s.strip() + ("." if s.strip() and not s.strip().endswith(".") else "")
        for s in re.split(r"(?<=[.!])\s+", summary_txt) if s.strip()
    ][:8]
    executive_summary = " ".join(executive_sentences) if executive_sentences else (
        "Your lab results have been reviewed. Values within the reference range support general health; any out-of-range parameters should be discussed with your doctor for follow-up or further tests." if lang != "tr"
        else "Laboratuvar sonuçlarınız değerlendirildi. Referans aralığındaki değerler genel sağlık açısından olumludur; referans dışı parametreleri hekiminizle görüşerek takip veya ek tetkik planlayabilirsiniz."
    )
    executive_summary = _strip_ai_from_text(executive_summary)

    # Summary tiles: Overall Score, Risk Level, Biological Age, Priority Focus
    health_age = 40
    try:
        health_age = int(round(40 + (100 - overall_score) / 4.0))
    except Exception:
        pass
    health_age = max(20, min(80, health_age))
    risk_level_label = _t_early("report_band_low", "Low") if overall_score <= 33 else (_t_early("report_band_mid", "Moderate") if overall_score <= 66 else _t_early("report_band_high", "Good"))
    priority_focus = ""
    if lab_values:
        try:
            rs = compute_risk(lab_values)
            hl = (rs.get("highlights") or [])
            for h in hl:
                if (h.get("level") or "").lower() in ("mid", "high"):
                    priority_focus = (h.get("test") or "") + (" — " + (h.get("action") or "")) if h.get("action") else (h.get("test") or "")
                    break
        except Exception:
            pass
    if not priority_focus:
        priority_focus = _t_early("report_priority_general", "General wellness") if lang != "tr" else "Genel iyilik hali"
    summary_tiles = [
        {"label": _t_early("report_tile_overall_score", "Overall Score"), "value": str(overall_score) + " / 100", "icon": "activity"},
        {"label": _t_early("report_tile_risk_level", "Risk Level"), "value": risk_level_label, "icon": "gauge"},
        {"label": _t_early("report_tile_bio_age", "Biological Age"), "value": "≈ " + str(health_age), "icon": "target"},
        {"label": _t_early("report_tile_priority", "Priority Focus"), "value": priority_focus[:50] + ("…" if len(priority_focus) > 50 else ""), "icon": "eye"},
    ]

    # Key areas to watch (2–5 items: parameter, why_it_matters, monitoring_focus)
    key_areas_to_watch: list[dict] = []
    if lab_values:
        try:
            rs = compute_risk(lab_values)
            for h in (rs.get("highlights") or []):
                if len(key_areas_to_watch) >= 5:
                    break
                if (h.get("level") or "").lower() in ("mid", "high"):
                    key_areas_to_watch.append({
                        "parameter": h.get("test") or "—",
                        "why_it_matters": _strip_ai_from_text(h.get("why") or ""),
                        "monitoring_focus": _strip_ai_from_text(h.get("action") or ""),
                    })
        except Exception:
            pass

    # Helper: madde satırlarını metinden çıkar (-, *, •, 1. 2. vb. veya kısa satırlar)
    def _bullet_lines(body: str, max_items: int = 10) -> list[str]:
        out: list[str] = []
        for line in (body or "").splitlines():
            s = line.strip().lstrip("-•*0123456789.) ")
            if not s or len(s) < 3:
                continue
            clean = _strip_ai_from_text(s)
            if not clean or len(clean) > 250:
                continue
            if clean not in out and len(out) < max_items:
                out.append(clean)
        return out

    # Foods to favor / limit: önce recommendations, sonra raw_sections (Diyet, Yenilmesi/Kaçınılması gerekenler vb.)
    rec_txt_pre = (base_context.get("recommendations") or "").strip().lower()
    foods_to_favor: list[str] = []
    foods_to_limit: list[str] = []
    for line in (base_context.get("recommendations") or "").splitlines():
        line = line.strip().lstrip("-•* ")
        if not line:
            continue
        line_clean = _strip_ai_from_text(line)
        if not line_clean:
            continue
        low = line_clean.lower()
        if any(x in low for x in ("favor", "eat more", "increase", "yenilmesi", "tüketilmesi", "önerilir", "tercih", "sebze", "vegetable", "fruit", "meyve", "fiber", "lif", "omega", "balık", "fish", "include", "tüket", "ye ")):
            if len(foods_to_favor) < 10 and line_clean not in foods_to_favor:
                foods_to_favor.append(line_clean)
        elif any(x in low for x in ("limit", "avoid", "reduce", "az tüket", "kaçının", "kısıtla", "sugar", "şeker", "salt", "tuz", "processed", "işlenmiş", "alcohol", "alkol", "yenilmemesi", "yemeyin")):
            if len(foods_to_limit) < 10 and line_clean not in foods_to_limit:
                foods_to_limit.append(line_clean)

    # raw_sections içinden diyet başlıklarını tara (Yenilmesi gerekenler, Foods to eat, Diyet, Beslenme vb.)
    favor_titles = ("yenilmesi gereken", "tercih edilebilecek", "foods to eat", "foods to include", "önerilen gıda", "eat more", "include", "diyet", "beslenme", "diet plan", "yemek", "tüketilmesi")
    avoid_titles = ("yenilmemesi", "kaçınılması", "sınırlanabilecek", "foods to avoid", "foods to limit", "avoid", "limit", "kısıtla", "yemeyin")
    for raw in base_context.get("raw_sections") or []:
        title = (raw.get("title") or "").strip().lower()
        body = (raw.get("body") or "").strip()
        if not body:
            continue
        if any(t in title for t in favor_titles):
            for item in _bullet_lines(body, 10):
                if item not in foods_to_favor and len(foods_to_favor) < 10:
                    foods_to_favor.append(item)
        elif any(t in title for t in avoid_titles):
            for item in _bullet_lines(body, 10):
                if item not in foods_to_limit and len(foods_to_limit) < 10:
                    foods_to_limit.append(item)

    # Varsayılan: tek satır yerine anlamlı madde listesi (PDF’te diyet bölümü her zaman dolu görünsün)
    default_favor_tr = [
        "Dengeli beslenme; sebze ve meyveler lif ve vitaminlerle genel sağlığı destekleyebilir.",
        "Sebze ve meyve: lif, vitamin ve antioksidan alımı için günde birkaç porsiyon önerilir.",
        "Tam tahıllar ve baklagiller: kan şekeri dengesi ve kalp sağlığı için faydalıdır.",
        "Yağlı balık (omega-3): haftada 1–2 porsiyon kalp ve beyin sağlığını destekleyebilir.",
        "Yeterli sıvı tüketimi: böbrek ve metabolizma için günde yaklaşık 1,5–2 litre önerilir.",
    ]
    default_favor_en = [
        "Balanced diet; vegetables and fruits provide fibre and vitamins that support general health.",
        "Vegetables and fruits: several servings per day are recommended for fibre, vitamins and antioxidants.",
        "Whole grains and legumes support blood sugar balance and heart health.",
        "Oily fish (omega-3): one to two portions per week may support heart and brain health.",
        "Adequate fluid intake: about 1.5–2 litres per day is recommended for kidney function and metabolism.",
    ]
    default_limit_tr = [
        "İşlenmiş gıdalar ve aşırı şeker sınırlanabilir; kan şekeri ve kilo dengesi için faydalıdır.",
        "İşlenmiş atıştırmalıklar ve hazır ürünler yerine taze veya az işlenmiş seçenekler tercih edilebilir.",
        "Eklenen şeker ve tatlılar ölçülü tüketilmeli; diş ve metabolizma sağlığı için önemlidir.",
        "Aşırı tuz ve doymuş yağ tansiyon ve kalp damar sağlığı açısından sınırlanabilir.",
        "Alkol ölçülü tüketilmeli; karaciğer ve genel sağlık için önerilen sınırlar aşılmamalıdır.",
    ]
    default_limit_en = [
        "Processed foods and excess sugar are worth limiting for blood sugar and weight balance.",
        "Prefer fresh or minimally processed options over processed snacks and ready-made products.",
        "Added sugar and sweets in moderation; important for dental and metabolic health.",
        "Excess salt and saturated fat may be limited for blood pressure and cardiovascular health.",
        "Alcohol in moderation; recommended limits should not be exceeded for liver and general health.",
    ]
    if not foods_to_favor:
        foods_to_favor = default_favor_tr if lang == "tr" else default_favor_en
    elif len(foods_to_favor) == 1:
        _low = _strip_ai_from_text(foods_to_favor[0]).lower()
        if "dengeli beslenme" in _low or "balanced diet" in _low:
            foods_to_favor = default_favor_tr if lang == "tr" else default_favor_en
    if not foods_to_limit:
        foods_to_limit = default_limit_tr if lang == "tr" else default_limit_en
    elif len(foods_to_limit) == 1:
        _low = _strip_ai_from_text(foods_to_limit[0]).lower()
        if "işlenmiş gıdalar" in _low or "processed foods" in _low:
            foods_to_limit = default_limit_tr if lang == "tr" else default_limit_en

    # Lifestyle suggestions (sleep, movement, hydration, stress, follow-up)
    lifestyle_suggestions: list[str] = []
    lifestyle_keywords = ("sleep", "uyku", "exercise", "hareket", "hydration", "sıvı", "water", "su", "stress", "stres", "follow", "takip", "kontrol", "repeat", "recheck")
    for line in (base_context.get("recommendations") or "").splitlines():
        line = line.strip().lstrip("-•* ")
        if not line or len(lifestyle_suggestions) >= 6:
            continue
        line_clean = _strip_ai_from_text(line)
        if any(k in line_clean.lower() for k in lifestyle_keywords):
            lifestyle_suggestions.append(line_clean)
    if not lifestyle_suggestions:
        lifestyle_suggestions = [
            _t_early("report_lifestyle_sleep", "Adequate sleep supports recovery.") if lang != "tr" else "Yeterli uyku toparlanmayı destekler.",
            _t_early("report_lifestyle_movement", "Regular movement is recommended.") if lang != "tr" else "Düzenli hareket önerilir.",
            _t_early("report_lifestyle_followup", "Discuss follow-up timing with your doctor.") if lang != "tr" else "Takip süresini hekiminizle görüşün.",
        ]

    # Sonuç odaklı: hareket, stres, uyku, sıvı (öneri metninden + lab_values ile zenginleştirme)
    rec_lines = (base_context.get("recommendations") or "").splitlines()
    movement_tips: list[str] = []
    stress_tips: list[str] = []
    sleep_tips: list[str] = []
    hydration_tips: list[str] = []
    move_kw = ("exercise", "egzersiz", "hareket", "yürüyüş", "walk", "spor", "yüzme", "bisiklet", "cardio", "movement", "activity")
    stress_kw = ("stress", "stres", "rahatlama", "relax", "nefes", "breathing", "meditation", "meditasyon")
    sleep_kw = ("sleep", "uyku", "dinlenme", "rest", "uyumak")
    hydration_kw = ("water", "su", "sıvı", "hydration", "hidrasyon", "sıvı tüket", "içme")
    for line in rec_lines:
        line = line.strip().lstrip("-•* ")
        if not line:
            continue
        line_clean = _strip_ai_from_text(line)
        if not line_clean:
            continue
        low = line_clean.lower()
        if any(k in low for k in move_kw) and len(movement_tips) < 5:
            movement_tips.append(line_clean)
        elif any(k in low for k in stress_kw) and len(stress_tips) < 5:
            stress_tips.append(line_clean)
        elif any(k in low for k in sleep_kw) and len(sleep_tips) < 5:
            sleep_tips.append(line_clean)
        elif any(k in low for k in hydration_kw) and len(hydration_tips) < 5:
            hydration_tips.append(line_clean)
    # Sonuç odaklı ek öneriler (lab_values / risk_summary)
    if lab_values:
        try:
            rs = compute_risk(lab_values)
            domains = rs.get("domains") or {}
            highlights = rs.get("highlights") or []
            names_lower = [str(v.get("name", "")).lower() for v in lab_values]
            # Kardiyo / lipid risk → hareket
            if domains.get("cardio", {}).get("level") in ("mid", "high") or any(n in " ".join(names_lower) for n in ("ldl", "hdl", "triglyceride", "kolesterol")):
                tip = _t_early("report_movement_default", "At least 150 minutes of moderate activity per week (walking, swimming, cycling) is recommended.") if lang != "tr" else "Haftada en az 150 dakika orta tempolu hareket (yürüyüş, yüzme, bisiklet) önerilir."
                if tip not in movement_tips and len(movement_tips) < 5:
                    movement_tips.append(tip)
            # D vitamini düşük → açık hava
            if any("vitamin d" in n or "d vitamini" in n for n in names_lower):
                for row in lab_values:
                    if "vitamin" in str(row.get("name", "")).lower() and row.get("value") is not None:
                        try:
                            val = float(str(row["value"]).replace(",", "."))
                            if val < 30:  # ng/mL düşük kabul
                                tip = "D vitamini için günde 15–20 dakika güneş ve açık havada yürüyüş düşünülebilir." if lang == "tr" else "Consider 15–20 minutes of sunlight and outdoor walking for vitamin D."
                                if tip not in movement_tips and len(movement_tips) < 5:
                                    movement_tips.append(tip)
                                break
                        except (ValueError, TypeError):
                            pass
            # CRP / enflamasyon → stres ve uyku
            if domains.get("inflammation", {}).get("level") in ("mid", "high") or any("crp" in n for n in names_lower):
                tip_s = _t_early("report_stress_default", "Stress reduction: breathing exercises, short breaks, regular sleep.") if lang != "tr" else "Stres azaltma: nefes egzersizleri, kısa molalar, düzenli uyku."
                if tip_s not in stress_tips and len(stress_tips) < 5:
                    stress_tips.append(tip_s)
                tip_sl = _t_early("report_sleep_default", "7–8 hours of sleep per night; pay attention to sleep hygiene.") if lang != "tr" else "Günde 7–8 saat uyku; uyku hijyenine dikkat edin."
                if tip_sl not in sleep_tips and len(sleep_tips) < 5:
                    sleep_tips.append(tip_sl)
            # Böbrek / kreatinin / eGFR → sıvı
            if any(n in " ".join(names_lower) for n in ("creatinine", "kreatinin", "egfr", "bun")):
                tip = _t_early("report_hydration_default", "About 1.5–2 litres of fluid per day is recommended.") if lang != "tr" else "Günde yaklaşık 1,5–2 litre sıvı tüketimi önerilir."
                if tip not in hydration_tips and len(hydration_tips) < 5:
                    hydration_tips.append(tip)
        except Exception:
            pass
    if not movement_tips:
        movement_tips = [_t_early("report_movement_default", "At least 150 minutes of moderate activity per week (walking, swimming, cycling) is recommended.") if lang != "tr" else "Haftada en az 150 dakika orta tempolu hareket (yürüyüş, yüzme, bisiklet) önerilir."]
    if not stress_tips:
        stress_tips = [_t_early("report_stress_default", "Stress reduction: breathing exercises, short breaks, regular sleep.") if lang != "tr" else "Stres azaltma: nefes egzersizleri, kısa molalar, düzenli uyku."]
    if not sleep_tips:
        sleep_tips = [_t_early("report_sleep_default", "7–8 hours of sleep per night; pay attention to sleep hygiene.") if lang != "tr" else "Günde 7–8 saat uyku; uyku hijyenine dikkat edin."]
    if not hydration_tips:
        hydration_tips = [_t_early("report_hydration_default", "About 1.5–2 litres of fluid per day is recommended.") if lang != "tr" else "Günde yaklaşık 1,5–2 litre sıvı tüketimi önerilir."]

    # Doctor discussion notes (2–4 neutral points)
    doctor_discussion_notes: list[str] = []
    if summary_txt:
        for s in re.split(r"(?<=[.!])\s+", summary_txt):
            s = s.strip()
            if s and len(s) > 25 and len(doctor_discussion_notes) < 4:
                doctor_discussion_notes.append(_strip_ai_from_text(s))
    if len(doctor_discussion_notes) < 2:
        doctor_discussion_notes.append(_t_early("report_doctor_note_1", "Share this report with your physician for context.") if lang != "tr" else "Bu raporu hekiminizle paylaşın.")
        doctor_discussion_notes.append(_t_early("report_doctor_note_2", "Any symptoms or concerns should be evaluated by a doctor.") if lang != "tr" else "Belirti veya endişeler hekim tarafından değerlendirilmelidir.")
    doctor_discussion_notes = doctor_discussion_notes[:12]

    # Refined disclaimer (informational only, consult physician)
    refined_disclaimer = _t_early("report_refined_disclaimer", "This report is for informational use only. It does not provide a diagnosis or treatment. For symptoms or treatment decisions, consult your physician.")

    # Trend placeholder when no history
    trend_placeholder_text = _t_early("report_trend_placeholder", "Trend becomes available with more reports over time.")

    # Bulgular: risk_indicators satırları veya summary cümleleri (3–6 madde)
    risk_txt = (base_context.get("risk_message") or base_context.get("risk_indicators") or "").strip()
    findings: list[str] = []
    if risk_txt:
        for line in risk_txt.splitlines():
            line = line.strip().lstrip("-•* ")
            if line and len(findings) < 6:
                findings.append(line)
    if len(findings) < 3 and base_context.get("summary"):
        summary = (base_context["summary"] or "").strip()
        for part in re.split(r"[.!]\s+", summary):
            part = part.strip()
            if part and len(part) > 20 and len(findings) < 6:
                findings.append(part + ("." if not part.endswith(".") else ""))
    if not findings:
        findings = [
            "Laboratuvar sonuçları değerlendirildi." if lang == "tr" else "Lab results have been reviewed.",
        ]
    findings = [_strip_ai_from_text(s) for s in findings if s]

    # Bulguları renkli kart olarak: metinden "X:** Düşük/Normal/Sınır" çıkar → status_class
    def _finding_status_class(text: str) -> str:
        t = (text or "").strip().lower()
        if "normal" in t or "referans" in t and "içinde" in t:
            return "normal"
        if "sınır" in t or "borderline" in t or "sınırda" in t:
            return "border"
        if "düşük" in t or "yüksek" in t or "risk" in t or "low" in t or "high" in t or "dikkat" in t:
            return "risk"
        return "normal"

    findings_cards: list[dict] = []
    for f in findings[:24]:
        f_clean = (f or "").strip()
        if not f_clean:
            continue
        # "Alüminyum:** Düşük seviyede." veya "Parametre: Normal"
        name_part = ""
        for sep in ("**:", ":**", ":"):
            if sep in f_clean:
                parts = f_clean.split(sep, 1)
                name_part = (parts[0] or "").strip().strip("*").strip()
                break
        if not name_part:
            name_part = f_clean[:40] + ("…" if len(f_clean) > 40 else "")
        findings_cards.append({
            "name": name_part,
            "text": f_clean,
            "status_class": _finding_status_class(f_clean),
        })

    # Test tablosu: biomarkers -> lab_rows + kategorize (hemogram, biyokimya grupları)
    biomarkers = base_context.get("biomarkers") or []
    def _status_class(s: str) -> str:
        s = (s or "").strip().lower()
        if s == "normal":
            return "normal"
        if s in ("border", "mid", "sınır", "borderline"):
            return "border"
        return "risk"  # low, high, riskli

    def _default_ref_for_biomarker(name: str) -> str | None:
        n = (name or "").strip().lower()
        for key, ref in DEFAULT_REF_RANGES.items():
            if key in n or n in key:
                return ref
        return None

    lab_rows = []
    for row in biomarkers:
        raw_status = (row.get("status") or "normal").strip().lower()
        status_class = _status_class(raw_status)
        ref = row.get("reference") or _default_ref_for_biomarker(row.get("name") or "")
        lab_rows.append({
            "name": row.get("name") or "—",
            "value": row.get("value") or "—",
            "unit": row.get("unit"),
            "ref": ref,
            "status": row.get("status_label") or "—",
            "status_class": status_class,
        })
    # Kan şekeri (Glukoz/HbA1c) raporda var mı?
    _glucose_keywords = ("glucose", "glukoz", "açlık glukoz", "fasting glucose", "hba1c", "hb a1c", "kan şekeri", "blood sugar")
    has_glucose = any(
        any(kw in (r.get("name") or "").strip().lower() for kw in _glucose_keywords)
        for r in lab_rows
    )
    # Kategori eşlemesi: hemogram (WBC,RBC,HGB,HCT,PLT,MCV,RDW), CRP, glukoz, lipidler, karaciğer, böbrek, demir, tiroid hemogram (WBC,RBC,HGB,HCT,PLT,MCV,RDW), CRP, glukoz, lipidler, karaciğer, böbrek, demir, tiroid
    _cat_order = (
        ("hemogram", "report_cat_hemogram", "bar-chart-2", ("wbc", "rbc", "hgb", "hct", "plt", "mcv", "rdw", "leukocyte", "lökosit", "erythrocyte", "eritrosit", "hemoglobin", "hematocrit", "platelet", "trombosit", "hemogram")),
        ("crp", "report_cat_crp", "alert-circle", ("crp", "c-reactive", "c reaktif", "enflamasyon")),
        ("glucose", "report_cat_glucose", "activity", ("glucose", "glukoz", "açlık", "fasting", "hba1c", "hb a1c")),
        ("lipids", "report_cat_lipids", "heart", ("ldl", "hdl", "triglyceride", "trigliserid", "cholesterol", "kolesterol", "lipid")),
        ("liver", "report_cat_liver", "bar-chart-2", ("alt", "ast", "ggt", "sgot", "sgpt", "karaciğer", "liver")),
        ("kidney", "report_cat_kidney", "info", ("urea", "üre", "creatinine", "kreatinin", "egfr", "bun", "böbrek", "kidney")),
        ("iron", "report_cat_iron", "activity", ("iron", "demir", "ferritin")),
        ("thyroid", "report_cat_thyroid", "gauge", ("tsh", "ft3", "ft4", "t3", "t4", "thyroid", "tiroid")),
        ("other", "report_cat_other", "grid", ()),
    )
    def _biomarker_category(name: str) -> str:
        n = (name or "").strip().lower()
        for cid, _lk, _ik, kws in _cat_order:
            if cid == "other":
                return "other"
            if any(kw in n or n in kw for kw in kws):
                return cid
        return "other"
    highlights_by_test: dict = {}
    if lab_values:
        try:
            rs = compute_risk(lab_values)
            for h in (rs.get("highlights") or []):
                tname = (h.get("test") or "").strip().lower()
                if tname:
                    highlights_by_test[tname] = {"action": h.get("action") or "", "level": (h.get("level") or "").lower()}
        except Exception:
            pass
    lab_categories: list[dict] = []
    for cid, label_key, icon_key, kws in _cat_order:
        rows_in_cat = [r for r in lab_rows if _biomarker_category(r["name"]) == cid]
        if not rows_in_cat:
            continue
        attention_do: list[str] = []
        attention_avoid: list[str] = []
        has_risk = any(r.get("status_class") == "risk" for r in rows_in_cat)
        has_border = any(r.get("status_class") == "border" for r in rows_in_cat)
        category_status = "risk" if has_risk else ("border" if has_border else "normal")
        for r in rows_in_cat:
            rname = (r.get("name") or "").strip().lower()
            if r.get("status_class") in ("border", "risk") and rname:
                hint = highlights_by_test.get(rname, {}).get("action") or ""
                if hint and hint not in attention_do:
                    attention_do.append(hint)
        recommendation_summary = (attention_do[0][:120] + "…" if attention_do and len(attention_do[0]) > 120 else (attention_do[0] if attention_do else "")) or (
            _t_early("report_cat_recommend_ok", "Values in range. Regular follow-up recommended.") if category_status == "normal"
            else _t_early("report_cat_recommend_mid", "Discuss with your doctor for follow-up and lifestyle advice.") if category_status == "border"
            else _t_early("report_cat_recommend_risk", "Discuss with your doctor.")
        )
        lab_categories.append({
            "id": cid,
            "label": _t_early(label_key, cid),
            "icon": icon_key,
            "rows": rows_in_cat,
        "attention_do": attention_do[:5],
        "attention_avoid": attention_avoid[:4],
            "category_status": category_status,
            "recommendation_summary": recommendation_summary,
        })

    # Klinik notlar: possible_causes maddeleri
    possible = (base_context.get("possible_causes") or "").strip()
    clinical_notes: list[str] = []
    for line in possible.splitlines():
        line = line.strip().lstrip("-•* ")
        if line:
            clinical_notes.append(line)
    if not clinical_notes:
        clinical_notes = [
            "Özet ve öneriler bölümüne bakınız." if lang == "tr" else "See summary and recommendations.",
        ]

    # Öneriler: recommendations maddeleri
    rec_txt = (base_context.get("recommendations") or "").strip()
    recommendations: list[str] = []
    for line in rec_txt.splitlines():
        line = line.strip().lstrip("-•* ")
        if line:
            recommendations.append(line)
    if not recommendations:
        recommendations = [
            "Sonuçları hekiminizle paylaşınız." if lang == "tr" else "Share results with your doctor.",
        ]

    # Klinik Notlar: tüm yorum içeriği başlık başlık (AI kelimesi yok)
    summary_txt = (base_context.get("summary") or "").strip()
    ai_summary: list[str] = []
    for part in re.split(r"(?<=[.!])\s+", summary_txt):
        part = part.strip()
        if part:
            ai_summary.append(part)
    if not ai_summary and summary_txt:
        ai_summary = [summary_txt]
    ai_summary = [_strip_ai_from_text(s) for s in ai_summary if s]

    ai_findings = [_strip_ai_from_text(s) for s in findings[:30] if s]

    possible_txt = (base_context.get("possible_causes") or "").strip()
    ai_causes = []
    for line in possible_txt.splitlines():
        line = line.strip().lstrip("-•* ")
        if line:
            ai_causes.append(_strip_ai_from_text(line))

    recos_all = recommendations[:50]
    followup_keywords = ("takip", "kontrol", "tekrar", "ay içinde", "hafta", "follow-up", "repeat", "recheck")
    ai_recos = []
    ai_followup = []
    for line in recos_all:
        line_clean = _strip_ai_from_text(line)
        if not line_clean:
            continue
        low = line_clean.lower()
        if any(k in low for k in followup_keywords):
            ai_followup.append(line_clean)
        else:
            ai_recos.append(line_clean)
    if not ai_recos and recos_all:
        ai_recos = recos_all
    if not ai_followup and lang == "tr":
        ai_followup = ["Gerekirse hekiminiz takip süresini belirleyebilir."]
    elif not ai_followup:
        ai_followup = ["Your doctor can recommend a follow-up schedule if needed."]

    labels = _pdf_labels(lang)
    fallback_en = PDF_LABELS.get("en", {})

    def _t(key: str, default: str = "") -> str:
        return (labels.get(key) or fallback_en.get(key) or default)

    doctor_note = _strip_ai_from_text(
        _t("report_share_note", "You can share this report with your doctor and plan further evaluation if needed.")
    )

    # Sağlık skoru bandı: 0-33 düşük, 34-66 orta, 67-100 iyi (renk: low=green, mid=orange, high=red)
    if overall_score <= 33:
        band_key = "report_band_low"
    elif overall_score <= 66:
        band_key = "report_band_mid"
    else:
        band_key = "report_band_high"
    health_score_band_label = _t(band_key, "Moderate")
    gauge_fill_class = "low" if overall_score <= 33 else ("mid" if overall_score <= 66 else "high")
    gauge_svg = _gauge_svg(overall_score, gauge_fill_class)

    # Trend: trend_data varsa SVG + bars; yoksa mesaj
    trend_has_data = bool(trend_data and (trend_data.get("dates") or trend_data.get("ldl") or trend_data.get("glucose") or trend_data.get("crp")))
    trend_bars: list = []
    trend_svg = _trend_svg(trend_data) if trend_data else ""
    if trend_has_data and trend_data:
        dates = trend_data.get("dates") or []
        ldl = trend_data.get("ldl") or []
        glucose = trend_data.get("glucose") or []
        crp = trend_data.get("crp") or []
        all_vals = [v for v in (ldl + glucose + crp) if v is not None]
        max_val = max(all_vals) if all_vals else 1
        if max_val <= 0:
            max_val = 1
        for i in range(min(3, len(dates))):
            ldl_pct = (100 * (ldl[i] or 0) / max_val) if i < len(ldl) and ldl[i] is not None else 0
            glu_pct = (100 * (glucose[i] or 0) / max_val) if i < len(glucose) and glucose[i] is not None else 0
            crp_pct = (100 * (crp[i] or 0) / max_val) if i < len(crp) and crp[i] is not None else 0
            trend_bars.append({"date": dates[i] or "", "ldl_pct": min(100, ldl_pct), "glucose_pct": min(100, glu_pct), "crp_pct": min(100, crp_pct)})
    trend_message = _t("report_trend_need_more", "More analyses needed for trend.")
    trend_locked_label = _t("report_trend_locked", "Trend analysis is available with subscription.")

    # Logo ve CSS: WeasyPrint için mutlak file:// URL (rapor ikonu: norya_report_icon.png)
    _logo_path = _PROJECT_ROOT / "static" / "norya_report_icon.png"
    logo_url = _logo_path.as_uri() if _logo_path.exists() else "static/norya_report_icon.png"
    _css_path = _PROJECT_ROOT / "static" / "report_premium.css"
    css_url = _css_path.as_uri() if _css_path.exists() else "static/report_premium.css"
    label_glucose_yes = _t("report_glucose_in_report_yes", "Blood sugar (Glucose/HbA1c): In report") if lang != "tr" else "Kan şekeri (Glukoz/HbA1c): Raporda var"
    label_glucose_no = _t("report_glucose_in_report_no", "Blood sugar (Glucose/HbA1c): Not in report") if lang != "tr" else "Kan şekeri (Glukoz/HbA1c): Raporda yok"
    label_glucose_in_report = label_glucose_yes if has_glucose else label_glucose_no

    def _normalize_what_changed(items: list) -> list[str]:
        out: list[str] = []
        for x in items[:10]:
            if isinstance(x, str):
                out.append(x)
            elif isinstance(x, dict):
                out.append((x.get("summary") or x.get("param") or x.get("name") or "").strip() or "—")
            else:
                out.append(str(x) if x else "—")
        return out

    return {
        "rid": report_id,
        "trend_locked": trend_locked,
        "label_report_trend_locked": trend_locked_label,
        "overall_score": overall_score,
        "report_datetime": report_date,
        "lang": lang,
        "user_id": user_id,
        "logo_url": logo_url,
        "css_url": css_url,
        "has_glucose": has_glucose,
        "label_glucose_in_report": label_glucose_in_report,
        "risk_cards": risk_cards,
        "findings": findings[:30],
        "findings_cards": findings_cards,
        "lab_rows": lab_rows,
        "lab_categories": lab_categories,
        "clinical_notes": clinical_notes[:30],
        "recommendations": recommendations[:30],
        "ai_summary": ai_summary,
        "ai_findings": ai_findings,
        "ai_causes": ai_causes,
        "ai_recos": ai_recos,
        "ai_followup": ai_followup,
        "doctor_note": doctor_note,
        "label_report_summary": _t("report_summary", "Summary"),
        "label_report_findings": _t("report_findings", "Findings"),
        "label_report_recommendations": _t("report_recommendations", "Recommendations"),
        "label_report_causes": _t("report_causes", "Possible Causes"),
        "label_report_followup": _t("report_followup", "Follow-up Plan"),
        "label_report_doctor_note": _t("report_doctor_note", "Note for Doctor"),
        "label_report_clinical_notes": _t("report_clinical_notes", "Clinical Notes"),
        "label_report_risk_summary": _t("report_risk_summary", "Risk Summary"),
        "label_report_findings_highlight": _t("report_findings_highlight", "Key Findings"),
        "label_report_test_results": _t("report_test_results", "Test Results"),
        "label_report_test": _t("report_test", "Test"),
        "label_report_result": _t("report_result", "Result"),
        "label_report_reference": _t("report_reference", "Reference"),
        "label_report_status": _t("report_status", "Status"),
        "label_report_alert_title": _t("report_alert_title", "For information only."),
        "label_report_alert_body": _t("report_alert_body", "This report does not replace medical diagnosis or treatment. Consult your doctor."),
        "label_report_disclaimer_title": _t("report_disclaimer_title", "For information only."),
        "label_report_disclaimer_text": _t("report_disclaimer_text", "This report does not replace medical diagnosis or treatment. Consult your doctor."),
        "label_report_footer": _t("report_footer", "Norya • For information only • support@noryaai.com"),
        "label_report_brand_sub": _t("report_brand_sub", "Clinical Report"),
        "label_report_doc_title": _t("report_doc_title", "Blood Test Analysis Report"),
        "label_report_doc_sub": _t("report_doc_sub", "Information-only clinical report format"),
        "label_report_rid": _t("report_rid_label", "Report No"),
        "label_report_user": _t("report_user_label", "User"),
        "label_report_date": _t("report_date_label_short", "Date"),
        "label_report_lang": _t("report_lang_label", "Language"),
        "label_verify_code": _t("report_verify_code", "Verification"),
        "label_report_verification_title": _t("report_verification_title", "Report Verification"),
        "label_report_verification_scan_hint": _t("report_verification_scan_hint", "Scan QR or enter the code on the verification page to confirm authenticity."),
        "label_report_page_title": _t("report_page_title", "Norya Clinical Report"),
        "label_report_health_score": _t("report_health_score", "Overall Health Score"),
        "label_report_risk_indicator": _t("report_risk_indicator", "Risk Indicator"),
        "label_report_trend_analysis": _t("report_trend_analysis", "Trend Analysis"),
        "label_report_health_age": _t("report_health_age_title", "Biological age estimate"),
        "health_age": health_age,
        "health_score_band_label": health_score_band_label,
        "gauge_svg": gauge_svg,
        "trend_has_data": trend_has_data,
        "trend_bars": trend_bars,
        "trend_svg": trend_svg,
        "trend_message": trend_message,
        "risk_distribution": risk_distribution,
        "dist_pct": dist_pct,
        "top_attention": top_attention,
        "radar_svg": radar_svg,
        "label_report_category_scores": _t("report_category_scores", "Category scores"),
        "label_report_risk_distribution": _t("report_risk_distribution", "Risk distribution"),
        "label_report_radar_balance": _t("report_radar_balance", "Biomarker balance"),
        "label_report_top_attention": _t("report_top_attention", "Top attention areas"),
        "label_dist_normal": _t("report_dist_normal", "Normal"),
        "label_dist_borderline": _t("report_dist_borderline", "Borderline"),
        "label_dist_attention": _t("report_dist_attention", "Attention"),
        "executive_summary": executive_summary,
        "summary_tiles": summary_tiles,
        "biomarker_highlights": biomarker_highlights,
        "key_areas_to_watch": key_areas_to_watch,
        "foods_to_favor": foods_to_favor,
        "foods_to_limit": foods_to_limit,
        "lifestyle_suggestions": lifestyle_suggestions,
        "movement_tips": movement_tips,
        "stress_tips": stress_tips,
        "sleep_tips": sleep_tips,
        "hydration_tips": hydration_tips,
        "doctor_discussion_notes": doctor_discussion_notes,
        "refined_disclaimer": refined_disclaimer,
        "trend_placeholder_text": trend_placeholder_text,
        "comparison_summary_text": (base_context.get("comparison_summary") or base_context.get("comparison", {}).get("summary") or "").strip(),
        "what_changed_items": _normalize_what_changed(base_context.get("what_changed") or (base_context.get("comparison") or {}).get("changes") or []),
        "label_report_comparison_title": _t("report_comparison_title", "Compare with previous analysis"),
        "label_report_what_changed_title": _t("report_what_changed_title", "What changed?"),
        "label_report_comparison_no_previous": _t("report_comparison_no_previous", "No previous analysis yet. After your next report, this section will show a comparison."),
        "label_report_what_changed_no_data": _t("report_what_changed_no_data", "Change summary will appear after your next report when comparison data is available."),
        "report_icons": REPORT_ICONS,
        "label_report_executive_summary": _t("report_executive_summary", "Executive Summary"),
        "label_report_summary_tiles": _t("report_summary_tiles", "Summary"),
        "label_report_biomarker_highlights": _t("report_biomarker_highlights", "Biomarker Highlights"),
        "label_report_risk_indicators": _t("report_risk_indicators", "Risk Indicators"),
        "label_report_risk_factors": _t("report_risk_factors", "Risk Factors"),
        "label_report_risk_factors_line_1": _t("report_risk_factors_line_1", "May indicate cardiovascular or metabolic factors. Discuss with your clinician."),
        "label_report_risk_factors_line_2": _t("report_risk_factors_line_2", "Lifestyle and diet may support overall wellness."),
        "label_report_key_areas": _t("report_key_areas", "Key Areas to Watch"),
        "label_report_foods_to_favor": _t("report_foods_to_favor", "Foods to Favor"),
        "label_report_foods_to_limit": _t("report_foods_to_limit", "Foods to Limit"),
        "label_report_foods_eat_heading": _t("report_foods_eat_heading", "Foods to Include"),
        "label_report_foods_avoid_heading": _t("report_foods_avoid_heading", "Foods to Avoid"),
        "label_report_lifestyle": _t("report_lifestyle", "Lifestyle Support"),
        "label_report_movement_heading": _t("report_movement_heading", "Movement & Exercise"),
        "label_report_stress_heading": _t("report_stress_heading", "Stress Management"),
        "label_report_sleep_heading": _t("report_sleep_heading", "Sleep & Rest"),
        "label_report_hydration_heading": _t("report_hydration_heading", "Hydration"),
        "label_report_attention_do": _t("report_attention_do", "What to pay attention to"),
        "label_report_attention_avoid": _t("report_attention_avoid", "What to avoid"),
        "label_report_common_refs": _t("report_common_refs", "Common reference ranges (info)"),
        "common_refs": [
            {"name": "Glucose (fasting)" if lang != "tr" else "Glukoz (açlık)", "ref": "70–100 mg/dL"},
            {"name": "HbA1c", "ref": "<5.7% normal"},
            {"name": "LDL cholesterol", "ref": "<100 mg/dL" if lang != "tr" else "<100 mg/dL optimal"},
            {"name": "HDL cholesterol", "ref": ">40 mg/dL (M), >50 (F)"},
            {"name": "CRP", "ref": "<3 mg/L"},
            {"name": "ALT", "ref": "7–56 U/L"},
        ],
        "label_report_doctor_discussion": _t("report_doctor_discussion", "Doctor Discussion Notes"),
        "label_report_tile_overall_score": _t("report_tile_overall_score", "Overall Score"),
        "label_report_tile_risk_level": _t("report_tile_risk_level", "Risk Level"),
        "label_report_tile_bio_age": _t("report_tile_bio_age", "Biological Age"),
        "label_report_tile_priority": _t("report_tile_priority", "Priority Focus"),
        "label_why_it_matters": _t("report_why_it_matters", "Why it matters"),
        "label_monitoring_focus": _t("report_monitoring_focus", "Monitoring focus"),
    }


def render_premium_pdf(context: dict) -> bytes:
    """Premium klinik rapor şablonu ile PDF üretir (WeasyPrint, running header/footer)."""
    from weasyprint import HTML
    context = dict(context)
    context["logo_base64"] = _logo_base64()
    template = _ENV.get_template("report_premium.html")
    html_str = template.render(**context)
    html_doc = HTML(string=html_str, base_url=str(_PROJECT_ROOT))
    return html_doc.write_pdf()


def render_doctor_pdf(context: dict) -> bytes:
    """Doktoruma götür şablonu ile PDF üretir (logo, hekime özel başlık ve uyarı metni)."""
    from weasyprint import HTML
    context = dict(context)
    context["logo_base64"] = _logo_base64()
    template = _ENV.get_template("doctor_pdf.html")
    html_str = template.render(**context)
    html_doc = HTML(string=html_str, base_url=str(_PROJECT_ROOT))
    return html_doc.write_pdf()


def _source_type_display(source: str | None, lang: str = "tr") -> str:
    """Kaynak türünü rapor diline göre görüntülenebilir metne çevirir."""
    if not source:
        return "—"
    m = {"text": "Metin" if lang == "tr" else "Text", "pdf": "PDF", "image": "Görsel" if lang == "tr" else "Image"}
    return m.get((source or "").strip().lower(), source)


def build_report_pdf(
    result_text: str,
    report_date: str | None = None,
    lang: str = "tr",
    *,
    report_id: str | int | None = None,
    user_identifier: str | None = None,
    patient_name: str | None = None,
    patient_age: str | None = None,
    patient_gender: str | None = None,
    plan_name: str | None = None,
    source_type: str | None = None,
    trend_data: dict | None = None,
    verification_info: dict | None = None,
) -> bytes:
    """result_text'ten PDF raporu üretir. premium plan ise report_premium.html, değilse report_pdf.html kullanılır.
    verification_info (aylık/yıllık pakette): report_id, verification_code, verification_url, qr_image_base64."""
    base_context = parse_report_to_context(result_text, report_date=report_date, lang=lang)
    report_date_str = base_context.get("report_date") or report_date or datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M")
    rid = str(report_id) if report_id is not None else "—"
    if verification_info and verification_info.get("report_id"):
        rid = str(verification_info["report_id"])
    user_id_str = (user_identifier or "").strip() or "—"
    plan = (plan_name or "").strip().lower()
    # Merkezi plan config (feature gating altyapısı; şablonlar ileride bu değerlere göre bölüm açacak)
    from app.core.plan_config import get_plan_config

    plan_cfg = get_plan_config(plan_name)
    plan_config_ctx = {
        "plan_name": plan_cfg.plan_name,
        "comparison_enabled": plan_cfg.comparison_enabled,
        "trend_enabled": plan_cfg.trend_enabled,
        "explanation_depth": plan_cfg.explanation_depth,
        "pdf_depth": plan_cfg.pdf_depth,
    }
    # premiumPdf: single, monthly, yearly, pro → premium şablon; premiumTrend: monthly, yearly, pro
    use_premium = plan == "premium" or plan in ("single", "monthly", "yearly", "pro")
    premium_trend = plan in ("monthly", "yearly", "pro")
    trend_locked = not premium_trend

    if use_premium:
        premium_ctx = _build_premium_context(
            base_context,
            report_id=rid,
            report_date=report_date_str,
            user_id=user_id_str,
            lang=lang,
            trend_data=trend_data,
            trend_locked=trend_locked,
        )
        if verification_info:
            premium_ctx["show_qr_verification"] = True
            premium_ctx["verification_url"] = verification_info.get("verification_url") or ""
            premium_ctx["verification_code"] = verification_info.get("verification_code") or ""
            premium_ctx["qr_image_base64"] = verification_info.get("qr_image_base64") or ""
        else:
            premium_ctx["show_qr_verification"] = False
            premium_ctx["verification_url"] = ""
            premium_ctx["verification_code"] = ""
            premium_ctx["qr_image_base64"] = ""
        premium_ctx["plan_config"] = plan_config_ctx
        _labels = _pdf_labels(lang)
        _fallback_en = PDF_LABELS.get("en", {})
        premium_ctx["label_report_doc_sub_single"] = _labels.get("report_doc_sub_single") or _fallback_en.get("report_doc_sub_single", "Single analysis report — Summary, values and recommendations; for information only.")
        premium_ctx["label_report_plan_badge_single"] = _labels.get("report_plan_badge_single") or _fallback_en.get("report_plan_badge_single", "REPORT")
        return render_premium_pdf(premium_ctx)

    context = base_context
    context["report_id"] = rid
    context["plan_config"] = plan_config_ctx
    context["user_id"] = user_id_str
    context["patient_name"] = (patient_name or "").strip() or "—"
    context["patient_age"] = (patient_age or "").strip() or "—"
    context["patient_gender"] = (patient_gender or "").strip() or "—"
    context["plan_name"] = (plan_name or "").strip() or "—"
    context["source_type"] = _source_type_display(source_type, lang)
    return render_pdf(context)


def build_doctor_pdf(
    result_text: str,
    report_date: str | None = None,
    lang: str = "tr",
) -> bytes:
    """result_text'ten 'Doktoruma götür' PDF'i üretir (aynı içerik, hekime özel başlık/banner)."""
    context = parse_report_to_context(result_text, report_date=report_date, lang=lang)
    return render_doctor_pdf(context)
