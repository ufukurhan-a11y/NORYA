#!/usr/bin/env python3
"""
Aylık abonelik (monthly) PDF çıktısını kontrol etmek için test scripti.
Premium şablon + trend + doğrulama kodu ile rapor üretir.

Çalıştırma (proje kökünden):
  .venv/bin/python scripts/test_monthly_pdf.py
  # veya: uv run python scripts/test_monthly_pdf.py

Oluşan dosya: test_monthly_report.pdf (proje kökünde)
Açmak: open test_monthly_report.pdf
"""
import sys
import os
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

SAMPLE_TREND_DATA = {
    "dates": ["01.01.2025", "15.01.2025", "01.02.2025"],
    "ldl": [128, 122, 118],
    "glucose": [98, 96, 95],
    "crp": [2.8, 2.5, 2.2],
}


def main():
    from app.services.report_verification import _qr_png_base64
    from app.services.report_pdf import build_report_pdf

    base_url = (os.environ.get("VERIFY_BASE_URL") or "http://127.0.0.1:8000").strip().rstrip("/")
    report_id = "test-monthly-uuid-87654321"
    token = "mock-monthly"
    verification_url = f"{base_url}/verify/{report_id}?token={token}"

    qr_b64 = _qr_png_base64(verification_url)
    if not qr_b64:
        print("Uyarı: QR görseli üretilemedi (qrcode kurulu mu?).")
    verification_info = {
        "report_id": report_id,
        "verification_code": "MONTH99",
        "verification_url": verification_url,
        "qr_image_base64": qr_b64 or "",
    }

    out_path = ROOT / "test_monthly_report.pdf"
    print("Aylık abonelik (monthly) PDF oluşturuluyor...")
    pdf_bytes = build_report_pdf(
        result_text=SAMPLE_RESULT_TEXT,
        report_date="07.03.2026 14:00",
        lang="tr",
        report_id="MONTHLY-TEST-001",
        user_identifier="test-monthly@norya.com",
        patient_name="Test Aylık Kullanıcı",
        plan_name="monthly",
        source_type="text",
        trend_data=SAMPLE_TREND_DATA,
        verification_info=verification_info,
    )
    out_path.write_bytes(pdf_bytes)
    print(f"PDF yazıldı: {out_path}")
    print("Açmak için: open test_monthly_report.pdf")
    return 0


if __name__ == "__main__":
    sys.exit(main())
