#!/usr/bin/env python3
"""
Generate Norya app icons from N-only icon: transparent background, multiple sizes.
Output: favicon 16x16, 32x32; apple-touch 180x180; PWA 192x192, 512x512.
"""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Install Pillow: pip install Pillow")

ASSETS = Path("/Users/ufukurhan/.cursor/projects/Users-ufukurhan-norya/assets")
SRC = ASSETS / "IMG_9337-4f97b837-1b4b-4833-8730-f22d55c2ae52.png"
OUT_DIR = Path(__file__).resolve().parent.parent / "static" / "icons"

# White/near-white → transparent
WHITE_THRESHOLD = 248

# Sizes: (filename, (w, h))
SIZES = [
    ("favicon-16x16.png", (16, 16)),
    ("favicon-32x32.png", (32, 32)),
    ("apple-touch-icon.png", (180, 180)),
    ("icon-192.png", (192, 192)),
    ("icon-512.png", (512, 512)),
]


def main():
    if not SRC.exists():
        raise SystemExit(f"Source image not found: {SRC}")

    img = Image.open(SRC).convert("RGBA")
    data = img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata()
    out_data = []
    for r, g, b, a in data:
        if r >= WHITE_THRESHOLD and g >= WHITE_THRESHOLD and b >= WHITE_THRESHOLD:
            out_data.append((r, g, b, 0))
        else:
            out_data.append((r, g, b, a))
    img.putdata(out_data)

    bbox = img.getbbox()
    if not bbox:
        raise SystemExit("Image is fully transparent after removing background.")
    img = img.crop(bbox)

    # Icon is roughly square; fit to square for consistent favicon/app icon
    w, h = img.size
    side = max(w, h)
    square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    ox = (side - w) // 2
    oy = (side - h) // 2
    square.paste(img, (ox, oy))
    img = square

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, (size_w, size_h) in SIZES:
        out = img.resize((size_w, size_h), Image.Resampling.LANCZOS)
        out_path = OUT_DIR / name
        out.save(out_path, "PNG", optimize=True)
        print(f"Saved: {out_path} ({size_w}x{size_h})")


if __name__ == "__main__":
    main()
