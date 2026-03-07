"""
Premium referans aralığı grafiği: SVG range bar + marker.
PDF raporuna gömülür; WeasyPrint ile keskin render için SVG kullanılır.
"""
import base64
# Renkler: İyi=yeşil, Sınırda=sarı, Düşük/Yüksek=kırmızı, arka plan gri
COLOR_NORMAL = "#16A34A"
COLOR_BORDER = "#F59E0B"
COLOR_RISK = "#DC2626"
COLOR_BG = "#E5E7EB"
COLOR_MARKER = "#1f2937"
COLOR_MARKER_TEXT = "#111827"
STATUS_LABELS = {"normal": "Normal", "low": "Riskli", "high": "Riskli", "border": "Sınır"}

WIDTH = 700
HEIGHT = 120
BAR_HEIGHT = 20
BAR_Y = 52
BAR_RX = 10
LABEL_Y = 38
MARKER_LINE_HEIGHT = 28
FONT_SIZE_LABEL = 13
FONT_SIZE_VALUE = 12
BADGE_X = WIDTH - 78
BADGE_Y = BAR_Y + BAR_HEIGHT // 2 - 8
BADGE_HEIGHT = 18
FONT_SIZE_BADGE = 11


def range_bar_svg(
    name: str,
    value: float,
    unit: str,
    ref_min: float,
    ref_max: float,
    status: str,
    display_min: float | None = None,
    display_max: float | None = None,
    status_label: str | None = None,
) -> str:
    """
    Tek parametre için SVG range bar grafiği döndürür. İyi/Düşük/Yüksek/Sınırda rozeti ekler.
    status: 'normal' | 'low' | 'high' | 'border'
    display_min/max yoksa ref aralığının %30 dışına taşarak otomatik hesaplanır.
    """
    badge_text = status_label or STATUS_LABELS.get(status, status)
    badge_color = COLOR_NORMAL if status == "normal" else (COLOR_BORDER if status == "border" else COLOR_RISK)
    if display_min is None or display_max is None:
        span = ref_max - ref_min
        padding = max(span * 0.3, span * 0.1) if span > 0 else 1.0
        display_min = min(ref_min, value) - padding
        display_max = max(ref_max, value) + padding
    if display_max <= display_min:
        display_max = display_min + 1.0

    range_span = display_max - display_min
    def x_pos(v: float) -> float:
        return 80 + (v - display_min) / range_span * (WIDTH - 160)

    # Bar bölgeleri: [display_min, ref_min), [ref_min, ref_max], (ref_max, display_max]
    x0 = 80
    x_ref_min = x_pos(ref_min)
    x_ref_max = x_pos(ref_max)
    x_end = WIDTH - 80

    # Renk: low = sol dışı risk, normal = orta yeşil, high = sağ dışı risk, border = sarı vurgu
    low_color = COLOR_RISK if status == "low" else COLOR_BG
    mid_color = COLOR_BORDER if status == "border" else COLOR_NORMAL
    high_color = COLOR_RISK if status == "high" else COLOR_BG

    value_x = x_pos(value)
    value_x_clamped = max(82, min(WIDTH - 100, value_x))
    value_label = f"{value:g}" + (f" {unit}" if unit else "")
    badge_width = min(56, len(badge_text) * 7)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" style="max-width:100%;height:auto;">
  <defs>
    <linearGradient id="gLow" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{low_color}"/><stop offset="1" stop-color="{low_color}"/></linearGradient>
    <linearGradient id="gMid" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{mid_color}"/><stop offset="1" stop-color="{mid_color}"/></linearGradient>
    <linearGradient id="gHigh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{high_color}"/><stop offset="1" stop-color="{high_color}"/></linearGradient>
  </defs>
  <text x="80" y="{LABEL_Y}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_LABEL}" font-weight="600" fill="{COLOR_MARKER_TEXT}">{_escape(name)}</text>
  <g transform="translate(0,{BAR_Y})">
    <rect x="{x0}" y="0" width="{x_ref_min - x0}" height="{BAR_HEIGHT}" rx="{BAR_RX}" ry="{BAR_RX}" fill="{low_color}"/>
    <rect x="{x_ref_min}" y="0" width="{x_ref_max - x_ref_min}" height="{BAR_HEIGHT}" rx="0" fill="{mid_color}"/>
    <rect x="{x_ref_max}" y="0" width="{x_end - x_ref_max}" height="{BAR_HEIGHT}" rx="{BAR_RX}" ry="{BAR_RX}" fill="{high_color}"/>
  </g>
  <line x1="{value_x_clamped}" y1="{BAR_Y + BAR_HEIGHT}" x2="{value_x_clamped}" y2="{BAR_Y + BAR_HEIGHT + MARKER_LINE_HEIGHT}" stroke="{COLOR_MARKER}" stroke-width="2.5" stroke-linecap="round"/>
  <text x="{value_x_clamped}" y="{BAR_Y + BAR_HEIGHT + MARKER_LINE_HEIGHT + 14}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_VALUE}" font-weight="700" fill="{COLOR_MARKER_TEXT}" text-anchor="middle">{_escape(value_label)}</text>
  <rect x="{BADGE_X}" y="{BADGE_Y}" width="{badge_width}" height="{BADGE_HEIGHT}" rx="9" fill="{badge_color}"/>
  <text x="{BADGE_X + badge_width / 2}" y="{BADGE_Y + BADGE_HEIGHT / 2 + 4}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_BADGE}" font-weight="600" fill="#fff" text-anchor="middle">{_escape(badge_text)}</text>
</svg>'''
    return svg


def _escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def simple_value_bar_svg(
    name: str,
    value: float,
    unit: str,
    status: str = "normal",
    status_label: str | None = None,
) -> str:
    """Referans aralığı olmayan parametre için tek çubuk: 0..max(value*1.3,1), değer işaretçi ve rozet."""
    display_max = max(value * 1.3, value + 1.0, 1.0)
    display_min = 0.0
    range_span = display_max - display_min
    if range_span <= 0:
        range_span = 1.0
    x_pos = lambda v: 80 + (v - display_min) / range_span * (WIDTH - 160)
    x0 = 80
    x_end = WIDTH - 80
    value_x = x_pos(value)
    value_x_clamped = max(82, min(WIDTH - 100, value_x))
    value_label = f"{value:g}" + (f" {unit}" if unit else "")
    badge_text = status_label or STATUS_LABELS.get(status, status)
    badge_color = COLOR_NORMAL if status == "normal" else (COLOR_BORDER if status == "border" else COLOR_RISK)
    badge_width = min(56, len(badge_text) * 7)
    bar_color = COLOR_NORMAL if status == "normal" else (COLOR_BORDER if status == "border" else COLOR_RISK)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" style="max-width:100%;height:auto;">
  <text x="80" y="{LABEL_Y}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_LABEL}" font-weight="600" fill="{COLOR_MARKER_TEXT}">{_escape(name)}</text>
  <g transform="translate(0,{BAR_Y})">
    <rect x="{x0}" y="0" width="{x_end - x0}" height="{BAR_HEIGHT}" rx="{BAR_RX}" ry="{BAR_RX}" fill="{COLOR_BG}"/>
    <rect x="{x0}" y="0" width="{value_x_clamped - x0}" height="{BAR_HEIGHT}" rx="{BAR_RX}" ry="{BAR_RX}" fill="{bar_color}"/>
  </g>
  <line x1="{value_x_clamped}" y1="{BAR_Y + BAR_HEIGHT}" x2="{value_x_clamped}" y2="{BAR_Y + BAR_HEIGHT + MARKER_LINE_HEIGHT}" stroke="{COLOR_MARKER}" stroke-width="2.5" stroke-linecap="round"/>
  <text x="{value_x_clamped}" y="{BAR_Y + BAR_HEIGHT + MARKER_LINE_HEIGHT + 14}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_VALUE}" font-weight="700" fill="{COLOR_MARKER_TEXT}" text-anchor="middle">{_escape(value_label)}</text>
  <rect x="{BADGE_X}" y="{BADGE_Y}" width="{badge_width}" height="{BADGE_HEIGHT}" rx="9" fill="{badge_color}"/>
  <text x="{BADGE_X + badge_width / 2}" y="{BADGE_Y + BADGE_HEIGHT / 2 + 4}" font-family="Helvetica,Arial,sans-serif" font-size="{FONT_SIZE_BADGE}" font-weight="600" fill="#fff" text-anchor="middle">{_escape(badge_text)}</text>
</svg>'''
    return svg


def simple_value_bar_svg_base64(
    name: str,
    value: float,
    unit: str,
    status: str = "normal",
    status_label: str | None = None,
) -> str:
    """Referansı olmayan parametre için basit çubuk grafik, base64."""
    svg = simple_value_bar_svg(name=name, value=value, unit=unit, status=status, status_label=status_label)
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")


def overall_score_svg(
    score: int,
    status: str,
    title: str = "Genel durum (0–100)",
    badge_label: str | None = None,
    include_title: bool = True,
) -> str:
    """
    Genel durum grafiği: 0-100 skor, yeşil/turuncu/kırmızı bölgeler.
    status: 'normal' | 'attention' | 'high' -> rozet rengi.
    include_title=False: PDF'te şablon zaten başlık veriyor, SVG içinde tekrar etmesin.
    """
    score = max(0, min(100, score))
    badge_text = badge_label or {"normal": "Normal", "attention": "Sınır", "high": "Riskli"}.get(status, "Normal")
    # 0-70 yeşil, 70-85 turuncu, 85-100 kırmızı (web ile aynı mantık)
    w = 600
    h = 100
    bar_y = 38
    bar_h = 22
    x0, x1, x2, x3 = 60, 60 + (w - 120) * 0.70, 60 + (w - 120) * 0.85, w - 60
    score_x = 60 + (w - 120) * (score / 100.0) if score <= 100 else w - 60
    score_x = max(62, min(w - 62, score_x))
    badge_color = COLOR_NORMAL if status == "normal" else (COLOR_BORDER if status == "attention" else COLOR_RISK)
    badge_w = min(58, len(badge_text) * 8)
    title_line = f'  <text x="60" y="22" font-family="Helvetica,Arial,sans-serif" font-size="13" font-weight="700" fill="{COLOR_MARKER_TEXT}">{_escape(title)}</text>\n' if include_title else ""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="max-width:100%;height:auto;">
{title_line}  <rect x="{x0}" y="{bar_y}" width="{x1 - x0}" height="{bar_h}" rx="6" fill="{COLOR_NORMAL}"/>
  <rect x="{x1}" y="{bar_y}" width="{x2 - x1}" height="{bar_h}" fill="{COLOR_BORDER}"/>
  <rect x="{x2}" y="{bar_y}" width="{x3 - x2}" height="{bar_h}" rx="6" fill="{COLOR_RISK}"/>
  <line x1="{score_x}" y1="{bar_y}" x2="{score_x}" y2="{bar_y + bar_h + 14}" stroke="{COLOR_MARKER}" stroke-width="2.5" stroke-linecap="round"/>
  <text x="{score_x}" y="{bar_y + bar_h + 32}" font-family="Helvetica,Arial,sans-serif" font-size="12" font-weight="700" fill="{COLOR_MARKER_TEXT}" text-anchor="middle">{score}/100</text>
  <rect x="{w - 60 - badge_w}" y="{bar_y + bar_h / 2 - 9}" width="{badge_w}" height="18" rx="9" fill="{badge_color}"/>
  <text x="{w - 60 - badge_w / 2}" y="{bar_y + bar_h / 2 + 4}" font-family="Helvetica,Arial,sans-serif" font-size="11" font-weight="600" fill="#fff" text-anchor="middle">{_escape(badge_text)}</text>
</svg>'''
    return svg


def overall_score_svg_base64(
    score: int,
    status: str,
    title: str = "Genel durum (0–100)",
    badge_label: str | None = None,
    include_title: bool = True,
) -> str:
    """Genel durum 0–100 grafiği, base64."""
    svg = overall_score_svg(score=score, status=status, title=title, badge_label=badge_label, include_title=include_title)
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")


def range_bar_svg_base64(
    name: str,
    value: float,
    unit: str,
    ref_min: float,
    ref_max: float,
    status: str,
    display_min: float | None = None,
    display_max: float | None = None,
    status_label: str | None = None,
) -> str:
    """Aynı parametrelerle SVG üretir ve base64 string döndürür (img src için). İyi/Düşük/Yüksek/Sınırda rozeti eklenir."""
    svg = range_bar_svg(
        name=name,
        value=value,
        unit=unit,
        ref_min=ref_min,
        ref_max=ref_max,
        status=status,
        display_min=display_min,
        display_max=display_max,
        status_label=status_label,
    )
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")
