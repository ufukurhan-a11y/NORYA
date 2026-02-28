#!/usr/bin/env python3
"""Logo PNG'deki siyah/şeffaf arka planı BEYAZ yapar. Her yerde aynı logo (beyaz arka plan).
   Kullanim: python3 scripts/logo_white_bg.py
   Gereksinim: Pillow (pip install Pillow veya .venv içinde)"""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow gerekli: pip install Pillow")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "static" / "logo.png"
OUT = ROOT / "static" / "logo.png"
THRESHOLD = 45  # Bu degerin alti siyah/koyu sayilir -> beyaz yapilir

if not LOGO.is_file():
    print("Bulunamadi:", LOGO)
    raise SystemExit(1)

img = Image.open(LOGO).convert("RGBA")
w, h = img.size
data = list(img.getdata())
new_data = []
white = (255, 255, 255, 255)
for item in data:
    r, g, b, a = item
    # Siyah veya cok koyu pikseller -> beyaz arka plan
    if (r <= THRESHOLD and g <= THRESHOLD and b <= THRESHOLD) or a < 128:
        new_data.append(white)
    else:
        new_data.append(item)
img.putdata(new_data)
# Beyaz arka plan icin RGB'ye cevir (PNG olarak kaydedince alpha kalir ama WeasyPrint vs icin bazen RGB yeterli)
img.save(OUT, "PNG")
print("Tamam: logo arka plani beyaz yapildi.", OUT)
