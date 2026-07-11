#!/usr/bin/env python3
"""Append 9 more Art Deco + Grunge mixture variations to generate_showcase.py."""
from pathlib import Path

NEW_ENTRIES = '''
    {
        "id": "decdecay",
        "name": "Deco Decay",
        "tagline": "Ornate frames left out in the rain.",
        "desc": "Deco Decay takes Korvia's heritage hotel lobbies and lets the moldings peel: gold leaf flaking off charcoal plaster, water-stained menus, and a sense of beautiful neglect.",
        "palette": ["#1A1510", "#C5A059", "#4A5D3A"],
        "shapes": ["peeling-frame", "water-stain", "crack"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=IM+Fell+English+SC\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Anton\u0026family=Cinzel:wght@400;700\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,700;1,400\u0026family=Cinzel:wght@400;700\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,600\u0026family=Cinzel:wght@400;700\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=IM+Fell+English\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Archivo+Black\u0026family=Cinzel:wght@400;700\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=Libre+Baskerville:ital@0;1\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=Oswald:wght@400;600\u0026display=swap');
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

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700\u0026family=Merriweather:ital@0;1\u0026display=swap');
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
