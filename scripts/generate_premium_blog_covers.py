from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "static" / "images" / "blog"
LOGO_PATH = ROOT / "static" / "norya_logo_transparent_trim.png"
OUT_SIZE = (1600, 900)

ARTICLES = [
    {
        "slug": "amh-test-ovarian-reserve",
        "file": "amh-hero.jpg",
        "title": "AMH Test",
        "subtitle": "Ovarian reserve and fertility context",
        "badge": "Fertility marker",
        "source": "static/images/blog/estradiol-hero.jpg",
        "accent": (34, 211, 238),
        "accent_2": (16, 185, 129),
        "focus": "left",
    },
    {
        "slug": "ana-antinuclear-antibody-test",
        "file": "ana-hero.jpg",
        "title": "ANA Test",
        "subtitle": "Autoimmune screening and antibody context",
        "badge": "Autoimmune screening",
        "source": "static/images/blog/neutrophils-hero.jpg",
        "accent": (168, 85, 247),
        "accent_2": (59, 130, 246),
        "focus": "left",
    },
    {
        "slug": "amylase-high-meaning",
        "file": "amylase-hero.jpg",
        "title": "Amylase",
        "subtitle": "Digestive enzyme and lab interpretation",
        "badge": "Enzyme marker",
        "source": "static/images/blog/hematocrit-hero.jpg",
        "accent": (245, 158, 11),
        "accent_2": (239, 68, 68),
        "focus": "right",
    },
    {
        "slug": "homocysteine-high-meaning",
        "file": "homocysteine-hero.jpg",
        "title": "Homocysteine",
        "subtitle": "Heart and vessel risk context",
        "badge": "Cardiovascular marker",
        "source": "static/images/blog/troponin-hero.jpg",
        "accent": (14, 165, 233),
        "accent_2": (99, 102, 241),
        "focus": "left",
    },
    {
        "slug": "rheumatoid-factor-rf-test",
        "file": "rf-hero.jpg",
        "title": "Rheumatoid Factor",
        "subtitle": "Inflammation and clinical evaluation",
        "badge": "Inflammatory clue",
        "source": "static/images/blog/hemoglobin-hero.jpg",
        "accent": (45, 212, 191),
        "accent_2": (59, 130, 246),
        "focus": "left",
    },
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates: list[str] = []
    if bold:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                "/Library/Fonts/Arial Bold.ttf",
                "/System/Library/Fonts/SFNS.ttf",
            ]
        )
    else:
        candidates.extend(
            [
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                "/Library/Fonts/Arial.ttf",
                "/System/Library/Fonts/Supplemental/Helvetica.ttc",
            ]
        )
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def load_photo(cfg: dict) -> Image.Image:
    source = ROOT / cfg["source"]
    if not source.exists():
        raise SystemExit(f"Missing source image: {source}")
    img = Image.open(source).convert("RGB")
    return ImageOps.fit(img, OUT_SIZE, method=Image.Resampling.LANCZOS, centering=_centering(cfg.get("focus", "center")))


def _centering(focus: str) -> tuple[float, float]:
    if focus == "left":
        return (0.35, 0.5)
    if focus == "right":
        return (0.7, 0.5)
    return (0.5, 0.5)


def add_photo_grade(base: Image.Image, cfg: dict) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = base.size

    for i in range(18):
        alpha = int(150 - i * 6)
        draw.rounded_rectangle(
            (30 + i, 30 + i, w - 30 - i, h - 30 - i),
            radius=34,
            outline=(255, 255, 255, max(alpha, 18)),
            width=1,
        )

    left_tint = Image.new("RGBA", base.size, cfg["accent"] + (0,))
    left_mask = Image.new("L", base.size, 0)
    left_draw = ImageDraw.Draw(left_mask)
    left_draw.rectangle((0, 0, int(w * 0.64), h), fill=225)
    left_mask = left_mask.filter(ImageFilter.GaussianBlur(150))
    overlay.alpha_composite(left_tint, (0, 0))
    overlay.putalpha(ImageChopsScreen(overlay.getchannel("A"), left_mask))

    dark = Image.new("RGBA", base.size, (7, 12, 24, 0))
    dark_mask = Image.new("L", base.size, 0)
    dark_draw = ImageDraw.Draw(dark_mask)
    dark_draw.rectangle((0, 0, int(w * 0.7), h), fill=205)
    dark_draw.rectangle((0, int(h * 0.72), w, h), fill=140)
    dark_mask = dark_mask.filter(ImageFilter.GaussianBlur(120))
    dark.putalpha(dark_mask)
    overlay.alpha_composite(dark)

    flare = Image.new("RGBA", base.size, cfg["accent_2"] + (0,))
    flare_mask = Image.new("L", base.size, 0)
    flare_draw = ImageDraw.Draw(flare_mask)
    flare_draw.ellipse((int(w * 0.66), int(h * 0.06), int(w * 1.02), int(h * 0.62)), fill=105)
    flare_mask = flare_mask.filter(ImageFilter.GaussianBlur(95))
    flare.putalpha(flare_mask)
    overlay.alpha_composite(flare)

    vignette = Image.new("RGBA", base.size, (0, 0, 0, 0))
    vig_mask = Image.new("L", base.size, 0)
    vig_draw = ImageDraw.Draw(vig_mask)
    vig_draw.rounded_rectangle((8, 8, w - 8, h - 8), radius=42, fill=255)
    vig_mask = ImageOps.invert(vig_mask.filter(ImageFilter.GaussianBlur(120)))
    vignette.putalpha(vig_mask)
    overlay.alpha_composite(vignette)

    base.alpha_composite(overlay)


def add_glass_panel(base: Image.Image, cfg: dict) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = base.size
    panel = (84, 96, 820, 664)
    draw.rounded_rectangle(panel, radius=38, fill=(12, 20, 36, 150), outline=(255, 255, 255, 56), width=2)
    highlight = (panel[0] + 24, panel[1] + 22, panel[2] - 24, panel[1] + 86)
    draw.rounded_rectangle(highlight, radius=24, fill=cfg["accent"] + (72,))
    base.alpha_composite(overlay)


def draw_text_block(base: Image.Image, cfg: dict) -> None:
    draw = ImageDraw.Draw(base)
    title_font = load_font(84, bold=True)
    subtitle_font = load_font(38, bold=False)
    badge_font = load_font(29, bold=True)
    body_font = load_font(25, bold=False)

    x = 140
    y = 138

    draw.text((x, y), cfg["badge"], font=badge_font, fill=(239, 250, 255))
    draw.text((x, y + 110), cfg["title"], font=title_font, fill=(255, 255, 255))
    draw.text((x, y + 220), cfg["subtitle"], font=subtitle_font, fill=(223, 235, 246))

    bullets = [
        "Photo-based premium medical cover",
        "Real clinical visual context",
        "Educational lab-result article",
    ]
    bullet_y = y + 326
    for i, text in enumerate(bullets):
        row_y = bullet_y + i * 48
        draw.ellipse((x, row_y + 8, x + 13, row_y + 21), fill=cfg["accent_2"] + (255,))
        draw.text((x + 28, row_y), text, font=body_font, fill=(225, 232, 241))


def add_logo(base: Image.Image) -> None:
    if not LOGO_PATH.exists():
        raise SystemExit(f"Logo missing: {LOGO_PATH}")
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo = ImageOps.contain(logo, (280, 72), Image.Resampling.LANCZOS)

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    w, h = base.size
    box = (w - 360, h - 120, w - 72, h - 46)
    draw.rounded_rectangle(box, radius=22, fill=(255, 255, 255, 225), outline=(255, 255, 255, 70), width=2)
    logo_x = box[0] + (box[2] - box[0] - logo.width) // 2
    logo_y = box[1] + (box[3] - box[1] - logo.height) // 2
    overlay.paste(logo, (logo_x, logo_y), logo)
    base.alpha_composite(overlay)


def add_bottom_fade(base: Image.Image) -> None:
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    w, h = base.size
    mask = Image.new("L", base.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((0, int(h * 0.7), w, h), fill=170)
    mask = mask.filter(ImageFilter.GaussianBlur(70))
    overlay.paste((5, 10, 20, 220), (0, 0, w, h))
    overlay.putalpha(mask)
    base.alpha_composite(overlay)


def build_cover(cfg: dict) -> Image.Image:
    photo = load_photo(cfg).convert("RGBA")
    add_photo_grade(photo, cfg)
    add_glass_panel(photo, cfg)
    draw_text_block(photo, cfg)
    add_bottom_fade(photo)
    add_logo(photo)
    return photo.convert("RGB")


def ImageChopsScreen(a: Image.Image, b: Image.Image) -> Image.Image:
    return ImageChops_like_screen(a, b)


def ImageChops_like_screen(a: Image.Image, b: Image.Image) -> Image.Image:
    a = a.convert("L")
    b = b.convert("L")
    out = Image.new("L", a.size)
    ap = a.load()
    bp = b.load()
    op = out.load()
    w, h = a.size
    for y in range(h):
        for x in range(w):
            av = ap[x, y]
            bv = bp[x, y]
            op[x, y] = 255 - ((255 - av) * (255 - bv) // 255)
    return out


def main() -> None:
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    for cfg in ARTICLES:
        out_path = BLOG_DIR / cfg["file"]
        image = build_cover(cfg)
        image.save(out_path, quality=93, optimize=True)
        print(f"Saved {out_path.relative_to(ROOT)} from {cfg['source']}")


if __name__ == "__main__":
    main()
