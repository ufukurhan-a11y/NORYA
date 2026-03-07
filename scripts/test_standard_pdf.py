#!/usr/bin/env python3
"""
Standart PDF (report_pdf.html) çıktısını görmek için test scripti.

Çalıştırma (proje kökünden):
  .venv/bin/python scripts/test_standard_pdf.py
  # veya: uv run python scripts/test_standard_pdf.py

Oluşan dosya: test_standard_report.pdf (proje kökünde)
Açmak: open test_standard_report.pdf
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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
    from app.services.report_pdf import build_report_pdf

    out_path = ROOT / "test_standard_report.pdf"
    print("Standart PDF oluşturuluyor...")
    pdf_bytes = build_report_pdf(
        result_text=SAMPLE_RESULT_TEXT,
        report_date="07.03.2026 12:00",
        lang="tr",
        report_id="STD-TEST-001",
        user_identifier="test@norya.com",
        patient_name="Test Kullanıcı",
        plan_name="free",
        source_type="text",
    )
    out_path.write_bytes(pdf_bytes)
    print(f"PDF yazıldı: {out_path}")
    print("Açmak için: open test_standard_report.pdf  (macOS)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
