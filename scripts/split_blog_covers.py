from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
GRID_PATH = ROOT / "static" / "images" / "blog" / "covers_grid.png"
OUTPUT_DIR = ROOT / "static" / "images" / "blog"

# Soldan sağa, yukarıdan aşağı sıralama
OUTPUT_NAMES = [
    "ferritin.webp",
    "b12.webp",
    "crp.webp",
    "alt-ast.webp",
    "vitamin-d.webp",
    "cbc.webp",
]


def _get_resample():
    # Pillow 10+ için Image.Resampling, eski sürümler için Image.LANCZOS
    return getattr(Image, "Resampling", Image).LANCZOS


def split_covers() -> None:
    if not GRID_PATH.is_file():
        raise SystemExit(f"Grid image not found: {GRID_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    img = Image.open(GRID_PATH).convert("RGB")
    w, h = img.size

    cols, rows = 2, 3
    tile_w = w // cols
    tile_h = h // rows

    target_size = (1200, 675)
    resample = _get_resample()

    index = 0
    for row in range(rows):
        for col in range(cols):
            if index >= len(OUTPUT_NAMES):
                break
            left = col * tile_w
            upper = row * tile_h
            right = left + tile_w
            lower = upper + tile_h

            tile = img.crop((left, upper, right, lower))
            tile = tile.resize(target_size, resample=resample)

            out_name = OUTPUT_NAMES[index]
            out_path = OUTPUT_DIR / out_name
            tile.save(out_path, format="WEBP", quality=90, method=6)
            print(f"Saved {out_path}")
            index += 1


if __name__ == "__main__":
    split_covers()

