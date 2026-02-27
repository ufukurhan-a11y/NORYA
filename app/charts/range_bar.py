"""
Premium referans aralığı grafiği: SVG range bar + marker.
PDF raporuna gömülür; WeasyPrint ile keskin render için SVG kullanılır.
"""
import base64
# Renkler: normal yeşil, sınır sarı, risk kırmızı, arka plan gri
COLOR_NORMAL = "#16A34A"
COLOR_BORDER = "#F59E0B"
COLOR_RISK = "#DC2626"
COLOR_BG = "#E5E7EB"
COLOR_MARKER = "#1f2937"
COLOR_MARKER_TEXT = "#111827"

WIDTH = 700
HEIGHT = 120
BAR_HEIGHT = 20
BAR_Y = 52
BAR_RX = 10
LABEL_Y = 38
MARKER_LINE_HEIGHT = 28
FONT_SIZE_LABEL = 13
FONT_SIZE_VALUE = 12


def range_bar_svg(
    name: str,
    value: float,
    unit: str,
    ref_min: float,
    ref_max: float,
    status: str,
    display_min: float | None = None,
    display_max: float | None = None,
) -> str:
    """
    Tek parametre için SVG range bar grafiği döndürür.
    status: 'normal' | 'low' | 'high' | 'border'
    display_min/max yoksa ref aralığının %30 dışına taşarak otomatik hesaplanır.
    """
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
    value_x_clamped = max(82, min(WIDTH - 82, value_x))
    value_label = f"{value:g}" + (f" {unit}" if unit else "")

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
</svg>'''
    return svg


def _escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def range_bar_svg_base64(
    name: str,
    value: float,
    unit: str,
    ref_min: float,
    ref_max: float,
    status: str,
    display_min: float | None = None,
    display_max: float | None = None,
) -> str:
    """Aynı parametrelerle SVG üretir ve base64 string döndürür (img src için)."""
    svg = range_bar_svg(
        name=name,
        value=value,
        unit=unit,
        ref_min=ref_min,
        ref_max=ref_max,
        status=status,
        display_min=display_min,
        display_max=display_max,
    )
    return base64.b64encode(svg.encode("utf-8")).decode("ascii")
