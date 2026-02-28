#!/usr/bin/env python3
"""Logo PNG'deki siyah arka plani seffaf yapar, istege bagli buyutur. Kullanim: python3 scripts/logo_transparent.py"""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow gerekli: pip install Pillow")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "static" / "logo.png"
OUT = ROOT / "static" / "logo.png"
SCALE = 1.25  # Biraz buyut
THRESHOLD = 40  # Bu degerin alti siyah sayilir, seffaf yapilir

if not LOGO.is_file():
    print("Bulunamadi:", LOGO)
    raise SystemExit(1)

img = Image.open(LOGO).convert("RGBA")
w, h = img.size
data = list(img.getdata())
new_data = []
for item in data:
    r, g, b, a = item
    if r <= THRESHOLD and g <= THRESHOLD and b <= THRESHOLD:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)
img.putdata(new_data)
# Buyut
nw, nh = int(w * SCALE), int(h * SCALE)
img = img.resize((nw, nh), Image.Resampling.LANCZOS)
img.save(OUT, "PNG")
print("Tamam: siyah arka plan kaldirildi, logo %d%% buyutuldu" % (SCALE * 100))
