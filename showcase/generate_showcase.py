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
    },
    {
        "id": "gildedgrunge",
        "name": "Gilded Grunge",
        "tagline": "Gold frames, torn edges, and a double rectangle that survived the night.",
        "desc": "Gilded Grunge dresses Korvia's late-night bars and live-music venues in Art Deco gold, then tears, stains, and noise it until the luxury feels lived-in.",
        "palette": ["#0F0A05", "#C5A059", "#B33939"],
        "shapes": ["double-rectangle", "torn-gold-panel", "stain"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Special+Elite&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Special Elite', monospace; background: #0f0a05; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1a120b; border-bottom: 1px dashed #c5a059;
    font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; letter-spacing: 0.08em; }
.desc { color: #a89f7e; font-size: 1.05rem; margin-bottom: 40px; }
.gilded-card {
    background: #1a120b; border: 1px solid #c5a059; padding: 28px; margin-bottom: 24px;
    position: relative; box-shadow: inset 0 0 40px rgba(197,160,89,0.08);
    clip-path: polygon(0% 2%, 100% 0%, 98% 98%, 2% 100%);
}
.gilded-card::before, .gilded-card::after { content: "◆"; color: #c5a059; position: absolute; font-size: 0.8rem; }
.gilded-card::before { top: 12px; left: 14px; } .gilded-card::after { bottom: 12px; right: 14px; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.15em; font-size: 0.8rem; cursor: pointer;
}
.gold-btn:hover { background: #c5a059; color: #0f0a05; }
.double-rect {
    width: 140px; height: 100px; position: relative; display: inline-block; margin-right: 30px; margin-bottom: 24px;
}
.double-rect::before, .double-rect::after {
    content: ""; position: absolute; border: 2px solid #c5a059; background: rgba(197,160,89,0.1);
}
.double-rect::before { width: 100%; height: 100%; top: 0; left: 0; clip-path: polygon(0 0, 100% 0, 100% 65%, 65% 65%, 65% 100%, 0 100%); }
.double-rect::after { width: 100%; height: 100%; top: 12px; left: 16px; clip-path: polygon(0 0, 100% 0, 100% 65%, 65% 65%, 65% 100%, 0 100%); z-index: -1; opacity: 0.5; }
.stain {
    width: 90px; height: 90px; background: radial-gradient(circle, rgba(179,57,57,0.35) 0%, transparent 70%); border-radius: 50%; display: inline-block; margin-right: 16px; margin-bottom: 24px;
}
.tape-rip {
    height: 24px; background: repeating-linear-gradient(90deg, #c5a059, #c5a059 18px, transparent 18px, transparent 24px); opacity: 0.4; margin-bottom: 24px;
}
.noise {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
}
.showcase-footer { padding: 20px; background: #1a120b; color: #8a7e63; border-top: 1px dashed #c5a059; text-align: center; }
        """,
        "content": """
<div class="noise"></div>
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
<a href="#client" class="gilded-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">👤</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p>
</a>
<a href="#restaurant" class="gilded-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p>
</a>
<a href="#hotel" class="gilded-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🏨</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p>
</a>
<a href="#events" class="gilded-card" style="text-align:center;display:block;">
<div style="font-size:1.8rem;margin-bottom:8px;">🎉</div>
<h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3>
<div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div>
<p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p>
</a>
</div>
<div style="margin:24px 0;">
<a href="#" class="gold-btn">Scan QR to order</a>
<a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a>
</div>
<h2>Direction accent</h2>
<div class="double-rect"></div>
<div class="stain"></div>
<div class="tape-rip" style="width:60%"></div>
</div>
"""
    },

    {
        "id": "decdecay",
        "name": "Deco Decay",
        "tagline": "Ornate frames left out in the rain.",
        "desc": "Deco Decay takes Korvia's heritage hotel lobbies and lets the moldings peel: gold leaf flaking off charcoal plaster, water-stained menus, and a sense of beautiful neglect.",
        "palette": ["#1A1510", "#C5A059", "#4A5D3A"],
        "shapes": ["peeling-frame", "water-stain", "crack"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=IM+Fell+English+SC&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'IM Fell English SC', serif; background: #1a1510; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120e0a; border-bottom: 1px dashed #6b5b3e;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; letter-spacing: 0.06em; }
.desc { color: #a89f7e; margin-bottom: 40px; }
.decayed-card {
    background: #201a12; border: 2px solid #c5a059; padding: 28px; margin-bottom: 24px;
    position: relative; box-shadow: inset 0 0 30px rgba(0,0,0,0.5);
    clip-path: polygon(2% 0, 100% 1%, 98% 100%, 0 98%);
}
.decayed-card::before { content: ""; position: absolute; inset: 6px; border: 1px dashed #c5a059; opacity: 0.4; pointer-events: none; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.12em; cursor: pointer;
}
.peel {
    width: 120px; height: 120px; border: 2px solid #c5a059; position: relative; display: inline-block; margin-right: 20px; margin-bottom: 24px;
}
.peel::after { content: ""; position: absolute; top: 8px; right: -10px; width: 100%; height: 100%; border: 2px solid #4a5d3a; z-index: -1; opacity: 0.6; }
.stain { width: 80px; height: 80px; background: radial-gradient(circle, rgba(74,93,58,0.4) 0%, transparent 70%); border-radius: 50%; display: inline-block; margin-right: 16px; }
.crack { height: 2px; background: repeating-linear-gradient(90deg, #c5a059, #c5a059 10px, transparent 10px, transparent 14px); opacity: 0.5; margin: 16px 0; }
.showcase-footer { padding: 20px; background: #120e0a; color: #6b5b3e; border-top: 1px dashed #6b5b3e; text-align: center; }
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
<a href="#client" class="decayed-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decayed-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decayed-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decayed-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="peel"></div><div class="stain"></div><div class="crack" style="width:50%"></div>
</div>
"""
    },
    {
        "id": "rustgold",
        "name": "Rusted Gold",
        "tagline": "When the gold has oxidized but still shines.",
        "desc": "Rusted Gold gives Korvia's rooftop grills and beach bars a weathered signboard feel: corroded metal, burnt orange patina, and barely-legible gilt lettering.",
        "palette": ["#2B1D16", "#C5A059", "#B3542F"],
        "shapes": ["rusted-plate", "patina-circle", "bolt"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Anton', sans-serif; background: #2b1d16; color: #e6d5b8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #1f140f; border-bottom: 3px solid #b3542f;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; letter-spacing: 0.08em; }
.desc { color: #c2a882; margin-bottom: 40px; }
.rust-card {
    background: repeating-linear-gradient(45deg, #3a271d, #3a271d 4px, #4a3428 4px, #4a3428 8px); border: 2px solid #c5a059;
    padding: 28px; margin-bottom: 24px; position: relative;
    clip-path: polygon(0% 0%, 100% 2%, 98% 100%, 2% 98%);
}
.rust-card::before { content: ""; position: absolute; inset: 8px; border: 1px solid #b3542f; opacity: 0.5; pointer-events: none; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #c5a059; background: #b3542f;
    color: #e6d5b8; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.plate { width: 130px; height: 90px; background: repeating-linear-gradient(45deg, #c5a059, #c5a059 3px, #b3542f 3px, #b3542f 6px); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.plate::after { content: ""; position: absolute; top: 6px; left: 6px; right: 6px; bottom: 6px; border: 1px dashed #2b1d16; }
.patina { width: 80px; height: 80px; border-radius: 50%; background: radial-gradient(circle, #b3542f 0%, transparent 70%); display: inline-block; margin-right: 16px; }
.bolt { width: 12px; height: 12px; background: #c5a059; border-radius: 50%; display: inline-block; margin: 4px; box-shadow: inset 0 0 3px #000; }
.showcase-footer { padding: 20px; background: #1f140f; color: #8a6a4a; border-top: 3px solid #b3542f; text-align: center; }
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
<a href="#client" class="rust-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="rust-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="rust-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="rust-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="plate"></div><div class="patina"></div><div style="margin-bottom:24px;"><div class="bolt"></div><div class="bolt"></div><div class="bolt"></div></div>
</div>
"""
    },
    {
        "id": "tornornate",
        "name": "Torn Ornate",
        "tagline": "Baroque frames ripped at the edges.",
        "desc": "Torn Ornate frames Korvia's banquet halls and wedding venues with gilded rococo borders that look like they were torn from an old ledger.",
        "palette": ["#151019", "#D4AF37", "#8B2047"],
        "shapes": ["torn-frame", "ornate-corner", "seal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Cormorant Garamond', serif; background: #151019; color: #f0e6d2;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #0e0a11; border-bottom: 1px solid #d4af37;
}
.showcase-nav a { color: #d4af37; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b0a27d; margin-bottom: 40px; font-style: italic; }
.ornate-card {
    background: #1f1822; border: 3px double #d4af37; padding: 28px; margin-bottom: 24px;
    position: relative; clip-path: polygon(0% 0%, 96% 4%, 100% 96%, 4% 100%);
}
.ornate-card::before, .ornate-card::after { content: "❦"; color: #d4af37; position: absolute; font-size: 1.2rem; }
.ornate-card::before { top: 8px; left: 12px; } .ornate-card::after { bottom: 8px; right: 12px; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #d4af37; text-transform: uppercase; letter-spacing: 0.12em; cursor: pointer; font-family: 'Cinzel', serif;
}
.frame {
    width: 120px; height: 150px; border: 4px double #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px;
    position: relative; clip-path: polygon(0 0, 100% 0, 100% 85%, 85% 100%, 0 100%);
}
.frame::after { content: ""; position: absolute; top: 10px; left: 10px; right: 10px; bottom: 10px; border: 1px dashed #8b2047; }
.seal { width: 60px; height: 60px; background: #8b2047; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; color: #f0e6d2; font-weight: 700; margin-right: 16px; }
.showcase-footer { padding: 20px; background: #0e0a11; color: #8a7e63; border-top: 1px solid #d4af37; text-align: center; }
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
<a href="#client" class="ornate-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="ornate-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="ornate-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="ornate-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="frame"></div><div class="seal">K</div>
</div>
"""
    },
    {
        "id": "velvetbruise",
        "name": "Velvet Bruise",
        "tagline": "Deep velvet, gold trauma, soft noise.",
        "desc": "Velvet Bruise wraps Korvia's cocktail lounges in purple velvet, then distresses it: cigarette burns, gold cracks, and a moody after-hours hum.",
        "palette": ["#1A0F1F", "#9B7EBD", "#D4AF37"],
        "shapes": ["velvet-rect", "bruise", "gold-crack"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,600&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Playfair Display', serif; background: #1a0f1f; color: #e8e0f0;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120916; border-bottom: 1px solid #9b7ebd;
}
.showcase-nav a { color: #d4af37; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b8a8c8; margin-bottom: 40px; font-style: italic; }
.velvet-card {
    background: #24132d; border: 1px solid #9b7ebd; padding: 28px; margin-bottom: 24px;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.4); position: relative;
}
.velvet-card::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, transparent, #d4af37, transparent); opacity: 0.6; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #d4af37; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.velvet { width: 120px; height: 80px; background: radial-gradient(ellipse at center, #4a2a5a 0%, #1a0f1f 100%); border: 1px solid #9b7ebd; display: inline-block; margin-right: 16px; margin-bottom: 24px; box-shadow: inset 0 0 20px rgba(0,0,0,0.5); }
.bruise { width: 80px; height: 80px; border-radius: 50%; background: radial-gradient(circle, rgba(155,126,189,0.5) 0%, transparent 70%); display: inline-block; margin-right: 16px; }
.crack { width: 100px; height: 2px; background: #d4af37; transform: rotate(-15deg); display: inline-block; margin-bottom: 24px; opacity: 0.7; }
.showcase-footer { padding: 20px; background: #120916; color: #8a7a9a; border-top: 1px solid #9b7ebd; text-align: center; }
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
<a href="#client" class="velvet-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="velvet-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="velvet-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="velvet-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="velvet"></div><div class="bruise"></div><div class="crack"></div>
</div>
"""
    },
    {
        "id": "brassrot",
        "name": "Brass Rot",
        "tagline": "Corroded brass and green verdigris.",
        "desc": "Brass Rot gives Korvia's old-school brasseries and colonial-era hotels a corroded metal interface: green patina, riveted plates, and tarnished edges.",
        "palette": ["#1A1710", "#8B7D4B", "#3A5A4A"],
        "shapes": ["verdigris-plate", "rivet", "tarnish"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=IM+Fell+English&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'IM Fell English', serif; background: #1a1710; color: #d8d0b8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #12100a; border-bottom: 2px solid #3a5a4a;
}
.showcase-nav a { color: #8b7d4b; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a8a080; margin-bottom: 40px; }
.brass-card {
    background: repeating-linear-gradient(90deg, #2a2518, #2a2518 3px, #3a3520 3px, #3a3520 6px);
    border: 2px solid #8b7d4b; padding: 28px; margin-bottom: 24px; position: relative;
    clip-path: polygon(0% 0%, 99% 2%, 100% 100%, 1% 98%);
}
.brass-card::before { content: ""; position: absolute; inset: 6px; border: 1px dashed #3a5a4a; pointer-events: none; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #8b7d4b; background: #3a5a4a;
    color: #d8d0b8; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.plate2 { width: 120px; height: 80px; background: linear-gradient(135deg, #8b7d4b, #3a5a4a); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.plate2::after { content: ""; position: absolute; top: 8px; left: 8px; right: 8px; bottom: 8px; border: 1px dotted #1a1710; }
.rivet { width: 10px; height: 10px; background: radial-gradient(circle at 30% 30%, #d8d0b8, #3a5a4a); border-radius: 50%; display: inline-block; margin: 3px; }
.tarnish { width: 90px; height: 90px; border-radius: 50%; background: radial-gradient(circle, rgba(58,90,74,0.5) 0%, transparent 70%); display: inline-block; margin-right: 16px; }
.showcase-footer { padding: 20px; background: #12100a; color: #6b6a58; border-top: 2px solid #3a5a4a; text-align: center; }
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
<a href="#client" class="brass-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="brass-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="brass-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="brass-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="plate2"></div><div class="tarnish"></div><div style="margin-bottom:24px;"><div class="rivet"></div><div class="rivet"></div><div class="rivet"></div></div>
</div>
"""
    },
    {
        "id": "gildedriot",
        "name": "Gilded Riot",
        "tagline": "Art Deco that got into a fight.",
        "desc": "Gilded Riot takes Korvia's VIP event entrances and covers them in gold leaf, then slaps on neon stickers, tape, and attitude.",
        "palette": ["#0A0A0A", "#D4AF37", "#FF2E88"],
        "shapes": ["sticker-rect", "gold-splat", "tape"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Archivo Black', sans-serif; background: #0a0a0a; color: #fff;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 4px solid #ff2e88;
}
.showcase-nav a { color: #d4af37; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d4af37; margin-bottom: 40px; }
.riot-card {
    background: #111; border: 2px solid #d4af37; padding: 28px; margin-bottom: 24px;
    position: relative; box-shadow: 8px 8px 0 #ff2e88;
    clip-path: polygon(0% 0%, 100% 0%, 98% 100%, 2% 96%);
}
.riot-card::before { content: "VIP"; position: absolute; top: -10px; left: 20px; background: #ff2e88; color: #000; padding: 2px 10px; font-size: 0.65rem; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 2px solid #d4af37; background: #ff2e88;
    color: #000; text-transform: uppercase; letter-spacing: 0.08em; cursor: pointer; font-weight: 700;
}
.sticker { width: 120px; height: 80px; background: #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; transform: rotate(-4deg); }
.sticker::after { content: ""; position: absolute; top: 8px; left: 8px; right: 8px; bottom: 8px; border: 2px dashed #0a0a0a; }
.tape { width: 100px; height: 24px; background: rgba(255,46,136,0.7); transform: rotate(8deg); display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.splat { width: 80px; height: 80px; background: #ff2e88; clip-path: polygon(50% 0%, 80% 10%, 100% 35%, 90% 70%, 60% 100%, 30% 90%, 0% 60%, 10% 30%); display: inline-block; margin-right: 16px; }
.showcase-footer { padding: 20px; background: #000; color: #d4af37; border-top: 4px solid #ff2e88; text-align: center; }
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
<a href="#client" class="riot-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="riot-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="riot-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="riot-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="sticker"></div><div class="tape"></div><div class="splat"></div>
</div>
"""
    },
    {
        "id": "palaceafterhours",
        "name": "Palace After Hours",
        "tagline": "Midnight luxury, soft damage, hushed gold.",
        "desc": "Palace After Hours gives Korvia's high-end hotel bars a quiet 3 AM feeling: chandeliers dimmed, gold trim scuffed, and a single waiter still taking orders.",
        "palette": ["#0D1321", "#C5A059", "#5A4A6A"],
        "shapes": ["chandelier-glow", "scuffed-frame", "velvet-stain"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Cormorant Garamond', serif; background: #0d1321; color: #e6dcc8;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #080c14; border-bottom: 1px solid #5a4a6a;
}
.showcase-nav a { color: #c5a059; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; font-style: italic; }
.palace-card {
    background: #121a2b; border: 1px solid #c5a059; padding: 28px; margin-bottom: 24px;
    box-shadow: 0 0 40px rgba(197,160,89,0.08); position: relative;
}
.palace-card::before { content: ""; position: absolute; top: -1px; left: 20%; right: 20%; height: 2px; background: #c5a059; opacity: 0.6; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #c5a059; background: transparent;
    color: #c5a059; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.glow { width: 100px; height: 100px; border-radius: 50%; background: radial-gradient(circle, rgba(197,160,89,0.3) 0%, transparent 70%); display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.scuff { width: 120px; height: 80px; border: 1px solid #5a4a6a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.scuff::after { content: ""; position: absolute; top: 20px; left: 10px; width: 80px; height: 2px; background: #c5a059; opacity: 0.4; transform: rotate(-5deg); }
.stain2 { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle, rgba(90,74,106,0.5) 0%, transparent 70%); display: inline-block; margin-right: 16px; }
.showcase-footer { padding: 20px; background: #080c14; color: #6b6278; border-top: 1px solid #5a4a6a; text-align: center; }
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
<a href="#client" class="palace-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="palace-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="palace-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="palace-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="glow"></div><div class="scuff"></div><div class="stain2"></div>
</div>
"""
    },
    {
        "id": "crackedgilding",
        "name": "Cracked Gilding",
        "tagline": "White marble, gold veins, hairline fractures.",
        "desc": "Cracked Gilding gives Korvia's patisseries and daytime cafés a bright, broken-luxury feel: white stone, gold cracks, and the charm of something once perfect.",
        "palette": ["#F5F1EA", "#D4AF37", "#8A7E72"],
        "shapes": ["cracked-rect", "gold-vein", "chip"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Libre+Baskerville:ital@0;1&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Libre Baskerville', serif; background: #f5f1ea; color: #3a3530;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #fff; border-bottom: 1px solid #d4af37;
}
.showcase-nav a { color: #8a7e72; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; color: #3a3530; }
.desc { color: #8a7e72; margin-bottom: 40px; }
.cracked-card {
    background: #fff; border: 1px solid #d4af37; padding: 28px; margin-bottom: 24px;
    position: relative; box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}
.cracked-card::before { content: ""; position: absolute; top: 10px; left: 10px; width: 40px; height: 1px; background: #d4af37; transform: rotate(35deg); opacity: 0.6; }
.cracked-card::after { content: ""; position: absolute; bottom: 20px; right: 15px; width: 60px; height: 1px; background: #d4af37; transform: rotate(-20deg); opacity: 0.5; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #8a7e72; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.marble { width: 120px; height: 90px; background: #fff; border: 1px solid #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.marble::after { content: ""; position: absolute; top: 20px; left: 10px; width: 80px; height: 1px; background: #d4af37; transform: rotate(25deg); opacity: 0.6; }
.vein { width: 100px; height: 2px; background: linear-gradient(90deg, transparent, #d4af37, transparent); transform: rotate(-12deg); display: inline-block; margin-bottom: 24px; opacity: 0.7; }
.chip { width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-bottom: 35px solid #d4af37; display: inline-block; margin-right: 16px; opacity: 0.6; }
.showcase-footer { padding: 20px; background: #fff; color: #8a7e72; border-top: 1px solid #d4af37; text-align: center; }
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
<a href="#client" class="cracked-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="cracked-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="cracked-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="cracked-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="marble"></div><div class="vein"></div><div class="chip"></div>
</div>
"""
    },
    {
        "id": "noirgrunge",
        "name": "Noir Grunge",
        "tagline": "Black and gold, grain, and shadow.",
        "desc": "Noir Grunge gives Korvia's speakeasies and jazz clubs a cinematic interface: deep blacks, single gold accent, film grain, and hard shadows.",
        "palette": ["#0A0A0A", "#D4AF37", "#333333"],
        "shapes": ["noir-rect", "film-grain", "gold-bar"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Oswald:wght@400;600&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Oswald', sans-serif; background: #0a0a0a; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #000; border-bottom: 1px solid #333;
}
.showcase-nav a { color: #d4af37; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #888; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 0.1em; }
.noir-card {
    background: #111; border: 1px solid #333; padding: 28px; margin-bottom: 24px;
    box-shadow: 6px 6px 0 #d4af37; position: relative;
}
.noir-card::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: #d4af37; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #d4af37; background: transparent;
    color: #d4af37; text-transform: uppercase; letter-spacing: 0.12em; cursor: pointer;
}
.noir-rect { width: 120px; height: 80px; background: #000; border: 1px solid #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.noir-rect::after { content: ""; position: absolute; top: 10px; left: 10px; right: -10px; bottom: -10px; border: 1px solid #333; z-index: -1; }
.bar { width: 100px; height: 8px; background: #d4af37; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.grain {
    position: fixed; inset: 0; pointer-events: none; z-index: -1;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.05'/%3E%3C/svg%3E");
}
.showcase-footer { padding: 20px; background: #000; color: #555; border-top: 1px solid #333; text-align: center; }
        """,
        "content": """
<div class="grain"></div>
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
<a href="#client" class="noir-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="noir-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="noir-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="noir-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="noir-rect"></div><div class="bar"></div>
</div>
"""
    },
    {
        "id": "smokinglounge",
        "name": "Smoking Lounge",
        "tagline": "Leather, smoke rings, and tarnished brass.",
        "desc": "Smoking Lounge gives Korvia's cigar bars and private clubs a heavy, atmospheric interface: tobacco browns, brass ashtrays, and smoke-stained edges.",
        "palette": ["#1F1A14", "#8B7D4B", "#5C4A3A"],
        "shapes": ["leather-panel", "smoke-ring", "ashtray"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Merriweather:ital@0;1&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Merriweather', serif; background: #1f1a14; color: #d8d0c0;
    min-height: 100vh; display: flex; flex-direction: column;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #15120d; border-bottom: 1px solid #5c4a3a;
}
.showcase-nav a { color: #8b7d4b; text-decoration: none; }
.wrap { flex: 1; max-width: 900px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f80; margin-bottom: 40px; font-style: italic; }
.lounge-card {
    background: #2a231a; border: 1px solid #5c4a3a; padding: 28px; margin-bottom: 24px;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.4); position: relative;
}
.lounge-card::before { content: ""; position: absolute; top: 12px; right: 12px; width: 30px; height: 30px; border: 1px solid #8b7d4b; border-radius: 50%; opacity: 0.4; }
.gold-btn {
    display: inline-block; padding: 14px 28px; border: 1px solid #8b7d4b; background: transparent;
    color: #8b7d4b; text-transform: uppercase; letter-spacing: 0.1em; cursor: pointer;
}
.leather { width: 120px; height: 90px; background: repeating-linear-gradient(90deg, #3a2f22, #3a2f22 2px, #4a3d2e 2px, #4a3d2e 4px); border: 1px solid #5c4a3a; display: inline-block; margin-right: 16px; margin-bottom: 24px; }
.ring { width: 80px; height: 80px; border: 2px solid #8b7d4b; border-radius: 50%; display: inline-block; margin-right: 16px; opacity: 0.5; }
.ring::after { content: ""; display: block; width: 50px; height: 50px; border: 1px solid #8b7d4b; border-radius: 50%; margin: 13px; opacity: 0.5; }
.ashtray { width: 60px; height: 20px; background: #3a3a3a; border-radius: 50%; border: 2px solid #8b7d4b; display: inline-block; margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: #15120d; color: #6b6048; border-top: 1px solid #5c4a3a; text-align: center; }
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
<a href="#client" class="lounge-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="lounge-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="lounge-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="lounge-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><div style="width:28px;height:3px;background:currentColor;margin:10px auto;opacity:.6;"></div><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="leather"></div><div class="ring"></div><div class="ashtray"></div>
</div>
"""
    },

    {
        "id": "swissgilded",
        "name": "Swiss Gilded Grunge",
        "tagline": "Gold frames locked in a Swiss grid, then distressed.",
        "desc": "Swiss Gilded Grunge forces Korvia's late-night venues into an asymmetric grid: gold borders, red accents, torn edges, and absolute order barely holding together.",
        "palette": ["#0A0A0A", "#C5A059", "#E42718"],
        "shapes": ["grid-rectangle", "gold-rule", "red-stamp"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Cinzel:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Anton&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cormorant+Garamond:ital,wght@0,600;1,600&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&family=Inter:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Merriweather:ital@0;1&display=swap');
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
    },
    {
        "id": "redglide",
        "name": "Red Deco Glide",
        "tagline": "Direction 43 with a fixed red Korvia square that moves against the scroll.",
        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and pins a red square logo holder to the left; as the page scrolls, the square stays fixed and appears to glide past the content.",
        "palette": ["#1A1510", "#C5A059", "#E42718"],
        "shapes": ["logo-square", "peeling-gold", "red-bar"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif; background: #1a1510; color: #d4c5a9;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #201a12; color: #d4c5a9;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #e42718;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #120e0a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #201a12; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #e42718;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #e42718;
    color: #1a1510; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #201a12; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #120e0a; color: #6b5b3e; text-align: center; }
        """,
        "content": """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
        "id": "neonglitch",
        "name": "Neon Glitch",
        "tagline": "Black canvas split by cyan and magenta dopamine rails.",
        "desc": "Neon Glitch takes the Direction 53 layout and pumps it with cyan voltage and magenta static.",
        "palette": ['#050505', '#00F0FF', '#FF00AA'],
        "shapes": ['logo-square', 'cyan-bar', 'magenta-dot'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #050505 0%, #0a0a12 100%);
    color: #e6f7ff;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #0d0d14; color: #e6f7ff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #00F0FF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #08080f;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #00F0FF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #7aa7b5; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #0d0d14; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #00F0FF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #00F0FF;
    color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #00F0FF, #00F0FF 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d0d14; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #00F0FF; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #08080f; color: #7aa7b5; text-align: center; }
.dopamine { width:120px;height:16px;background:linear-gradient(90deg,#00F0FF,#FF00AA);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "sunsetpop",
        "name": "Sunset Pop",
        "tagline": "Warm gradient dusk with tangerine energy.",
        "desc": "Sunset Pop soaks the Direction 53 layout in tangerine, amber, and deep plum shadows.",
        "palette": ['#2A1515', '#FF6B35', '#F7C548'],
        "shapes": ['logo-square', 'orange-bar', 'gold-pill'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #2A1515 0%, #3D1E1E 100%);
    color: #fff0e6;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #241313; color: #fff0e6;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #FF6B35;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #1f0f0f;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #FF6B35; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c98d75; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #241313; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #FF6B35;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #FF6B35;
    color: #1a0a05; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF6B35, #FF6B35 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #241313; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF6B35; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f0f0f; color: #c98d75; text-align: center; }
.dopamine { width:80px;height:80px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#F7C548,#FF6B35);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "mintchoco",
        "name": "Mint Choco",
        "tagline": "Dark chocolate softened by electric mint.",
        "desc": "Mint Choco pairs the Direction 53 grid with rich chocolate browns and a fresh mint accent.",
        "palette": ['#1F1612', '#7FFFD4', '#5C4033'],
        "shapes": ['logo-square', 'mint-stripe', 'choco-dot'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1F1612 0%, #2a1e18 100%);
    color: #f0fff7;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #261c17; color: #f0fff7;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #7FFFD4;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #16100d;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #7FFFD4; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8fb8a8; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #261c17; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #7FFFD4;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #7FFFD4;
    color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #7FFFD4, #7FFFD4 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #261c17; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #7FFFD4; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #16100d; color: #8fb8a8; text-align: center; }
.dopamine { width:100px;height:12px;background:repeating-linear-gradient(90deg,#7FFFD4,#7FFFD4 10px,transparent 10px,transparent 18px);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "lavenderhaze",
        "name": "Lavender Haze",
        "tagline": "Deep purple calm with a lavender spark.",
        "desc": "Lavender Haze drapes the Direction 53 layout in midnight violet and soft lavender highlights.",
        "palette": ['#1A1025', '#B18CFF', '#7C3AED'],
        "shapes": ['logo-square', 'lavender-bar', 'haze-glow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1A1025 0%, #241338 100%);
    color: #f3e8ff;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #1e1229; color: #f3e8ff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #B18CFF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #120a1a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #B18CFF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #9b8db5; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #1e1229; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #B18CFF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #B18CFF;
    color: #1a1025; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #B18CFF, #B18CFF 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #1e1229; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B18CFF; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #120a1a; color: #9b8db5; text-align: center; }
.dopamine { width:64px;height:64px;border-radius:12px;background:linear-gradient(135deg,#B18CFF,#7C3AED);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "olivegold",
        "name": "Olive Gold",
        "tagline": "Military olive charged with gold voltage.",
        "desc": "Olive Gold gives the Direction 53 layout an underground bunker feel with olive drab and antique gold.",
        "palette": ['#1A1A10', '#B5BD68', '#D4AF37'],
        "shapes": ['logo-square', 'olive-bar', 'gold-tick'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1A1A10 0%, #252516 100%);
    color: #f4f3d9;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #202013; color: #f4f3d9;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #B5BD68;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #11110a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #B5BD68; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #9ea36b; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #202013; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #B5BD68;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #B5BD68;
    color: #1a1a10; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #B5BD68, #B5BD68 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #202013; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B5BD68; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #11110a; color: #9ea36b; text-align: center; }
.dopamine { width:90px;height:90px;background:repeating-linear-gradient(45deg,#B5BD68,#B5BD68 4px,#202013 4px,#202013 8px);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "berrycream",
        "name": "Berry Cream",
        "tagline": "Dark berry base with a cream swirl.",
        "desc": "Berry Cream softens the Direction 53 layout with plum darkness, cream text, and a ripe berry accent.",
        "palette": ['#1F0F1A', '#D81B60', '#FFF5E6'],
        "shapes": ['logo-square', 'berry-bar', 'cream-pill'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1F0F1A 0%, #2a1522 100%);
    color: #FFF5E6;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #241220; color: #FFF5E6;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #D81B60;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #150a12;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #D81B60; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c9929e; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #241220; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #D81B60;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #D81B60;
    color: #fff5e6; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #D81B60, #D81B60 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #241220; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #D81B60; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #150a12; color: #c9929e; text-align: center; }
.dopamine { width:120px;height:14px;border-radius:7px;background:linear-gradient(90deg,#D81B60,#FFF5E6);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "tealdusk",
        "name": "Teal Dusk",
        "tagline": "Night dive into saturated teal.",
        "desc": "Teal Dusk pulls the Direction 53 layout under deep water with dark teal depths and a bright surface accent.",
        "palette": ['#0F1F1F', '#2DD4BF', '#115E59'],
        "shapes": ['logo-square', 'teal-bar', 'dusk-wave'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0F1F1F 0%, #142b2b 100%);
    color: #e6fffa;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #132525; color: #e6fffa;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #2DD4BF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #0a1616;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #2DD4BF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #6abfb5; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #132525; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #2DD4BF;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #2DD4BF;
    color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #2DD4BF, #2DD4BF 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #132525; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #2DD4BF; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0a1616; color: #6abfb5; text-align: center; }
.dopamine { width:0;height:0;border-left:40px solid transparent;border-right:40px solid transparent;border-bottom:70px solid #2DD4BF;display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "cobaltrush",
        "name": "Cobalt Rush",
        "tagline": "Midnight blue lit by cobalt lightning.",
        "desc": "Cobalt Rush runs the Direction 53 layout through a deep-blue hour with electric cobalt edges.",
        "palette": ['#0A1220', '#3B82F6', '#60A5FA'],
        "shapes": ['logo-square', 'cobalt-bar', 'rush-bolt'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0A1220 0%, #0f1a2e 100%);
    color: #e8f1ff;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #0d1626; color: #e8f1ff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #3B82F6;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #060c16;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #3B82F6; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #7ca1d8; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #0d1626; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #3B82F6;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #3B82F6;
    color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #3B82F6, #3B82F6 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d1626; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #3B82F6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #060c16; color: #7ca1d8; text-align: center; }
.dopamine { width:12px;height:80px;background:#3B82F6;box-shadow:0 0 12px #60A5FA;display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "rosewood",
        "name": "Rosewood",
        "tagline": "Polished dark wood with a rose highlight.",
        "desc": "Rosewood warms the Direction 53 layout with dark rosewood grain tones and a dusty-rose accent.",
        "palette": ['#2A1518', '#FF6F91', '#5C2A32'],
        "shapes": ['logo-square', 'rose-bar', 'wood-dot'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #2A1518 0%, #351a1e 100%);
    color: #fff0f3;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #30181c; color: #fff0f3;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #FF6F91;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #1e0f12;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #FF6F91; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c98a97; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #30181c; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #FF6F91;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #FF6F91;
    color: #2a1518; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF6F91, #FF6F91 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #30181c; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF6F91; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1e0f12; color: #c98a97; text-align: center; }
.dopamine { width:70px;height:70px;border-radius:50%;background:#FF6F91;opacity:.85;display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "limewire",
        "name": "Lime Wire",
        "tagline": "Dark forest floor wired with lime.",
        "desc": "Lime Wire roots the Direction 53 layout in dark green soil and threads it with acid lime.",
        "palette": ['#0F1A0F', '#84CC16', '#3F6212'],
        "shapes": ['logo-square', 'lime-bar', 'wire-zig'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0F1A0F 0%, #152415 100%);
    color: #f0ffe6;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #132113; color: #f0ffe6;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #84CC16;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #0a120a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #84CC16; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8fb86e; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #132113; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #84CC16;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #84CC16;
    color: #0f1a0f; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #84CC16, #84CC16 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #132113; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #84CC16; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0a120a; color: #8fb86e; text-align: center; }
.dopamine { width:100px;height:8px;background:#84CC16;border-radius:4px;box-shadow:0 0 10px #84CC16;display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "coralreef",
        "name": "Coral Reef",
        "tagline": "Deep navy reef with living coral.",
        "desc": "Coral Reef sinks the Direction 53 layout into deep navy water and lets coral accents glow.",
        "palette": ['#0F172A', '#FF7F50', '#1E293B'],
        "shapes": ['logo-square', 'coral-bar', 'reef-bubble'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0F172A 0%, #162033 100%);
    color: #fff3ef;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #121b2e; color: #fff3ef;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #FF7F50;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #0a101f;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #FF7F50; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c99a8a; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #121b2e; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #FF7F50;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #FF7F50;
    color: #0f172a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF7F50, #FF7F50 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #121b2e; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF7F50; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0a101f; color: #c99a8a; text-align: center; }
.dopamine { width:60px;height:60px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#FF7F50,#c94f28);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "icebreaker",
        "name": "Ice Breaker",
        "tagline": "Near-black frost with an ice-blue crack.",
        "desc": "Ice Breaker freezes the Direction 53 layout in near-black ice and fractures it with a cold blue accent.",
        "palette": ['#111827', '#93C5FD', '#1E3A8A'],
        "shapes": ['logo-square', 'ice-bar', 'frost-ring'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #111827 0%, #182435 100%);
    color: #eff6ff;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #151d2b; color: #eff6ff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #93C5FD;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #0c111b;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #93C5FD; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8ba6c7; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #151d2b; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #93C5FD;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #93C5FD;
    color: #111827; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #93C5FD, #93C5FD 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151d2b; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #93C5FD; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0c111b; color: #8ba6c7; text-align: center; }
.dopamine { width:90px;height:90px;border:2px solid #93C5FD;border-radius:50%;display:inline-block;margin-right:16px;position:relative; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "ambernight",
        "name": "Amber Night",
        "tagline": "Pitch black warmed by glowing amber.",
        "desc": "Amber Night keeps the Direction 53 layout in pure darkness and lights it with molten amber.",
        "palette": ['#1F140A', '#F59E0B', '#78350F'],
        "shapes": ['logo-square', 'amber-bar', 'night-glow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1F140A 0%, #2a1b0e 100%);
    color: #fffbeb;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #24170c; color: #fffbeb;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #F59E0B;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #150d06;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #F59E0B; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #cfa876; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #24170c; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #F59E0B;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #F59E0B;
    color: #1f140a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #F59E0B, #F59E0B 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #24170c; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #F59E0B; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #150d06; color: #cfa876; text-align: center; }
.dopamine { width:120px;height:14px;background:linear-gradient(90deg,#F59E0B,#78350F);border-radius:7px;display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "bubblegumgrunge",
        "name": "Bubblegum Grunge",
        "tagline": "Charcoal concrete splashed with bubblegum and cyan.",
        "desc": "Bubblegum Grunge smears the Direction 53 layout with hot pink and cyan against dirty charcoal.",
        "palette": ['#1F1A24', '#EC4899', '#22D3EE'],
        "shapes": ['logo-square', 'pink-bar', 'cyan-splash'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1F1A24 0%, #28222e 100%);
    color: #fff0f8;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #221d27; color: #fff0f8;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #EC4899;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #17131c;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #EC4899; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c996b3; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #221d27; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #EC4899;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #EC4899;
    color: #1f1a24; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #EC4899, #EC4899 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #221d27; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #EC4899; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #17131c; color: #c996b3; text-align: center; }
.dopamine { width:80px;height:80px;background:linear-gradient(135deg,#EC4899,#22D3EE);clip-path:polygon(50% 0%,100% 50%,50% 100%,0% 50%);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "forestfunk",
        "name": "Forest Funk",
        "tagline": "Dark forest floor with moss and earth sparks.",
        "desc": "Forest Funk grounds the Direction 53 layout in dark forest green and accents it with moss and stone.",
        "palette": ['#0F1F15', '#86EFAC', '#A8A29E'],
        "shapes": ['logo-square', 'moss-bar', 'stone-dot'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body {
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0F1F15 0%, #152a1d 100%);
    color: #f0fdf4;
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}
.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #12241a; color: #f0fdf4;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #86EFAC;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #0a160f;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #86EFAC; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8fb89d; margin-bottom: 40px; max-width: 560px; }
.decay-card {
    background: #12241a; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid #86EFAC;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}
.gold-btn {
    display: inline-block; padding: 14px 28px; background: #86EFAC;
    color: #0f1f15; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #86EFAC, #86EFAC 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #12241a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #86EFAC; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0a160f; color: #8fb89d; text-align: center; }
.dopamine { width:100px;height:14px;border-radius:7px;background:repeating-linear-gradient(90deg,#86EFAC,#86EFAC 8px,#A8A29E 8px,#A8A29E 16px);display:inline-block;margin-right:16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "duotone",
        "name": "Duotone Fire",
        "tagline": "High-contrast black and red duotone burn.",
        "desc": "Duotone Fire pushes the Direction 53 layout into a stark black-and-red duotone with boosted contrast.",
        "palette": ['#000000', '#FF2200', '#FFFFFF'],
        "shapes": ['logo-square', 'red-dot', 'contrast-boost'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #000; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF2200; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #000; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF2200; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; filter: contrast(1.25); }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0a0a0a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF2200; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF2200; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF2200, #FF2200 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0a0a0a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF2200; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #000; color: #777; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: #FF2200; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "noisefield",
        "name": "Noise Field",
        "tagline": "Analog noise over a red-black signal.",
        "desc": "Noise Field layers analog film grain over the Direction 53 layout for a textured, broadcast feel.",
        "palette": ['#0A0A0A', '#E42718', '#444'],
        "shapes": ['logo-square', 'noise-overlay', 'red-bar'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #f4f3ef; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.12'/%3E%3C/svg%3E"); pointer-events: none; z-index: 200; opacity: 0.35; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #f4f3ef; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #1a1a1a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #e42718; color: #1a1510; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #1a1a1a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #6b5b3e; text-align: center; }
.dopamine { width: 120px; height: 16px; background: #e42718; opacity: 0.8; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "glassmorphism",
        "name": "Glassmorphism",
        "tagline": "Frosted glass cards over a red glow.",
        "desc": "Glassmorphism turns the Direction 53 cards into translucent frosted panels with a soft red aura.",
        "palette": ['#0F0505', '#E42718', '#FFFFFF'],
        "shapes": ['logo-square', 'glass-card', 'red-glow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 20% 20%, #2a0a0a 0%, #0a0505 60%); color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(255,255,255,0.06); backdrop-filter: blur(10px); color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid rgba(228,39,24,0.85); clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 8px 32px rgba(228,39,24,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,5,5,0.6); backdrop-filter: blur(8px); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d4c5a9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(255,255,255,0.05); backdrop-filter: blur(12px); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid rgba(228,39,24,0.8); clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: rgba(228,39,24,0.9); color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, rgba(228,39,24,0.8), rgba(228,39,24,0.8) 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(255,255,255,0.05); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid rgba(228,39,24,0.6); z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,5,5,0.6); color: #a89f7e; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: rgba(228,39,24,0.25); backdrop-filter: blur(6px); border: 1px solid rgba(228,39,24,0.5); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "halftone",
        "name": "Halftone Hero",
        "tagline": "Comic-book halftone dots over red ink.",
        "desc": "Halftone Hero prints the Direction 53 layout like a comic cover with red halftone dots and bold contrast.",
        "palette": ['#F4F3EF', '#E42718', '#111'],
        "shapes": ['logo-square', 'halftone-dots', 'red-ink'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #f4f3ef; color: #111; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle, #e42718 1px, transparent 1.5px); background-size: 10px 10px; opacity: 0.12; pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #111; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #e42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #777; text-align: center; }
.dopamine { width: 80px; height: 80px; border-radius: 50%; background: radial-gradient(circle, #e42718 20%, transparent 25%); background-size: 8px 8px; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "crtlines",
        "name": "CRT Lines",
        "tagline": "Retro CRT scanlines with a red cursor.",
        "desc": "CRT Lines renders the Direction 53 layout on an old monitor with scanlines and a glowing red accent.",
        "palette": ['#050505', '#FF2A2A', '#33FF33'],
        "shapes": ['logo-square', 'scanlines', 'red-cursor'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #e8ffe8; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.4) 2px, rgba(0,0,0,0.4) 4px); pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #0a0a0a; color: #33ff33; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF2A2A; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; text-shadow: 0 0 6px #33ff33; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #080808; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF2A2A; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 0 0 8px #33ff33; }
.desc { color: #7f9e7f; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0d0d0d; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF2A2A; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF2A2A; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF2A2A, #FF2A2A 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d0d0d; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF2A2A; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #080808; color: #4a6b4a; text-align: center; }
.dopamine { width: 14px; height: 70px; background: #33ff33; box-shadow: 0 0 10px #33ff33; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "vhs",
        "name": "VHS Glitch",
        "tagline": "Tracking error colors and chromatic drift.",
        "desc": "VHS Glitch smears the Direction 53 layout with cyan/magenta drift and tracking-bar energy.",
        "palette": ['#0A0A0A', '#00F0FF', '#FF00AA'],
        "shapes": ['logo-square', 'tracking-bar', 'chromatic-drift'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #111; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #00F0FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; text-shadow: 3px 0 #FF00AA, -3px 0 #00F0FF; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00F0FF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 3px 0 #FF00AA, -3px 0 #00F0FF; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #00F0FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #00F0FF; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #00F0FF, #00F0FF 20px, #FF00AA 20px, #FF00AA 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF00AA; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #777; text-align: center; }
.dopamine { width: 120px; height: 10px; background: linear-gradient(90deg, #00F0FF, #FF00AA); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "aurora",
        "name": "Aurora Borealis",
        "tagline": "Slow-moving northern lights behind the layout.",
        "desc": "Aurora Borealis places the Direction 53 layout over a shifting green-purple-blue glow.",
        "palette": ['#0A0F14', '#2DD4BF', '#A855F7'],
        "shapes": ['logo-square', 'aurora-glow', 'shimmer-pill'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0f14; color: #e6fffa; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(120deg, #0a0f14, #2dd4bf33, #a855f733, #0a0f14); background-size: 300% 300%; animation: aurora 10s ease infinite; pointer-events: none; z-index: -1; }
@keyframes aurora { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(10,15,20,0.8); color: #e6fffa; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #2DD4BF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,20,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #2DD4BF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #9bd5c9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(10,15,20,0.75); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #2DD4BF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #2DD4BF; color: #0a0f14; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #2DD4BF, #2DD4BF 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(10,15,20,0.75); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #A855F7; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,20,0.7); color: #7aa3a8; text-align: center; }
.dopamine { width: 90px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #2DD4BF, #A855F7); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "pasteldream",
        "name": "Pastel Dream",
        "tagline": "Soft gradients for a calm dopamine hit.",
        "desc": "Pastel Dream wraps the Direction 53 layout in lavender, blush, and mint gradients for a gentle feel.",
        "palette": ['#FFF0F5', '#FFB7B2', '#B5EAD7'],
        "shapes": ['logo-square', 'pastel-pill', 'soft-glow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #fff0f5 0%, #e0f7fa 100%); color: #4a3b3b; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #4a3b3b; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFB7B2; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 6px 18px rgba(255,183,178,0.3); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF8A80; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8a7070; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFB7B2; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); box-shadow: 0 4px 14px rgba(255,183,178,0.2); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFB7B2; color: #4a3b3b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFB7B2, #FFB7B2 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; box-shadow: 0 4px 14px rgba(181,234,215,0.3); }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B5EAD7; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.7); color: #9e8585; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: linear-gradient(135deg, #FFB7B2, #B5EAD7); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "highcontrast",
        "name": "High Contrast",
        "tagline": "Black, white, and one red accent only.",
        "desc": "High Contrast strips the Direction 53 layout to pure black, pure white, and a single red accent.",
        "palette": ['#000000', '#FFFFFF', '#E42718'],
        "shapes": ['logo-square', 'red-slash', 'white-card'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #000; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #000; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; color: #fff; }
.desc { color: #ccc; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; color: #000; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #555; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 35px solid transparent; border-right: 35px solid transparent; border-bottom: 70px solid #E42718; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "neongrid",
        "name": "Neon Grid",
        "tagline": "Red square locked inside a glowing grid.",
        "desc": "Neon Grid lays a glowing red wireframe behind the Direction 53 layout.",
        "palette": ['#050505', '#E42718', '#330a0a'],
        "shapes": ['logo-square', 'neon-grid', 'red-wire'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(90deg, rgba(228,39,24,0.15) 1px, transparent 1px), linear-gradient(rgba(228,39,24,0.15) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #0a0a0a; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 0 20px rgba(228,39,24,0.4); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #080808; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0d0d0d; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d0d0d; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #080808; color: #777; text-align: center; }
.dopamine { width: 60px; height: 60px; background: #0a0a0a; border: 2px solid #E42718; box-shadow: 0 0 12px #E42718; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "sunsetbleed",
        "name": "Sunset Bleed",
        "tagline": "Warm sunset tones bleeding across the page.",
        "desc": "Sunset Bleed washes the Direction 53 layout in orange, coral, and plum gradients.",
        "palette": ['#2A0F0F', '#FF6B35', '#5C2A32'],
        "shapes": ['logo-square', 'sunset-gradient', 'coral-pill'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #2a0f0f 0%, #4a1a1a 50%, #5c2a32 100%); color: #fff5f0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(40,15,15,0.85); color: #fff5f0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF6B35; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(30,10,10,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF6B35; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #e8b8a8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(40,15,15,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF6B35; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF6B35; color: #2a0f0f; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF6B35, #FF6B35 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(40,15,15,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF6B35; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(30,10,10,0.8); color: #b5857a; text-align: center; }
.dopamine { width: 90px; height: 90px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #FF6B35, #5c2a32); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "noirfilm",
        "name": "Noir Film",
        "tagline": "Black-and-white cinema with one red accent.",
        "desc": "Noir Film turns the Direction 53 layout into a grayscale movie frame with a single red accent.",
        "palette": ['#0A0A0A', '#E42718', '#D4D4D4'],
        "shapes": ['logo-square', 'film-grain', 'red-accent'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #d4d4d4; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; filter: grayscale(100%); }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #d4d4d4; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #999; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #777; text-align: center; }
.dopamine { width: 100px; height: 12px; background: #E42718; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "popartfilter",
        "name": "Pop Art Filter",
        "tagline": "Bold primary colors and comic energy over the final layout.",
        "desc": "Pop Art gives the Direction 53 layout a Roy Lichtenstein treatment with primary colors and Ben-Day dots.",
        "palette": ['#FFFBEA', '#E42718', '#3B82F6'],
        "shapes": ['logo-square', 'ben-day-dots', 'primary-burst'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #fffbea; color: #111; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle, #3b82f6 1.5px, transparent 2px); background-size: 12px 12px; opacity: 0.12; pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #111; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; border: 3px solid #111; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; border-bottom: 3px solid #111; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; border: 3px solid #111; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: 3px solid #111; }
.grid-line { height: 4px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, #3B82F6 20px, #3B82F6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; border: 3px solid #111; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; background: #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; border-top: 3px solid #111; color: #555; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle, #E42718 25%, transparent 30%); background-size: 10px 10px; border: 3px solid #111; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "acidinvert",
        "name": "Acid Invert",
        "tagline": "Inverted acid green with a black accent.",
        "desc": "Acid Invert flips the Direction 53 layout into a toxic green world with black cutouts.",
        "palette": ['#CCFF00', '#000000', '#1A1A1A'],
        "shapes": ['logo-square', 'acid-green', 'black-cutout'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #CCFF00; color: #000; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #000; color: #CCFF00; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #fff; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #b8e600; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #000; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #333; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #000; color: #CCFF00; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #fff; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #000; color: #CCFF00; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: 2px solid #000; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #000, #000 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #000; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #fff; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #b8e600; color: #333; text-align: center; }
.dopamine { width: 80px; height: 80px; background: #000; clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "sepiawarm",
        "name": "Sepia Warm",
        "tagline": "Old photograph warmth with a red seal.",
        "desc": "Sepia Warm gives the Direction 53 layout an aged-photo feel with brown tones and a red wax seal accent.",
        "palette": ['#2A1F18', '#E42718', '#C5A059'],
        "shapes": ['logo-square', 'sepia-filter', 'wax-seal'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1f18; color: #f4e4d4; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; filter: sepia(0.4); }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3a2a20; color: #f4e4d4; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #221712; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c9b49e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3a2a20; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C5A059; color: #2a1f18; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C5A059, #C5A059 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3a2a20; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #221712; color: #a08b76; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: #E42718; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "bluemonotone",
        "name": "Blue Monotone",
        "tagline": "Every tone is a shade of blue.",
        "desc": "Blue Monotone dyes the entire Direction 53 layout in a single blue family.",
        "palette": ['#0A1628', '#3B82F6', '#93C5FD'],
        "shapes": ['logo-square', 'blue-wash', 'monotone-bar'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a1628; color: #dbeafe; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #112240; color: #dbeafe; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #3B82F6; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #081020; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #3B82F6; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; filter: saturate(0.7); }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #93c5fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #112240; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #3B82F6; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #3B82F6, #3B82F6 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #112240; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #3B82F6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #081020; color: #93c5fd; text-align: center; }
.dopamine { width: 100px; height: 12px; background: linear-gradient(90deg, #3B82F6, #93C5FD); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "holographic",
        "name": "Holographic",
        "tagline": "Iridescent shimmer over dark chrome.",
        "desc": "Holographic coats the Direction 53 layout in shifting rainbow sheen and silver type.",
        "palette": ['#0A0A0A', '#C0C0C0', '#E42718'],
        "shapes": ['logo-square', 'holo-sheen', 'chrome-text'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #e0e0e0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(120deg, rgba(255,0,85,0.15), rgba(0,240,255,0.15), rgba(120,255,120,0.15), rgba(255,0,85,0.15)); background-size: 300% 300%; animation: holo 6s linear infinite; pointer-events: none; z-index: -1; }
@keyframes holo { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #e0e0e0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; background: linear-gradient(90deg, #c0c0c0, #fff, #c0c0c0); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.desc { color: #999; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: linear-gradient(90deg, #c0c0c0, #fff, #c0c0c0); color: #0a0a0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #888; text-align: center; }
.dopamine { width: 90px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #ff0055, #00f0ff, #78ff78, #ff0055); background-size: 200% auto; animation: holo 3s linear infinite; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "fireflies",
        "name": "Fireflies",
        "tagline": "Glowing fireflies drift through a warm night.",
        "desc": "Fireflies fills the Direction 53 layout with slow-moving yellow-green glow orbs in a dark meadow.",
        "palette": ['#0F1A0F', '#ADFF2F', '#1A2E1A'],
        "shapes": ['logo-square', 'firefly-orb', 'meadow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 50% 100%, #1a2e1a 0%, #0f1a0f 60%); color: #f0ffe6; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 20% 60%, rgba(173,255,47,0.2) 0%, transparent 3%), radial-gradient(circle at 70% 30%, rgba(173,255,47,0.25) 0%, transparent 4%), radial-gradient(circle at 40% 80%, rgba(173,255,47,0.15) 0%, transparent 2%); animation: drift 8s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes drift { from { transform: translate(0,0); } to { transform: translate(20px,-15px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #162b16; color: #f0ffe6; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #ADFF2F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #121f12; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #ADFF2F; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b8e08a; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #162b16; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #ADFF2F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #ADFF2F; color: #0f1a0f; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #ADFF2F, #ADFF2F 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #162b16; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #ADFF2F; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #121f12; color: #8fb86e; text-align: center; }
.dopamine { width: 16px; height: 16px; border-radius: 50%; background: #ADFF2F; box-shadow: 0 0 12px #ADFF2F; animation: pulse 2s infinite; display: inline-block; margin-right: 16px; }
@keyframes pulse { 0%,100% { opacity: 0.6; } 50% { opacity: 1; } }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "blinkingstars",
        "name": "Blinking Stars",
        "tagline": "A navy sky full of twinkling stars.",
        "desc": "Blinking Stars places the Direction 53 layout under a deep navy sky with twinkling star dots.",
        "palette": ['#0A0F1E', '#FFE4B5', '#1E293B'],
        "shapes": ['logo-square', 'twinkle-star', 'night-sky'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(ellipse at bottom, #1e293b 0%, #0a0f1e 100%); color: #fffbeb; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background-image: radial-gradient(#ffe4b5 1px, transparent 1px), radial-gradient(#ffe4b5 1px, transparent 1px); background-size: 60px 60px, 100px 100px; background-position: 0 0, 30px 30px; opacity: 0.25; animation: twinkle 3s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes twinkle { from { opacity: 0.15; } to { opacity: 0.35; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(20,30,50,0.9); color: #fffbeb; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFE4B5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFE4B5; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c4b5fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFE4B5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFE4B5; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFE4B5, #FFE4B5 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(20,30,50,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFE4B5; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,30,0.8); color: #a5b4fc; text-align: center; }
.dopamine { width: 24px; height: 24px; background: #FFE4B5; clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); animation: twinkle 1.5s infinite alternate; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "wildflowers",
        "name": "Wildflowers",
        "tagline": "A soft meadow of colorful blooms.",
        "desc": "Wildflowers spreads a gentle green meadow behind the Direction 53 layout with scattered flower accents.",
        "palette": ['#F0FDF4', '#FF69B4', '#86EFAC'],
        "shapes": ['logo-square', 'flower', 'meadow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #f0fdf4 0%, #dcfce7 100%); color: #14532d; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 15% 85%, rgba(255,105,180,0.25) 0%, transparent 6%), radial-gradient(circle at 75% 80%, rgba(250,204,21,0.25) 0%, transparent 5%), radial-gradient(circle at 45% 90%, rgba(139,92,246,0.2) 0%, transparent 7%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #14532d; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF69B4; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF69B4; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #3f6212; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF69B4; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #86EFAC; color: #14532d; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF69B4, #FF69B4 20px, #86EFAC 20px, #86EFAC 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #86EFAC; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #3f6212; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #FF69B4 30%, #86EFAC 31%, #86EFAC 45%, #FACC15 46%, #FACC15 55%, transparent 56%); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "lavablob",
        "name": "Lava Blob",
        "tagline": "Gooey lava-lamp blobs floating behind the cards.",
        "desc": "Lava Blob gives the Direction 53 layout a classic lava lamp feel with slow purple and orange blobs.",
        "palette": ['#1A0A1A', '#FF8C00', '#8B5CF6'],
        "shapes": ['logo-square', 'blob', 'lava'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0a1a; color: #fff7ed; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 30% 30%, rgba(255,140,0,0.35) 0%, transparent 25%), radial-gradient(circle at 70% 70%, rgba(139,92,246,0.35) 0%, transparent 25%); filter: blur(30px); animation: blobmove 10s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes blobmove { from { transform: scale(1) translate(0,0); } to { transform: scale(1.2) translate(-30px, 30px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a122a; color: #fff7ed; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f0f1f; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF8C00; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d8b4fe; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a122a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #8B5CF6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF8C00, #FF8C00 20px, #8B5CF6 20px, #8B5CF6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a122a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #8B5CF6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f0f1f; color: #c4b5fd; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #FF8C00, #8B5CF6); filter: blur(2px); animation: blobmove 4s ease-in-out infinite alternate; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "woodgrain",
        "name": "Wood Grain",
        "tagline": "Polished timber and warm copper hardware.",
        "desc": "Wood Grain gives the Direction 53 layout a rich timber surface with copper accents.",
        "palette": ['#3E2723', '#B87333', '#8D6E63'],
        "shapes": ['logo-square', 'timber', 'copper'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #3e2723; color: #efebe9; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(90deg, rgba(0,0,0,0.1) 0px, transparent 2px, rgba(255,255,255,0.05) 4px, transparent 8px); background-size: 60px 100%; opacity: 0.4; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #4e342e; color: #efebe9; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #B87333; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #2d1b18; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #B87333; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d7ccc8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #4e342e; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #B87333; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #B87333; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #B87333, #B87333 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #4e342e; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B87333; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #2d1b18; color: #a1887f; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #B87333, #5d4037); box-shadow: inset 0 0 10px rgba(0,0,0,0.5); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "brushedmetal",
        "name": "Brushed Metal",
        "tagline": "Cool steel with machined highlights.",
        "desc": "Brushed Metal turns the Direction 53 layout into a sheet of steel with a machined accent.",
        "palette": ['#212121', '#C0C0C0', '#607D8B'],
        "shapes": ['logo-square', 'steel', 'rivet'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #424242 0%, #212121 100%); color: #eceff1; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255,255,255,0.05) 2px, rgba(255,255,255,0.05) 4px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #616161; color: #eceff1; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #212121; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b0bec5; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #424242; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #212121; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #424242; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #C0C0C0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #212121; color: #90a4ae; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #E0E0E0, #616161); box-shadow: inset 0 0 8px rgba(0,0,0,0.5); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "glassblocks",
        "name": "Glass Blocks",
        "tagline": "Frosted glass bricks with cool light.",
        "desc": "Glass Blocks stacks translucent panels behind the Direction 53 layout with a soft blue glow.",
        "palette": ['#0A1A2E', '#87CEEB', '#1E3A8A'],
        "shapes": ['logo-square', 'glass-brick', 'blue-light'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a1a2e; color: #e0f2fe; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(90deg, rgba(135,206,235,0.1) 1px, transparent 1px), linear-gradient(rgba(135,206,235,0.1) 1px, transparent 1px); background-size: 80px 80px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(135,206,235,0.1); backdrop-filter: blur(8px); color: #e0f2fe; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #87CEEB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,26,46,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #87CEEB; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #bae6fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(135,206,235,0.1); backdrop-filter: blur(8px); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #87CEEB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #87CEEB; color: #0a1a2e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #87CEEB, #87CEEB 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(135,206,235,0.1); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #87CEEB; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,26,46,0.8); color: #bae6fd; text-align: center; }
.dopamine { width: 70px; height: 70px; background: rgba(135,206,235,0.2); backdrop-filter: blur(4px); border: 1px solid #87CEEB; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "shutters",
        "name": "Shutters",
        "tagline": "Sunlight cuts through window shutters.",
        "desc": "Shutters casts warm golden slats of light across the Direction 53 layout.",
        "palette": ['#2A1B0A', '#FFD700', '#8B4513'],
        "shapes": ['logo-square', 'shutter-slat', 'sunbeam'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1b0a; color: #fff8e1; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(75deg, rgba(255,215,0,0.15) 0px, rgba(255,215,0,0.15) 20px, transparent 20px, transparent 60px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3e2723; color: #fff8e1; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFD700; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f1408; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFD700; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #ffe082; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3e2723; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFD700; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFD700; color: #2a1b0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFD700, #FFD700 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3e2723; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFD700; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f1408; color: #c9a66b; text-align: center; }
.dopamine { width: 100px; height: 10px; background: #FFD700; box-shadow: 0 0 10px #FFD700; transform: rotate(-10deg); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "candlelight",
        "name": "Candlelight",
        "tagline": "Warm amber flicker in a dark room.",
        "desc": "Candlelight gives the Direction 53 layout a cozy, flickering amber glow.",
        "palette": ['#1A0F0A', '#FFAE42', '#5D4037'],
        "shapes": ['logo-square', 'flame', 'flicker'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0f0a; color: #fff3e0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 10%; left: 30%; width: 300px; height: 300px; border-radius: 50%; background: radial-gradient(circle, rgba(255,174,66,0.25) 0%, transparent 60%); animation: flicker 0.1s infinite alternate; pointer-events: none; z-index: -1; }
@keyframes flicker { from { opacity: 0.8; transform: scale(1); } to { opacity: 1; transform: scale(1.05); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a1a10; color: #fff3e0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFAE42; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1a0f0a; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFAE42; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #ffcc80; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a1a10; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFAE42; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFAE42; color: #1a0f0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFAE42, #FFAE42 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a1a10; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFAE42; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1a0f0a; color: #c7a07a; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-bottom: 60px solid #FFAE42; border-radius: 50%; filter: drop-shadow(0 0 8px #FFAE42); animation: flicker 0.2s infinite alternate; display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "moonlight",
        "name": "Moonlight",
        "tagline": "Silver moon glow on a dark blue canvas.",
        "desc": "Moonlight washes the Direction 53 layout in cool silver moonbeams.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['logo-square', 'crescent', 'moonbeam'],
        "css": """


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
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "rainonwindow",
        "name": "Rain on Window",
        "tagline": "Droplets sliding down dark glass.",
        "desc": "Rain on Window puts the Direction 53 layout behind a wet pane with sliding raindrops.",
        "palette": ['#0F172A', '#5F9EA0', '#334155'],
        "shapes": ['logo-square', 'raindrop', 'wet-glass'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); color: #e2e8f0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.08) 0%, transparent 3%), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.06) 0%, transparent 2%), radial-gradient(circle at 50% 80%, rgba(255,255,255,0.07) 0%, transparent 4%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(30,41,59,0.9); color: #e2e8f0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #5F9EA0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(15,23,42,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #5F9EA0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #94a3b8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(30,41,59,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #5F9EA0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #5F9EA0; color: #0f172a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #5F9EA0, #5F9EA0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(30,41,59,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #5F9EA0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(15,23,42,0.8); color: #94a3b8; text-align: center; }
.dopamine { width: 20px; height: 30px; border-radius: 50%; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); box-shadow: inset 0 -5px 5px rgba(255,255,255,0.2); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "sunbeams",
        "name": "Sunbeams",
        "tagline": "Golden light rays cutting through dust.",
        "desc": "Sunbeams shoots warm light rays across the Direction 53 layout.",
        "palette": ['#2A1B0A', '#FFFACD', '#DAA520'],
        "shapes": ['logo-square', 'ray', 'dust'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1b0a; color: #fffbe6; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: -50%; left: -20%; width: 140vw; height: 140vh; background: conic-gradient(from 0deg at 50% 0%, transparent 0deg, rgba(255,250,205,0.1) 20deg, transparent 40deg, rgba(255,250,205,0.08) 60deg, transparent 80deg); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3e2c14; color: #fffbe6; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFFACD; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f1508; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFFACD; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #f3e5ab; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3e2c14; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFFACD; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #DAA520; color: #2a1b0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFFACD, #FFFACD 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3e2c14; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #DAA520; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f1508; color: #c9a66b; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-bottom: 100px solid rgba(255,250,205,0.3); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "confetti",
        "name": "Confetti",
        "tagline": "Colorful paper falling in celebration.",
        "desc": "Confetti rains bright colored paper over the Direction 53 layout.",
        "palette": ['#FFFFFF', '#FF00FF', '#00BFFF'],
        "shapes": ['logo-square', 'confetti-piece', 'celebration'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #fff; color: #222; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(45deg, rgba(255,0,255,0.1) 25%, transparent 25%, transparent 50%, rgba(0,191,255,0.1) 50%, rgba(0,191,255,0.1) 75%, transparent 75%); background-size: 40px 40px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #f8f8f8; color: #222; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF00FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00BFFF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF00FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #00BFFF; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF00FF, #FF00FF 20px, #00BFFF 20px, #00BFFF 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF00FF; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #777; text-align: center; }
.dopamine { width: 16px; height: 8px; background: #FF00FF; transform: rotate(15deg); box-shadow: 20px 10px 0 #00BFFF, -10px 25px 0 #FFD700; display: inline-block; margin-right: 40px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "neonlightsign",
        "name": "Neon Light Sign",
        "tagline": "A pink neon tube hums behind the cards.",
        "desc": "Neon Light Sign gives the Direction 53 layout a buzzing pink neon glow against dark brick.",
        "palette": ['#1A0A14', '#FF10F0', '#2A1B1B'],
        "shapes": ['logo-square', 'neon-tube', 'brick'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0a14; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, rgba(255,16,240,0.05) 0px, transparent 2px, transparent 80px, rgba(255,16,240,0.05) 82px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a1224; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF10F0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 0 20px rgba(255,16,240,0.3); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f0f1a; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF10F0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 0 0 12px #FF10F0; }
.desc { color: #f9a8d4; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a1224; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF10F0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF10F0; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF10F0, #FF10F0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a1224; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF10F0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f0f1a; color: #f9a8d4; text-align: center; }
.dopamine { width: 100px; height: 8px; border-radius: 4px; background: #FF10F0; box-shadow: 0 0 12px #FF10F0; animation: buzz 1.5s infinite alternate; display: inline-block; margin-right: 16px; }
@keyframes buzz { from { opacity: 0.8; } to { opacity: 1; } }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "cherryblossom",
        "name": "Cherry Blossom",
        "tagline": "Pink petals drift across a soft sky.",
        "desc": "Cherry Blossom showers the Direction 53 layout with falling pink petals.",
        "palette": ['#FFF0F5', '#FFB7C5', '#FBCFE8'],
        "shapes": ['logo-square', 'petal', 'blossom'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #fff0f5 0%, #fce7f3 100%); color: #831843; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 20% 20%, #ffb7c5 0%, transparent 4%), radial-gradient(circle at 70% 40%, #fbcfe8 0%, transparent 3%), radial-gradient(circle at 40% 70%, #ffb7c5 0%, transparent 5%); opacity: 0.6; animation: fall 8s linear infinite; pointer-events: none; z-index: -1; }
@keyframes fall { 0% { transform: translateY(-20px) rotate(0deg); } 100% { transform: translateY(20px) rotate(10deg); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #831843; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFB7C5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #DB2777; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #be185d; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFB7C5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFB7C5; color: #831843; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFB7C5, #FFB7C5 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFB7C5; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #be185d; text-align: center; }
.dopamine { width: 30px; height: 30px; border-radius: 50% 0 50% 50%; background: #FFB7C5; transform: rotate(-45deg); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "tropicalfruit",
        "name": "Tropical Fruit",
        "tagline": "Juicy citrus and berry colors.",
        "desc": "Tropical Fruit squeezes bright orange, lime, and berry juice into the Direction 53 layout.",
        "palette": ['#FFFBEB', '#FF8C00', '#84CC16'],
        "shapes": ['logo-square', 'citrus', 'juice'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 10% 20%, #fffbeb 0%, #fef3c7 100%); color: #451a03; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 80% 80%, rgba(255,140,0,0.15) 0%, transparent 25%), radial-gradient(circle at 20% 80%, rgba(132,204,22,0.15) 0%, transparent 25%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #451a03; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #84CC16; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #92400e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #84CC16; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF8C00, #FF8C00 20px, #84CC16 20px, #84CC16 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #84CC16; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #92400e; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: repeating-conic-gradient(#FF8C00 0deg 10deg, #fff 10deg 20deg, #84CC16 20deg 30deg); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "northernlights",
        "name": "Northern Lights",
        "tagline": "Green and violet aurora waves.",
        "desc": "Northern Lights paints the Direction 53 layout with slow aurora ribbons.",
        "palette": ['#0A0F14', '#00FF7F', '#8B5CF6'],
        "shapes": ['logo-square', 'aurora-ribbon', 'wave'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0f14; color: #e6fffa; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(ellipse at 50% 100%, rgba(0,255,127,0.25) 0%, transparent 40%), radial-gradient(ellipse at 30% 100%, rgba(139,92,246,0.2) 0%, transparent 35%); filter: blur(20px); animation: aurora 8s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes aurora { 0% { transform: scaleY(1) translateY(0); } 100% { transform: scaleY(1.1) translateY(-20px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(10,20,30,0.9); color: #e6fffa; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #00FF7F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,20,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00FF7F; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a7f3d0; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(10,20,30,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #00FF7F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #8B5CF6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #00FF7F, #00FF7F 20px, #8B5CF6 20px, #8B5CF6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(10,20,30,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #8B5CF6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,20,0.8); color: #a7f3d0; text-align: center; }
.dopamine { width: 100px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #00FF7F, #8B5CF6); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "citylights",
        "name": "City Lights",
        "tagline": "Bokeh skyline at night.",
        "desc": "City Lights blurs a distant downtown skyline behind the Direction 53 layout.",
        "palette": ['#0A0A0A', '#FFA500', '#3B82F6'],
        "shapes": ['logo-square', 'bokeh', 'skyline'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; bottom: 0; left: 0; right: 0; height: 50vh; background: radial-gradient(circle at 20% 80%, rgba(255,165,0,0.3) 0%, transparent 15%), radial-gradient(circle at 50% 70%, rgba(59,130,246,0.25) 0%, transparent 12%), radial-gradient(circle at 80% 85%, rgba(255,255,255,0.2) 0%, transparent 10%); filter: blur(15px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFA500; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFA500; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #fde68a; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #1a1a1a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFA500; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFA500, #FFA500 20px, #3B82F6 20px, #3B82F6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #1a1a1a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #3B82F6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #93c5fd; text-align: center; }
.dopamine { width: 20px; height: 20px; border-radius: 50%; background: #FFA500; box-shadow: 0 0 12px #FFA500, 25px 10px 0 #3B82F6, -15px 20px 0 #fff; filter: blur(2px); display: inline-block; margin-right: 40px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "sanddunes",
        "name": "Sand Dunes",
        "tagline": "Warm desert curves and shadows.",
        "desc": "Sand Dunes shapes the Direction 53 layout from warm desert gradients and soft shadows.",
        "palette": ['#EDC9AF', '#D2691E', '#F4A460'],
        "shapes": ['logo-square', 'dune', 'desert'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #edc9af 0%, #d2691e 100%); color: #4a2511; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; bottom: 0; left: 0; right: 0; height: 60vh; background: radial-gradient(ellipse at 30% 100%, rgba(244,164,96,0.5) 0%, transparent 50%), radial-gradient(ellipse at 70% 100%, rgba(210,105,30,0.4) 0%, transparent 50%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #f5e6d3; color: #4a2511; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #D2691E; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(245,230,211,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #D2691E; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #7c3d16; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #f5e6d3; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #D2691E; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #D2691E; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #D2691E, #D2691E 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #f5e6d3; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #F4A460; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(245,230,211,0.8); color: #7c3d16; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 60px solid transparent; border-right: 60px solid transparent; border-bottom: 30px solid rgba(210,105,30,0.4); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "watercolor",
        "name": "Watercolor",
        "tagline": "Soft paint washes bleeding into each other.",
        "desc": "Watercolor softens the Direction 53 layout with pastel washes and gentle splashes.",
        "palette": ['#FDF2F8', '#9370DB', '#87CEFA'],
        "shapes": ['logo-square', 'paint-splash', 'wash'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 20% 30%, rgba(147,112,219,0.2) 0%, transparent 30%), radial-gradient(circle at 80% 70%, rgba(135,206,250,0.25) 0%, transparent 35%), #fdf2f8; color: #4c1d95; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #4c1d95; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #9370DB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #9370DB; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #6d28d9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #9370DB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #87CEFA; color: #1e3a8a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #9370DB, #9370DB 20px, #87CEFA 20px, #87CEFA 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #87CEFA; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.7); color: #6d28d9; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #9370DB 30%, #87CEFA 70%); filter: blur(2px); display: inline-block; margin-right: 16px; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
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
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>

        """
    },
    {
        "id": "qrkblock",
        "name": "QR K Block",
        "tagline": "The letter K built from QR modules.",
        "desc": "The Korvia wordmark with the K constructed from black-and-white QR code blocks.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'qr-k', 'modules'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; display: inline-block; }
.logo-wordmark .k { display: inline-block; width: 1.1em; height: 1.1em; background: #f8fafc; position: relative; vertical-align: middle; margin-right: 0.1em; }
.logo-wordmark .k::before { content: ""; position: absolute; inset: 0; background-image: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrofinder",
        "name": "QR Finder O",
        "tagline": "The O in Korvia becomes a QR finder pattern.",
        "desc": "A wordmark where the letter O is replaced by a QR code finder square.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'finder-o', 'square'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark .o { display: inline-block; width: 0.85em; height: 0.85em; border: 4px solid #f8fafc; border-radius: 0; position: relative; vertical-align: middle; margin: 0 0.05em; }
.logo-wordmark .o::before { content: ""; position: absolute; inset: 6px; border: 3px solid #f8fafc; }
.logo-wordmark .o::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 12px; height: 12px; background: #f8fafc; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "pixelkorvia",
        "name": "Pixel Korvia",
        "tagline": "Korvia rendered as crisp QR pixels.",
        "desc": "The wordmark uses a pixel-grid font treatment reminiscent of QR module arrays.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'pixel', 'grid'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; text-shadow: 4px 4px 0 rgba(192,192,192,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrcorners",
        "name": "QR Corners",
        "tagline": "Three QR finder corners frame the wordmark.",
        "desc": "The Korvia wordmark is framed by the three signature QR finder-pattern corners.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'corners', 'frame'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 18px; }
.logo-wrap::before, .logo-wrap::after, .logo-wrap .corner-br { content: ""; position: absolute; width: 28px; height: 28px; border-color: #C0C0C0; border-style: solid; }
.logo-wrap::before { top: 0; left: 0; border-width: 4px 0 0 4px; }
.logo-wrap::after { top: 0; right: 0; border-width: 4px 4px 0 0; }
.logo-wrap .corner-br { bottom: 0; right: 0; border-width: 0 4px 4px 0; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "scanframe",
        "name": "Scan Frame",
        "tagline": "A phone-style QR scanner frame around Korvia.",
        "desc": "The wordmark sits inside a pulsating QR scanner frame with corner brackets.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'scanner', 'frame'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 24px 48px; border: 1px dashed rgba(192,192,192,0.4); }
.logo-wrap::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: #C0C0C0; animation: scan 2.5s ease-in-out infinite; }
@keyframes scan { 0%,100% { transform: translateY(0); opacity: 0.3; } 50% { transform: translateY(80px); opacity: 1; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "dotmatrix",
        "name": "Dot Matrix",
        "tagline": "Korvia dotted like a thermal QR printer.",
        "desc": "The wordmark is built from a dense dot matrix, evoking QR code modules.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'dots', 'matrix'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; }
.logo-wordmark::after { content: ""; position: absolute; inset: -10px; background: radial-gradient(circle, rgba(192,192,192,0.3) 1px, transparent 1px); background-size: 6px 6px; opacity: 0.4; pointer-events: none; mask-image: linear-gradient(90deg, transparent, black 10%, black 90%, transparent); -webkit-mask-image: linear-gradient(90deg, transparent, black 10%, black 90%, transparent); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrmosaic",
        "name": "QR Mosaic",
        "tagline": "The letters emerge from a mosaic of QR modules.",
        "desc": "A mosaic of small squares forms the negative space around the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'mosaic', 'modules'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 20px 40px; background: linear-gradient(90deg, transparent 0%, rgba(20,30,50,0.85) 20%, rgba(20,30,50,0.85) 80%, transparent 100%); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wrap::before { content: ""; position: absolute; inset: 0; background-image: repeating-linear-gradient(0deg, rgba(192,192,192,0.15) 0px, rgba(192,192,192,0.15) 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, rgba(192,192,192,0.15) 0px, rgba(192,192,192,0.15) 4px, transparent 4px, transparent 8px); pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "stylizedk",
        "name": "Stylized K",
        "tagline": "A single lettermark K made of QR modules.",
        "desc": "A bold K lettermark built entirely from QR-style squares, paired with a clean Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lettermark', 'k', 'modules'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-mark { display: inline-block; width: 1.2em; height: 1.2em; background: #f8fafc; vertical-align: middle; margin-right: 0.15em; position: relative; }
.logo-mark::before { content: ""; position: absolute; inset: 0; background: #0a0f1e; clip-path: polygon(20% 0%, 40% 0%, 40% 40%, 70% 0%, 100% 0%, 55% 55%, 100% 100%, 70% 100%, 40% 60%, 40% 100%, 20% 100%, 20% 20%, 0% 40%, 0% 20%); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "concentricqr",
        "name": "Concentric QR",
        "tagline": "Concentric square rings echo QR finder patterns.",
        "desc": "The Korvia wordmark is paired with a concentric square ring mark inspired by QR finder patterns.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'rings', 'finder'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 64px; height: 64px; border: 3px solid #f8fafc; display: grid; place-items: center; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 8px; border: 2px solid #f8fafc; }
.logo-mark::after { content: ""; width: 14px; height: 14px; background: #f8fafc; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "fragmentedqr",
        "name": "Fragmented QR",
        "tagline": "Korvia with fragmented QR blocks breaking away.",
        "desc": "The wordmark features small QR-style squares that appear to fragment and scatter.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'fragments', 'scatter'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.fragment { position: absolute; width: 8px; height: 8px; background: #C0C0C0; }
.fragment:nth-child(1) { top: 10%; right: -20px; }
.fragment:nth-child(2) { top: 40%; right: -35px; }
.fragment:nth-child(3) { bottom: 15%; right: -18px; }
.fragment:nth-child(4) { top: 20%; left: -25px; }
.fragment:nth-child(5) { bottom: 25%; left: -30px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "scanline",
        "name": "Scan Line",
        "tagline": "A horizontal laser scan line crosses Korvia.",
        "desc": "A glowing horizontal scan line moves across the wordmark like a QR scanner.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'scan', 'laser'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.logo-wordmark::after { content: ""; position: absolute; left: 0; right: 0; height: 2px; background: #C0C0C0; box-shadow: 0 0 10px #C0C0C0; animation: scanline 2s ease-in-out infinite; }
@keyframes scanline { 0%,100% { top: 0; } 50% { top: 100%; } }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrspacing",
        "name": "QR Spacing",
        "tagline": "The letters are spaced by tiny QR modules.",
        "desc": "Small square modules separate the letters of Korvia, creating a QR-like rhythm.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'spacing', 'modules'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.logo-wordmark::after { content: ""; display: block; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 6px, transparent 6px, transparent 12px); margin-top: 8px; opacity: 0.7; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "finderdots",
        "name": "Finder Dots",
        "tagline": "The i-dots become QR finder squares.",
        "desc": "A subtle wordmark treatment where the dot of the i is a QR finder pattern square.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'dots', 'finder'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark .dot { display: inline-block; width: 0.18em; height: 0.18em; background: #f8fafc; vertical-align: super; margin-left: -0.05em; position: relative; }
.logo-wordmark .dot::before { content: ""; position: absolute; inset: 3px; border: 1px solid #0a0f1e; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "modulargrid",
        "name": "Modular Grid",
        "tagline": "Each letter sits on a modular QR grid.",
        "desc": "The Korvia letters each rest inside their own square module cell.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'grid', 'cells'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark span { display: inline-block; width: 1.1em; height: 1.1em; line-height: 1.1em; text-align: center; border: 1px solid rgba(192,192,192,0.3); margin: 0 2px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrshadow",
        "name": "QR Shadow",
        "tagline": "The Korvia wordmark casts a QR module shadow.",
        "desc": "A clean wordmark with a shadow made of QR-style squares.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'shadow', 'squares'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; text-shadow: 8px 8px 0 rgba(192,192,192,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrshimmer",
        "name": "QR Shimmer",
        "tagline": "QR modules shimmer across the wordmark.",
        "desc": "The Korvia wordmark has a subtle animated shimmer of QR modules moving across it.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'shimmer', 'animation'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.logo-wordmark::before { content: ""; position: absolute; inset: -10px; background: repeating-linear-gradient(90deg, transparent, transparent 10px, rgba(192,192,192,0.15) 10px, rgba(192,192,192,0.15) 14px); animation: shimmer 3s linear infinite; pointer-events: none; }
@keyframes shimmer { from { transform: translateX(-20px); } to { transform: translateX(20px); } }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qr3d",
        "name": "3D QR Block",
        "tagline": "A dimensional QR block sits beside Korvia.",
        "desc": "A 3D-style QR cube mark paired with the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'cube', '3d'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 60px; height: 60px; background: #f8fafc; position: relative; transform: rotateX(15deg) rotateY(-15deg); box-shadow: 8px 8px 0 rgba(192,192,192,0.3); flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 6px; background: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 5px, transparent 5px, transparent 10px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 5px, transparent 5px, transparent 10px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "circularqr",
        "name": "Circular QR",
        "tagline": "QR modules arranged in a circle around Korvia.",
        "desc": "A circular ring of QR-style modules surrounds the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'circle', 'ring'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 30px; }
.logo-wrap::before { content: ""; position: absolute; inset: 0; border-radius: 50%; border: 2px dashed rgba(192,192,192,0.4); }
.logo-wrap::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 90%; border-radius: 50%; border: 8px dotted rgba(192,192,192,0.5); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; z-index: 1; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrmerge",
        "name": "QR Merge",
        "tagline": "The QR pattern merges into the Korvia letterforms.",
        "desc": "A gradient transition where QR modules dissolve into the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'merge', 'transition'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; background: linear-gradient(90deg, rgba(192,192,192,0.2) 0%, #f8fafc 30%, #f8fafc 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "minimalqr",
        "name": "Minimal QR",
        "tagline": "The smallest possible QR nod in a clean wordmark.",
        "desc": "A minimal, refined Korvia wordmark with a single subtle QR square accent.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'minimal', 'square'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: 0.12em; text-transform: uppercase; }
.logo-wordmark::after { content: ""; display: inline-block; width: 10px; height: 10px; background: #C0C0C0; margin-left: 8px; vertical-align: super; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrtag",
        "name": "QR Tag",
        "tagline": "Korvia sits on a price-tag-shaped QR plate.",
        "desc": "The wordmark is paired with a QR code tag shape reminiscent of retail and hospitality labels.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'tag', 'label'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 56px; height: 80px; background: #f8fafc; clip-path: polygon(0 0, 100% 0, 100% 75%, 50% 100%, 0 75%); position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; top: 8px; left: 50%; transform: translateX(-50%); width: 8px; height: 8px; border-radius: 50%; background: #0a0f1e; }
.logo-mark::after { content: ""; position: absolute; top: 24px; left: 8px; right: 8px; bottom: 18px; background: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrbadge",
        "name": "QR Badge",
        "tagline": "A circular badge with a QR pattern holds the K.",
        "desc": "A circular badge containing a QR pattern and the letter K, next to the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'badge', 'circle'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 70px; height: 70px; border-radius: 50%; background: #f8fafc; display: grid; place-items: center; font-family: 'Cinzel', serif; font-size: 1.8rem; font-weight: 700; color: #0a0f1e; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 6px; border-radius: 50%; border: 2px dashed #0a0f1e; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "binaryqr",
        "name": "Binary QR",
        "tagline": "Binary code streams into the Korvia wordmark.",
        "desc": "A tech-forward wordmark with binary digits and QR modules flowing behind the text.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'binary', 'stream'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; }
.logo-wrap::before { content: "10110010 01101011 01101111 01110010 01110110 01101001 01100001"; position: absolute; top: -14px; left: 0; font-family: monospace; font-size: 0.55rem; color: rgba(192,192,192,0.35); letter-spacing: 0.1em; white-space: nowrap; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrpath",
        "name": "QR Path",
        "tagline": "A path of QR modules leads to Korvia.",
        "desc": "Small QR squares form a dotted path leading into the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'path', 'trail'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding-left: 50px; }
.logo-wrap::before { content: ""; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 40px; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 6px, transparent 6px, transparent 12px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrstack",
        "name": "QR Stack",
        "tagline": "Stacked QR squares form a monogram beside Korvia.",
        "desc": "A monogram of stacked QR squares sits next to the Korvia wordmark.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'stack', 'monogram'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { display: grid; grid-template-columns: repeat(2, 18px); gap: 4px; flex-shrink: 0; }
.logo-mark span { width: 18px; height: 18px; background: #f8fafc; }
.logo-mark span:nth-child(2), .logo-mark span:nth-child(3) { background: rgba(192,192,192,0.4); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrkmonogram",
        "name": "QR K Monogram",
        "tagline": "A monogram where K and QR become one shape.",
        "desc": "A compact monogram combining the letter K with a QR finder pattern.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['monogram', 'k', 'finder'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 64px; height: 64px; border: 4px solid #f8fafc; display: grid; place-items: center; font-family: 'Cinzel', serif; font-size: 1.6rem; font-weight: 700; color: #f8fafc; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 8px; border: 3px solid #f8fafc; }
.logo-mark::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 12px; height: 12px; background: #f8fafc; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qroutline",
        "name": "QR Outline",
        "tagline": "The Korvia letters are outlined with QR module corners.",
        "desc": "An outline wordmark where each letter is traced by QR-style corner brackets.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['wordmark', 'outline', 'corners'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; -webkit-text-stroke: 1px #f8fafc; color: transparent; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "stackedtagline",
        "name": "Stacked Tagline",
        "tagline": "Korvia sits above Karibu, tukuhudumie in a clean stack.",
        "desc": "A vertical lockup with Korvia wordmark above the Swahili tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'stacked', 'tagline'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; display: inline-block; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: clamp(0.9rem, 2.5vw, 1.3rem); letter-spacing: 0.25em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; }
.logo-lockup::after { content: ""; display: block; width: 60px; height: 2px; background: #C0C0C0; margin: 16px auto 0; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "horizontallockup",
        "name": "Horizontal Lockup",
        "tagline": "Korvia and tagline sit on one line.",
        "desc": "A horizontal logo lockup with the tagline separated by a vertical rule.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'horizontal', 'rule'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; align-items: center; gap: 20px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-rule { width: 2px; height: 40px; background: #C0C0C0; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase; color: #94a3b8; line-height: 1.4; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "framedlockup",
        "name": "Framed Lockup",
        "tagline": "Korvia and tagline inside a QR-corner frame.",
        "desc": "The logo and tagline are enclosed by QR finder-pattern corner brackets.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'frame', 'corners'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 50px; }
.logo-lockup::before, .logo-lockup::after, .logo-lockup .corner-br { content: ""; position: absolute; width: 24px; height: 24px; border-color: #C0C0C0; border-style: solid; }
.logo-lockup::before { top: 0; left: 0; border-width: 4px 0 0 4px; }
.logo-lockup::after { top: 0; right: 0; border-width: 4px 4px 0 0; }
.logo-lockup .corner-br { bottom: 0; right: 0; border-width: 0 4px 4px 0; }
.logo-lockup .corner-bl { position: absolute; bottom: 0; left: 0; width: 24px; height: 24px; border-color: #C0C0C0; border-style: solid; border-width: 0 0 4px 4px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "badgelockup",
        "name": "Badge Lockup",
        "tagline": "Korvia inside a circular badge with tagline ribbon.",
        "desc": "A circular badge containing the Korvia wordmark with a ribbon-style tagline below.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'badge', 'ribbon'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; flex-direction: column; align-items: center; }
.logo-badge { width: 160px; height: 160px; border-radius: 50%; border: 2px solid #C0C0C0; display: grid; place-items: center; position: relative; }
.logo-badge::before { content: ""; position: absolute; inset: 8px; border-radius: 50%; border: 1px dashed rgba(192,192,192,0.5); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: 1.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }
.logo-ribbon { background: #C0C0C0; color: #0a0f1e; padding: 8px 24px; font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; margin-top: -14px; z-index: 1; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "twolinetagline",
        "name": "Two-Line Tagline",
        "tagline": "Karibu on one line, tukuhudumie on the next.",
        "desc": "The tagline is split into two lines for a more dramatic lockup.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'two-line', 'dramatic'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; margin-bottom: 12px; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: clamp(0.8rem, 2vw, 1.1rem); letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; display: block; }
.logo-tagline span { display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrfullframe",
        "name": "QR Full Frame",
        "tagline": "The entire logo lockup sits inside a QR scanner frame.",
        "desc": "A full scanner frame with corner brackets encloses the Korvia wordmark and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'scanner', 'frame'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 40px 60px; border: 1px dashed rgba(192,192,192,0.4); }
.logo-lockup::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: #C0C0C0; animation: scan 2.5s ease-in-out infinite; }
@keyframes scan { 0%,100% { transform: translateY(0); opacity: 0.3; } 50% { transform: translateY(110px); opacity: 1; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; text-align: center; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "monogramlockup",
        "name": "Monogram Lockup",
        "tagline": "A K monogram anchors the full Korvia wordmark and tagline.",
        "desc": "A K monogram sits above or beside the full Korvia name and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'monogram', 'k'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; align-items: center; gap: 20px; }
.logo-monogram { width: 80px; height: 80px; background: #f8fafc; color: #0a0f1e; font-family: 'Cinzel', serif; font-size: 2.5rem; font-weight: 700; display: grid; place-items: center; }
.logo-text { display: flex; flex-direction: column; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2rem, 6vw, 4rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 4px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "swahilifirst",
        "name": "Swahili First",
        "tagline": "Karibu, tukuhudumie leads, Korvia follows.",
        "desc": "A reverse lockup where the Swahili tagline is primary and Korvia is secondary.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'swahili', 'reverse'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-tagline { font-family: 'Cinzel', serif; font-size: clamp(1.4rem, 4vw, 2.5rem); font-weight: 400; letter-spacing: 0.12em; text-transform: uppercase; color: #C0C0C0; display: block; margin-bottom: 8px; }
.logo-wordmark { font-family: 'Inter', sans-serif; font-size: clamp(0.9rem, 2.5vw, 1.2rem); letter-spacing: 0.4em; text-transform: uppercase; color: #94a3b8; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrruled",
        "name": "QR Ruled",
        "tagline": "Ruled lines connect the wordmark and tagline like a form.",
        "desc": "A technical, ruled layout with Korvia above and tagline below, connected by vertical lines.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'ruled', 'technical'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-grid; grid-template-columns: 1fr auto 1fr; gap: 12px; align-items: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; grid-column: 1 / -1; text-align: center; border-bottom: 1px solid rgba(192,192,192,0.4); padding-bottom: 12px; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: #94a3b8; grid-column: 1 / -1; text-align: center; padding-top: 8px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrmicro",
        "name": "QR Micro Tagline",
        "tagline": "The tagline is rendered in tiny QR modules.",
        "desc": "Korvia in full size with the tagline spelled out in small square modules below.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'micro', 'modules'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.65rem; letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; }
.logo-tagline::after { content: ""; display: block; width: 100%; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 4px, transparent 4px, transparent 8px); margin-top: 8px; opacity: 0.5; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "ticketlockup",
        "name": "Ticket Lockup",
        "tagline": "Korvia and tagline on a hospitality ticket shape.",
        "desc": "A ticket-shaped container holds the Korvia wordmark and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'ticket', 'hospitality'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; background: rgba(20,30,50,0.85); border: 1px solid rgba(192,192,192,0.3); padding: 24px 48px; position: relative; }
.logo-lockup::before, .logo-lockup::after { content: ""; position: absolute; top: 50%; transform: translateY(-50%); width: 20px; height: 20px; border-radius: 50%; background: #0a0f1e; border: 1px solid rgba(192,192,192,0.3); }
.logo-lockup::before { left: -10px; }
.logo-lockup::after { right: -10px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; text-align: center; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "africanpattern",
        "name": "East African Pattern",
        "tagline": "A subtle kanga-pattern accent under the lockup.",
        "desc": "Korvia wordmark and tagline with a subtle East African geometric pattern band.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'pattern', 'african'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-pattern { height: 12px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 8px, transparent 8px, transparent 16px, #C0C0C0 16px, #C0C0C0 20px, transparent 20px, transparent 28px); margin: 12px 0; opacity: 0.6; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "moonandqr",
        "name": "Moon and QR",
        "tagline": "A crescent moon cradles the Korvia lockup.",
        "desc": "The Moonlight theme is echoed by a crescent shape behind the wordmark and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'moon', 'crescent'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 50px; }
.logo-lockup::before { content: ""; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); width: 120px; height: 120px; border-radius: 50%; box-shadow: inset -20px 0 0 0 rgba(192,192,192,0.15); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; position: relative; z-index: 1; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; position: relative; z-index: 1; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "glasscard",
        "name": "Glass Card",
        "tagline": "The lockup floats on a frosted glass card.",
        "desc": "Korvia and tagline on a translucent frosted card with a subtle QR grid behind.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'glass', 'card'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; background: rgba(20,30,50,0.6); backdrop-filter: blur(8px); border: 1px solid rgba(192,192,192,0.2); padding: 36px 56px; border-radius: 4px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #cbd5e1; margin-top: 12px; display: block; text-align: center; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "ruledbackground",
        "name": "Ruled Background",
        "tagline": "The lockup sits on the ruled Moonlight grid.",
        "desc": "Korvia and tagline aligned to a subtle ruled grid background.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'ruled', 'grid'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; padding: 24px 0; border-top: 1px solid rgba(192,192,192,0.3); border-bottom: 1px solid rgba(192,192,192,0.3); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.25em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "animatedscanlockup",
        "name": "Animated Scan Lockup",
        "tagline": "A scanning line animates across the full lockup.",
        "desc": "The Korvia wordmark and tagline with a continuous scanning animation.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'animation', 'scan'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; text-align: center; }
.logo-lockup::after { content: ""; position: absolute; left: 0; right: 0; height: 2px; background: #C0C0C0; box-shadow: 0 0 8px #C0C0C0; animation: scanlock 2.5s ease-in-out infinite; }
@keyframes scanlock { 0%,100% { top: 0; } 50% { top: 100%; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "minimaltagline",
        "name": "Minimal Tagline",
        "tagline": "The simplest possible Korvia + tagline treatment.",
        "desc": "A minimal lockup with generous spacing and a delicate tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'minimal', 'spacious'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: 0.15em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "boldtagline",
        "name": "Bold Tagline",
        "tagline": "A heavy, confident Korvia with a bold tagline.",
        "desc": "A bold, high-impact lockup with thick lettering and a strong tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'bold', 'heavy'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3.2rem, 11vw, 7rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; display: block; -webkit-text-stroke: 1px #f8fafc; color: transparent; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase; color: #C0C0C0; margin-top: 12px; display: block; font-weight: 700; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "editoriallockup",
        "name": "Editorial Lockup",
        "tagline": "A magazine-style Korvia headline with tagline.",
        "desc": "An editorial layout with Korvia as a headline and the tagline as a byline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'editorial', 'headline'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: left; max-width: 600px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: -0.02em; text-transform: uppercase; display: block; line-height: 0.95; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; font-style: italic; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "stamplockup",
        "name": "Stamp Lockup",
        "tagline": "Korvia stamped in a rectangular seal with tagline.",
        "desc": "A stamp-like rectangular seal containing the Korvia wordmark and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'stamp', 'seal'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; border: 3px solid #C0C0C0; padding: 20px 40px; position: relative; transform: rotate(-2deg); }
.logo-lockup::before { content: ""; position: absolute; inset: 4px; border: 1px solid #C0C0C0; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; text-align: center; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "neonlockup",
        "name": "Neon Lockup",
        "tagline": "Korvia and tagline glow like a neon sign.",
        "desc": "A neon-style treatment with glowing outlines for both wordmark and tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'neon', 'glow'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; color: #f8fafc; text-shadow: 0 0 10px #C0C0C0, 0 0 20px #C0C0C0; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.25em; text-transform: uppercase; color: #C0C0C0; margin-top: 12px; display: block; text-shadow: 0 0 6px #C0C0C0; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "embossedlockup",
        "name": "Embossed Lockup",
        "tagline": "Korvia and tagline look pressed into metal.",
        "desc": "An embossed effect with subtle highlights and shadows on the lockup.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'embossed', 'metal'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; color: #e2e8f0; text-shadow: 1px 1px 0 rgba(255,255,255,0.2), -1px -1px 0 rgba(0,0,0,0.3); }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; text-shadow: 1px 1px 0 rgba(255,255,255,0.1); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "pixellockup",
        "name": "Pixel Lockup",
        "tagline": "Korvia and tagline in a pixelated arcade style.",
        "desc": "A pixelated treatment for both the wordmark and the tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'pixel', 'arcade'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Press+Start+2P&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Press Start 2P', cursive; font-size: clamp(1.8rem, 6vw, 3.5rem); letter-spacing: 0.04em; text-transform: uppercase; display: block; line-height: 1.4; }
.logo-tagline { font-family: 'Press Start 2P', cursive; font-size: 0.55rem; letter-spacing: 0.1em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; line-height: 1.6; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "geometriclockup",
        "name": "Geometric Lockup",
        "tagline": "Korvia and tagline locked in a geometric construction.",
        "desc": "A geometric frame of circles and lines contains the Korvia lockup.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'geometric', 'construction'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 60px; }
.logo-lockup::before { content: ""; position: absolute; top: 0; bottom: 0; left: 20px; width: 1px; background: rgba(192,192,192,0.3); }
.logo-lockup::after { content: ""; position: absolute; top: 0; bottom: 0; right: 20px; width: 1px; background: rgba(192,192,192,0.3); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; text-align: center; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "signaturelockup",
        "name": "Signature Lockup",
        "tagline": "Korvia as a signature with a handwritten tagline.",
        "desc": "A signature-style wordmark with an elegant script tagline.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'signature', 'script'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Dancing+Script:wght@700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Dancing Script', cursive; font-size: clamp(1.2rem, 3vw, 2rem); color: #C0C0C0; margin-top: 4px; display: block; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
    {
        "id": "qrradiant",
        "name": "QR Radiant",
        "tagline": "QR modules radiate outward from Korvia.",
        "desc": "The lockup sits at the center with radiating QR module lines.",
        "palette": ['#0A0F1E', '#C0C0C0', '#1E3A8A'],
        "shapes": ['lockup', 'radiant', 'lines'],
        "css": """


@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; text-align: center; padding: 20px 40px; }
.logo-lockup::before { content: ""; position: absolute; top: 50%; left: -80px; right: -80px; height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 4px, transparent 4px, transparent 8px); transform: translateY(-50%); opacity: 0.4; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; position: relative; z-index: 1; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; position: relative; z-index: 1; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        
        """,
        "content": """

<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
<div class="grid-line" style="width:80%"></div>
</div>

        """
    },
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
  <a href="index.html">Showcase · __INDEX__ / __TOTAL__</a>
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
.index { color: #b45309; font-weight: 800; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
footer { padding: 32px; text-align: center; color: #78716c; font-size: 0.85rem; border-top: 1px solid #e7e5e4; }
</style>
</head>
<body>
<header>
    <h1>Korvia Design Direction Showcase</h1>
    <p class="lead">One hundred fifty-eight human interface directions for Korvia — a QR-first hospitality operating system for East Africa.</p>
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
