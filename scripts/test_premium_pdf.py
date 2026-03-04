#!/usr/bin/env python3
"""
Premium PDF çıktısını görmek için test scripti.

Çalıştırma (proje kökünden):
  .venv/bin/python scripts/test_premium_pdf.py
  # veya uv kuruluysa: uv run python scripts/test_premium_pdf.py

Oluşan dosya: test_premium_report.pdf (proje kökünde)
Açmak: open test_premium_report.pdf
"""
import sys
from pathlib import Path

# Proje kökünü path'e ekle (app import için)
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Örnek rapor metni: parse_report_to_context'in beklediği **Başlık** bölümleri
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

# Trend verisi (premium PDF'de mini bar chart için)
SAMPLE_TREND_DATA = {
    "dates": ["01.01.2025", "15.01.2025", "01.02.2025"],
    "ldl": [128, 122, 118],
    "glucose": [98, 96, 95],
    "crp": [2.8, 2.5, 2.2],
}


def main():
    from app.services.report_pdf import build_report_pdf

    out_path = ROOT / "test_premium_report.pdf"
    print("Premium PDF oluşturuluyor...")
    pdf_bytes = build_report_pdf(
        result_text=SAMPLE_RESULT_TEXT,
        report_date="03.03.2025 14:00",
        lang="tr",
        report_id="TEST-001",
        user_identifier="test@norya.com",
        patient_name="Test Kullanıcı",
        plan_name="premium",
        source_type="text",
        trend_data=SAMPLE_TREND_DATA,
    )
    out_path.write_bytes(pdf_bytes)
    print(f"PDF yazıldı: {out_path}")
    print("Açmak için: open test_premium_report.pdf  (macOS) veya xdg-open test_premium_report.pdf (Linux)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
