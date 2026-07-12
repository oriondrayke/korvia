#!/usr/bin/env python3
"""Append 20 Korvia whole-word wordmark concepts (IDs 179-198) in the Moonlight setting."""
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
.logo-mark svg {{ max-width: 320px; width: 100%; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }}
.logo-tagline {{ font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }}
a {{ text-decoration: none; color: inherit; }}
</style>
<div class="logo-mark">{svg}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


CONCEPTS = [
    {
        "id": "cityskyline",
        "name": "City Skyline",
        "desc": "The letters of Korvia rise as a city skyline silhouette, with glowing windows cut into each letterform.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "skyline", "city"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 22px rgba(192,192,192,0.4)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia city skyline wordmark">
  <defs>
    <clipPath id="skytext">
      <text x="180" y="88" font-family="Cinzel, serif" font-size="58" font-weight="700" text-anchor="middle" letter-spacing="0.06em">KORVIA</text>
    </clipPath>
  </defs>
  <rect x="0" y="0" width="360" height="120" fill="#0A0F1E" clip-path="url(#skytext)"/>
  <g clip-path="url(#skytext)">
    <rect x="42" y="40" width="22" height="60" fill="#1E3A8A"/>
    <rect x="82" y="25" width="26" height="75" fill="#1E3A8A"/>
    <rect x="126" y="50" width="20" height="50" fill="#1E3A8A"/>
    <rect x="166" y="30" width="28" height="70" fill="#1E3A8A"/>
    <rect x="212" y="45" width="18" height="55" fill="#1E3A8A"/>
    <rect x="250" y="20" width="24" height="80" fill="#1E3A8A"/>
    <rect x="290" y="48" width="22" height="52" fill="#1E3A8A"/>
    <rect x="54" y="55" width="6" height="8" fill="#C0C0C0"/>
    <rect x="92" y="40" width="6" height="8" fill="#C0C0C0"/>
    <rect x="138" y="62" width="5" height="7" fill="#C0C0C0"/>
    <rect x="178" y="45" width="6" height="8" fill="#C0C0C0"/>
    <rect x="220" y="58" width="5" height="7" fill="#C0C0C0"/>
    <rect x="262" y="38" width="6" height="8" fill="#C0C0C0"/>
    <rect x="300" y="65" width="5" height="7" fill="#C0C0C0"/>
  </g>
  <text x="180" y="88" font-family="Cinzel, serif" font-size="58" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="none" stroke="#C0C0C0" stroke-width="2">KORVIA</text>
</svg>''',
    },
    {
        "id": "platesetting",
        "name": "Plate Setting",
        "desc": "The Korvia wordmark sits on a dinner plate, with a fork and knife rising to merge with letter stems.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "plate", "fork", "knife"],
        "mark_css": ".logo-mark svg { max-width: 340px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia plate setting wordmark">
  <ellipse cx="180" cy="102" rx="130" ry="14" fill="none" stroke="#C0C0C0" stroke-width="4"/>
  <ellipse cx="180" cy="102" rx="110" ry="9" fill="#1E3A8A" opacity="0.5"/>
  <text x="180" y="78" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.05em" fill="#C0C0C0">KORVIA</text>
  <line x1="62" y1="28" x2="62" y2="88" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <path d="M62 28 Q62 55 92 62" fill="none" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <path d="M62 55 Q62 80 94 86" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="298" y1="28" x2="298" y2="88" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="288" y1="32" x2="308" y2="32" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "qrdissolve",
        "name": "QR Dissolve",
        "desc": "Korvia emerges from a dissolving QR code as a scan line sweeps across the wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "qr", "scan"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 18px rgba(30,58,138,0.5)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia QR dissolve wordmark">
  <g opacity="0.7">
    <rect x="20" y="25" width="12" height="12" fill="#C0C0C0"/>
    <rect x="20" y="45" width="12" height="12" fill="#C0C0C0"/>
    <rect x="20" y="65" width="12" height="12" fill="#C0C0C0"/>
    <rect x="40" y="25" width="12" height="12" fill="#1E3A8A"/>
    <rect x="60" y="45" width="12" height="12" fill="#1E3A8A"/>
    <rect x="40" y="65" width="12" height="12" fill="#1E3A8A"/>
    <rect x="60" y="65" width="12" height="12" fill="#C0C0C0"/>
    <rect x="80" y="25" width="10" height="10" fill="#C0C0C0"/>
    <rect x="80" y="45" width="10" height="10" fill="#C0C0C0"/>
    <rect x="80" y="68" width="10" height="10" fill="#C0C0C0"/>
  </g>
  <text x="205" y="80" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.05em" fill="#C0C0C0">KORVIA</text>
  <rect x="110" y="22" width="3" height="76" fill="#1E3A8A" opacity="0.9"/>
  <rect x="110" y="22" width="3" height="76" fill="none" stroke="#C0C0C0" stroke-width="1"/>
</svg>''',
    },
    {
        "id": "bedheadboard",
        "name": "Bed Headboard",
        "desc": "The Korvia letters are built into a hotel bed headboard, with pillows tucked into the O and R.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "bed", "headboard", "hotel"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 20px rgba(30,58,138,0.5)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia bed headboard wordmark">
  <rect x="30" y="55" width="300" height="50" rx="6" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="4"/>
  <rect x="48" y="70" width="34" height="26" rx="4" fill="#C0C0C0"/>
  <rect x="102" y="70" width="34" height="26" rx="4" fill="#C0C0C0"/>
  <text x="180" y="52" font-family="Cinzel, serif" font-size="46" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">KORVIA</text>
  <rect x="145" y="60" width="28" height="18" rx="9" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="2"/>
  <rect x="188" y="60" width="28" height="18" rx="4" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="2"/>
</svg>''',
    },
    {
        "id": "oceanwave",
        "name": "Ocean Wave",
        "desc": "Rolling ocean waves shape and flow through the Korvia wordmark, nodding to coastal Tanzania.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "wave", "ocean"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 22px rgba(30,58,138,0.55)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia ocean wave wordmark">
  <path d="M0 95 Q45 70 90 85 Q135 100 180 82 Q225 64 270 80 Q315 96 360 75" fill="none" stroke="#1E3A8A" stroke-width="10" stroke-linecap="round"/>
  <path d="M0 70 Q45 45 90 60 Q135 75 180 57 Q225 39 270 55 Q315 71 360 50" fill="none" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round" opacity="0.8"/>
  <text x="180" y="62" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.05em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "acaciacanopy",
        "name": "Acacia Canopy",
        "desc": "The Korvia letters hang like branches beneath the flat canopy of an East African acacia tree.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "acacia", "tree", "africa"],
        "mark_css": ".logo-mark svg { max-width: 360px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia acacia canopy wordmark">
  <line x1="60" y1="115" x2="60" y2="70" stroke="#C0C0C0" stroke-width="6" stroke-linecap="round"/>
  <path d="M60 70 Q40 55 20 50" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <path d="M60 75 Q90 58 120 55" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="25" cy="48" rx="22" ry="9" fill="#C0C0C0"/>
  <ellipse cx="125" cy="52" rx="28" ry="10" fill="#C0C0C0"/>
  <text x="210" y="88" font-family="Cinzel, serif" font-size="50" font-weight="700" text-anchor="middle" letter-spacing="0.05em" fill="#C0C0C0">KORVIA</text>
  <line x1="120" y1="55" x2="145" y2="75" stroke="#1E3A8A" stroke-width="3" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "opendoor",
        "name": "Open Door",
        "desc": "The O in Korvia becomes a hotel door swinging open, with silver light spilling into the wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "door", "portal"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 24px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia open door wordmark">
  <text x="180" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">K</text>
  <text x="208" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">R</text>
  <text x="270" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">VIA</text>
  <path d="M228 28 L258 38 L258 92 L228 102 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="3"/>
  <path d="M258 38 L288 28 L288 102 L258 92 Z" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="3"/>
  <circle cx="250" cy="65" r="3" fill="#C0C0C0"/>
  <path d="M228 28 L288 28 L288 102 L228 102 Z" fill="none" stroke="#C0C0C0" stroke-width="2"/>
</svg>''',
    },
    {
        "id": "coffeepour",
        "name": "Coffee Pour",
        "desc": "Coffee cups and a pouring stream assemble into the Korvia wordmark for East African cafés.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "coffee", "pour"],
        "mark_css": ".logo-mark svg { max-width: 340px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia coffee pour wordmark">
  <text x="180" y="82" font-family="Cinzel, serif" font-size="50" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">KORVIA</text>
  <path d="M88 28 Q95 55 88 82" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <path d="M88 28 Q82 55 88 82" fill="none" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <path d="M285 25 Q292 55 285 85" fill="none" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="285" cy="90" rx="14" ry="6" fill="#C0C0C0"/>
  <ellipse cx="88" cy="90" rx="12" ry="5" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "kangapattern",
        "name": "Kanga Pattern",
        "desc": "The Korvia wordmark is filled with an East African kanga fabric motif and framed by border patterns.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "kanga", "pattern", "africa"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia kanga pattern wordmark">
  <defs>
    <pattern id="kanga" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <rect width="20" height="20" fill="#1E3A8A"/>
      <circle cx="10" cy="10" r="4" fill="#C0C0C0"/>
      <path d="M0 10 L20 10 M10 0 L10 20" stroke="#0A0F1E" stroke-width="2"/>
    </pattern>
  </defs>
  <rect x="28" y="22" width="304" height="8" fill="#C0C0C0"/>
  <rect x="28" y="92" width="304" height="8" fill="#C0C0C0"/>
  <text x="180" y="80" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="url(#kanga)" stroke="#C0C0C0" stroke-width="1">KORVIA</text>
</svg>''',
    },
    {
        "id": "chandelier",
        "name": "Chandelier",
        "desc": "The Korvia letters hang like crystals from a lit hospitality chandelier.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "chandelier", "light"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 24px rgba(192,192,192,0.45)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia chandelier wordmark">
  <line x1="180" y1="10" x2="180" y2="28" stroke="#C0C0C0" stroke-width="3"/>
  <line x1="60" y1="28" x2="300" y2="28" stroke="#C0C0C0" stroke-width="3"/>
  <line x1="70" y1="28" x2="70" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="115" y1="28" x2="115" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="160" y1="28" x2="160" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="205" y1="28" x2="205" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="250" y1="28" x2="250" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="295" y1="28" x2="295" y2="45" stroke="#C0C0C0" stroke-width="2"/>
  <text x="180" y="90" font-family="Cinzel, serif" font-size="48" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#C0C0C0">KORVIA</text>
  <circle cx="70" cy="50" r="4" fill="#1E3A8A"/>
  <circle cx="115" cy="50" r="4" fill="#1E3A8A"/>
  <circle cx="160" cy="50" r="4" fill="#1E3A8A"/>
  <circle cx="205" cy="50" r="4" fill="#1E3A8A"/>
  <circle cx="250" cy="50" r="4" fill="#1E3A8A"/>
  <circle cx="295" cy="50" r="4" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "servingtray",
        "name": "Serving Tray",
        "desc": "A silver cloche lifts from a serving tray to reveal the Korvia wordmark beneath.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "tray", "cloche", "serve"],
        "mark_css": ".logo-mark svg { max-width: 340px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia serving tray wordmark">
  <path d="M70 45 Q180 5 290 45" fill="none" stroke="#C0C0C0" stroke-width="4"/>
  <line x1="180" y1="12" x2="180" y2="28" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="180" cy="55" rx="115" ry="16" fill="none" stroke="#C0C0C0" stroke-width="4"/>
  <text x="180" y="82" font-family="Cinzel, serif" font-size="42" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "maproute",
        "name": "Map Route",
        "desc": "A dotted route line connects the Korvia letters as stops on a hospitality map.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "map", "route", "navigation"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 18px rgba(30,58,138,0.45)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia map route wordmark">
  <path d="M20 90 Q80 30 140 70 Q200 110 260 60 Q320 30 340 80" fill="none" stroke="#1E3A8A" stroke-width="3" stroke-dasharray="6 6"/>
  <text x="180" y="58" font-family="Cinzel, serif" font-size="48" font-weight="700" text-anchor="middle" letter-spacing="0.07em" fill="#C0C0C0">KORVIA</text>
  <circle cx="50" cy="78" r="5" fill="#C0C0C0"/>
  <circle cx="110" cy="52" r="5" fill="#C0C0C0"/>
  <circle cx="170" cy="70" r="5" fill="#C0C0C0"/>
  <circle cx="230" cy="60" r="5" fill="#C0C0C0"/>
  <circle cx="290" cy="52" r="5" fill="#C0C0C0"/>
  <circle cx="320" cy="72" r="5" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "cocktailbar",
        "name": "Cocktail Bar",
        "desc": "Cocktail glasses and bottles shape the Korvia wordmark for bars and nightlife.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "cocktail", "bar", "nightlife"],
        "mark_css": ".logo-mark svg { max-width: 340px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia cocktail bar wordmark">
  <text x="180" y="72" font-family="Cinzel, serif" font-size="48" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">KORVIA</text>
  <path d="M60 92 L75 55 L90 92 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="75" y1="92" x2="75" y2="105" stroke="#C0C0C0" stroke-width="3"/>
  <line x1="68" y1="105" x2="82" y2="105" stroke="#C0C0C0" stroke-width="3"/>
  <rect x="285" y="48" width="16" height="50" rx="3" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <rect x="288" y="42" width="10" height="10" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "moonphases",
        "name": "Moon Phases",
        "desc": "Each letter of Korvia frames a different phase of the moon against the dark canvas.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "moon", "phases"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 20px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia moon phases wordmark">
  <text x="180" y="88" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.07em" fill="#C0C0C0">KORVIA</text>
  <circle cx="62" cy="42" r="10" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <circle cx="110" cy="42" r="10" fill="#C0C0C0"/>
  <circle cx="158" cy="42" r="10" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <path d="M198 42 A10 10 0 1 1 198 62 A8 8 0 1 0 198 42 Z" fill="#C0C0C0"/>
  <circle cx="250" cy="42" r="10" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <path d="M294 42 A10 10 0 1 0 294 62 A6 6 0 1 1 294 42 Z" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "staircase",
        "name": "Staircase",
        "desc": "The Korvia wordmark climbs a set of ascending stairs, one letter per step.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stairs", "ascent"],
        "mark_css": ".logo-mark svg { max-width: 360px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia staircase wordmark">
  <path d="M20 100 L60 100 L60 85 L100 85 L100 70 L140 70 L140 55 L180 55 L180 40 L220 40 L220 25 L260 25" fill="none" stroke="#1E3A8A" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M20 100 L60 100 L60 85 L100 85 L100 70 L140 70 L140 55 L180 55 L180 40 L220 40 L220 25 L260 25" fill="none" stroke="#C0C0C0" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="150" y="62" font-family="Cinzel, serif" font-size="34" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "ribbonbanner",
        "name": "Ribbon Banner",
        "desc": "The Korvia wordmark is embroidered across a folded silver ribbon banner.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "ribbon", "banner"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia ribbon banner wordmark">
  <path d="M20 45 L40 35 L320 35 L340 45 L320 80 L40 80 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="3"/>
  <path d="M20 45 L10 55 L20 65 L35 55 Z" fill="#C0C0C0"/>
  <path d="M340 45 L350 55 L340 65 L325 55 Z" fill="#C0C0C0"/>
  <text x="180" y="66" font-family="Cinzel, serif" font-size="38" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "palmfronds",
        "name": "Palm Fronds",
        "desc": "Palm fronds weave through and around the Korvia wordmark for a coastal resort feel.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "palm", "fronds", "coast"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 18px rgba(30,58,138,0.4)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia palm fronds wordmark">
  <path d="M-10 120 Q40 60 90 50 Q140 40 160 80" fill="none" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <path d="M370 120 Q320 60 270 50 Q220 40 200 80" fill="none" stroke="#1E3A8A" stroke-width="6" stroke-linecap="round"/>
  <path d="M30 75 Q60 55 90 65" fill="none" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <path d="M330 75 Q300 55 270 65" fill="none" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <text x="180" y="88" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.06em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "utensilstems",
        "name": "Utensil Stems",
        "desc": "A fork, spoon, and knife replace or merge with the vertical stems of the Korvia letters.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "fork", "spoon", "knife"],
        "mark_css": ".logo-mark svg { max-width: 360px; }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia utensil stems wordmark">
  <text x="180" y="84" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.07em" fill="#C0C0C0">KORVIA</text>
  <line x1="58" y1="18" x2="58" y2="98" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <path d="M52 18 L52 40 M58 18 L58 40 M64 18 L64 40" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="250" cy="28" rx="6" ry="10" fill="#C0C0C0"/>
  <line x1="250" y1="38" x2="250" y2="98" stroke="#1E3A8A" stroke-width="5" stroke-linecap="round"/>
  <line x1="306" y1="18" x2="306" y2="98" stroke="#C0C0C0" stroke-width="5" stroke-linecap="round"/>
  <line x1="296" y1="22" x2="316" y2="22" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "keycard",
        "name": "Keycard",
        "desc": "The Korvia wordmark sits inside a hotel keycard, complete with a silver magnetic strip.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "keycard", "hotel"],
        "mark_css": ".logo-mark svg { max-width: 340px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia keycard wordmark">
  <rect x="45" y="20" width="270" height="80" rx="10" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="3"/>
  <rect x="45" y="38" width="270" height="14" fill="#C0C0C0"/>
  <text x="180" y="78" font-family="Cinzel, serif" font-size="34" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="#C0C0C0">KORVIA</text>
  <rect x="275" y="62" width="24" height="18" rx="2" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="1"/>
</svg>''',
    },
    {
        "id": "rooftopsign",
        "name": "Rooftop Sign",
        "desc": "Korvia is rendered as a steel and neon rooftop hotel sign glowing above the city.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "rooftop", "sign", "neon"],
        "mark_css": ".logo-mark svg { max-width: 360px; filter: drop-shadow(0 0 28px rgba(192,192,192,0.55)); }",
        "svg": '''<svg viewBox="0 0 360 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia rooftop sign wordmark">
  <rect x="40" y="40" width="280" height="54" rx="4" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="4"/>
  <text x="180" y="78" font-family="Cinzel, serif" font-size="40" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
  <line x1="70" y1="94" x2="70" y2="110" stroke="#C0C0C0" stroke-width="4"/>
  <line x1="290" y1="94" x2="290" y2="110" stroke="#C0C0C0" stroke-width="4"/>
  <line x1="40" y1="110" x2="320" y2="110" stroke="#1E3A8A" stroke-width="4"/>
  <circle cx="55" cy="55" r="4" fill="#1E3A8A"/>
  <circle cx="305" cy="55" r="4" fill="#1E3A8A"/>
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
    print(f"Appended {len(CONCEPTS)} whole-word Korvia wordmark concepts.")


if __name__ == "__main__":
    main()
