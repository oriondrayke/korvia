#!/usr/bin/env python3
"""Append 20 Korvia symbolic logo-mark concepts (IDs 159-178) in the Moonlight setting."""
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
.logo-mark svg {{ max-width: 220px; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }}
.logo-tagline {{ font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }}
a {{ text-decoration: none; color: inherit; }}
</style>
<div class="logo-mark">{svg}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


CONCEPTS = [
    {
        "id": "ktower",
        "name": "K-Tower",
        "desc": "A hospitality tower whose silhouette reads as the letter K, complete with glowing windows.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "tower", "windows"],
        "mark_css": ".logo-mark svg { max-height: 210px; filter: drop-shadow(0 0 22px rgba(192,192,192,0.45)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Tower mark">
  <rect x="70" y="60" width="28" height="140" fill="#C0C0C0"/>
  <polygon points="55,60 113,60 84,20" fill="#C0C0C0"/>
  <polygon points="113,60 158,200 128,200 100,80" fill="#1E3A8A"/>
  <rect x="76" y="85" width="16" height="16" fill="#0A0F1E"/>
  <rect x="76" y="115" width="16" height="16" fill="#0A0F1E"/>
  <rect x="76" y="145" width="16" height="16" fill="#0A0F1E"/>
</svg>''',
    },
    {
        "id": "kumbrella",
        "name": "K-Umbrella",
        "desc": "A sheltering umbrella whose canopy and handle trace the letter K above a plate.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "umbrella", "plate"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 22px rgba(30,58,138,0.5)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Umbrella mark">
  <line x1="80" y1="40" x2="80" y2="180" stroke="#C0C0C0" stroke-width="8" stroke-linecap="round"/>
  <path d="M30 85 Q80 35 130 85 L115 100 Q80 65 45 100 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="4"/>
  <line x1="80" y1="55" x2="125" y2="100" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round"/>
  <ellipse cx="90" cy="170" rx="32" ry="10" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "kplate",
        "name": "K-Plate",
        "desc": "A plate, fork, and knife arranged so the utensils form a K over the dish.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "plate", "fork", "knife"],
        "mark_css": ".logo-mark svg { max-width: 200px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Plate mark">
  <ellipse cx="100" cy="170" rx="60" ry="16" fill="#C0C0C0"/>
  <path d="M70 40 L70 150" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <path d="M70 40 L125 105" stroke="#1E3A8A" stroke-width="12" stroke-linecap="round"/>
  <path d="M125 50 L125 150" stroke="#C0C0C0" stroke-width="8" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kqr",
        "name": "K-QR",
        "desc": "QR-code finder modules assembled into the shape of the letter K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "qr", "modules"],
        "mark_css": ".logo-mark svg { background: rgba(20,30,50,0.6); border-radius: 12px; padding: 12px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K QR mark">
  <rect x="40" y="40" width="30" height="30" fill="#C0C0C0"/>
  <rect x="40" y="80" width="30" height="30" fill="#C0C0C0"/>
  <rect x="40" y="120" width="30" height="30" fill="#C0C0C0"/>
  <rect x="80" y="40" width="30" height="30" fill="#1E3A8A"/>
  <rect x="120" y="80" width="30" height="30" fill="#1E3A8A"/>
  <rect x="80" y="120" width="30" height="30" fill="#1E3A8A"/>
  <rect x="120" y="120" width="30" height="30" fill="#C0C0C0"/>
  <rect x="160" y="40" width="20" height="20" fill="#C0C0C0"/>
  <rect x="160" y="80" width="20" height="20" fill="#C0C0C0"/>
  <rect x="160" y="130" width="20" height="20" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "kkey",
        "name": "K-Key",
        "desc": "A key whose bow carries a K monogram, unlocking the Korvia door.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "key", "door"],
        "mark_css": ".logo-mark svg { transform: rotate(-8deg); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Key mark">
  <circle cx="80" cy="80" r="42" fill="none" stroke="#C0C0C0" stroke-width="10"/>
  <line x1="62" y1="55" x2="62" y2="105" stroke="#0A0F1E" stroke-width="8" stroke-linecap="round"/>
  <line x1="62" y1="55" x2="95" y2="80" stroke="#0A0F1E" stroke-width="8" stroke-linecap="round"/>
  <line x1="62" y1="80" x2="95" y2="105" stroke="#0A0F1E" stroke-width="8" stroke-linecap="round"/>
  <line x1="113" y1="110" x2="155" y2="152" stroke="#1E3A8A" stroke-width="14" stroke-linecap="round"/>
  <rect x="145" y="142" width="36" height="24" rx="4" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "kcrown",
        "name": "K-Crown",
        "desc": "A crown-shaped mark where the peak and bands form a refined K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "crown", "premium"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 24px rgba(192,192,192,0.5)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Crown mark">
  <path d="M30 80 L50 140 L150 140 L170 80 L140 100 L100 60 L60 100 Z" fill="#C0C0C0"/>
  <line x1="100" y1="60" x2="100" y2="140" stroke="#1E3A8A" stroke-width="10"/>
  <line x1="100" y1="60" x2="140" y2="100" stroke="#1E3A8A" stroke-width="8"/>
  <circle cx="50" cy="80" r="8" fill="#1E3A8A"/>
  <circle cx="100" cy="60" r="8" fill="#1E3A8A"/>
  <circle cx="150" cy="80" r="8" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "kfork",
        "name": "K-Fork",
        "desc": "A fork and knife cross to create a bold, appetizing K mark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "fork", "knife"],
        "mark_css": ".logo-mark svg { max-height: 200px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Fork mark">
  <line x1="70" y1="40" x2="70" y2="180" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <path d="M70 40 Q70 80 110 90" fill="none" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <path d="M70 70 Q70 110 115 120" fill="none" stroke="#1E3A8A" stroke-width="10" stroke-linecap="round"/>
  <line x1="130" y1="40" x2="130" y2="180" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kpin",
        "name": "K-Pin",
        "desc": "A map pin containing a K, marking every Korvia venue.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "pin", "location"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 20px rgba(30,58,138,0.55)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Pin mark">
  <path d="M100 30 C60 30 40 70 40 100 C40 140 100 190 100 190 C100 190 160 140 160 100 C160 70 140 30 100 30 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="80" y1="60" x2="80" y2="130" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="80" y1="60" x2="120" y2="95" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="80" y1="95" x2="120" y2="130" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kacacia",
        "name": "K-Acacia",
        "desc": "An acacia tree silhouette whose trunk and branches become the letter K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "acacia", "tree"],
        "mark_css": ".logo-mark svg { max-height: 205px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Acacia mark">
  <line x1="100" y1="180" x2="100" y2="80" stroke="#C0C0C0" stroke-width="14" stroke-linecap="round"/>
  <path d="M100 110 Q70 90 50 70" fill="none" stroke="#1E3A8A" stroke-width="8" stroke-linecap="round"/>
  <path d="M100 90 Q130 70 150 50" fill="none" stroke="#1E3A8A" stroke-width="8" stroke-linecap="round"/>
  <path d="M40 65 Q30 50 50 45 Q70 40 80 55 Q90 70 70 75 Q50 80 40 65 Z" fill="#C0C0C0"/>
  <path d="M140 45 Q130 30 150 25 Q170 20 180 35 Q190 50 170 55 Q150 60 140 45 Z" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "ksunrise",
        "name": "K-Sunrise",
        "desc": "A sun rising over the horizon, with rays and landscape shaping a K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "sun", "horizon"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 26px rgba(192,192,192,0.4)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Sunrise mark">
  <path d="M0 160 Q100 120 200 160 L200 220 L0 220 Z" fill="#1E3A8A"/>
  <circle cx="100" cy="110" r="35" fill="#C0C0C0"/>
  <line x1="70" y1="50" x2="70" y2="140" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <line x1="70" y1="50" x2="115" y2="95" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <line x1="70" y1="95" x2="115" y2="140" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kspice",
        "name": "K-Spice",
        "desc": "A chili pod curved into a K, celebrating East African flavor.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "chili", "spice"],
        "mark_css": ".logo-mark svg { transform: rotate(3deg); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Spice mark">
  <path d="M80 40 Q120 80 80 180" fill="none" stroke="#C0C0C0" stroke-width="14" stroke-linecap="round"/>
  <path d="M80 40 Q40 80 80 120" fill="none" stroke="#1E3A8A" stroke-width="10" stroke-linecap="round"/>
  <path d="M80 90 Q130 70 150 110 Q130 130 80 110" fill="#C0C0C0"/>
  <path d="M75 25 L85 25 L80 45 Z" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "kglass",
        "name": "K-Glass",
        "desc": "A wine glass whose bowl, stem, and pour form an elegant K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "glass", "wine"],
        "mark_css": ".logo-mark svg { max-height: 195px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Glass mark">
  <path d="M75 40 L75 140 Q75 170 100 170 Q125 170 125 140 L125 40 Z" fill="none" stroke="#C0C0C0" stroke-width="8"/>
  <line x1="100" y1="170" x2="100" y2="200" stroke="#C0C0C0" stroke-width="8"/>
  <line x1="75" y1="40" x2="75" y2="130" stroke="#1E3A8A" stroke-width="6"/>
  <line x1="75" y1="40" x2="115" y2="85" stroke="#1E3A8A" stroke-width="6"/>
  <line x1="75" y1="85" x2="115" y2="130" stroke="#1E3A8A" stroke-width="6"/>
</svg>''',
    },
    {
        "id": "kbed",
        "name": "K-Bed",
        "desc": "A hotel bed whose headboard and frame shape a resting K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "bed", "hotel"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 20px rgba(30,58,138,0.5)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Bed mark">
  <rect x="40" y="90" width="120" height="70" rx="8" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="6"/>
  <rect x="50" y="100" width="35" height="25" rx="4" fill="#C0C0C0"/>
  <rect x="115" y="100" width="35" height="25" rx="4" fill="#C0C0C0"/>
  <line x1="60" y1="50" x2="60" y2="90" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="60" y1="50" x2="100" y2="75" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="60" y1="70" x2="100" y2="90" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kflag",
        "name": "K-Flag",
        "desc": "A pennant flag whose pole and fabric create a waving K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "flag", "banner"],
        "mark_css": ".logo-mark svg { transform: rotate(-3deg); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Flag mark">
  <line x1="60" y1="40" x2="60" y2="180" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <path d="M60 50 L160 80 L60 110 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="4"/>
  <line x1="60" y1="50" x2="110" y2="80" stroke="#C0C0C0" stroke-width="8" stroke-linecap="round"/>
  <line x1="60" y1="80" x2="110" y2="110" stroke="#C0C0C0" stroke-width="8" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kwave",
        "name": "K-Wave",
        "desc": "An ocean wave rolling beneath a K mark, nodding to coastal Tanzania.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "wave", "coast"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 22px rgba(30,58,138,0.55)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Wave mark">
  <path d="M20 180 Q60 140 100 160 Q140 180 180 140" fill="none" stroke="#1E3A8A" stroke-width="14" stroke-linecap="round"/>
  <path d="M20 150 Q60 110 100 130" fill="none" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="75" y1="50" x2="75" y2="140" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <line x1="75" y1="50" x2="115" y2="95" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
  <line x1="75" y1="95" x2="115" y2="140" stroke="#C0C0C0" stroke-width="12" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kplateqr",
        "name": "K-PlateQR",
        "desc": "A dinner plate with a QR pattern seated inside the bowl.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "plate", "qr"],
        "mark_css": ".logo-mark svg { border-radius: 50%; background: rgba(20,30,50,0.55); padding: 10px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Plate QR mark">
  <circle cx="100" cy="110" r="75" fill="none" stroke="#C0C0C0" stroke-width="8"/>
  <rect x="55" y="65" width="20" height="20" fill="#C0C0C0"/>
  <rect x="85" y="65" width="20" height="20" fill="#1E3A8A"/>
  <rect x="125" y="65" width="20" height="20" fill="#C0C0C0"/>
  <rect x="55" y="95" width="20" height="20" fill="#1E3A8A"/>
  <rect x="85" y="95" width="20" height="20" fill="#C0C0C0"/>
  <rect x="125" y="95" width="20" height="20" fill="#1E3A8A"/>
  <rect x="55" y="125" width="20" height="20" fill="#C0C0C0"/>
  <rect x="85" y="125" width="20" height="20" fill="#1E3A8A"/>
  <rect x="125" y="125" width="20" height="20" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "kchat",
        "name": "K-Chat",
        "desc": "A service chat bubble shaped into a friendly K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "chat", "bubble"],
        "mark_css": ".logo-mark svg { max-height: 190px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Chat mark">
  <path d="M40 50 Q40 30 60 30 L140 30 Q160 30 160 50 L160 120 Q160 140 140 140 L100 140 L70 180 L80 140 L60 140 Q40 140 40 120 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="75" y1="65" x2="75" y2="115" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="75" y1="65" x2="110" y2="90" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="75" y1="90" x2="110" y2="115" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "kcompass",
        "name": "K-Compass",
        "desc": "A navigation compass whose needle points to K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "compass", "navigation"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 24px rgba(192,192,192,0.45)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Compass mark">
  <circle cx="100" cy="110" r="70" fill="none" stroke="#C0C0C0" stroke-width="8"/>
  <line x1="100" y1="40" x2="100" y2="50" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="100" y1="170" x2="100" y2="180" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="30" y1="110" x2="40" y2="110" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="160" y1="110" x2="170" y2="110" stroke="#C0C0C0" stroke-width="6"/>
  <polygon points="100,55 120,110 100,165 80,110" fill="#1E3A8A"/>
  <line x1="100" y1="55" x2="100" y2="165" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="100" y1="55" x2="135" y2="110" stroke="#C0C0C0" stroke-width="5"/>
  <line x1="100" y1="110" x2="135" y2="165" stroke="#C0C0C0" stroke-width="5"/>
</svg>''',
    },
    {
        "id": "kdrum",
        "name": "K-Drum",
        "desc": "An African drum whose body and straps form a rhythmic K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "drum", "africa"],
        "mark_css": ".logo-mark svg { max-height: 205px; }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Drum mark">
  <ellipse cx="100" cy="60" rx="50" ry="18" fill="#C0C0C0"/>
  <rect x="50" y="60" width="100" height="100" fill="#1E3A8A"/>
  <path d="M50 160 Q100 185 150 160" fill="none" stroke="#C0C0C0" stroke-width="8"/>
  <line x1="75" y1="40" x2="75" y2="150" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="75" y1="40" x2="115" y2="95" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
  <line x1="75" y1="95" x2="115" y2="150" stroke="#C0C0C0" stroke-width="10" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "klantern",
        "name": "K-Lantern",
        "desc": "A glowing hospitality lantern framed by the letter K.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-mark", "lantern", "glow"],
        "mark_css": ".logo-mark svg { filter: drop-shadow(0 0 28px rgba(255,250,205,0.25)); }",
        "svg": '''<svg viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-label="K Lantern mark">
  <line x1="100" y1="30" x2="100" y2="60" stroke="#C0C0C0" stroke-width="8"/>
  <path d="M70 60 L130 60 L120 160 L80 160 Z" fill="none" stroke="#C0C0C0" stroke-width="8"/>
  <rect x="80" y="70" width="40" height="80" fill="#1E3A8A" opacity="0.8"/>
  <line x1="80" y1="70" x2="80" y2="150" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="80" y1="70" x2="110" y2="110" stroke="#C0C0C0" stroke-width="6"/>
  <line x1="80" y1="110" x2="110" y2="150" stroke="#C0C0C0" stroke-width="6"/>
  <path d="M85 160 Q100 180 115 160" fill="none" stroke="#C0C0C0" stroke-width="6"/>
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
    print(f"Appended {len(CONCEPTS)} symbolic logo-mark concepts.")


if __name__ == "__main__":
    main()
