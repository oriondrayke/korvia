#!/usr/bin/env python3
"""Append 20 refined whole-word Korvia wordmark concepts (IDs 199-218) in the Moonlight setting."""
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
.logo-mark svg {{ max-width: 360px; width: 100%; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }}
.logo-tagline {{ font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }}
a {{ text-decoration: none; color: inherit; }}
</style>
<div class="logo-mark">{svg}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


CONCEPTS = [
    {
        "id": "neonsign",
        "name": "Neon Sign",
        "desc": "Korvia rendered as glowing neon tube letters mounted on a dark wall with flicker-soft glow.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "neon", "sign", "tube"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 26px rgba(192,192,192,0.65)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia neon sign wordmark">
  <rect x="25" y="25" width="330" height="80" rx="6" fill="#0A0F1E" stroke="#1E3A8A" stroke-width="2"/>
  <line x1="45" y1="35" x2="45" y2="28" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="335" y1="35" x2="335" y2="28" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="45" y1="95" x2="45" y2="102" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="335" y1="95" x2="335" y2="102" stroke="#C0C0C0" stroke-width="2"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="#f8fafc" stroke="#C0C0C0" stroke-width="3">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="none" stroke="#e2e8f0" stroke-width="1" opacity="0.9">KORVIA</text>
  <circle cx="50" cy="38" r="2" fill="#1E3A8A"/>
  <circle cx="330" cy="38" r="2" fill="#1E3A8A"/>
  <circle cx="50" cy="92" r="2" fill="#1E3A8A"/>
  <circle cx="330" cy="92" r="2" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "glassetch",
        "name": "Glass Etch",
        "desc": "The Korvia wordmark etched into a frosted glass panel, catching silver moonlight at its edges.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "glass", "etch", "frost"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 20px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia glass etch wordmark">
  <rect x="30" y="20" width="320" height="90" rx="4" fill="rgba(200,210,230,0.08)" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="30" y1="20" x2="350" y2="110" stroke="rgba(192,192,192,0.25)" stroke-width="1"/>
  <line x1="350" y1="20" x2="30" y2="110" stroke="rgba(192,192,192,0.25)" stroke-width="1"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="rgba(248,250,252,0.15)" stroke="#C0C0C0" stroke-width="2">KORVIA</text>
  <text x="192" y="80" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="rgba(192,192,192,0.6)" stroke-width="1">KORVIA</text>
</svg>''',
    },
    {
        "id": "waxseal",
        "name": "Wax Seal",
        "desc": "Korvia embossed on a regal wax seal with a silver ribbon, ready to certify hospitality.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "wax", "seal", "ribbon"],
        "mark_css": ".logo-mark svg { max-width: 320px; filter: drop-shadow(0 0 22px rgba(192,192,192,0.4)); }",
        "svg": '''<svg viewBox="0 0 320 160" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia wax seal wordmark">
  <path d="M30 30 L290 30 L290 50 L30 50 Z" fill="#1E3A8A"/>
  <path d="M30 110 L290 110 L290 130 L30 130 Z" fill="#1E3A8A"/>
  <circle cx="160" cy="80" r="55" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="5"/>
  <circle cx="160" cy="80" r="48" fill="none" stroke="#1E3A8A" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="160" y="86" font-family="Cinzel, serif" font-size="28" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="#C0C0C0">KORVIA</text>
  <circle cx="160" cy="52" r="4" fill="#C0C0C0"/>
  <circle cx="160" cy="108" r="4" fill="#C0C0C0"/>
</svg>''',
    },
    {
        "id": "metalstamp",
        "name": "Metal Stamp",
        "desc": "Industrial metal-stamped Korvia letters with beveled depth and machine-bolt corners.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "metal", "stamp", "industrial"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(4px 6px 0 rgba(0,0,0,0.45)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia metal stamp wordmark">
  <text x="194" y="86" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#0A0F1E">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0" stroke="#1E3A8A" stroke-width="2">KORVIA</text>
  <circle cx="48" cy="42" r="3" fill="#1E3A8A"/>
  <circle cx="332" cy="42" r="3" fill="#1E3A8A"/>
  <circle cx="48" cy="94" r="3" fill="#1E3A8A"/>
  <circle cx="332" cy="94" r="3" fill="#1E3A8A"/>
  <line x1="48" y1="42" x2="48" y2="94" stroke="#1E3A8A" stroke-width="1"/>
  <line x1="332" y1="42" x2="332" y2="94" stroke="#1E3A8A" stroke-width="1"/>
</svg>''',
    },
    {
        "id": "embroidery",
        "name": "Embroidery",
        "desc": "Korvia stitched like silver thread on dark fabric, with loose needle paths and cloth weave.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "embroidery", "thread", "fabric"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 14px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia embroidery wordmark">
  <defs>
    <pattern id="weave" x="0" y="0" width="8" height="8" patternUnits="userSpaceOnUse">
      <path d="M0 4 L8 4 M4 0 L4 8" stroke="rgba(192,192,192,0.15)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect x="30" y="25" width="320" height="80" fill="url(#weave)"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="#C0C0C0" stroke-width="3" stroke-dasharray="5 3">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="#1E3A8A" stroke-width="1" stroke-dasharray="3 5" opacity="0.7">KORVIA</text>
  <line x1="340" y1="45" x2="360" y2="35" stroke="#C0C0C0" stroke-width="2" stroke-linecap="round"/>
  <circle cx="362" cy="34" r="3" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "stonecarve",
        "name": "Stone Carve",
        "desc": "The Korvia wordmark chiseled from a solid stone block, with rough fractures and chisel marks.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stone", "carve", "chisel"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.25)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia stone carve wordmark">
  <rect x="30" y="25" width="320" height="80" rx="2" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="3"/>
  <path d="M35 30 L60 100 M345 30 L320 100 M50 35 L90 95 M330 35 L290 95" stroke="rgba(10,15,30,0.4)" stroke-width="2"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="3">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="rgba(192,192,192,0.4)" stroke-width="1">KORVIA</text>
</svg>''',
    },
    {
        "id": "waterreflection",
        "name": "Water Reflection",
        "desc": "Korvia sits on the waterline, its mirrored reflection rippling below in still moonlit water.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "water", "reflection", "ripple"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 22px rgba(30,58,138,0.5)); }",
        "svg": '''<svg viewBox="0 0 380 150" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia water reflection wordmark">
  <text x="190" y="68" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
  <text x="190" y="112" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0" opacity="0.25" transform="scale(1,-1) translate(0,-224)">KORVIA</text>
  <line x1="30" y1="78" x2="350" y2="78" stroke="#1E3A8A" stroke-width="2"/>
  <path d="M40 92 Q60 84 80 92 Q100 100 120 92 Q140 84 160 92" fill="none" stroke="#1E3A8A" stroke-width="2" opacity="0.5"/>
  <path d="M220 100 Q240 92 260 100 Q280 108 300 100 Q320 92 340 100" fill="none" stroke="#1E3A8A" stroke-width="2" opacity="0.5"/>
</svg>''',
    },
    {
        "id": "longshadow",
        "name": "Long Shadow",
        "desc": "Korvia casts a dramatic flat long shadow across the dark canvas, depth without noise.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "shadow", "flat", "depth"],
        "mark_css": ".logo-mark svg { max-width: 380px; }",
        "svg": '''<svg viewBox="0 0 420 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia long shadow wordmark">
  <text x="194" y="86" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#1E3A8A">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "blueprint",
        "name": "Blueprint",
        "desc": "Korvia drawn as architectural blueprint lines over a construction grid and dimension marks.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "blueprint", "architecture", "grid"],
        "mark_css": ".logo-mark svg { max-width: 380px; background: rgba(30,58,138,0.25); border: 1px solid #C0C0C0; }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia blueprint wordmark">
  <defs>
    <pattern id="grid" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0 L0 0 L0 20" fill="none" stroke="rgba(192,192,192,0.2)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect x="25" y="20" width="330" height="90" fill="url(#grid)"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="none" stroke="#C0C0C0" stroke-width="1.5">KORVIA</text>
  <line x1="40" y1="35" x2="40" y2="50" stroke="#1E3A8A" stroke-width="2"/>
  <line x1="35" y1="42" x2="45" y2="42" stroke="#1E3A8A" stroke-width="2"/>
  <line x1="340" y1="80" x2="340" y2="95" stroke="#1E3A8A" stroke-width="2"/>
  <line x1="335" y1="87" x2="345" y2="87" stroke="#1E3A8A" stroke-width="2"/>
  <line x1="40" y1="42" x2="340" y2="87" stroke="rgba(192,192,192,0.4)" stroke-width="1" stroke-dasharray="4 4"/>
</svg>''',
    },
    {
        "id": "mosaictile",
        "name": "Mosaic Tile",
        "desc": "The Korvia wordmark built from small hand-laid mosaic tiles with silver grout lines.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "mosaic", "tile", "grout"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 16px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia mosaic tile wordmark">
  <defs>
    <clipPath id="tiletext">
      <text x="190" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.08em">KORVIA</text>
    </clipPath>
  </defs>
  <g clip-path="url(#tiletext)">
    <rect x="0" y="0" width="380" height="130" fill="#0A0F1E"/>
    <g stroke="#C0C0C0" stroke-width="1">
      <rect x="40" y="35" width="28" height="28" fill="#1E3A8A"/>
      <rect x="68" y="35" width="28" height="28" fill="#C0C0C0"/>
      <rect x="96" y="35" width="28" height="28" fill="#1E3A8A"/>
      <rect x="124" y="35" width="28" height="28" fill="#C0C0C0"/>
      <rect x="152" y="35" width="28" height="28" fill="#1E3A8A"/>
      <rect x="180" y="35" width="28" height="28" fill="#C0C0C0"/>
      <rect x="208" y="35" width="28" height="28" fill="#1E3A8A"/>
      <rect x="40" y="63" width="28" height="28" fill="#C0C0C0"/>
      <rect x="68" y="63" width="28" height="28" fill="#1E3A8A"/>
      <rect x="96" y="63" width="28" height="28" fill="#C0C0C0"/>
      <rect x="124" y="63" width="28" height="28" fill="#1E3A8A"/>
      <rect x="152" y="63" width="28" height="28" fill="#C0C0C0"/>
      <rect x="180" y="63" width="28" height="28" fill="#1E3A8A"/>
      <rect x="208" y="63" width="28" height="28" fill="#C0C0C0"/>
    </g>
  </g>
  <text x="190" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="none" stroke="#C0C0C0" stroke-width="2">KORVIA</text>
</svg>''',
    },
    {
        "id": "leatheremboss",
        "name": "Leather Emboss",
        "desc": "Korvia stamped into luxury leather grain, with pressed depth and silver foil edges.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "leather", "emboss", "luxury"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia leather emboss wordmark">
  <defs>
    <filter id="grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" result="noise"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.6  0 0 0 0 0.6  0 0 0 0 0.6  0 0 0 0.3 0"/>
    </filter>
  </defs>
  <rect x="30" y="25" width="320" height="80" rx="8" fill="#1E3A8A"/>
  <rect x="30" y="25" width="320" height="80" rx="8" filter="url(#grain)"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#0A0F1E" stroke="#C0C0C0" stroke-width="2">KORVIA</text>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="52" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="rgba(192,192,192,0.5)" stroke-width="1">KORVIA</text>
</svg>''',
    },
    {
        "id": "sanddunesmark",
        "name": "Sand Dunes Wordmark",
        "desc": "The Korvia wordmark rises and falls like wind-sculpted desert dunes under moonlight.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "dunes", "sand", "desert"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 20px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia sand dunes wordmark">
  <path d="M0 110 Q60 70 120 90 Q180 110 240 80 Q300 50 380 70 L380 130 L0 130 Z" fill="#1E3A8A" opacity="0.7"/>
  <path d="M0 125 Q80 95 160 110 Q240 125 320 100 Q350 90 380 95 L380 130 L0 130 Z" fill="#C0C0C0" opacity="0.3"/>
  <text x="190" y="78" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "firelight",
        "name": "Firelight",
        "desc": "Korvia glows like embers and firelight, with warm silver sparks above each letter.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "fire", "embers", "glow"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 28px rgba(192,192,192,0.55)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia firelight wordmark">
  <text x="190" y="88" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
  <path d="M60 45 Q65 30 70 45 Q75 30 80 45" fill="none" stroke="#C0C0C0" stroke-width="2" opacity="0.8"/>
  <path d="M115 40 Q120 22 125 40 Q130 22 135 40" fill="none" stroke="#C0C0C0" stroke-width="2" opacity="0.8"/>
  <path d="M170 45 Q175 30 180 45 Q185 30 190 45" fill="none" stroke="#C0C0C0" stroke-width="2" opacity="0.8"/>
  <path d="M225 40 Q230 22 235 40 Q240 22 245 40" fill="none" stroke="#C0C0C0" stroke-width="2" opacity="0.8"/>
  <path d="M280 45 Q285 30 290 45 Q295 30 300 45" fill="none" stroke="#C0C0C0" stroke-width="2" opacity="0.8"/>
  <circle cx="70" cy="38" r="2" fill="#1E3A8A"/>
  <circle cx="125" cy="34" r="2" fill="#1E3A8A"/>
  <circle cx="180" cy="38" r="2" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "icecrystal",
        "name": "Ice Crystal",
        "desc": "Korvia frozen inside sharp ice shards, with fracture lines catching silver light.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "ice", "crystal", "frozen"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 22px rgba(192,192,192,0.45)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia ice crystal wordmark">
  <path d="M40 20 L190 65 L40 110 Z" fill="rgba(192,192,192,0.08)" stroke="#C0C0C0" stroke-width="2"/>
  <path d="M340 20 L190 65 L340 110 Z" fill="rgba(192,192,192,0.08)" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="190" y1="20" x2="190" y2="110" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="100" y1="42" x2="280" y2="88" stroke="rgba(30,58,138,0.5)" stroke-width="1"/>
  <line x1="280" y1="42" x2="100" y2="88" stroke="rgba(30,58,138,0.5)" stroke-width="1"/>
  <text x="190" y="78" font-family="Cinzel, serif" font-size="50" font-weight="700" text-anchor="middle" letter-spacing="0.12em" fill="#C0C0C0">KORVIA</text>
</svg>''',
    },
    {
        "id": "bambooweave",
        "name": "Bamboo Weave",
        "desc": "Korvia woven from horizontal bamboo and reed strips, overlapping like a screen.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "bamboo", "weave", "reeds"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 16px rgba(30,58,138,0.4)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia bamboo weave wordmark">
  <defs>
    <clipPath id="bambootext">
      <text x="190" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.1em">KORVIA</text>
    </clipPath>
  </defs>
  <g clip-path="url(#bambootext)">
    <rect x="0" y="0" width="380" height="130" fill="#0A0F1E"/>
    <rect x="30" y="35" width="320" height="12" fill="#C0C0C0"/>
    <rect x="30" y="51" width="320" height="12" fill="#1E3A8A"/>
    <rect x="30" y="67" width="320" height="12" fill="#C0C0C0"/>
    <rect x="30" y="83" width="320" height="12" fill="#1E3A8A"/>
    <line x1="60" y1="35" x2="60" y2="95" stroke="#0A0F1E" stroke-width="4"/>
    <line x1="110" y1="35" x2="110" y2="95" stroke="#0A0F1E" stroke-width="4"/>
    <line x1="160" y1="35" x2="160" y2="95" stroke="#0A0F1E" stroke-width="4"/>
    <line x1="210" y1="35" x2="210" y2="95" stroke="#0A0F1E" stroke-width="4"/>
    <line x1="260" y1="35" x2="260" y2="95" stroke="#0A0F1E" stroke-width="4"/>
    <line x1="310" y1="35" x2="310" y2="95" stroke="#0A0F1E" stroke-width="4"/>
  </g>
  <text x="190" y="84" font-family="Cinzel, serif" font-size="56" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="none" stroke="#C0C0C0" stroke-width="2">KORVIA</text>
</svg>''',
    },
    {
        "id": "sailboat",
        "name": "Sailboat",
        "desc": "The letters of Korvia become sails on two boats drifting across silver water.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "sailboat", "sails", "water"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 18px rgba(30,58,138,0.45)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia sailboat wordmark">
  <path d="M20 100 Q80 85 140 95 Q200 105 260 92 Q320 79 360 88" fill="none" stroke="#1E3A8A" stroke-width="4" stroke-linecap="round"/>
  <path d="M50 90 L50 45 L110 90 Z" fill="#C0C0C0" opacity="0.9"/>
  <text x="80" y="78" font-family="Cinzel, serif" font-size="28" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#0A0F1E">KOR</text>
  <line x1="50" y1="95" x2="110" y2="95" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round"/>
  <path d="M220 90 L220 45 L280 90 Z" fill="#C0C0C0" opacity="0.9"/>
  <text x="250" y="78" font-family="Cinzel, serif" font-size="28" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#0A0F1E">VIA</text>
  <line x1="220" y1="95" x2="280" y2="95" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round"/>
</svg>''',
    },
    {
        "id": "coffeesteam",
        "name": "Coffee Steam",
        "desc": "The word Korvia forms from the rising steam above a coffee cup, curling into letterforms.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "coffee", "steam", "cup"],
        "mark_css": ".logo-mark svg { max-width: 340px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia coffee steam wordmark">
  <path d="M100 95 Q95 75 105 60 Q115 45 105 30" fill="none" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round" opacity="0.9"/>
  <path d="M140 95 Q135 70 145 55 Q155 40 145 25" fill="none" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round" opacity="0.85"/>
  <path d="M180 95 Q175 72 185 58 Q195 44 185 30" fill="none" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round" opacity="0.8"/>
  <path d="M220 95 Q215 74 225 60 Q235 46 225 32" fill="none" stroke="#C0C0C0" stroke-width="4" stroke-linecap="round" opacity="0.75"/>
  <text x="170" y="120" font-family="Cinzel, serif" font-size="44" font-weight="700" text-anchor="middle" letter-spacing="0.14em" fill="#C0C0C0">KORVIA</text>
  <ellipse cx="170" cy="132" rx="55" ry="10" fill="none" stroke="#1E3A8A" stroke-width="4"/>
</svg>''',
    },
    {
        "id": "citrusgarnish",
        "name": "Citrus Garnish",
        "desc": "Korvia peeled from curling citrus rind, with juicy segments forming punctuation.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "citrus", "garnish", "peel"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 16px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia citrus garnish wordmark">
  <path d="M30 70 Q60 40 90 70 Q120 100 150 70 Q180 40 210 70 Q240 100 270 70 Q300 40 330 70 Q360 100 380 80" fill="none" stroke="#C0C0C0" stroke-width="7" stroke-linecap="round"/>
  <path d="M30 70 Q60 40 90 70 Q120 100 150 70 Q180 40 210 70 Q240 100 270 70 Q300 40 330 70 Q360 100 380 80" fill="none" stroke="#1E3A8A" stroke-width="3" stroke-linecap="round"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="48" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#0A0F1E">KORVIA</text>
  <circle cx="350" cy="55" r="12" fill="#C0C0C0" opacity="0.9"/>
  <line x1="342" y1="55" x2="358" y2="55" stroke="#0A0F1E" stroke-width="1"/>
  <line x1="350" y1="47" x2="350" y2="63" stroke="#0A0F1E" stroke-width="1"/>
</svg>''',
    },
    {
        "id": "streetmural",
        "name": "Street Mural",
        "desc": "Korvia spray-painted as a bold street mural across a dark brick wall with drips.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "mural", "brick", "street"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 20px rgba(192,192,192,0.3)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia street mural wordmark">
  <defs>
    <pattern id="brick" x="0" y="0" width="40" height="20" patternUnits="userSpaceOnUse">
      <rect width="40" height="20" fill="#0A0F1E"/>
      <path d="M0 20 L40 20 M20 0 L20 20" stroke="#1E3A8A" stroke-width="2"/>
    </pattern>
  </defs>
  <rect x="20" y="15" width="340" height="100" fill="url(#brick)"/>
  <text x="190" y="82" font-family="Cinzel, serif" font-size="58" font-weight="700" text-anchor="middle" letter-spacing="0.08em" fill="#C0C0C0" stroke="#1E3A8A" stroke-width="2">KORVIA</text>
  <path d="M130 95 L134 115" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <path d="M250 95 L246 118" stroke="#C0C0C0" stroke-width="3" stroke-linecap="round"/>
  <circle cx="170" cy="55" r="4" fill="#1E3A8A"/>
  <circle cx="220" cy="75" r="3" fill="#1E3A8A"/>
</svg>''',
    },
    {
        "id": "origamifold",
        "name": "Origami Fold",
        "desc": "Korvia folded from paper planes and cranes, each letter a crisp paper facet.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "origami", "paper", "fold"],
        "mark_css": ".logo-mark svg { max-width: 380px; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }",
        "svg": '''<svg viewBox="0 0 380 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia origami fold wordmark">
  <text x="190" y="86" font-family="Cinzel, serif" font-size="54" font-weight="700" text-anchor="middle" letter-spacing="0.1em" fill="#C0C0C0">KORVIA</text>
  <path d="M55 35 L80 55 L55 75 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <path d="M320 35 L345 55 L320 75 Z" fill="#1E3A8A" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="70" y1="55" x2="90" y2="55" stroke="#C0C0C0" stroke-width="2"/>
  <line x1="290" y1="55" x2="310" y2="55" stroke="#C0C0C0" stroke-width="2"/>
  <path d="M150 25 L160 40 L140 40 Z" fill="#C0C0C0" opacity="0.9"/>
  <path d="M230 25 L240 40 L220 40 Z" fill="#C0C0C0" opacity="0.9"/>
  <path d="M140 40 L160 40 L150 55 Z" fill="#1E3A8A" opacity="0.8"/>
  <path d="M220 40 L240 40 L230 55 Z" fill="#1E3A8A" opacity="0.8"/>
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
    print(f"Appended {len(CONCEPTS)} refined whole-word Korvia wordmark concepts.")


if __name__ == "__main__":
    main()
