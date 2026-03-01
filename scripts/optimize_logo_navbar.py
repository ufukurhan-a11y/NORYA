#!/usr/bin/env python3
"""
Optimize Norya logo for navbar: transparent background, tight crop, high-res PNG.
"""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow: pip install Pillow")

# Paths
ASSETS = Path("/Users/ufukurhan/.cursor/projects/Users-ufukurhan-norya/assets")
SRC = ASSETS / "IMG_9336-aa63e877-2394-440b-9bbf-028b3878b589.png"
OUT_DIR = Path(__file__).resolve().parent.parent / "static"
OUT = OUT_DIR / "norya_logo_transparent_trim.png"

# White → transparent threshold (0–255). Pixels with R,G,B all >= this become transparent.
WHITE_THRESHOLD = 248
# Retina: scale factor for export (2 = 2x resolution for sharpness)
RETINA_SCALE = 2


def main():
    if not SRC.exists():
        raise SystemExit(f"Source image not found: {SRC}")

    img = Image.open(SRC).convert("RGBA")
    w, h = img.size
    data = img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()
    out_data = []
    for r, g, b, a in data:
        if r >= WHITE_THRESHOLD and g >= WHITE_THRESHOLD and b >= WHITE_THRESHOLD:
            out_data.append((r, g, b, 0))
        else:
            out_data.append((r, g, b, a))

    img.putdata(out_data)

    # Trim: get bounding box of non‑fully‑transparent pixels
    bbox = img.getbbox()
    if not bbox:
        raise SystemExit("Image is fully transparent after removing background.")
    img = img.crop(bbox)

    # Optional: scale up for retina (keeps aspect ratio, sharp)
    if RETINA_SCALE > 1:
        nw, nh = img.size
        img = img.resize((nw * RETINA_SCALE, nh * RETINA_SCALE), Image.Resampling.LANCZOS)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"Saved: {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
