#!/usr/bin/env python3
"""
Standard PDF (report_pdf.html) içinde kartların doğru görünmesini kontrol eder.
Özellikle: Hb/RBC/WBC/HCT/MCV/MCH/MCHC/PLT/CRP/Glucose/LDL/HDL/Vitamin D/Ferritin
ve Anti HCV/Anti HIV için test-bazlı "Ne gösterir?" + referans durumuna göre kısa yorumlar.

Çalıştırma (proje kökünden):
  python scripts/test_standard_pdf_example_cards.py

Oluşan dosya: test_standard_report_example_cards.pdf
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SAMPLE_RESULT_TEXT = """
**Özet**:
Genel durum iyi. Bazı parametreler referans sınırında veya referans dışı görünüyor.

**Risk göstergeleri**:
LDL, glukoz ve CRP takip edilmeli.

**Değerler**:
Datum: 18.03.2026.
Seite: 1.

**Hb**: 11.2 g/dL Reference: 13.5-17.5 g/dL. Low.
**RBC**: 3.9 M/µL Reference: 4.5-5.5 M/µL. Low.
**WBC**: 10.8 K/µL Reference: 4.5-11.0 K/µL. Borderline.
**HCT**: 35 % Reference: 38.8-50 %. Low.
**MCV**: 78 fL Reference: 80-100. Low.
**MCH**: 24 pg Reference: 27-33. Low.
**MCHC**: 30 g/dL Reference: 32-36. Low.
**PLT**: 420 K/µL Reference: 150-400. High.

**CRP**: 3.5 mg/L Reference: <3 mg/L. High.
**Glucose**: 105 mg/dL Reference: 70-100. High.

**LDL**: 105 mg/dL Reference: <100 mg/dL optimal. Borderline.
**HDL**: 38 mg/dL Reference: >40 mg/dL (M), >50 (F). Low.

Vitamin D**: 28 ng/mL Reference: 30-100. Borderline.
**Ferritin**: 18 ng/mL Reference: 12-150. Borderline.

**Anti HCV**: Nonreaktif.
**Anti HIV**: Reaktif.

**Olası nedenler**:
- Referans dışı sonuçlar klinik bağlamla birlikte değerlendirilmelidir.

**Öneriler**:
- Raporu doktorunuzla paylaşın; gerekirse takip ve tekrar ölçüm planlayın.
"""


def main() -> int:
    from app.services.report_pdf import build_report_pdf
    from app.services.report_verification import _qr_png_base64

    # QR'ın PDF içinde görünmesi için demo doğrulama bilgisi veriyoruz.
    base_url = "http://127.0.0.1:8015"
    report_id = "STD-EXAMPLE-CARDS-001"
    verification_url = f"{base_url}/verify/{report_id}?token=dev-token"
    verification_code = "DEV-SAMPLE"
    qr_b64 = _qr_png_base64(verification_url) or ""

    out_path = ROOT / "test_standard_report_example_cards.pdf"
    print("Standard PDF oluşturuluyor...")
    pdf_bytes = build_report_pdf(
        result_text=SAMPLE_RESULT_TEXT,
        report_date="07.03.2026 12:00",
        lang="tr",
        report_id=report_id,
        user_identifier="test@norya.com",
        patient_name="Test Kullanıcı",
        plan_name="free",
        source_type="text",
        verification_info={
            "report_id": report_id,
            "verification_code": verification_code,
            "verification_url": verification_url,
            "qr_image_base64": qr_b64,
        },
    )
    out_path.write_bytes(pdf_bytes)
    print(f"PDF yazıldı: {out_path}")
    print("Açmak için: open test_standard_report_example_cards.pdf  (macOS)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

