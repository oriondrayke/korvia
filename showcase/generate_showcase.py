#!/usr/bin/env python3
"""Generate a standalone showcase of non-AI UI directions."""
import os

DIRECTIONS = [
    {
        "id": "brutalist",
        "name": "Brutalist Raw",
        "tagline": "System fonts, thick borders, rectangles only, zero polish.",
        "desc": "Brutalist Raw makes Korvia's kitchen display impossible to ignore during a rush. Thick borders and screaming contrast turn ticket status into commands, not suggestions.",
        "palette": ["#000000", "#FFFFFF", "#FF0000"],
        "shapes": ["square", "rectangle", "rectangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Space Mono', monospace; background: #fff; color: #000;
    min-height: 100vh; display: flex; flex-direction: column; border: 12px solid #000;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; border-bottom: 4px solid #000; background: #ff0000; color: #fff;
    font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700;
}
.showcase-nav a { color: #fff; text-decoration: underline; }
.wrap { flex: 1; padding: 40px 24px; max-width: 960px; margin: 0 auto; width: 100%; }
h1 { font-size: clamp(3rem, 12vw, 7rem); line-height: 0.9; margin: 0 0 24px; text-transform: uppercase; }
h2 { font-size: 1rem; text-transform: uppercase; margin: 40px 0 16px; border-bottom: 2px solid #000; padding-bottom: 8px; }
.desc { font-size: 1.1rem; border: 3px solid #000; padding: 16px; margin-bottom: 40px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 80px; height: 80px; border: 3px solid #000; }
.swatch span { display: block; font-size: 0.65rem; padding: 4px; background: #fff; border-top: 2px solid #000; }
.shapes { display: flex; gap: 20px; align-items: flex-end; margin-bottom: 32px; }
.shape { border: 3px solid #000; background: #fff; }
.square { width: 60px; height: 60px; }
.rect { width: 120px; height: 60px; background: #ff0000; }
.big-btn {
    display: inline-block; padding: 18px 32px; border: 4px solid #000; background: #000; color: #fff;
    font-weight: 700; text-transform: uppercase; cursor: pointer; font-size: 1rem;
}
.big-btn.secondary { background: #fff; color: #000; }
.type-scale p { margin: 8px 0; border-bottom: 1px solid #ccc; padding-bottom: 8px; }
.stripes {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: repeating-linear-gradient(-45deg, #fff, #fff 20px, #ff0000 20px, #ff0000 40px);
    opacity: 0.08;
}
.showcase-footer { padding: 20px; border-top: 4px solid #000; text-align: center; font-size: 0.8rem; }
        """,
        "content": """
<div class="stripes"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="big-btn" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="shape rect" style="width:auto;height:auto;color:#fff;padding:22px;margin-bottom:12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="shape rect" style="width:auto;height:auto;color:#fff;padding:22px;margin-bottom:12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="shape rect" style="width:auto;height:auto;color:#fff;padding:22px;margin-bottom:12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="shape rect" style="width:auto;height:auto;color:#fff;padding:22px;margin-bottom:12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="big-btn" style="">Scan QR to order</a>
<a href="#" class="big-btn secondary" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="shapes"><div class="shape square"></div><div class="shape rect"></div></div>
</div>
"""
    },
    {
        "id": "swiss",
        "name": "Swiss Grid",
        "tagline": "Asymmetric grids, red accents, absolute order.",
        "desc": "Swiss Grid brings editorial order to the Korvia venue dashboard, separating revenue, open tables, and live orders into a scan-friendly hierarchy with one disciplined accent color.",
        "palette": ["#111111", "#F4F4F4", "#FF2500"],
        "shapes": ["square", "rectangle", "rectangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #f4f4f4; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 32px; background: #fff; border-bottom: 1px solid #ddd;
    font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #ff2500; text-decoration: none; }
.wrap { flex: 1; max-width: 1100px; margin: 0 auto; padding: 64px 32px; width: 100%; }
h1 { font-size: clamp(2.5rem, 6vw, 5rem); line-height: 0.95; margin: 0 0 16px; font-weight: 900; letter-spacing: -0.04em; }
.desc { color: #555; font-size: 1.1rem; max-width: 560px; margin-bottom: 48px; }
h2 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; margin: 40px 0 20px; font-weight: 700; }
.grid { display: grid; grid-template-columns: 2fr 1fr; gap: 1px; background: #111; border: 1px solid #111; margin-bottom: 48px; }
.cell { background: #fff; padding: 32px; }
.cell.red { background: #ff2500; color: #fff; }
.cell.black { background: #111; color: #fff; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 100px; height: 60px; }
.swatch span { display: block; font-size: 0.65rem; margin-top: 68px; }
.type-scale p { margin: 10px 0; padding-bottom: 10px; border-bottom: 1px solid #ddd; }
.squares {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background:
        linear-gradient(#ff2500, #ff2500) 8% 12% / 120px 120px no-repeat,
        linear-gradient(#111, #111) 90% 85% / 80px 80px no-repeat;
    opacity: 0.10;
}
.showcase-footer { padding: 24px 32px; background: #fff; border-top: 1px solid #ddd; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: #666; }
        """,
        "content": """
<div class="squares"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="cell" style="text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="cell" style="text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="cell" style="text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="cell" style="text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="shapes"><div class="shape" style="width:80px;height:80px;background:#ff2500;"></div><div class="shape" style="width:60px;height:60px;background:#111;"></div></div>
</div>
"""
    },
    {
        "id": "editorial",
        "name": "Editorial Magazine",
        "tagline": "Serif headlines, columns, pull quotes, footnotes.",
        "desc": "Editorial Magazine treats the Korvia menu like a feature story: generous whitespace, drop caps, and pull quotes turn each dish into a reason to order.",
        "palette": ["#2A2520", "#FAF8F3", "#8B0000"],
        "shapes": ["rectangle", "rectangle", "rectangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Source Sans 3', sans-serif; background: #faf8f3; color: #2a2520;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 40px; border-bottom: 1px solid #d4cfc5; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em;
}
.showcase-nav a { color: #8b0000; text-decoration: none; font-weight: 600; }
.wrap { flex: 1; max-width: 960px; margin: 0 auto; padding: 64px 40px; width: 100%; }
h1 { font-family: 'Playfair Display', serif; font-size: clamp(2.8rem, 7vw, 5.5rem); font-weight: 400; line-height: 1; margin: 0 0 16px; }
.deck { font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.4rem; color: #5c5449; margin: 0 0 48px; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; margin-bottom: 40px; }
.drop-cap::first-letter {
    font-family: 'Playfair Display', serif; float: left; font-size: 4.2rem; line-height: 0.8;
    padding-right: 10px; color: #8b0000;
}
.pull-quote {
    border-top: 3px solid #2a2520; border-bottom: 1px solid #d4cfc5;
    padding: 24px 0; margin: 32px 0; font-family: 'Playfair Display', serif; font-size: 1.5rem; font-style: italic;
}
.swatches { display: flex; gap: 16px; margin: 32px 0; }
.swatch { width: 90px; height: 90px; border: 1px solid #d4cfc5; }
.swatch span { display: block; font-size: 0.7rem; padding-top: 96px; }
h2 { font-family: 'Playfair Display', serif; font-size: 1.4rem; margin: 40px 0 16px; }
.lines {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: repeating-linear-gradient(to bottom, transparent, transparent 31px, #e8e3d9 32px);
    opacity: 0.5;
}
.showcase-footer { padding: 30px 40px; border-top: 1px solid #d4cfc5; text-align: center; font-size: 0.75rem; color: #8a8175; }
        """,
        "content": """
<div class="lines"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="pull-quote" style="text-align:center;padding:24px 12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="pull-quote" style="text-align:center;padding:24px 12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="pull-quote" style="text-align:center;padding:24px 12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="pull-quote" style="text-align:center;padding:24px 12px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="columns" style="margin-bottom:24px;"><div class="drop-cap" style="font-size:1rem;">Korvia home portal</div></div>
</div>
"""
    },
    {
        "id": "memphis",
        "name": "Memphis Pop",
        "tagline": "Squiggles, circles, triangles, pastel chaos.",
        "desc": "Memphis Pop turns a Korvia order card into a playful, high-energy ticket that floor staff can read at a glance during peak service.",
        "palette": ["#F6D7FF", "#FFF6A3", "#A3FFF0", "#FFC4A3"],
        "shapes": ["circle", "triangle", "squiggle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Syne', sans-serif; background: #f6d7ff; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 16px 24px; background: #fff; border-bottom: 4px solid #111;
}
.showcase-nav a { color: #111; font-weight: 800; text-decoration: underline; text-decoration-style: wavy; }
.wrap { flex: 1; padding: 48px 24px; max-width: 1000px; margin: 0 auto; width: 100%; }
h1 { font-size: clamp(2.5rem, 8vw, 5rem); margin: 0 0 24px; font-weight: 800; }
.desc { font-size: 1.1rem; background: #fff; border: 3px solid #111; padding: 16px; margin-bottom: 40px; transform: rotate(-1deg); }
.swatches { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 40px; }
.swatch { width: 80px; height: 80px; border: 3px solid #111; }
.swatch span { display: block; font-size: 0.65rem; background: #fff; border-top: 3px solid #111; padding: 2px; margin-top: 80px; }
.shapes { display: flex; flex-wrap: wrap; gap: 28px; align-items: center; margin-bottom: 40px; }
.shape { border: 3px solid #111; }
.circle { width: 70px; height: 70px; border-radius: 50%; background: #ff3d00; }
.triangle { width: 70px; height: 70px; background: #00e676; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); }
.squiggle { width: 90px; height: 40px; border: none; background: repeating-linear-gradient(45deg, #7c4dff, #7c4dff 8px, transparent 8px, transparent 16px); transform: rotate(-5deg); }
.card {
    background: #fff; border: 3px solid #111; padding: 24px; width: 220px; display: inline-block;
    transform: rotate(2deg); margin-right: 16px; margin-bottom: 16px;
}
.squiggle-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background:
        radial-gradient(circle at 10% 20%, #ff3d00 20px, transparent 21px),
        radial-gradient(circle at 90% 80%, #7c4dff 30px, transparent 31px),
        radial-gradient(circle at 50% 50%, #00e676 40px, transparent 41px);
    opacity: 0.25;
}
.showcase-footer { padding: 20px; border-top: 4px solid #111; text-align: center; background: #fff; }
        """,
        "content": """
<div class="squiggle-bg"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="card" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="card" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="card" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="card" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="circle"></div><div class="triangle"></div><div class="squiggle"></div>
</div>
"""
    },
    {
        "id": "bauhaus",
        "name": "Bauhaus Function",
        "tagline": "Circles, squares, triangles, primary colors.",
        "desc": "Bauhaus Function maps Korvia's core hospitality jobs to primary forms: red for urgent orders, yellow for menus, and blue for QR status.",
        "palette": ["#E63946", "#FFCC00", "#1D3557"],
        "shapes": ["circle", "square", "triangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Jost:wght@400;600;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Jost', sans-serif; background: #e8e6e1; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 28px; background: #111; color: #fff; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em;
}
.showcase-nav a { color: #ffcc00; text-decoration: none; font-weight: 700; }
.wrap { flex: 1; max-width: 960px; margin: 0 auto; padding: 56px 28px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 8px; font-weight: 700; text-transform: lowercase; }
.desc { font-size: 1.1rem; color: #444; margin-bottom: 40px; }
.stage { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 40px; }
.module {
    aspect-ratio: 1; display: flex; flex-direction: column; justify-content: space-between;
    padding: 24px; border: 2px solid #111;
}
.module.red { background: #e63946; color: #fff; }
.module.yellow { background: #ffcc00; }
.module.blue { background: #1d3557; color: #fff; }
.module.white { background: #fff; }
.module h2 { margin: 0; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em; }
.module .big { font-size: 2.6rem; font-weight: 700; line-height: 1; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 80px; height: 80px; border: 2px solid #111; }
.swatch span { display: block; font-size: 0.65rem; margin-top: 86px; }
.shapes { display: flex; gap: 24px; align-items: center; margin-bottom: 32px; }
.shape { border: 2px solid #111; }
.sq { width: 60px; height: 60px; background: #e63946; }
.ci { width: 60px; height: 60px; border-radius: 50%; background: #ffcc00; }
.tr { width: 60px; height: 60px; background: #1d3557; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); }
.geo {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background:
        radial-gradient(circle, #e63946 40px, transparent 41px) 5% 10%,
        linear-gradient(45deg, transparent 48%, #1d3557 49%, #1d3557 51%, transparent 52%) 90% 90% / 120px 120px no-repeat;
    opacity: 0.12;
}
.showcase-footer { padding: 20px 28px; background: #111; color: #999; text-align: center; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; }
        """,
        "content": """
<div class="geo"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="module" style="aspect-ratio:auto;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="module" style="aspect-ratio:auto;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="module" style="aspect-ratio:auto;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="module" style="aspect-ratio:auto;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="sq"></div><div class="ci"></div><div class="tr"></div>
</div>
"""
    },
    {
        "id": "handdrawn",
        "name": "Hand-Drawn Sketch",
        "tagline": "Rough edges, paper texture, pencil marks.",
        "desc": "Hand-Drawn Sketch makes Korvia feel like the head chef's personal tickets: quick, human, and easy to annotate during a busy prep window.",
        "palette": ["#F7F2E6", "#3A3026", "#B45F06"],
        "shapes": ["circle", "blob", "rectangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&family=Patrick+Hand&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Kalam', cursive; background: #f7f2e6; color: #3a3026;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 16px 24px; border-bottom: 2px dashed #a89f91; font-size: 1.1rem;
}
.showcase-nav a { color: #b45f06; text-decoration: underline wavy; }
.wrap { flex: 1; max-width: 780px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Patrick Hand', cursive; font-size: clamp(2.5rem, 8vw, 5rem); margin: 0 0 16px; transform: rotate(-1deg); }
.desc { font-size: 1.15rem; color: #6b5e4f; margin-bottom: 40px; }
.napkin {
    background: #fffef8; border: 2px solid #3a3026; border-radius: 2px 24px 3px 18px;
    padding: 32px; box-shadow: 4px 4px 0 #d4c5a9; transform: rotate(0.5deg); margin-bottom: 32px; position: relative;
}
.tape {
    position: absolute; top: -12px; left: 30px; width: 90px; height: 24px;
    background: rgba(255, 235, 59, 0.6); transform: rotate(-3deg);
}
.row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px dashed #a89f91; font-size: 1.2rem; }
.row:last-child { border-bottom: none; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 80px; height: 80px; border: 2px solid #3a3026; border-radius: 40% 60% 30% 70% / 60% 40% 70% 30%; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 90px; }
.sketch-btn {
    display: inline-block; padding: 12px 24px; border: 2px solid #3a3026; border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
    background: #fffef8; color: #3a3026; font-family: 'Kalam', cursive; font-size: 1.1rem; cursor: pointer; margin-right: 12px;
}
.paper {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background-image: radial-gradient(#d4c5a9 1px, transparent 1px); background-size: 22px 22px; opacity: 0.25;
}
.showcase-footer { padding: 20px; border-top: 2px dashed #a89f91; text-align: center; color: #a89f91; }
        """,
        "content": """
<div class="paper"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="sketch-btn" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="napkin" style="text-align:center;display:block;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="napkin" style="text-align:center;display:block;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="napkin" style="text-align:center;display:block;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="napkin" style="text-align:center;display:block;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="sketch-btn" style="">Scan QR to order</a>
<a href="#" class="sketch-btn" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="napkin" style="display:inline-block;position:relative;padding:20px;margin-right:12px;"><div class="tape"></div>Sketch note</div>
</div>
"""
    },
    {
        "id": "artdeco",
        "name": "Art Deco Luxe",
        "tagline": "Gold, black, stepped geometry, fan patterns.",
        "desc": "Art Deco Luxe frames Korvia's fine-dining venues with gilded panels and diamond motifs, turning a reservation screen into part of the guest experience.",
        "palette": ["#050505", "#C5A059", "#F5E7C8"],
        "shapes": ["fan", "stepped-rectangle", "diamond"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Marcellus&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Marcellus', serif; background: #050505; color: #f5e7c8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 22px 36px; background: #0a0a0a; border-bottom: 1px solid #c5a059;
    font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.2em;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 56px 36px; width: 100%; text-align: center; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; letter-spacing: 0.12em; }
.desc { color: #b0a27d; font-size: 1.05rem; max-width: 560px; margin: 0 auto 48px; }
.fan {
    width: 160px; height: 80px; margin: 0 auto 40px;
    background: repeating-conic-gradient(from 0deg at 50% 100%, #c5a059 0deg 10deg, transparent 10deg 20deg);
    opacity: 0.6;
}
.panel {
    border: 1px solid #c5a059; padding: 32px; margin-bottom: 24px; background: #0f0f0f; position: relative;
}
.panel::before, .panel::after { content: "◆"; color: #c5a059; position: absolute; top: 12px; font-size: 0.8rem; }
.panel::before { left: 16px; } .panel::after { right: 16px; }
.swatches { display: flex; gap: 16px; justify-content: center; margin-bottom: 40px; }
.swatch { width: 80px; height: 80px; border: 1px solid #c5a059; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 90px; color: #b0a27d; }
.shapes { display: flex; gap: 32px; justify-content: center; margin-bottom: 40px; }
.diamond { width: 60px; height: 60px; background: #c5a059; transform: rotate(45deg); }
.step { width: 80px; height: 80px; background: #c5a059; clip-path: polygon(0 0, 100% 0, 100% 40%, 60% 40%, 60% 100%, 0 100%); }
.gold-btn {
    display: inline-block; padding: 14px 36px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.2em; font-size: 0.8rem; cursor: pointer;
}
.gold-btn:hover { background: #c5a059; color: #050505; }
.showcase-footer { padding: 24px; border-top: 1px solid #c5a059; color: #8a7e63; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="gold-btn" style="">Scan QR to order</a>
<a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="shapes"><div class="diamond"></div><div class="step"></div><div class="fan"></div></div>
</div>
"""
    },
    {
        "id": "scrapbook",
        "name": "Scrapbook Collage",
        "tagline": "Washi tape, polaroids, layered paper, soft dopamine.",
        "desc": "Scrapbook Collage lets Korvia venues paste together photos, polaroids, and washi-tape notes for a personality-rich events board.",
        "palette": ["#E6F0E8", "#E07050", "#FFB74D"],
        "shapes": ["polaroid", "tape-strip", "circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Gochi+Hand&family=Nunito:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Nunito', sans-serif; background: #e6f0e8; color: #2f3e35;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 16px 24px; background: #fff; box-shadow: 0 2px 0 rgba(0,0,0,0.05);
}
.showcase-nav a { color: #e07050; font-weight: 700; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Gochi Hand', cursive; font-size: clamp(2.4rem, 7vw, 4.5rem); margin: 0 0 16px; transform: rotate(-1deg); color: #e07050; }
.desc { color: #5a6b60; margin-bottom: 40px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 80px; height: 80px; border: 2px dashed #fff; box-shadow: 2px 2px 0 rgba(0,0,0,0.08); }
.swatch span { display: block; font-size: 0.65rem; padding-top: 90px; }
.collage { display: flex; flex-wrap: wrap; gap: 28px; justify-content: center; margin-bottom: 40px; }
.polaroid {
    background: #fff; padding: 12px 12px 40px; width: 220px; box-shadow: 3px 4px 10px rgba(0,0,0,0.12);
    transform: rotate(var(--r, -2deg)); position: relative;
}
.polaroid:nth-child(2) { --r: 3deg; }
.polaroid:nth-child(3) { --r: -1deg; }
.polaroid .img {
    width: 100%; height: 160px; background: #c8ddd0; display: grid; place-items: center; font-size: 3rem;
}
.polaroid p { margin: 12px 0 0; font-family: 'Gochi Hand', cursive; font-size: 1.2rem; text-align: center; }
.washi {
    position: absolute; top: -10px; left: 50%; transform: translateX(-50%) rotate(-2deg);
    width: 80px; height: 22px; background: rgba(255, 183, 77, 0.75);
}
.cork {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background:
        radial-gradient(circle at 20% 30%, rgba(224,112,80,0.15) 80px, transparent 81px),
        radial-gradient(circle at 80% 70%, rgba(255,193,7,0.15) 100px, transparent 101px);
}
.showcase-footer { padding: 20px; text-align: center; color: #7a8a7e; }
        """,
        "content": """
<div class="cork"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="polaroid" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="polaroid" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="polaroid" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="polaroid" style="width:auto;display:block;text-align:center;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="collage"><div class="polaroid" style="display:inline-block;"><div class="img">📷</div><p>Korvia</p></div></div>
</div>
"""
    },
    {
        "id": "japanese",
        "name": "Japanese Minimal",
        "tagline": "Space, ink, red seals, vertical rhythm.",
        "desc": "Japanese Minimal gives Korvia the calm of a ryokan check-in: one seal, one vertical accent, and absolute clarity between occupied and empty space.",
        "palette": ["#F7F5F0", "#2B2B2B", "#B02A2A"],
        "shapes": ["circle", "vertical-line", "rectangle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300;600;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Noto Serif JP', serif; background: #f7f5f0; color: #2b2b2b;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 28px 48px; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase;
}
.showcase-nav a { color: #b02a2a; text-decoration: none; }
.wrap { flex: 1; max-width: 840px; margin: 0 auto; padding: 80px 48px; width: 100%; }
h1 { font-size: clamp(2.6rem, 6vw, 4.5rem); font-weight: 300; margin: 0 0 24px; letter-spacing: 0.15em; }
.desc { color: #6b6b6b; font-size: 1.05rem; margin-bottom: 48px; max-width: 520px; }
.vertical {
    writing-mode: vertical-rl; text-orientation: upright; font-size: 0.9rem; letter-spacing: 0.3em;
    color: #8c8c8c; height: 200px; float: right; margin-left: 48px;
}
.seal {
    width: 72px; height: 72px; background: #b02a2a; color: #fff;
    display: grid; place-items: center; font-size: 0.9rem; border-radius: 4px; margin: 40px 0;
}
.swatches { display: flex; gap: 16px; margin-bottom: 40px; }
.swatch { width: 80px; height: 80px; border: 1px solid #d9d5cc; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 90px; color: #6b6b6b; }
.type-line { padding: 18px 0; border-bottom: 1px solid #d9d5cc; font-weight: 300; }
.ink {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: radial-gradient(circle at 90% 10%, rgba(176,42,42,0.08) 0%, transparent 40%);
}
.showcase-footer { padding: 32px 48px; border-top: 1px solid #d9d5cc; text-align: center; color: #8c8c8c; font-size: 0.75rem; letter-spacing: 0.15em; }
        """,
        "content": """
<div class="ink"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="type-line" style="display:block;text-align:center;padding:20px 0;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="type-line" style="display:block;text-align:center;padding:20px 0;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="type-line" style="display:block;text-align:center;padding:20px 0;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="type-line" style="display:block;text-align:center;padding:20px 0;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="seal">門</div><div class="vertical">Korvia</div>
</div>
"""
    },
    {
        "id": "terminal",
        "name": "Retro Terminal",
        "tagline": "Monospace green, scanlines, CRT glow.",
        "desc": "Retro Terminal turns Korvia into a heads-down command center for back-of-house: logs, prompts, and a blinking cursor keep cooks in flow.",
        "palette": ["#050A05", "#33FF00", "#0F3D0F"],
        "shapes": ["rectangle", "cursor", "grid"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'VT323', monospace; background: #050a05; color: #33ff00;
    min-height: 100vh; display: flex; flex-direction: column; text-shadow: 0 0 5px #33ff0055;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 12px 24px; background: #0a140a; border-bottom: 1px solid #33ff0033;
    font-size: 1.1rem;
}
.showcase-nav a { color: #33ff00; text-decoration: none; }
.wrap { flex: 1; max-width: 800px; margin: 0 auto; padding: 32px 24px; width: 100%; }
h1 { font-size: clamp(2rem, 6vw, 3.5rem); margin: 0 0 16px; font-weight: 400; }
.desc { color: #33ff00aa; font-size: 1.1rem; margin-bottom: 32px; }
.log {
    border: 1px solid #33ff0066; background: #081008; padding: 20px; font-size: 1.2rem; line-height: 1.6; margin-bottom: 32px;
}
.log p { margin: 0 0 6px; }
.prompt { color: #33ff00; }
.cursor { animation: blink 1s step-end infinite; }
@keyframes blink { 50% { opacity: 0; } }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 80px; height: 80px; border: 1px solid #33ff0066; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 90px; color: #33ff0099; }
.shapes { display: flex; gap: 16px; margin-bottom: 32px; }
.bar { width: 60px; height: 30px; border: 1px solid #33ff00; }
.grid2 { width: 60px; height: 60px; background: repeating-linear-gradient(to right, #33ff00 0 2px, transparent 2px 12px); opacity: 0.3; }
.scanlines {
    position: fixed; inset: 0; pointer-events: none; z-index: 9999;
    background: repeating-linear-gradient(to bottom, transparent 0px, transparent 2px, rgba(0,0,0,0.25) 3px);
}
.showcase-footer { padding: 14px 24px; border-top: 1px solid #33ff0033; background: #0a140a; color: #33ff0099; text-align: center; }
        """,
        "content": """
<div class="scanlines"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="log" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="log" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="log" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="log" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="bar"></div><div class="grid2"></div><span class="cursor">_</span>
</div>
"""
    },
    {
        "id": "organic",
        "name": "Organic Blob",
        "tagline": "Fluid shapes, earth tones, no sharp edges.",
        "desc": "Organic Blob softens Korvia's guest touchpoints with fluid shapes that feel welcoming, like a reservation card made of warm earth.",
        "palette": ["#E6DDD4", "#7A6A5A", "#C4A77D"],
        "shapes": ["blob", "oval", "wave"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Quicksand', sans-serif; background: #e6ddd4; color: #4a4239;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 28px; background: #f3ece4; border-bottom: 1px solid #d1c4b6;
}
.showcase-nav a { color: #7a6a5a; font-weight: 700; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 56px 28px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 700; }
.desc { color: #7a6a5a; font-size: 1.1rem; margin-bottom: 40px; }
.blob {
    background: #c4a77d; border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    padding: 48px; margin-bottom: 32px; color: #fff; font-size: 1.2rem;
}
.oval {
    width: 160px; height: 90px; background: #7a6a5a; border-radius: 50%; display: inline-flex;
    align-items: center; justify-content: center; color: #fff; margin-right: 16px; margin-bottom: 16px;
}
.wave { height: 60px; background: repeating-linear-gradient(45deg, #c4a77d, #c4a77d 10px, transparent 10px, transparent 20px); border-radius: 30px; margin-bottom: 32px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 50%; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #7a6a5a; }
.organic {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: radial-gradient(circle at 20% 30%, rgba(196,167,125,0.2) 120px, transparent 121px);
}
.showcase-footer { padding: 24px 28px; background: #f3ece4; border-top: 1px solid #d1c4b6; text-align: center; color: #7a6a5a; }
        """,
        "content": """
<div class="organic"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="blob" style="display:block;text-align:center;border-radius:30px;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="blob" style="display:block;text-align:center;border-radius:30px;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="blob" style="display:block;text-align:center;border-radius:30px;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="blob" style="display:block;text-align:center;border-radius:30px;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="oval">Korvia</div><div class="wave"></div>
</div>
"""
    },
    {
        "id": "neobrutal",
        "name": "Neobrutalism",
        "tagline": "Bright colors, hard shadows, rounded but bold.",
        "desc": "Neobrutalism gives Korvia chunky cards and loud shadows so hosts and managers never miss the next actionable order.",
        "palette": ["#FF6B6B", "#4ECDC4", "#FFE66D"],
        "shapes": ["rounded-rect", "star", "circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'DM Sans', sans-serif; background: #f7f7f7; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #ff6b6b; color: #111; border-bottom: 4px solid #111;
    font-weight: 700;
}
.showcase-nav a { color: #111; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 700; }
.desc { font-size: 1.1rem; margin-bottom: 40px; }
.card2 {
    background: #fff; border: 3px solid #111; border-radius: 16px;
    padding: 28px; margin-bottom: 24px; box-shadow: 8px 8px 0 #111;
}
.card2.coral { background: #ff6b6b; }
.card2.mint { background: #4ecdc4; }
.card2.lemon { background: #ffe66d; }
.neo-btn {
    display: inline-block; padding: 14px 28px; border: 3px solid #111; border-radius: 12px;
    background: #fff; color: #111; font-weight: 700; box-shadow: 5px 5px 0 #111; margin-right: 12px; cursor: pointer;
}
.star { width: 70px; height: 70px; background: #ffe66d; clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); margin-bottom: 24px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 3px solid #111; border-radius: 12px; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; border-top: 4px solid #111; background: #ff6b6b; text-align: center; font-weight: 700; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="neo-btn" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="card2" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="card2" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="card2" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="card2" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="neo-btn" style="">Scan QR to order</a>
<a href="#" class="neo-btn" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="star"></div>
</div>
"""
    },
    {
        "id": "clay",
        "name": "Claymorphism",
        "tagline": "Soft 3D pastels, puffy shapes, inner shadows.",
        "desc": "Claymorphism makes Korvia buttons and cards feel squeezable — ideal for tablet-based hosts tapping through reservations with gloved hands.",
        "palette": ["#FFE5EC", "#C1E1C1", "#B5DEFF"],
        "shapes": ["puffy-circle", "soft-rect", "sphere"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Nunito', sans-serif; background: #f0f4f8; color: #4a5568;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #e2e8f0;
}
.showcase-nav a { color: #4a5568; font-weight: 700; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 700; }
.desc { font-size: 1.1rem; margin-bottom: 40px; }
.clay-card {
    background: #ffe5ec; border-radius: 32px; padding: 32px; margin-bottom: 28px;
    box-shadow: inset 8px 8px 16px rgba(255,255,255,0.7), inset -8px -8px 16px rgba(0,0,0,0.05), 12px 12px 24px rgba(0,0,0,0.08);
}
.clay-card.green { background: #c1e1c1; }
.clay-card.blue { background: #b5deff; }
.puffy {
    width: 100px; height: 100px; border-radius: 50%; background: #ffe5ec; display: inline-flex;
    align-items: center; justify-content: center; margin-right: 20px; margin-bottom: 20px;
    box-shadow: inset 6px 6px 12px rgba(255,255,255,0.8), inset -6px -6px 12px rgba(0,0,0,0.06), 8px 8px 16px rgba(0,0,0,0.08);
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 24px; box-shadow: inset 4px 4px 8px rgba(255,255,255,0.6), inset -4px -4px 8px rgba(0,0,0,0.05); }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #e2e8f0; text-align: center; color: #718096; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="puffy" style="width:auto;height:auto;padding:12px 28px;border-radius:999px;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="clay-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="clay-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="clay-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="clay-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="puffy" style="width:auto;height:auto;padding:12px 28px;border-radius:999px;">Scan QR to order</a>
<a href="#" class="puffy" style="margin-left:12px;width:auto;height:auto;padding:12px 28px;border-radius:999px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="puffy">K</div><div class="puffy" style="background:#c1e1c1;">V</div>
</div>
"""
    },
    {
        "id": "cyberpunk",
        "name": "Cyberpunk Neon",
        "tagline": "Dark city, neon edges, sharp angles.",
        "desc": "Cyberpunk Neon turns Korvia's late-night bar mode into a glowing command deck where orders pulse and QR scans cut through the dark.",
        "palette": ["#0A0A12", "#FF00FF", "#00FFFF"],
        "shapes": ["triangle", "hexagon", "grid"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Orbitron', sans-serif; background: #0a0a12; color: #00ffff;
    min-height: 100vh; display: flex; flex-direction: column; text-shadow: 0 0 8px #00ffff66;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #12121f; border-bottom: 1px solid #ff00ff;
}
.showcase-nav a { color: #ff00ff; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2rem, 6vw, 3.6rem); margin: 0 0 16px; font-weight: 700; letter-spacing: 0.08em; }
.desc { color: #00ffffaa; margin-bottom: 40px; }
.neon-box {
    border: 1px solid #00ffff; padding: 24px; margin-bottom: 24px; background: #12121f;
    box-shadow: 0 0 12px #00ffff33; position: relative;
}
.neon-box::before {
    content: ""; position: absolute; top: -1px; right: -1px; width: 20px; height: 20px;
    border-top: 2px solid #ff00ff; border-right: 2px solid #ff00ff;
}
.tri { width: 80px; height: 80px; background: #ff00ff; clip-path: polygon(50% 0%, 0% 100%, 100% 100%); margin-bottom: 24px; filter: drop-shadow(0 0 8px #ff00ff); }
.hex { width: 80px; height: 80px; background: #00ffff; clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); display: inline-block; margin-right: 16px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 1px solid #00ffff; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #00ffffaa; }
.grid-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: linear-gradient(to bottom, transparent 95%, #00ffff11 95%), linear-gradient(to right, transparent 95%, #00ffff11 95%); background-size: 40px 40px;
}
.showcase-footer { padding: 20px; background: #12121f; border-top: 1px solid #ff00ff; text-align: center; color: #ff00ff; }
        """,
        "content": """
<div class="grid-bg"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="neon-box" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="neon-box" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="neon-box" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="neon-box" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="tri"></div><div class="hex"></div>
</div>
"""
    },
    {
        "id": "steampunk",
        "name": "Steampunk Brass",
        "tagline": "Gears, gauges, copper, and rivets.",
        "desc": "Steampunk Brass wraps Korvia's heritage hotel dashboard in riveted plates and gauges, making occupancy and service diagnostics feel tangible.",
        "palette": ["#3E2723", "#B87333", "#E6D5B8"],
        "shapes": ["gear", "rivet", "gauge"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Rye&family=Roboto+Slab:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Roboto Slab', serif; background: #3e2723; color: #e6d5b8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #281815; border-bottom: 4px solid #b87333;
    font-family: 'Rye', cursive;
}
.showcase-nav a { color: #b87333; text-decoration: none; }
.wrap { flex: 1; max-width: 880px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Rye', cursive; font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; }
.desc { color: #c2b096; margin-bottom: 40px; }
.plate {
    background: repeating-linear-gradient(45deg, #b87333, #b87333 2px, #9c5f28 2px, #9c5f28 4px);
    border: 4px solid #5d4037; border-radius: 8px; padding: 28px; margin-bottom: 24px;
    color: #281815; box-shadow: inset 0 0 20px rgba(0,0,0,0.3);
}
.gear {
    width: 80px; height: 80px; background: #b87333; border-radius: 50%;
    background-image: radial-gradient(circle at center, #3e2723 20px, transparent 21px),
        repeating-conic-gradient(from 0deg, #b87333 0deg 15deg, #8d5524 15deg 30deg);
    margin-bottom: 24px;
}
.rivet { width: 14px; height: 14px; background: radial-gradient(circle at 30% 30%, #e6d5b8, #5d4037); border-radius: 50%; display: inline-block; margin: 4px; }
.gauge { width: 120px; height: 60px; background: #e6d5b8; border-radius: 120px 120px 0 0; border: 4px solid #b87333; position: relative; margin-bottom: 24px; }
.gauge::after { content: ""; position: absolute; bottom: 0; left: 50%; width: 4px; height: 50px; background: #b87333; transform: rotate(45deg); transform-origin: bottom left; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #b87333; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #c2b096; }
.showcase-footer { padding: 20px; background: #281815; border-top: 4px solid #b87333; text-align: center; color: #b87333; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="plate" style="text-align:center;display:block;color:#281815;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="plate" style="text-align:center;display:block;color:#281815;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="plate" style="text-align:center;display:block;color:#281815;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="plate" style="text-align:center;display:block;color:#281815;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="gear"></div><div class="gauge"></div><div class="rivet"></div><div class="rivet"></div>
</div>
"""
    },
    {
        "id": "cottagecore",
        "name": "Cottagecore Floral",
        "tagline": "Soft florals, rounded script, gentle dopamine.",
        "desc": "Cottagecore Floral gives Korvia's farm-to-table venues a pressed-flower warmth that matches menus built on local ingredients.",
        "palette": ["#FAF6F0", "#E8B4B8", "#A8C686"],
        "shapes": ["flower", "rounded-rect", "leaf"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=Dancing+Script:wght@600&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Playfair Display', serif; background: #faf6f0; color: #5d4e4e;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #f5ebe0;
}
.showcase-nav a { color: #a8c686; font-weight: 700; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-style: italic; }
.desc { color: #8a7878; margin-bottom: 40px; }
.floral-card {
    background: #fff; border-radius: 24px; padding: 28px; margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(93,78,78,0.08); border: 1px solid #e8d5d5;
}
.flower {
    width: 70px; height: 70px; background: #e8b4b8; border-radius: 50%;
    position: relative; margin-bottom: 24px;
}
.flower::before, .flower::after {
    content: ""; position: absolute; width: 70px; height: 70px; background: #e8b4b8; border-radius: 50%;
}
.flower::before { left: -30px; } .flower::after { right: -30px; }
.leaf { width: 50px; height: 80px; background: #a8c686; border-radius: 0 80% 0 80%; display: inline-block; margin-right: 16px; transform: rotate(-20deg); }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 50%; border: 2px solid #e8d5d5; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #8a7878; }
.floral-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: radial-gradient(circle at 10% 20%, rgba(232,180,184,0.2) 60px, transparent 61px),
        radial-gradient(circle at 90% 80%, rgba(168,198,134,0.2) 80px, transparent 81px);
}
.showcase-footer { padding: 20px; background: #f5ebe0; text-align: center; color: #8a7878; }
        """,
        "content": """
<div class="floral-bg"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="floral-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="floral-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="floral-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="floral-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="flower"></div><div class="leaf"></div>
</div>
"""
    },
    {
        "id": "acid",
        "name": "Acid Rave",
        "tagline": "Neon green, chrome, warped geometry.",
        "desc": "Acid Rave keeps Korvia's festival and event pop-ups readable under strobe conditions with high-voltage boxes and dripping urgency.",
        "palette": ["#1A1A1A", "#CCFF00", "#9D00FF"],
        "shapes": ["wave", "drip", "chrome-circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Rubik+Mono+One&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Rubik Mono One', sans-serif; background: #1a1a1a; color: #ccff00;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 2px solid #ccff00;
}
.showcase-nav a { color: #9d00ff; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2rem, 6vw, 3.6rem); margin: 0 0 16px; -webkit-text-stroke: 1px #ccff00; color: transparent; }
.desc { color: #ccff00aa; font-family: sans-serif; margin-bottom: 40px; }
.acid-box {
    border: 2px solid #ccff00; padding: 24px; margin-bottom: 24px;
    background: repeating-linear-gradient(90deg, #000, #000 10px, #ccff00 10px, #ccff00 12px);
    color: #fff;
}
.drip {
    width: 120px; height: 80px; background: #ccff00; border-radius: 20px 20px 40px 60px;
    margin-bottom: 24px;
}
.warp {
    width: 100px; height: 100px; background: #9d00ff; border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    display: inline-block; margin-right: 16px; animation: morph 4s ease-in-out infinite;
}
@keyframes morph { 0%,100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; } 50% { border-radius: 60% 40% 30% 70% / 50% 60% 40% 50%; } }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #ccff00; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #ccff00aa; }
.showcase-footer { padding: 20px; background: #000; border-top: 2px solid #ccff00; text-align: center; color: #9d00ff; }
        """,
        "content": """
<div class="warp"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="acid-box" style="text-align:center;display:block;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="acid-box" style="text-align:center;display:block;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="acid-box" style="text-align:center;display:block;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="acid-box" style="text-align:center;display:block;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="drip"></div><div class="warp"></div>
</div>
"""
    },
    {
        "id": "deconstruct",
        "name": "Deconstructivism",
        "tagline": "Broken grid, diagonal slices, overlapping planes.",
        "desc": "Deconstructivism breaks the Korvia dashboard into overlapping shards so managers can compare kitchen load, floor plan, and QR traffic at once.",
        "palette": ["#F5F5F5", "#111111", "#FF4D4D"],
        "shapes": ["diagonal", "overlap", "shard"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Archivo Black', sans-serif; background: #f5f5f5; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #111; color: #f5f5f5;
}
.showcase-nav a { color: #ff4d4d; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; transform: skewX(-8deg); }
.desc { font-family: sans-serif; color: #444; margin-bottom: 48px; max-width: 560px; }
.shard {
    width: 160px; height: 160px; background: #ff4d4d; clip-path: polygon(0 0, 100% 20%, 80% 100%, 20% 80%);
    display: inline-block; margin-right: -40px; margin-bottom: 24px;
}
.shard.blue { background: #111; clip-path: polygon(20% 0, 100% 0, 80% 100%, 0 80%); }
.slice {
    background: #111; color: #fff; padding: 24px; margin-bottom: 24px; transform: skewX(-12deg);
}
.slice:nth-child(even) { background: #ff4d4d; transform: skewX(12deg); color: #111; }
.overlap {
    position: relative; height: 180px; margin-bottom: 32px;
}
.overlap .box {
    position: absolute; width: 200px; height: 120px; border: 3px solid #111; background: #fff;
}
.overlap .box:nth-child(1) { top: 0; left: 0; transform: rotate(-5deg); }
.overlap .box:nth-child(2) { top: 30px; left: 80px; background: #ff4d4d; transform: rotate(4deg); z-index: 1; }
.overlap .box:nth-child(3) { top: 60px; left: 160px; transform: rotate(-3deg); }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #111; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #111; color: #888; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="slice" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="slice" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="slice" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="slice" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="shard"></div><div class="shard blue"></div><div class="overlap"><div class="box"></div><div class="box"></div><div class="box"></div></div>
</div>
"""
    },
    {
        "id": "biophilic",
        "name": "Biophilic Nature",
        "tagline": "Leaf forms, earth tones, living lines.",
        "desc": "Biophilic Nature weaves Korvia's eco-lodge and farm venues into leaf, branch, and stone textures that echo their sustainability story.",
        "palette": ["#F4F1EA", "#4A5D23", "#D4A373"],
        "shapes": ["leaf", "branch", "pebble"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;600&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Work Sans', sans-serif; background: #f4f1ea; color: #3a4422;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #e8e4da;
}
.showcase-nav a { color: #4a5d23; font-weight: 600; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 600; }
.desc { color: #5e6b3a; margin-bottom: 40px; }
.leaf {
    width: 80px; height: 140px; background: #4a5d23; border-radius: 0 80% 0 80%; display: inline-block;
    margin-right: 20px; margin-bottom: 24px; transform: rotate(-10deg);
}
.leaf.two { background: #d4a373; transform: rotate(10deg); border-radius: 80% 0 80% 0; }
.pebble {
    width: 100px; height: 60px; background: #8c8c74; border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.branch { height: 4px; background: #4a5d23; border-radius: 2px; margin-bottom: 16px; }
.nature-card {
    background: #fff; border-radius: 24px 4px 24px 4px; padding: 28px; margin-bottom: 24px;
    border: 1px solid #d4c8b0;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 50%; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #5e6b3a; }
.nature-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background: radial-gradient(circle at 80% 20%, rgba(74,93,35,0.08) 120px, transparent 121px);
}
.showcase-footer { padding: 20px; background: #e8e4da; text-align: center; color: #5e6b3a; }
        """,
        "content": """
<div class="nature-bg"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="nature-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="nature-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="nature-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="nature-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="branch"></div><div class="leaf"></div><div class="pebble"></div>
</div>
"""
    },
    {
        "id": "constructivist",
        "name": "Constructivism",
        "tagline": "Red, black, diagonals, propaganda posters.",
        "desc": "Constructivism delivers Korvia's service updates like rally posters: skewed banners and bold wedges broadcast priorities across a noisy kitchen.",
        "palette": ["#D62828", "#111111", "#F4F1DE"],
        "shapes": ["diagonal-banner", "photomontage", "wedge"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Oswald', sans-serif; background: #f4f1de; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #111; color: #f4f1de; text-transform: uppercase;
}
.showcase-nav a { color: #d62828; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; text-transform: uppercase; font-weight: 700; }
.desc { font-family: sans-serif; margin-bottom: 40px; }
.banner {
    background: #d62828; color: #fff; padding: 18px 24px; margin-bottom: 24px;
    transform: skewX(-15deg); text-transform: uppercase; font-weight: 700; font-size: 1.2rem;
}
.wedge {
    width: 120px; height: 120px; background: #111; clip-path: polygon(0 0, 100% 0, 0 100%); display: inline-block; margin-right: -30px; margin-bottom: 24px;
}
.wedge.red { background: #d62828; clip-path: polygon(100% 0, 100% 100%, 0 100%); }
.photo {
    width: 160px; height: 120px; background: #111; border: 4px solid #d62828; display: inline-block; margin-right: 16px; margin-bottom: 16px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #111; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #111; color: #f4f1de; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="photo" style="width:auto;height:auto;display:block;text-align:center;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="photo" style="width:auto;height:auto;display:block;text-align:center;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="photo" style="width:auto;height:auto;display:block;text-align:center;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="photo" style="width:auto;height:auto;display:block;text-align:center;padding:24px;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="banner">Korvia</div><div class="wedge"></div><div class="wedge red"></div>
</div>
"""
    },
    {
        "id": "psychedelic",
        "name": "Psychedelic 70s",
        "tagline": "Wavy patterns, warm colors, groovy type.",
        "desc": "Psychedelic 70s turns Korvia's happy-hour dashboard into a sunburst of color-coded bubbles, making promo items impossible to miss.",
        "palette": ["#FF9F1C", "#FFBF69", "#9B5DE5"],
        "shapes": ["wave", "bubble", "sunburst"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Fredoka One', cursive; background: #ffbf69; color: #3a0ca3;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #ff9f1c;
}
.showcase-nav a { color: #3a0ca3; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; }
.desc { font-family: sans-serif; margin-bottom: 40px; }
.bubble {
    background: #9b5de5; color: #fff; border-radius: 40px; padding: 24px; margin-bottom: 24px;
    display: inline-block; margin-right: 16px;
}
.wavey {
    height: 40px; background: repeating-linear-gradient(135deg, #ff9f1c, #ff9f1c 15px, #9b5de5 15px, #9b5de5 30px);
    border-radius: 20px; margin-bottom: 24px;
}
.sunburst {
    width: 120px; height: 120px; background: repeating-conic-gradient(from 0deg, #ff9f1c 0deg 10deg, #ffbf69 10deg 20deg);
    border-radius: 50%; margin-bottom: 24px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 50%; border: 3px solid #3a0ca3; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #ff9f1c; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="bubble" style="display:block;text-align:center;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="bubble" style="display:block;text-align:center;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="bubble" style="display:block;text-align:center;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="bubble" style="display:block;text-align:center;color:#fff;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="sunburst"></div><div class="wavey"></div>
</div>
"""
    },
    {
        "id": "popart",
        "name": "Pop Art",
        "tagline": "Ben-Day dots, bold outlines, comic panels.",
        "desc": "Pop Art makes Korvia's menu items jump off the screen like comic panels, ideal for fast-casual counters where guests order from tablets.",
        "palette": ["#FFD400", "#FF3333", "#0066CC"],
        "shapes": ["speech-bubble", "dot-pattern", "starburst"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Bangers', cursive; background: #fff; color: #111;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #ffd400; border-bottom: 4px solid #111;
}
.showcase-nav a { color: #111; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.5rem, 7vw, 5rem); margin: 0 0 16px; letter-spacing: 0.04em; -webkit-text-stroke: 2px #111; }
.desc { font-family: sans-serif; margin-bottom: 40px; }
.comic-panel {
    border: 4px solid #111; padding: 24px; margin-bottom: 24px; background: #fff;
    box-shadow: 6px 6px 0 #111;
}
.comic-panel.red { background: #ff3333; color: #fff; }
.comic-panel.blue { background: #0066cc; color: #fff; }
.speech {
    position: relative; background: #fff; border: 4px solid #111; border-radius: 50%; padding: 24px; width: 180px; text-align: center; margin-bottom: 24px;
}
.speech::after { content: ""; position: absolute; bottom: -20px; left: 30px; border: 10px solid transparent; border-top-color: #111; }
.dots {
    width: 140px; height: 80px; background: #fff; background-image: radial-gradient(#ff3333 3px, transparent 3px); background-size: 10px 10px;
    border: 4px solid #111; margin-bottom: 24px;
}
.starburst {
    width: 100px; height: 100px; background: #ffd400; clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
    border: 3px solid #111; margin-bottom: 24px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 3px solid #111; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #ffd400; border-top: 4px solid #111; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="comic-panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="comic-panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="comic-panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="comic-panel" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="speech">POP!</div><div class="starburst"></div><div class="dots"></div>
</div>
"""
    },
    {
        "id": "nordic",
        "name": "Nordic Minimal",
        "tagline": "Muted colors, soft curves, cozy utility.",
        "desc": "Nordic Minimal keeps Korvia's front desk calm with soft cards, rounded pills, and quiet color that lets guest information breathe.",
        "palette": ["#F5F1ED", "#D4C5B9", "#A8B8A6"],
        "shapes": ["soft-rectangle", "rounded-pill", "circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Quicksand', sans-serif; background: #f5f1ed; color: #4a4a48;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #e8e2db;
}
.showcase-nav a { color: #a8b8a6; font-weight: 700; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 700; }
.desc { color: #7a7a78; margin-bottom: 40px; }
.nordic-card {
    background: #fff; border-radius: 20px; padding: 28px; margin-bottom: 24px;
    border: 1px solid #d4c5b9;
}
.pill {
    display: inline-flex; align-items: center; justify-content: center; padding: 12px 28px;
    background: #a8b8a6; color: #fff; border-radius: 999px; font-weight: 600; margin-right: 12px; margin-bottom: 12px;
}
.soft-circle {
    width: 90px; height: 90px; background: #d4c5b9; border-radius: 50%; display: inline-flex;
    align-items: center; justify-content: center; margin-right: 16px; margin-bottom: 24px; font-weight: 700;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 16px; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #7a7a78; }
.showcase-footer { padding: 20px; background: #e8e2db; text-align: center; color: #7a7a78; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="pill" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="nordic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="nordic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="nordic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="nordic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="pill" style="">Scan QR to order</a>
<a href="#" class="pill" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="soft-circle">K</div><div class="pill" style="cursor:default;">hygge</div>
</div>
"""
    },
    {
        "id": "tropical",
        "name": "Tropical Vibes",
        "tagline": "Palm leaves, vivid color, organic shapes.",
        "desc": "Tropical Vibes dresses Korvia's beach resort and rooftop pool menus in sun, arch, and palm shapes that feel like vacation from the first tap.",
        "palette": ["#06D6A0", "#FFD166", "#EF476F"],
        "shapes": ["palm-leaf", "arch", "sun"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700;800&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Poppins', sans-serif; background: #fffbe6; color: #073b4c;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #06d6a0; color: #fff; font-weight: 700;
}
.showcase-nav a { color: #073b4c; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-weight: 800; }
.desc { color: #118ab2; margin-bottom: 40px; }
.palm {
    width: 100px; height: 160px; background: #06d6a0; clip-path: polygon(50% 0%, 65% 35%, 100% 35%, 70% 60%, 85% 100%, 50% 75%, 15% 100%, 30% 60%, 0% 35%, 35% 35%);
    display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.arch {
    width: 120px; height: 160px; background: #ffd166; border-radius: 60px 60px 0 0; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.sun {
    width: 100px; height: 100px; background: #ef476f; border-radius: 50%; display: inline-block; margin-bottom: 24px;
}
.tropic-card {
    background: #fff; border-radius: 24px; padding: 28px; margin-bottom: 24px;
    border: 2px solid #ffd166;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border-radius: 50%; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #06d6a0; color: #fff; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="tropic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="tropic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="tropic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="tropic-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="palm"></div><div class="sun"></div><div class="arch"></div>
</div>
"""
    },
    {
        "id": "grunge",
        "name": "Grunge Distress",
        "tagline": "Torn paper, noise, rough edges.",
        "desc": "Grunge Distress fits Korvia's dive bar and live-music venues: torn cards, stains, and tape-ripped textures match the grit of a busy service.",
        "palette": ["#2B2B2B", "#8C8C8C", "#B33939"],
        "shapes": ["torn-rect", "scratch", "stain"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Special+Elite&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Special Elite', monospace; background: #2b2b2b; color: #d4d4d4;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1a1a1a; border-bottom: 2px dashed #555;
}
.showcase-nav a { color: #b33939; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; }
.desc { color: #999; margin-bottom: 40px; }
.torn {
    background: #3a3a3a; padding: 28px; margin-bottom: 24px;
    clip-path: polygon(0% 3%, 100% 0%, 98% 95%, 2% 100%); border-left: 4px solid #b33939;
}
.stain {
    width: 100px; height: 100px; background: radial-gradient(circle, rgba(179,57,57,0.4) 0%, transparent 70%); border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.tape-rip {
    height: 30px; background: repeating-linear-gradient(90deg, #555, #555 20px, transparent 20px, transparent 25px); margin-bottom: 24px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 1px solid #555; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #999; }
.grunge-bg {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.08'/%3E%3C/svg%3E");
}
.showcase-footer { padding: 20px; background: #1a1a1a; color: #666; text-align: center; }
        """,
        "content": """
<div class="grunge-bg"></div>
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="torn" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="torn" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="torn" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="torn" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="stain"></div><div class="tape-rip"></div>
</div>
"""
    },
    {
        "id": "futurist",
        "name": "Futurist Aero",
        "tagline": "Speed lines, silver, streamlined motion.",
        "desc": "Futurist Aero gives Korvia's high-end hotel and airport F&B kiosks a speed-driven, silver-sheeted interface that signals precision.",
        "palette": ["#C0C0C0", "#1E3A5F", "#E8E8E8"],
        "shapes": ["airfoil", "speed-line", "silver-circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Anton', sans-serif; background: #e8e8e8; color: #1e3a5f;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1e3a5f; color: #e8e8e8; text-transform: uppercase;
}
.showcase-nav a { color: #c0c0c0; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; letter-spacing: 0.04em; }
.desc { font-family: sans-serif; color: #4a6fa5; margin-bottom: 40px; }
.airfoil {
    width: 220px; height: 80px; background: #c0c0c0; border-radius: 50% 10% 50% 10%; margin-bottom: 24px;
    box-shadow: inset -10px -10px 20px rgba(0,0,0,0.1), inset 10px 10px 20px rgba(255,255,255,0.6);
}
.speed {
    height: 8px; background: repeating-linear-gradient(90deg, #1e3a5f, #1e3a5f 40px, transparent 40px, transparent 60px); margin-bottom: 16px; border-radius: 4px;
}
.silver-circle {
    width: 100px; height: 100px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #fff, #c0c0c0 50%, #888); display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.aero-card {
    background: #fff; border-radius: 40px 10px 40px 10px; padding: 28px; margin-bottom: 24px;
    border: 2px solid #c0c0c0;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #1e3a5f; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; }
.showcase-footer { padding: 20px; background: #1e3a5f; color: #c0c0c0; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="aero-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="aero-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="aero-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="aero-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="airfoil"></div><div class="silver-circle"></div><div class="speed"></div>
</div>
"""
    },
    {
        "id": "rococo",
        "name": "Rococo Ornate",
        "tagline": "Pastel frames, gold flourishes, decorative excess.",
        "desc": "Rococo Ornate frames Korvia's heritage tea rooms and wedding venues in gilded flourishes, turning bookings into invitations.",
        "palette": ["#FFF0F5", "#D4AF37", "#98D8C8"],
        "shapes": ["scroll-frame", "oval", "flourish"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Cormorant Garamond', serif; background: #fff0f5; color: #5a4a4a;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 28px; background: #f8e1e7; border-bottom: 2px solid #d4af37;
}
.showcase-nav a { color: #d4af37; text-decoration: none; font-weight: 700; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 28px; width: 100%; text-align: center; }
h1 { font-size: clamp(2.4rem, 6vw, 4.5rem); margin: 0 0 16px; font-style: italic; }
.desc { font-size: 1.15rem; color: #8a6a6a; margin-bottom: 40px; }
.ornate {
    border: 4px double #d4af37; border-radius: 20px; padding: 32px; margin-bottom: 24px; background: #fff;
    position: relative;
}
.ornate::before, .ornate::after { content: "❧"; color: #d4af37; position: absolute; font-size: 1.5rem; }
.ornate::before { top: 10px; left: 14px; } .ornate::after { bottom: 10px; right: 14px; }
.oval2 { width: 160px; height: 100px; background: #98d8c8; border-radius: 50%; border: 3px solid #d4af37; display: inline-block; margin: 0 12px 24px; }
.flourish { height: 40px; background: radial-gradient(circle, transparent 20%, #d4af37 25%, transparent 30%); background-size: 40px 40px; margin-bottom: 24px; }
.swatches { display: flex; gap: 16px; justify-content: center; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #d4af37; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #8a6a6a; }
.showcase-footer { padding: 20px; background: #f8e1e7; color: #8a6a6a; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="ornate" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="ornate" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="ornate" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="ornate" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="flourish"></div><div class="oval2"></div>
</div>
"""
    },
    {
        "id": "pixel",
        "name": "Pixel 8-bit",
        "tagline": "Blocky squares, limited palette, retro sprites.",
        "desc": "Pixel 8-bit gives Korvia a playful retro game aesthetic for family restaurants and arcade bars, making QR ordering feel like a power-up.",
        "palette": ["#000000", "#FF004D", "#00E436"],
        "shapes": ["pixel-square", "sprite", "block"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Press Start 2P', cursive; background: #202020; color: #fff;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 4px solid #ff004d;
    font-size: 0.7rem;
}
.showcase-nav a { color: #00e436; text-decoration: none; }
.wrap { flex: 1; max-width: 860px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(1.4rem, 4vw, 2.4rem); margin: 0 0 24px; line-height: 1.5; }
.desc { font-family: sans-serif; font-size: 0.95rem; color: #aaa; margin-bottom: 40px; line-height: 1.6; }
.pixel-btn {
    display: inline-block; padding: 16px 24px; background: #00e436; color: #000;
    border: 4px solid #fff; box-shadow: 4px 4px 0 #000; font-size: 0.8rem; margin-right: 12px; margin-bottom: 16px;
}
.sprite {
    width: 80px; height: 80px; background: #ff004d;
    box-shadow:
        20px 0 0 #ff004d, 40px 0 0 #ff004d,
        0 20px 0 #ff004d, 20px 20px 0 #fff, 40px 20px 0 #ff004d,
        0 40px 0 #ff004d, 20px 40px 0 #ff004d, 40px 40px 0 #ff004d;
    margin: 0 60px 60px 0;
}
.block { width: 64px; height: 64px; background: #00e436; border: 4px solid #fff; display: inline-block; margin-right: 12px; margin-bottom: 24px; }
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 64px; height: 64px; border: 4px solid #fff; }
.swatch span { display: block; font-size: 0.55rem; padding-top: 72px; color: #aaa; }
.showcase-footer { padding: 20px; background: #000; color: #888; text-align: center; font-size: 0.7rem; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="pixel-btn" style="">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="block" style="width:auto;height:auto;display:block;text-align:center;padding:20px;color:#000;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="block" style="width:auto;height:auto;display:block;text-align:center;padding:20px;color:#000;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="block" style="width:auto;height:auto;display:block;text-align:center;padding:20px;color:#000;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="block" style="width:auto;height:auto;display:block;text-align:center;padding:20px;color:#000;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="pixel-btn" style="">Scan QR to order</a>
<a href="#" class="pixel-btn" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="sprite"></div><div class="block"></div>
</div>
"""
    },
    {
        "id": "afrofuturism",
        "name": "Afrofuturism",
        "tagline": "Metallics, bold patterns, ancestral geometry.",
        "desc": "Afrofuturism connects Korvia's Pan-African venues to a forward-looking visual lineage where sun motifs and earth grids honor the menu's roots.",
        "palette": ["#1A1A1A", "#B87333", "#F4E4BC"],
        "shapes": ["mud-cloth", "sunburst", "copper-arc"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Space+Grotesk:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Space Grotesk', sans-serif; background: #1a1a1a; color: #f4e4bc;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #111; border-bottom: 2px solid #b87333;
}
.showcase-nav a { color: #b87333; text-decoration: none; font-weight: 700; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Bebas Neue', sans-serif; font-size: clamp(2.6rem, 7vw, 5rem); margin: 0 0 16px; letter-spacing: 0.06em; }
.desc { color: #c2b58a; margin-bottom: 40px; }
.mud {
    width: 140px; height: 140px; background: #f4e4bc;
    background-image:
        linear-gradient(#1a1a1a 10px, transparent 10px),
        linear-gradient(90deg, #1a1a1a 10px, transparent 10px);
    background-size: 40px 40px; border: 4px solid #b87333; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.sun2 {
    width: 120px; height: 120px; background: #b87333; border-radius: 50%;
    background-image: repeating-conic-gradient(from 0deg, #b87333 0deg 10deg, #f4e4bc 10deg 20deg);
    display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.arc {
    width: 140px; height: 70px; background: #b87333; border-radius: 140px 140px 0 0; display: inline-block; margin-bottom: 24px;
}
.afro-card {
    background: #111; border: 2px solid #b87333; padding: 28px; margin-bottom: 24px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 2px solid #b87333; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #c2b58a; }
.showcase-footer { padding: 20px; background: #111; color: #b87333; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="afro-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="afro-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="afro-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="afro-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="sun2"></div><div class="arc"></div><div class="mud"></div>
</div>
"""
    },
    {
        "id": "darkacademia",
        "name": "Dark Academia",
        "tagline": "Old paper, deep green, serifs, wax seals.",
        "desc": "Dark Academia gives Korvia's historic hotel and library cafes a scholarly ledger feel, with parchment panels and wax-seal confirmations.",
        "palette": ["#2C3E2D", "#D4C5A9", "#8B0000"],
        "shapes": ["seal", "book-spine", "oval-frame"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,700;1,400&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Crimson Text', serif; background: #2c3e2d; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1f2c1f; border-bottom: 1px solid #4a5d3a;
}
.showcase-nav a { color: #d4c5a9; text-decoration: none; }
.wrap { flex: 1; max-width: 820px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-size: clamp(2.2rem, 6vw, 4rem); margin: 0 0 16px; font-style: italic; }
.desc { color: #a89f7e; margin-bottom: 40px; }
.parchment {
    background: #d4c5a9; color: #2c3e2d; padding: 32px; margin-bottom: 24px; border-radius: 4px;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.15);
}
.seal2 {
    width: 70px; height: 70px; background: #8b0000; border-radius: 50%; display: inline-flex;
    align-items: center; justify-content: center; color: #d4c5a9; font-weight: 700; margin-right: 16px; margin-bottom: 24px;
}
.spine {
    width: 50px; height: 160px; background: #1f2c1f; border-left: 4px solid #d4c5a9; border-right: 4px solid #d4c5a9; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.oval-frame {
    width: 140px; height: 100px; border: 4px solid #d4c5a9; border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.swatches { display: flex; gap: 16px; margin-bottom: 32px; }
.swatch { width: 70px; height: 70px; border: 1px solid #4a5d3a; }
.swatch span { display: block; font-size: 0.65rem; padding-top: 80px; color: #a89f7e; }
.showcase-footer { padding: 20px; background: #1f2c1f; color: #a89f7e; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button style="display:inline-block;padding:10px 20px;border:2px solid currentColor;background:transparent;color:inherit;font:inherit;cursor:pointer;">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="parchment" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="parchment" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="parchment" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="parchment" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" style="display:inline-block;padding:12px 24px;background:#000;color:#fff;border:none;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Scan QR to order</a>
<a href="#" style="display:inline-block;padding:12px 24px;background:transparent;color:inherit;border:2px solid currentColor;font:inherit;cursor:pointer;margin-right:12px;margin-bottom:12px;text-decoration:none;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="oval-frame"></div><div class="seal2">K</div><div class="spine"></div>
</div>
"""
    }
]

BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ — Korvia Design Direction</title>
<style>
__CSS__
</style>
</head>
<body>
<nav class="showcase-nav">
  <a href="__PREV__.html">← Prev</a>
  <a href="index.html">Showcase</a>
  <a href="__NEXT__.html">Next →</a>
</nav>
__CONTENT__
<footer class="showcase-footer">Korvia Design Direction Showcase · __INDEX__ / __TOTAL__</footer>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Korvia Design Direction Showcase</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #f9f8f6; color: #1c1917;
    min-height: 100vh; display: flex; flex-direction: column;
}
header { padding: 56px 32px 32px; text-align: center; border-bottom: 1px solid #e7e5e4; }
h1 { font-size: clamp(2rem, 5vw, 3.2rem); margin: 0 0 12px; }
p.lead { color: #78716c; margin: 0; }
main { flex: 1; max-width: 960px; margin: 0 auto; padding: 40px 24px; width: 100%; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; }
.card {
    background: #fff; border: 1px solid #e7e5e4; border-radius: 4px; padding: 24px;
    transition: transform 150ms ease, border-color 150ms ease;
}
.card:hover { transform: translateY(-3px); border-color: #b45309; }
.card a { text-decoration: none; color: inherit; display: block; }
.card h2 { margin: 0 0 8px; font-size: 1.15rem; }
.card p { margin: 0; font-size: 0.9rem; color: #78716c; }
.index { color: #b45309; font-weight: 800; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
footer { padding: 32px; text-align: center; color: #78716c; font-size: 0.85rem; border-top: 1px solid #e7e5e4; }
</style>
</head>
<body>
<header>
    <h1>Korvia Design Direction Showcase</h1>
    <p class="lead">Thirty human interface directions for Korvia — a QR-first hospitality operating system for East Africa.</p>
</header>
<main>
    <div class="grid">
__CARDS__
    </div>
</main>
<footer>← Click a direction, then use Next / Showcase to browse →</footer>
</body>
</html>
"""


def main():
    out = os.path.expanduser("~/github-recovery/korvia/showcase")
    os.makedirs(out, exist_ok=True)
    total = len(DIRECTIONS)

    for i, d in enumerate(DIRECTIONS):
        next_id = DIRECTIONS[(i + 1) % total]["id"]
        prev_id = DIRECTIONS[(i - 1) % total]["id"]
        html = BASE
        html = html.replace("__TITLE__", f"{d['name']}")
        html = html.replace("__CSS__", d["css"])
        html = html.replace("__PREV__", prev_id)
        html = html.replace("__NEXT__", next_id)
        html = html.replace("__CONTENT__", d["content"])
        html = html.replace("__INDEX__", str(i + 1))
        html = html.replace("__TOTAL__", str(total))
        path = os.path.join(out, f"{d['id']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {path}")

    cards = []
    for i, d in enumerate(DIRECTIONS, start=1):
        cards.append(
            f'<div class="card"><a href="{d["id"]}.html"><div class="index">Direction {i:02d}</div>'
            f'<h2>{d["name"]}</h2><p>{d["tagline"]}</p></a></div>'
        )
    index_html = INDEX.replace("__CARDS__", "\n".join(cards))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("wrote showcase/index.html")


if __name__ == "__main__":
    main()
