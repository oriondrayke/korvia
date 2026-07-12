#!/usr/bin/env python3
"""Append 20 pure typographic Korvia logo concepts (IDs 239-258) in the Moonlight setting."""
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


def build_content(html, tagline):
    portal = PORTAL_CONTENT.replace("{tagline}", tagline)
    return f'''<style>
.portal-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }}
.logo-mark {{ text-align: center; margin: 0 0 12px; }}
.logo-tagline {{ font-family: 'Inter', sans-serif; font-size: clamp(0.95rem, 2.2vw, 1.25rem); letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; text-align: center; margin: 0 0 40px; }}
a {{ text-decoration: none; color: inherit; }}
</style>
<div class="logo-mark">{html}</div>
<p class="logo-tagline">{tagline}</p>
{portal}'''


CONCEPTS = [
    {
        "id": "typo-connected",
        "name": "Connected",
        "desc": "All six letters of Korvia are linked by a single continuous stroke so the word reads as one flowing gesture.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "connected", "script"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: -0.14em; color: #C0C0C0; display: inline-block; position: relative; padding-bottom: 10px; }
.logo-mark .korvia-word::after { content: ""; position: absolute; left: 4%; right: 4%; bottom: 0; height: 5px; background: linear-gradient(90deg, #C0C0C0, #1E3A8A); border-radius: 3px; }
.logo-mark .korvia-word span { display: inline-block; position: relative; }
.logo-mark .korvia-word span:nth-child(1) { transform: translateY(-2px); }
.logo-mark .korvia-word span:nth-child(4) { transform: translateY(2px); }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-ligature",
        "name": "Ligature",
        "desc": "The letters o+r and v+i are drawn as custom ligatures, merging adjacent forms into unified glyphs.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "ligature", "merge"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.02em; color: #C0C0C0; }
.logo-mark .korvia-word span { display: inline-block; position: relative; }
.logo-mark .korvia-word span:nth-child(2)::after { content: "r"; position: absolute; left: 70%; top: 0; color: #1E3A8A; }
.logo-mark .korvia-word span:nth-child(4)::after { content: "i"; position: absolute; left: 58%; top: 0; color: #1E3A8A; }
.logo-mark .korvia-word span:nth-child(2),
.logo-mark .korvia-word span:nth-child(4) { margin-right: 0.22em; }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-stacked",
        "name": "Stacked",
        "desc": "The six letters of Korvia are stacked vertically into a single centered column.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stacked", "vertical"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.2rem, 7vw, 4rem); font-weight: 700; line-height: 0.85; color: #C0C0C0; display: inline-flex; flex-direction: column; align-items: center; }
.logo-mark .korvia-word span { display: block; }
.logo-mark .korvia-word span:nth-child(odd) { color: #C0C0C0; }
.logo-mark .korvia-word span:nth-child(even) { color: #1E3A8A; text-shadow: -1px -1px 0 #C0C0C0, 1px -1px 0 #C0C0C0, -1px 1px 0 #C0C0C0, 1px 1px 0 #C0C0C0; }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-arched",
        "name": "Arched",
        "desc": "The Korvia wordmark bends along an upward arc like a marquee sign.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "arched", "curve"],
        "mark_css": """
.logo-mark svg { max-width: 420px; width: 100%; height: auto; filter: drop-shadow(0 0 18px rgba(192,192,192,0.35)); }
        """,
        "html": """<svg viewBox="0 0 420 140" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia arched wordmark">
  <defs>
    <path id="arch" d="M 40 110 Q 210 10 380 110" fill="none"/>
    <linearGradient id="archGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A"/>
      <stop offset="50%" stop-color="#C0C0C0"/>
      <stop offset="100%" stop-color="#1E3A8A"/>
    </linearGradient>
  </defs>
  <text font-family="Cinzel, serif" font-size="56" font-weight="700" fill="url(#archGrad)" letter-spacing="0.04em">
    <textPath href="#arch" startOffset="50%" text-anchor="middle">Korvia</textPath>
  </text>
</svg>""",
    },
    {
        "id": "typo-mirror",
        "name": "Mirror",
        "desc": "Korvia is reflected below a horizontal line, fading into the dark canvas like moonlight on water.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "mirror", "reflection"],
        "mark_css": """
.logo-mark .mirror-wrap { position: relative; display: inline-block; }
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; color: #C0C0C0; display: block; }
.logo-mark .korvia-reflect { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; color: #C0C0C0; display: block; transform: scaleY(-1); opacity: 0.35; mask-image: linear-gradient(to bottom, rgba(0,0,0,0.7), transparent); -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,0.7), transparent); margin-top: -0.15em; }
        """,
        "html": """<span class="mirror-wrap"><span class="korvia-word">Korvia</span><span class="korvia-reflect">Korvia</span></span>""",
    },
    {
        "id": "typo-overlap",
        "name": "Overlap",
        "desc": "Each letter of Korvia overlaps the next with transparency and a soft blend, creating depth from the letterforms alone.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "overlap", "blend"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: -0.18em; color: #C0C0C0; }
.logo-mark .korvia-word span { display: inline-block; mix-blend-mode: screen; opacity: 0.92; }
.logo-mark .korvia-word span:nth-child(1) { color: #C0C0C0; }
.logo-mark .korvia-word span:nth-child(2) { color: #1E3A8A; }
.logo-mark .korvia-word span:nth-child(3) { color: #C0C0C0; }
.logo-mark .korvia-word span:nth-child(4) { color: #1E3A8A; }
.logo-mark .korvia-word span:nth-child(5) { color: #C0C0C0; }
.logo-mark .korvia-word span:nth-child(6) { color: #1E3A8A; }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-inline",
        "name": "Inline",
        "desc": "Korvia is rendered with an inner inline stroke running through every letterform.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "inline", "stroke"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; color: #C0C0C0; position: relative; }
.logo-mark .korvia-word::before { content: "Korvia"; position: absolute; left: 0; top: 0; color: transparent; -webkit-text-stroke: 1px #1E3A8A; text-stroke: 1px #1E3A8A; z-index: -1; transform: scale(0.96); }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-extruded",
        "name": "Extruded Shadow",
        "desc": "A deep 3D extruded shadow extends from the Korvia letters toward the lower right.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "extruded", "shadow"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; color: #C0C0C0; text-shadow: 1px 1px 0 #1E3A8A, 2px 2px 0 #1E3A8A, 3px 3px 0 #1E3A8A, 4px 4px 0 #1E3A8A, 5px 5px 0 #1E3A8A, 6px 6px 0 #1E3A8A, 7px 7px 0 #1E3A8A, 8px 8px 0 rgba(30,58,138,0.7), 12px 12px 24px rgba(0,0,0,0.4); }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-stencil",
        "name": "Stencil",
        "desc": "Korvia is cut as stencil letterforms with deliberate gaps in the strokes.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stencil", "cut"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.12em; color: #C0C0C0; position: relative; }
.logo-mark .korvia-word::after { content: ""; position: absolute; inset: 0; background: repeating-linear-gradient(90deg, transparent 0px, transparent 18px, #0A0F1E 18px, #0A0F1E 22px); mix-blend-mode: darken; pointer-events: none; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-wavy",
        "name": "Wavy Baseline",
        "desc": "The Korvia letters bounce along a gently wavy baseline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "wavy", "bounce"],
        "mark_css": """
.logo-mark svg { max-width: 420px; width: 100%; height: auto; filter: drop-shadow(0 0 16px rgba(192,192,192,0.3)); }
        """,
        "html": """<svg viewBox="0 0 420 130" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia wavy baseline wordmark">
  <defs>
    <path id="wave" d="M 20 75 Q 70 45 120 75 Q 170 105 220 75 Q 270 45 320 75 Q 370 105 420 75" fill="none"/>
  </defs>
  <text font-family="Cinzel, serif" font-size="48" font-weight="700" fill="#C0C0C0" letter-spacing="0.06em">
    <textPath href="#wave" startOffset="8%">Korvia</textPath>
  </text>
  <path d="M 20 75 Q 70 45 120 75 Q 170 105 220 75 Q 270 45 320 75 Q 370 105 420 75" fill="none" stroke="#1E3A8A" stroke-width="2" stroke-dasharray="6 6" opacity="0.5"/>
</svg>""",
    },
    {
        "id": "typo-vertical",
        "name": "Vertical",
        "desc": "Korvia is rotated and read vertically from top to bottom.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "vertical", "rotated"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.6rem, 8vw, 4.6rem); font-weight: 700; letter-spacing: 0.2em; color: #C0C0C0; writing-mode: vertical-rl; text-orientation: upright; display: inline-block; border-left: 3px solid #1E3A8A; padding-left: 12px; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-thickthin",
        "name": "Thick Thin",
        "desc": "Korvia alternates between dramatic thick and razor-thin strokes.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "contrast", "thick-thin"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); letter-spacing: 0.02em; }
.logo-mark .korvia-word span { display: inline-block; }
.logo-mark .korvia-word span:nth-child(1),
.logo-mark .korvia-word span:nth-child(4),
.logo-mark .korvia-word span:nth-child(6) { font-weight: 700; color: #C0C0C0; }
.logo-mark .korvia-word span:nth-child(2),
.logo-mark .korvia-word span:nth-child(3),
.logo-mark .korvia-word span:nth-child(5) { font-weight: 400; color: #1E3A8A; text-shadow: 0 0 1px #C0C0C0; }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-negative",
        "name": "Negative Cut",
        "desc": "The word Korvia is carved out of a solid moonlit block by negative space.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "negative", "cutout"],
        "mark_css": """
.logo-mark .negative-block { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; background: linear-gradient(135deg, #C0C0C0, #1E3A8A); color: transparent; -webkit-background-clip: text; background-clip: text; position: relative; display: inline-block; }
.logo-mark .negative-block::before { content: "Korvia"; position: absolute; left: 0; top: 0; color: #0A0F1E; z-index: -1; transform: translate(4px, 4px); }
        """,
        "html": """<span class="negative-block">Korvia</span>""",
    },
    {
        "id": "typo-fragmented",
        "name": "Fragmented",
        "desc": "The Korvia letters are broken into sharp, angular fragments and reassembled.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "fragmented", "sharp"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.06em; color: #C0C0C0; }
.logo-mark .korvia-word span { display: inline-block; }
.logo-mark .korvia-word span:nth-child(1) { clip-path: polygon(0 0, 100% 15%, 85% 100%, 10% 90%); }
.logo-mark .korvia-word span:nth-child(2) { clip-path: polygon(10% 10%, 90% 0, 100% 85%, 0 100%); }
.logo-mark .korvia-word span:nth-child(3) { clip-path: polygon(0 15%, 100% 0, 90% 100%, 15% 85%); }
.logo-mark .korvia-word span:nth-child(4) { clip-path: polygon(15% 0, 100% 10%, 85% 90%, 0 100%); }
.logo-mark .korvia-word span:nth-child(5) { clip-path: polygon(0 0, 85% 15%, 100% 100%, 10% 85%); }
.logo-mark .korvia-word span:nth-child(6) { clip-path: polygon(10% 10%, 90% 0, 100% 100%, 0 90%); }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-folded",
        "name": "Folded Paper",
        "desc": "Each letter of Korvia is shaded like a strip of folded paper catching moonlight.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "folded", "paper"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.6rem, 8.5vw, 5rem); font-weight: 700; letter-spacing: 0.04em; }
.logo-mark .korvia-word span { display: inline-block; background: linear-gradient(105deg, #C0C0C0 45%, #8a9ac0 50%, #1E3A8A 55%); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0 1px; filter: drop-shadow(2px 2px 0 rgba(0,0,0,0.35)); }
        """,
        "html": """<span class="korvia-word"><span>K</span><span>o</span><span>r</span><span>v</span><span>i</span><span>a</span></span>""",
    },
    {
        "id": "typo-stripe",
        "name": "Stripe Through",
        "desc": "A single horizontal silver stripe cuts through the center of every Korvia letter.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stripe", "cut"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.08em; color: #C0C0C0; position: relative; display: inline-block; }
.logo-mark .korvia-word::after { content: ""; position: absolute; left: -2%; right: -2%; top: 52%; height: 5px; background: #1E3A8A; mix-blend-mode: overlay; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-sharedcrossbar",
        "name": "Shared Crossbar",
        "desc": "A continuous horizontal crossbar is shared across the Korvia letterforms.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "crossbar", "shared"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.06em; color: #C0C0C0; position: relative; display: inline-block; }
.logo-mark .korvia-word::before { content: ""; position: absolute; left: 0; right: 0; top: 38%; height: 4px; background: #C0C0C0; z-index: -1; }
.logo-mark .korvia-word::after { content: ""; position: absolute; left: 0; right: 0; top: 62%; height: 4px; background: #1E3A8A; z-index: -1; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-mosaic",
        "name": "Mosaic Type",
        "desc": "The Korvia letters are filled with a mosaic of small square tiles.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "mosaic", "tiles"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.06em; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 6px, #1E3A8A 6px, #1E3A8A 12px), repeating-linear-gradient(0deg, #C0C0C0 0px, #C0C0C0 6px, #0A0F1E 6px, #0A0F1E 12px); background-size: 12px 12px; -webkit-background-clip: text; background-clip: text; color: transparent; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
    {
        "id": "typo-brush",
        "name": "Brush Stroke",
        "desc": "Korvia is lettered with bold, brush-painted strokes and ragged edges.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "brush", "paint"],
        "mark_css": """
.logo-mark svg { max-width: 420px; width: 100%; height: auto; filter: drop-shadow(4px 4px 0 rgba(30,58,138,0.5)); }
        """,
        "html": """<svg viewBox="0 0 420 120" xmlns="http://www.w3.org/2000/svg" aria-label="Korvia brush stroke wordmark">
  <defs>
    <filter id="rough">
      <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
  <text x="210" y="78" font-family="Cinzel, serif" font-size="60" font-weight="700" text-anchor="middle" letter-spacing="0.02em" fill="#C0C0C0" filter="url(#rough)">Korvia</text>
  <text x="210" y="78" font-family="Cinzel, serif" font-size="60" font-weight="700" text-anchor="middle" letter-spacing="0.02em" fill="none" stroke="#1E3A8A" stroke-width="2" opacity="0.4" filter="url(#rough)">Korvia</text>
</svg>""",
    },
    {
        "id": "typo-neon",
        "name": "Neon Outline",
        "desc": "Hollow outlined Korvia letters glow with a cool neon silver light.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "neon", "outline"],
        "mark_css": """
.logo-mark .korvia-word { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.4rem); font-weight: 700; letter-spacing: 0.1em; color: #0A0F1E; -webkit-text-stroke: 2px #C0C0C0; text-stroke: 2px #C0C0C0; text-shadow: 0 0 8px #C0C0C0, 0 0 18px #1E3A8A, 0 0 32px #1E3A8A; }
        """,
        "html": """<span class="korvia-word">Korvia</span>""",
    },
]


def build_entry(c, tagline):
    css = MOONLIGHT_CSS.strip() + "\n" + c["mark_css"].strip()
    content = build_content(c["html"], tagline)
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
    print(f"Appended {len(CONCEPTS)} pure typographic Korvia logo concepts.")


if __name__ == "__main__":
    main()
