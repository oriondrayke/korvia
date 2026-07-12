#!/usr/bin/env python3
"""Append 20 minimal abstract Korvia logo-mark concepts (IDs 219-238) in the Moonlight setting."""
from pathlib import Path

TAGLINES = [
    "Karibu, tukuhudumie",
    "Chakula, kulala, sherehe",
    "Kila chombo, kidigitali",
    "QR inafungua uzo",
    "Huduma mkononi",
    "Karibu kwenye mfumo",
    "Kila mgeni, muhimu",
    "Orderi kwa kiganja",
    "Upishi, ukumbi, usiku",
    "Mfumo wa mapokezi",
    "Chapa, scan, huduma",
    "Ramani ya hoteli",
    "Kila kivinjari, kimoja",
    "Msimbo wa huduma",
    "Kitovu cha ukarimu",
    "Fungua uzo kwa simu",
    "Mfumo wa kisasa",
    "Punguza mzozo, ongeza starehe",
    "Kila chumba, kila chakula, kila tukio",
    "Ukarimu wa kidigitali",
]

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


def build_content(svg, tagline):
    portal = PORTAL_CONTENT.replace("{tagline}", tagline)
    return f'''<style>
.portal-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }}
.logo-mark {{ text-align: center; margin: 0 0 12px; }}
.logo-mark svg {{ max-width: 340px; width: 100%; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }}
.logo-tagline {{ font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }}
a {{ text-decoration: none; color: inherit; }}
</style>
<div class="logo-mark">{svg}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


WORDMARK = "<text x=\"175\" y=\"58\" font-family=\"Cinzel, serif\" font-size=\"36\" font-weight=\"700\" letter-spacing=\"0.08em\" fill=\"#C0C0C0\">KORVIA</text>"

CONCEPTS = [
    {
        "id": "circlek",
        "name": "Circle K",
        "desc": "A clean K monogram centered inside a perfect silver circle — a logo-system mark that reads instantly at any scale.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "circle", "monogram"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Circle K mark">
  <circle cx="45" cy="45" r="32" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="38" y1="28" x2="38" y2="62" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="28" x2="60" y2="45" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="45" x2="60" y2="62" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "squarecutout",
        "name": "Square Cutout",
        "desc": "The letter K is cut away as negative space from a solid square, turning figure and ground into one minimal form.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "square", "negative-space"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Square Cutout mark">
  <rect x="18" y="18" width="54" height="54" rx="4" fill="#C0C0C0"/>
  <line x1="35" y1="30" x2="35" y2="60" stroke="#0A0F1E" stroke-width="7" stroke-linecap="round"/>
  <line x1="35" y1="30" x2="55" y2="45" stroke="#0A0F1E" stroke-width="7" stroke-linecap="round"/>
  <line x1="35" y1="45" x2="55" y2="60" stroke="#0A0F1E" stroke-width="7" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "stackedbars",
        "name": "Stacked Bars",
        "desc": "Three horizontal bars align and angle into a crisp K shape, evoking a menu, a list, and a digital stack.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "bars", "stack"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Stacked Bars mark">
  <rect x="18" y="24" width="54" height="9" rx="2" fill="#C0C0C0"/>
  <rect x="18" y="40" width="32" height="9" rx="2" fill="#1E3A8A"/>
  <rect x="18" y="56" width="54" height="9" rx="2" fill="#C0C0C0"/>
  <line x1="50" y1="49" x2="72" y2="31" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="50" y1="49" x2="72" y2="67" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "curvedk",
        "name": "Curved K",
        "desc": "A single continuous curved stroke resolves into the letter K — fluid, modern, and unmistakably hand-tuned.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "curve", "stroke"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Curved K mark">
  <path d="M35 22 Q35 44 35 66" fill="none" stroke="#C0C0C0" stroke-width="8" stroke-linecap="round"/>
  <path d="M35 44 C35 44 50 22 62 22 C50 22 50 44 62 66" fill="none" stroke="#1E3A8A" stroke-width="8" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "dotgrid",
        "name": "Dot Grid",
        "desc": "A 3x3 dot grid highlights the path of a K, turning the symbol into a modular, app-icon friendly mark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "dots", "grid"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Dot Grid mark">
  <circle cx="28" cy="28" r="6" fill="#C0C0C0"/>
  <circle cx="45" cy="28" r="6" fill="#1E3A8A"/>
  <circle cx="62" cy="28" r="6" fill="#C0C0C0"/>
  <circle cx="28" cy="45" r="6" fill="#C0C0C0"/>
  <circle cx="45" cy="45" r="6" fill="#1E3A8A"/>
  <circle cx="62" cy="45" r="6" fill="#C0C0C0"/>
  <circle cx="28" cy="62" r="6" fill="#C0C0C0"/>
  <circle cx="45" cy="62" r="6" fill="#C0C0C0"/>
  <circle cx="62" cy="62" r="6" fill="#1E3A8A"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "hexagonk",
        "name": "Hexagon K",
        "desc": "A K sits centered inside a balanced hexagon, suggesting structure, hospitality modules, and a honeycomb of services.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "hexagon", "module"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Hexagon K mark">
  <path d="M45 18 L68 31 L68 57 L45 70 L22 57 L22 31 Z" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="38" y1="30" x2="38" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="30" x2="56" y2="44" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="44" x2="56" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "mountaink",
        "name": "Mountain K",
        "desc": "Triangular peaks rise into a K silhouette — stable, aspirational, and ready for signage across any venue.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "mountain", "peak"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Mountain K mark">
  <path d="M32 66 L32 26 L52 46 L32 46 L56 66" fill="none" stroke="#C0C0C0" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M32 46 L56 66" fill="none" stroke="#1E3A8A" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "loopmark",
        "name": "Loop Mark",
        "desc": "A continuous loop cradles a K inside its curve, symbolizing seamless service and returning guests.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "loop", "infinity"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Loop Mark">
  <path d="M30 45 C30 32 42 32 45 45 C48 58 60 58 63 45 C66 32 78 32 78 45" fill="none" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round"/>
  <line x1="45" y1="32" x2="45" y2="58" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="45" y1="32" x2="63" y2="45" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="45" y1="45" x2="63" y2="58" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "overlapcircles",
        "name": "Overlap Circles",
        "desc": "Two overlapping circles intersect to reveal a K — a clean Venn of hospitality and digital service.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "circles", "overlap"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Overlap Circles mark">
  <circle cx="40" cy="45" r="24" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <circle cx="62" cy="45" r="24" fill="none" stroke="#1E3A8A" stroke-width="5"/>
  <line x1="40" y1="21" x2="40" y2="69" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="21" x2="62" y2="45" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="45" x2="62" y2="69" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "semiarc",
        "name": "Semi Arc",
        "desc": "A semicircle and a vertical line snap together into a bold, architectural K mark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "arc", "semicircle"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Semi Arc mark">
  <path d="M32 66 A22 22 0 0 1 76 66" fill="none" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round"/>
  <line x1="32" y1="44" x2="32" y2="66" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="32" y1="44" x2="54" y2="55" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="32" y1="55" x2="54" y2="66" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "starburst",
        "name": "Star Burst",
        "desc": "A four-point star frames a K at its center — bright, directional, and easy to recognize as a favicon.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "star", "burst"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Star Burst mark">
  <path d="M45 18 L52 38 L72 45 L52 52 L45 72 L38 52 L18 45 L38 38 Z" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="40" y1="33" x2="40" y2="57" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="33" x2="55" y2="45" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="45" x2="55" y2="57" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "spiralk",
        "name": "Spiral K",
        "desc": "A spiral tightens and resolves into a K — motion, discovery, and the journey from scan to service.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "spiral", "motion"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Spiral K mark">
  <path d="M45 45 Q45 25 65 25 Q85 25 85 45 Q85 65 65 65 Q50 65 50 50" fill="none" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="62" y1="36" x2="62" y2="54" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="62" y1="36" x2="74" y2="45" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="62" y1="45" x2="74" y2="54" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "diamondk",
        "name": "Diamond K",
        "desc": "A K is set inside a rotated square — a diamond badge that works as an app icon, stamp, or embossed seal.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "diamond", "badge"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Diamond K mark">
  <polygon points="45,18 72,45 45,72 18,45" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="40" y1="33" x2="40" y2="57" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="33" x2="55" y2="45" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="40" y1="45" x2="55" y2="57" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "roundedsquare",
        "name": "Rounded Square",
        "desc": "A soft rounded square contains a precise K — friendly enough for an app, refined enough for a hotel facade.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "rounded", "app-icon"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Rounded Square mark">
  <rect x="20" y="20" width="50" height="50" rx="14" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="37" y1="33" x2="37" y2="57" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="37" y1="33" x2="55" y2="45" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="37" y1="45" x2="55" y2="57" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "patharrow",
        "name": "Path Arrow",
        "desc": "A K doubles as a forward arrow — pointing guests from QR scan to table, room, or event.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "arrow", "direction"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Path Arrow mark">
  <path d="M30 66 L30 24 L55 45 L30 45 L60 66" fill="none" stroke="#C0C0C0" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M55 45 L68 45" fill="none" stroke="#1E3A8A" stroke-width="7" stroke-linecap="round"/>
  <path d="M60 38 L68 45 L60 52" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "windowgrid",
        "name": "Window Grid",
        "desc": "Four square panes tile together; a K cuts across them like light through a hotel window grid.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "grid", "window"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Window Grid mark">
  <rect x="22" y="22" width="22" height="22" fill="#C0C0C0"/>
  <rect x="46" y="22" width="22" height="22" fill="#1E3A8A"/>
  <rect x="22" y="46" width="22" height="22" fill="#1E3A8A"/>
  <rect x="46" y="46" width="22" height="22" fill="#C0C0C0"/>
  <line x1="28" y1="28" x2="28" y2="62" stroke="#0A0F1E" stroke-width="5" stroke-linecap="round"/>
  <line x1="28" y1="28" x2="62" y2="45" stroke="#0A0F1E" stroke-width="5" stroke-linecap="round"/>
  <line x1="28" y1="45" x2="62" y2="62" stroke="#0A0F1E" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "signalwaves",
        "name": "Signal Waves",
        "desc": "Radiating waves emanate from a vertical K stem — connectivity, QR reach, and digital hospitality.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "waves", "signal"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Signal Waves mark">
  <line x1="32" y1="24" x2="32" y2="66" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round"/>
  <path d="M32 32 Q55 24 70 32" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <path d="M32 45 Q55 37 70 45" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <path d="M32 58 Q55 50 70 58" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "radialslice",
        "name": "Radial Slice",
        "desc": "Pie-shaped radial segments alternate to reveal a K at the center of a service dial.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "radial", "pie"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Radial Slice mark">
  <circle cx="45" cy="45" r="28" fill="none" stroke="#C0C0C0" stroke-width="4"/>
  <path d="M45 45 L45 17 A28 28 0 0 1 73 45 Z" fill="#1E3A8A"/>
  <path d="M45 45 L73 45 A28 28 0 0 1 45 73 Z" fill="#C0C0C0" opacity="0.5"/>
  <path d="M45 45 L45 73 A28 28 0 0 1 17 45 Z" fill="#1E3A8A"/>
  <path d="M45 45 L17 45 A28 28 0 0 1 45 17 Z" fill="#C0C0C0" opacity="0.5"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "bookmarkflag",
        "name": "Bookmark Flag",
        "desc": "A K is shaped into a bookmark flag — save a venue, save an order, save the moment.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "bookmark", "flag"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Bookmark Flag mark">
  <path d="M28 20 L62 20 L62 70 L45 55 L28 70 Z" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="38" y1="32" x2="38" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="32" x2="52" y2="45" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="45" x2="52" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
    },
    {
        "id": "orderbubble",
        "name": "Order Bubble",
        "desc": "A minimal chat bubble carries a K — instant ordering, guest messaging, and front-desk conversation.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "chat", "bubble"],
        "mark_css": ".logo-mark svg { max-width: 320px; }",
        "svg": f'''<svg viewBox="0 0 300 90" xmlns="http://www.w3.org/2000/svg" aria-label="Order Bubble mark">
  <path d="M22 28 Q22 18 32 18 L68 18 Q78 18 78 28 L78 55 Q78 65 68 65 L48 65 L32 75 L36 65 L32 65 Q22 65 22 55 Z" fill="none" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="38" y1="32" x2="38" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="32" x2="55" y2="45" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <line x1="38" y1="45" x2="55" y2="58" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  {WORDMARK}
</svg>''',
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
    print(f"Appended {len(CONCEPTS)} minimal abstract Korvia logo-mark concepts.")


if __name__ == "__main__":
    main()
