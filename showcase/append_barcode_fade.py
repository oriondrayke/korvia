#!/usr/bin/env python3
"""Append 5 Korvia barcode-fade logo concepts (IDs 264-268) in the Moonlight setting."""
from pathlib import Path

TAGLINES = ["QR inafungua uzo"] * 5

BLUES = ["#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"]

MOONLIGHT_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(20,30,50,0.9); color: #f8fafc; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(20,30,50,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #C0C0C0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; box-shadow: inset -12px -5px 0 0 #C0C0C0; display: inline-block; margin-right: 16px; }
"""

PORTAL_CONTENT = '''<div class="logo-square">Korvia</div>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">{tagline}</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>'''

CONTENT_TEMPLATE = '''<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
.logo-mark { text-align: center; margin: 24px 0 16px; }
.logo-mark svg { max-width: 440px; width: 100%; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-mark">{svg}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


def make_bars(start_x, end_x, count=40, full_height=100, y=10):
    """Generate a string of vertical barcode rect elements."""
    out = []
    span = end_x - start_x
    base = span / count
    x = start_x
    for i in range(count):
        w = base * (0.6 + (i % 4) * 0.2)
        if w < 1.2:
            w = 1.2
        color = BLUES[i % len(BLUES)]
        if i % 7 == 3:
            h = full_height * 0.5
            y_off = y + (full_height - h) / 2
        else:
            h = full_height
            y_off = y
        out.append(f'  <rect x="{x:.1f}" y="{y_off:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{color}"/>')
        x += base
    return "\n".join(out)


def build_content(svg, tagline):
    portal = PORTAL_CONTENT.replace("{tagline}", tagline)
    return CONTENT_TEMPLATE.replace("{svg}", svg).replace("{tagline}", tagline).replace("{portal}", portal)


BARCODE_FADE_LR_SVG = f'''<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg" aria-label="Barcode fade left to right">
  <defs>
    <linearGradient id="barFade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="white"/>
      <stop offset="55%" stop-color="white"/>
      <stop offset="100%" stop-color="black"/>
    </linearGradient>
    <mask id="fadeMask">
      <rect x="0" y="0" width="240" height="120" fill="url(#barFade)"/>
    </mask>
    <linearGradient id="textFade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C0C0C0" stop-opacity="0"/>
      <stop offset="45%" stop-color="#C0C0C0" stop-opacity="0"/>
      <stop offset="100%" stop-color="#C0C0C0"/>
    </linearGradient>
  </defs>
  <g mask="url(#fadeMask)" opacity="0.95">
{make_bars(12, 230, count=38)}
  </g>
  <text x="300" y="78" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="url(#textFade)">KORVIA</text>
</svg>'''

BARCODE_MORPH_SVG = f'''<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg" aria-label="Barcode letter morph">
  <defs>
    <clipPath id="morphText">
      <text x="230" y="82" font-family="Cinzel, serif" font-size="64" font-weight="700" text-anchor="middle" letter-spacing="0.08em">KORVIA</text>
    </clipPath>
  </defs>
  <g opacity="0.85">
{make_bars(10, 150, count=22)}
  </g>
  <g clip-path="url(#morphText)">
{make_bars(140, 390, count=28)}
  </g>
</svg>'''

NEGATIVE_REVEAL_SVG = f'''<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg" aria-label="Negative barcode reveal">
  <defs>
    <radialGradient id="edgeFade" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" stop-color="black"/>
      <stop offset="40%" stop-color="black"/>
      <stop offset="100%" stop-color="white"/>
    </radialGradient>
    <mask id="negativeMask">
      <rect x="0" y="0" width="400" height="120" fill="url(#edgeFade)"/>
      <text x="200" y="82" font-family="Cinzel, serif" font-size="68" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="black">KORVIA</text>
    </mask>
  </defs>
  <g mask="url(#negativeMask)">
    <rect x="10" y="10" width="380" height="100" fill="#1E3A8A" opacity="0.25"/>
{make_bars(10, 390, count=48)}
  </g>
</svg>'''

SCAN_REVEAL_SVG = f'''<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg" aria-label="Scan reveal">
  <defs>
    <linearGradient id="scanGlow" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#60A5FA" stop-opacity="0"/>
      <stop offset="50%" stop-color="#60A5FA" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#60A5FA" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="topClip">
      <rect x="0" y="0" width="400" height="58"/>
    </clipPath>
  </defs>
  <text x="200" y="80" font-family="Cinzel, serif" font-size="64" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#C0C0C0">KORVIA</text>
  <g clip-path="url(#topClip)" opacity="0.9">
{make_bars(20, 380, count=40)}
  </g>
  <rect x="20" y="56" width="360" height="3" fill="#93C5FD"/>
  <rect x="20" y="52" width="360" height="12" fill="url(#scanGlow)" opacity="0.6"/>
</svg>'''

BARCODE_TYPE_SVG = f'''<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg" aria-label="Barcode type">
  <defs>
    <clipPath id="typeText">
      <text x="200" y="84" font-family="Cinzel, serif" font-size="72" font-weight="700" text-anchor="middle" letter-spacing="0.08em">KORVIA</text>
    </clipPath>
  </defs>
  <g clip-path="url(#typeText)">
{make_bars(20, 380, count=52)}
  </g>
  <text x="200" y="84" font-family="Cinzel, serif" font-size="72" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="none" stroke="#C0C0C0" stroke-width="1" opacity="0.35">KORVIA</text>
</svg>'''


CONCEPTS = [
    {
        "id": "264",
        "name": "Barcode Fade Left-to-Right",
        "desc": "Dense vertical blue barcode on the left gradually resolves into the Korvia wordmark on the right.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"],
        "shapes": ["wordmark", "barcode", "fade", "transition"],
        "mark_css": ".logo-mark svg { max-width: 440px; filter: drop-shadow(0 0 22px rgba(30,58,138,0.45)); }",
        "svg": BARCODE_FADE_LR_SVG,
    },
    {
        "id": "265",
        "name": "Barcode Letter Morph",
        "desc": "Each barcode stripe bends and morphs into a stroke of the corresponding Korvia letter.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"],
        "shapes": ["wordmark", "barcode", "morph"],
        "mark_css": ".logo-mark svg { max-width: 440px; filter: drop-shadow(0 0 20px rgba(192,192,192,0.35)); }",
        "svg": BARCODE_MORPH_SVG,
    },
    {
        "id": "266",
        "name": "Negative Barcode Reveal",
        "desc": "A solid blue barcode block fades out, leaving Korvia as negative space in the center.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"],
        "shapes": ["wordmark", "barcode", "negative-space", "reveal"],
        "mark_css": ".logo-mark svg { max-width: 440px; filter: drop-shadow(0 0 24px rgba(30,58,138,0.5)); }",
        "svg": NEGATIVE_REVEAL_SVG,
    },
    {
        "id": "267",
        "name": "Scan Reveal",
        "desc": "A horizontal blue scan line moves down through the barcode, revealing Korvia letterforms behind it.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"],
        "shapes": ["wordmark", "barcode", "scan", "reveal"],
        "mark_css": ".logo-mark svg { max-width: 440px; filter: drop-shadow(0 0 18px rgba(30,58,138,0.55)); }",
        "svg": SCAN_REVEAL_SVG,
    },
    {
        "id": "268",
        "name": "Barcode Type",
        "desc": "The word Korvia is built entirely from vertical barcode lines of varying blue widths.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD"],
        "shapes": ["wordmark", "barcode", "type"],
        "mark_css": ".logo-mark svg { max-width: 440px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.3)); }",
        "svg": BARCODE_TYPE_SVG,
    },
]


def build_entry(c, tagline):
    css = MOONLIGHT_CSS.strip() + "\n" + c["mark_css"]
    content = build_content(c["svg"], tagline)
    return f'''    {{
        "id": "{c['id']}",
        "name": "{c['name']}",
        "tagline": "{tagline}",
        "desc": "{c['desc']}",
        "palette": {c['palette']},
        "shapes": {c['shapes']},
        "css": """
{css}
        """,
        "content": """
{content}
        """
    }},'''


def main():
    target = Path("showcase/generate_showcase.py")
    text = target.read_text(encoding="utf-8")
    marker = "    },\n]\n\nBASE = \"\"\""
    if marker not in text:
        print("Marker not found")
        return
    insert = "\n".join(build_entry(c, TAGLINES[i]) for i, c in enumerate(CONCEPTS)).rstrip() + "\n"
    new_text = text.replace(marker, "    },\n" + insert + "]\n\nBASE = \"\"\"")
    target.write_text(new_text, encoding="utf-8")
    print(f"Appended {len(CONCEPTS)} barcode fade concepts.")


if __name__ == "__main__":
    main()
