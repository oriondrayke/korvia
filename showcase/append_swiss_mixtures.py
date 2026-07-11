#!/usr/bin/env python3
"""Append 10 Art Deco + Grunge + Swiss Grid mixture directions."""
from pathlib import Path

NEW_ENTRIES = '''
    {
        "id": "swissgilded",
        "name": "Swiss Gilded Grunge",
        "tagline": "Gold frames locked in a Swiss grid, then distressed.",
        "desc": "Swiss Gilded Grunge forces Korvia's late-night venues into an asymmetric grid: gold borders, red accents, torn edges, and absolute order barely holding together.",
        "palette": ["#0A0A0A", "#C5A059", "#E42718"],
        "shapes": ["grid-rectangle", "gold-rule", "red-stamp"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #f4f3ef;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 8px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; letter-spacing: 0.06em; }
.desc { color: #a8a29e; margin-bottom: 40px; max-width: 560px; }
.swiss-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: #e42718; border: 1px solid #e42718; margin-bottom: 24px; }
.swiss-cell { background: #111; padding: 24px; border: 1px solid #333; }
.swiss-cell.red { background: #e42718; color: #fff; }
.swiss-cell.gold { background: #c5a059; color: #000; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem; font-weight: 700; cursor: pointer;
}
.rule { height: 4px; background: #e42718; margin-bottom: 24px; }
.stamp { width: 70px; height: 70px; background: #e42718; color: #fff; display: inline-flex; align-items: center; justify-content: center; font-weight: 800; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #000; color: #78716c; border-top: 8px solid #e42718; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="swiss-grid">
<a href="#client" class="swiss-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="swiss-cell gold" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="swiss-cell red" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="swiss-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="rule" style="width:70%"></div><div class="stamp">K</div>
</div>
"""
    },
    {
        "id": "reddecay",
        "name": "Red Deco Decay",
        "tagline": "Swiss red cutting through rotting gold.",
        "desc": "Red Deco Decay gives Korvia's historic venues a Swiss grid spine with peeling gold walls and a single aggressive red accent.",
        "palette": ["#1A1510", "#C5A059", "#E42718"],
        "shapes": ["red-bar", "peeling-gold", "grid-line"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #1a1510; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #201a12; border: 1px solid #c5a059; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #e42718;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; border: 2px solid #c5a059; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px; background: #120e0a; color: #6b5b3e; border-top: 1px solid #6b5b3e; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div>
</div>
"""
    },
    {
        "id": "gridrust",
        "name": "Grid Rust",
        "tagline": "Swiss grid held together with rusty bolts.",
        "desc": "Grid Rust gives Korvia's industrial food halls a Swiss layout with rusted plates, gold labels, and red warning marks.",
        "palette": ["#2B1D16", "#C5A059", "#E42718"],
        "shapes": ["grid-plate", "rust-bolt", "red-tick"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Anton\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #2b1d16; color: #e6d5b8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1f140f; border-bottom: 3px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Anton', sans-serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-transform: uppercase; }
.desc { color: #c2a882; margin-bottom: 40px; }
.rust-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background: #e42718; border: 2px solid #e42718; margin-bottom: 24px; }
.rust-cell { background: #3a271d; padding: 24px; border: 1px solid #8b7d4b; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #c5a059; background: #b3542f;
    color: #e6d5b8; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.plate { width: 120px; height: 80px; background: repeating-linear-gradient(45deg, #c5a059, #c5a059 3px, #b3542f 3px, #b3542f 6px); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.bolt { width: 12px; height: 12px; background: #c5a059; border-radius: 50%; display: inline-block; margin: 3px; box-shadow: inset 0 0 3px #000; }
.tick { width: 60px; height: 8px; background: #e42718; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #1f140f; color: #8a6a4a; border-top: 3px solid #e42718; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="rust-grid">
<a href="#client" class="rust-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="rust-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="rust-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="rust-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="plate"></div><div class="tick"></div><div style="margin-bottom:24px;"><div class="bolt"></div><div class="bolt"></div><div class="bolt"></div></div>
</div>
"""
    },
    {
        "id": "brutalornate",
        "name": "Brutal Ornate",
        "tagline": "Ornate frames smashed into a Swiss grid.",
        "desc": "Brutal Ornate gives Korvia's gallery cafés and concept stores a clash: delicate gold borders, harsh grid lines, and thick red rules.",
        "palette": ["#F4F3EF", "#111111", "#E42718"],
        "shapes": ["framed-grid", "red-rule", "gold-border"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cormorant+Garamond:ital,wght@0,600;1,600\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #f4f3ef; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #fff; border-bottom: 8px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #111; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; font-style: italic; }
.desc { color: #555; margin-bottom: 40px; }
.brutal-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 2px; background: #111; border: 2px solid #111; margin-bottom: 24px; }
.brutal-cell { background: #fff; padding: 24px; border: 1px solid #111; }
.brutal-cell.red { background: #e42718; color: #fff; }
.brutal-cell.gold { background: #f4f3ef; border: 3px double #c5a059; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #111; background: #111;
    color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.frame { width: 100px; height: 140px; border: 4px double #c5a059; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.rule { height: 6px; background: #e42718; width: 120px; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #111; color: #fff; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="brutal-grid">
<a href="#client" class="brutal-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="brutal-cell gold" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="brutal-cell red" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="brutal-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;background:#fff;color:#111;border:2px solid #111;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="frame"></div><div class="rule"></div>
</div>
"""
    },
    {
        "id": "swissvelvet",
        "name": "Swiss Velvet",
        "tagline": "Purple velvet folded into a Swiss grid.",
        "desc": "Swiss Velvet gives Korvia's lounges a strict asymmetric layout in deep velvet, gold, and a single red signal.",
        "palette": ["#1A0F1F", "#9B7EBD", "#E42718"],
        "shapes": ["velvet-grid", "gold-rule", "red-signal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Playfair+Display:ital,wght@0,600;1,600\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #1a0f1f; color: #e8e0f0;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120916; border-bottom: 1px solid #9b7ebd;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Playfair Display', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b8a8c8; margin-bottom: 40px; }
.velvet-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 1px; background: #9b7ebd; border: 1px solid #9b7ebd; margin-bottom: 24px; }
.velvet-cell { background: #24132d; padding: 24px; }
.velvet-cell.signal { background: #e42718; color: #fff; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.velvet-swatch { width: 100px; height: 80px; background: radial-gradient(ellipse at center, #4a2a5a 0%, #1a0f1f 100%); border: 1px solid #9b7ebd; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.gold-rule { height: 2px; background: linear-gradient(90deg, transparent, #c5a059, transparent); width: 150px; display: inline-block; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #120916; color: #6b6278; border-top: 1px solid #9b7ebd; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="velvet-grid">
<a href="#client" class="velvet-cell signal" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="velvet-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="velvet-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="velvet-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="velvet-swatch"></div><div class="gold-rule"></div>
</div>
"""
    },
    {
        "id": "constructedbrass",
        "name": "Constructed Brass",
        "tagline": "Swiss constructivism meets corroded brass.",
        "desc": "Constructed Brass gives Korvia's transit-hub kiosks a poster-style grid in red, black, and tarnished brass.",
        "palette": ["#1A1710", "#8B7D4B", "#E42718"],
        "shapes": ["construct-grid", "brass-triangle", "red-diagonal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700\u0026family=Inter:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #1a1710; color: #d8d0c0;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #12100a; border-bottom: 2px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #8b7d4b; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Oswald', sans-serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-transform: uppercase; }
.desc { color: #a8a080; margin-bottom: 40px; }
.const-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; background: #e42718; border: 2px solid #e42718; margin-bottom: 24px; }
.const-cell { background: #2a2518; padding: 20px; text-align: center; }
.const-cell.red { background: #e42718; color: #fff; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #8b7d4b; background: transparent;
    color: #8b7d4b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.brass-tri { width: 0; height: 0; border-left: 40px solid transparent; border-right: 40px solid transparent; border-bottom: 70px solid #8b7d4b; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.diag { width: 120px; height: 12px; background: #e42718; transform: rotate(-30deg); display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #12100a; color: #6b6048; border-top: 2px solid #e42718; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="const-grid">
<a href="#client" class="const-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1rem;">Client</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Discover venues.</p></a>
<a href="#restaurant" class="const-cell red" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1rem;">Restaurant</h3><p style="margin:0;font-size:.75rem;line-height:1.4;">QR menus.</p></a>
<a href="#hotel" class="const-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1rem;">Hotel</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Room service.</p></a>
<a href="#events" class="const-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1rem;">Events</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Parties.</p></a>
<a href="#" class="const-cell red" style="display:block;"><h3 style="margin:0;font-size:1rem;">Scan QR</h3></a>
<a href="#" class="const-cell" style="display:block;"><h3 style="margin:0;font-size:1rem;">Dashboard</h3></a>
</div>
<h2>Direction accent</h2>
<div class="brass-tri"></div><div class="diag"></div>
</div>
"""
    },
    {
        "id": "gridriot",
        "name": "Grid Riot",
        "tagline": "A Swiss grid spray-painted gold and pink.",
        "desc": "Grid Riot gives Korvia's festival pop-ups a strict grid that has been stickered, taped, and tagged.",
        "palette": ["#0A0A0A", "#D4AF37", "#FF2E88"],
        "shapes": ["grid-sticker", "gold-tag", "pink-tape"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Archivo+Black\u0026family=Inter:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #fff;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 4px solid #ff2e88;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #d4af37; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Archivo Black', sans-serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d4af37; margin-bottom: 40px; }
.riot-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2px; background: #ff2e88; border: 2px solid #ff2e88; margin-bottom: 24px; }
.riot-cell { background: #111; padding: 24px; border: 1px solid #333; }
.riot-cell.gold { background: #d4af37; color: #000; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #d4af37; background: #ff2e88;
    color: #000; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; cursor: pointer;
}
.sticker { width: 100px; height: 70px; background: #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; transform: rotate(-6deg); position: relative; }
.sticker::after { content: "VIP"; position: absolute; inset: 0; display: grid; place-items: center; color: #000; font-weight: 700; }
.tape { width: 90px; height: 22px; background: rgba(255,46,136,0.8); transform: rotate(10deg); display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #000; color: #d4af37; border-top: 4px solid #ff2e88; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="riot-grid">
<a href="#client" class="riot-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="riot-cell gold" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="riot-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="riot-cell gold" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="sticker"></div><div class="tape"></div>
</div>
"""
    },
    {
        "id": "asymmetricpalace",
        "name": "Asymmetric Palace",
        "tagline": "Palace luxury pushed off-center.",
        "desc": "Asymmetric Palace gives Korvia's boutique hotels a Swiss layout where every element is intentionally off-center, framed in gold, and slightly worn.",
        "palette": ["#0D1321", "#C5A059", "#E42718"],
        "shapes": ["off-center-frame", "gold-rule", "red-dot"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=Inter:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #0d1321; color: #e6dcc8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #080c14; border-bottom: 1px solid #c5a059;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; }
.asym-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 2px; background: #c5a059; border: 1px solid #c5a059; margin-bottom: 24px; }
.asym-cell { background: #121a2b; padding: 24px; }
.asym-cell.red { background: #e42718; color: #fff; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.frame2 { width: 120px; height: 80px; border: 2px solid #c5a059; margin-left: 40px; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.frame2::after { content: ""; position: absolute; top: 10px; left: -20px; width: 100%; height: 100%; border: 1px solid #e42718; z-index: -1; }
.red-dot { width: 20px; height: 20px; background: #e42718; border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #080c14; color: #6b6278; border-top: 1px solid #c5a059; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="asym-grid">
<a href="#client" class="asym-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="asym-cell red" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="asym-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="asym-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="frame2"></div><div class="red-dot"></div>
</div>
"""
    },
    {
        "id": "swisscracked",
        "name": "Swiss Cracked",
        "tagline": "White grid, gold cracks, red signal.",
        "desc": "Swiss Cracked gives Korvia's daytime cafés a clean Swiss layout with hairline gold fractures and one urgent red mark.",
        "palette": ["#F5F1EA", "#D4AF37", "#E42718"],
        "shapes": ["cracked-grid", "gold-fracture", "red-mark"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #f5f1ea; color: #3a3530;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #fff; border-bottom: 8px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #3a3530; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8a7e72; margin-bottom: 40px; }
.cracked-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2px; background: #3a3530; border: 2px solid #3a3530; margin-bottom: 24px; }
.cracked-cell { background: #fff; padding: 24px; border: 1px solid #d4af37; position: relative; }
.cracked-cell::before { content: ""; position: absolute; top: 20px; left: 10px; width: 50px; height: 1px; background: #d4af37; transform: rotate(30deg); opacity: 0.6; }
.cracked-cell.red { background: #e42718; color: #fff; border-color: #e42718; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #8a7e72; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.marble2 { width: 120px; height: 90px; background: #fff; border: 1px solid #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.marble2::after { content: ""; position: absolute; top: 30px; left: 15px; width: 70px; height: 1px; background: #d4af37; transform: rotate(-20deg); opacity: 0.6; }
.mark { width: 60px; height: 8px; background: #e42718; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #3a3530; color: #fff; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="cracked-grid">
<a href="#client" class="cracked-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="cracked-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="cracked-cell red" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="cracked-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="marble2"></div><div class="mark"></div>
</div>
"""
    },
    {
        "id": "noirgrid",
        "name": "Noir Grid",
        "tagline": "Black, gold, red, and a grid you cannot escape.",
        "desc": "Noir Grid gives Korvia's speakeasies a cinematic Swiss layout: black background, gold rules, red signals, and hard shadows.",
        "palette": ["#0A0A0A", "#D4AF37", "#E42718"],
        "shapes": ["noir-grid", "gold-rule", "red-signal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 1px solid #333;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #888; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 0.1em; }
.noir-grid2 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: #333; border: 1px solid #333; margin-bottom: 24px; }
.noir-cell { background: #111; padding: 20px; text-align: center; border: 1px solid #222; }
.noir-cell.red { background: #e42718; color: #000; }
.noir-cell.gold { background: #d4af37; color: #000; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #d4af37; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; cursor: pointer;
}
.noir-rect2 { width: 100px; height: 80px; background: #000; border: 1px solid #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; box-shadow: 6px 6px 0 #333; }
.rule2 { width: 120px; height: 2px; background: #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.signal { width: 16px; height: 16px; background: #e42718; border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px; box-shadow: 0 0 10px #e42718; }
.showcase-footer { padding: 20px; background: #000; color: #555; border-top: 1px solid #333; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="noir-grid2">
<a href="#client" class="noir-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1rem;">Client</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Discover venues.</p></a>
<a href="#restaurant" class="noir-cell gold" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1rem;">Restaurant</h3><p style="margin:0;font-size:.75rem;line-height:1.4;">QR menus.</p></a>
<a href="#hotel" class="noir-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1rem;">Hotel</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Room service.</p></a>
<a href="#events" class="noir-cell" style="display:block;"><div style="font-size:1.6rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1rem;">Events</h3><p style="margin:0;font-size:.75rem;line-height:1.4;opacity:.9;">Parties.</p></a>
<a href="#" class="noir-cell red" style="display:block;"><h3 style="margin:0;font-size:1rem;">Scan QR</h3></a>
<a href="#" class="noir-cell" style="display:block;"><h3 style="margin:0;font-size:1rem;">Dashboard</h3></a>
</div>
<h2>Direction accent</h2>
<div class="noir-rect2"></div><div class="rule2"></div><div class="signal"></div>
</div>
"""
    },
    {
        "id": "swisslounge",
        "name": "Swiss Lounge",
        "tagline": "Leather club chairs arranged in a grid.",
        "desc": "Swiss Lounge gives Korvia's cigar bars a rigid grid layout in tobacco brown, gold, and red stitching.",
        "palette": ["#1F1A14", "#8B7D4B", "#E42718"],
        "shapes": ["leather-grid", "gold-stitch", "red-piping"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Merriweather:ital@0;1\u0026display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #1f1a14; color: #d8d0c0;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #15120d; border-bottom: 2px solid #e42718;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #8b7d4b; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Merriweather', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; font-style: italic; }
.desc { color: #a89f80; margin-bottom: 40px; }
.lounge-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2px; background: #5c4a3a; border: 2px solid #5c4a3a; margin-bottom: 24px; }
.lounge-cell { background: #2a231a; padding: 24px; border: 1px solid #8b7d4b; }
.lounge-cell.red { background: #e42718; color: #fff; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #8b7d4b; background: transparent;
    color: #8b7d4b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer;
}
.leather2 { width: 110px; height: 80px; background: repeating-linear-gradient(90deg, #3a2f22, #3a2f22 2px, #4a3d2e 2px, #4a3d2e 4px); border: 2px solid #5c4a3a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.leather2::after { content: ""; position: absolute; top: -4px; left: -4px; right: -4px; bottom: -4px; border: 1px solid #e42718; }
.stitch { width: 100px; height: 2px; background: repeating-linear-gradient(90deg, #8b7d4b, #8b7d4b 5px, transparent 5px, transparent 10px); display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #15120d; color: #6b6048; border-top: 2px solid #e42718; text-align: center; }
        """,
        "content": """
<style>
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="lounge-grid">
<a href="#client" class="lounge-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="lounge-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="lounge-cell red" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.85rem;line-height:1.4;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="lounge-cell" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.85rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="leather2"></div><div class="stitch"></div>
</div>
"""
    }
]
'''


def main():
    target = Path("showcase/generate_showcase.py")
    text = target.read_text(encoding="utf-8")
    marker = "    }\n]\n\nBASE = \"\"\""
    if marker not in text:
        print("Marker not found")
        return
    insert = NEW_ENTRIES.rstrip() + "\n"
    new_text = text.replace(marker, "    }\n" + insert + "]\n\nBASE = \"\"\"")
    target.write_text(new_text, encoding="utf-8")
    print(f"Appended {len(NEW_ENTRIES)} characters.")


if __name__ == "__main__":
    main()
