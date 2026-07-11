#!/usr/bin/env python3
"""Generate a standalone showcase of non-AI UI directions."""
import os

DIRECTIONS = [
    {
        "id": "brutalist",
        "name": "Brutalist Raw",
        "tagline": "System fonts, thick borders, rectangles only, zero polish.",
        "desc": "No radius, no gradients, no harmony. Type is huge, borders are weapons, and the grid is implied by brute force. The dopamine comes from contrast and raw structure.",
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
<div class="wrap">
    <h1>Brutalist Raw</h1>
    <p class="desc">No radius, no gradients, no harmony. Type is huge, borders are weapons, and the grid is implied by brute force.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#000;"><span>#000000</span></div>
        <div class="swatch" style="background:#fff;"><span>#FFFFFF</span></div>
        <div class="swatch" style="background:#ff0000;"><span style="color:#fff">#FF0000</span></div>
    </div>

    <h2>Shapes</h2>
    <div class="shapes">
        <div class="shape square"></div>
        <div class="shape rect"></div>
        <div class="shape rect" style="width:180px;"></div>
    </div>

    <h2>Type Scale</h2>
    <div class="type-scale">
        <p style="font-size:2.5rem; font-weight:700;">Display — 40px bold</p>
        <p style="font-size:1.25rem; font-weight:700;">Headline — 20px bold uppercase</p>
        <p style="font-size:1rem;">Body — 16px monospace, harsh line breaks</p>
        <p style="font-size:0.75rem; color:#666;">Caption — 12px muted</p>
    </div>

    <h2>Components</h2>
    <button class="big-btn">Primary</button>
    <button class="big-btn secondary">Secondary</button>
</div>
"""
    },
    {
        "id": "swiss",
        "name": "Swiss Grid",
        "tagline": "Asymmetric grids, red accents, absolute order.",
        "desc": "Helvetica discipline: flush left, ragged right, a single accent color, and negative space treated as a material.",
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
<div class="wrap">
    <h1>Swiss Grid</h1>
    <p class="desc">Helvetica discipline: flush left, ragged right, a single accent color, and negative space treated as a material.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#111;"><span style="color:#fff">#111111</span></div>
        <div class="swatch" style="background:#f4f4f4;"><span>#F4F4F4</span></div>
        <div class="swatch" style="background:#ff2500;"><span>#FF2500</span></div>
    </div>

    <h2>Grid / Asymmetry</h2>
    <div class="grid">
        <div class="cell"><p style="font-size:2rem; font-weight:900; margin:0;">Aa</p><p class="label" style="font-size:0.65rem; text-transform:uppercase; letter-spacing:0.1em; color:#666; margin-top:8px;">Display type</p></div>
        <div class="cell red"><p style="font-size:1.4rem; font-weight:700; margin:0;">01</p></div>
        <div class="cell black"><p style="margin:0; font-size:0.9rem;">Small caps labels carry hierarchy.</p></div>
        <div class="cell"><p style="font-size:1.8rem; font-weight:900; margin:0;">24px</p></div>
    </div>

    <h2>Type Scale</h2>
    <div class="type-scale">
        <p style="font-size:2.4rem; font-weight:900; letter-spacing:-0.03em;">Display — tight, loud</p>
        <p style="font-size:1rem; font-weight:700; text-transform:uppercase; letter-spacing:0.1em;">Headline — small caps</p>
        <p style="font-size:1rem;">Body — neutral sans, generous line height</p>
        <p style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em; color:#888;">Caption — metadata grey</p>
    </div>
</div>
"""
    },
    {
        "id": "editorial",
        "name": "Editorial Magazine",
        "tagline": "Serif headlines, columns, pull quotes, footnotes.",
        "desc": "Magazine layout logic: big display type, multi-column body, generous margins, and a pull quote that interrupts the flow.",
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
<div class="wrap">
    <h1>Editorial Magazine</h1>
    <p class="deck">Magazine layout logic: big display type, multi-column body, generous margins, and a pull quote that interrupts the flow.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#2a2520;"><span style="color:#fff">Ink</span></div>
        <div class="swatch" style="background:#faf8f3;"><span>Paper</span></div>
        <div class="swatch" style="background:#8b0000;"><span style="color:#fff">Accent</span></div>
    </div>

    <div class="columns">
        <p class="drop-cap">Serif display type sets the mood before the reader absorbs a single word. The body follows in a neutral sans, held in by columns and ruled lines.</p>
        <p>Footnotes, captions, and pull quotes are not decoration — they are the rhythm section. They give the eye places to rest and the brain places to land.</p>
    </div>

    <blockquote class="pull-quote">"Good typography is invisible. Great typography is unforgettable."</blockquote>

    <h2>Type Scale</h2>
    <p style="font-family:'Playfair Display',serif; font-size:2.2rem; margin:8px 0;">Display serif — elegant authority</p>
    <p style="font-family:'Playfair Display',serif; font-size:1.3rem; font-style:italic; margin:8px 0;">Italic subhead — conversational rhythm</p>
    <p style="font-size:1rem; margin:8px 0;">Body sans — readable, neutral, generous</p>
    <p style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; color:#8a8175; margin:8px 0;">Caption — small, spaced, grey</p>
</div>
"""
    },
    {
        "id": "memphis",
        "name": "Memphis Pop",
        "tagline": "Squiggles, circles, triangles, pastel chaos.",
        "desc": "The 80s are back: clashing pastels, bold black outlines, primitive geometry, and a composition that refuses to sit still.",
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
<div class="wrap">
    <h1>Memphis Pop</h1>
    <p class="desc">The 80s are back: clashing pastels, bold black outlines, primitive geometry, and a composition that refuses to sit still.</p>

    <h2 style="margin-top:0;">Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#f6d7ff;"><span>Lavender</span></div>
        <div class="swatch" style="background:#fff6a3;"><span>Lemon</span></div>
        <div class="swatch" style="background:#a3fff0;"><span>Mint</span></div>
        <div class="swatch" style="background:#ffc4a3;"><span>Peach</span></div>
    </div>

    <h2>Shapes</h2>
    <div class="shapes">
        <div class="shape circle"></div>
        <div class="shape triangle"></div>
        <div class="shape squiggle"></div>
        <div class="shape circle" style="background:#7c4dff;"></div>
    </div>

    <h2>Cards</h2>
    <div class="card"><h3 style="margin:0 0 8px;">Pop</h3><p style="margin:0; font-size:0.9rem;">Bold, rotated, unapologetic.</p></div>
    <div class="card" style="background:#fff6a3; transform:rotate(-3deg);"><h3 style="margin:0 0 8px;">Zig</h3><p style="margin:0; font-size:0.9rem;">No two cards align.</p></div>
</div>
"""
    },
    {
        "id": "bauhaus",
        "name": "Bauhaus Function",
        "tagline": "Circles, squares, triangles, primary colors.",
        "desc": "Primary forms for primary functions. Red, yellow, and blue sit on a neutral ground while circles, squares, and triangles do all the talking.",
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
<div class="wrap">
    <h1>Bauhaus Function</h1>
    <p class="desc">Primary forms for primary functions. Red, yellow, and blue sit on a neutral ground while circles, squares, and triangles do all the talking.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#e63946;"><span style="color:#fff">Red</span></div>
        <div class="swatch" style="background:#ffcc00;"><span>Yellow</span></div>
        <div class="swatch" style="background:#1d3557;"><span style="color:#fff">Blue</span></div>
    </div>

    <h2>Primary Shapes</h2>
    <div class="shapes">
        <div class="shape sq"></div>
        <div class="shape ci"></div>
        <div class="shape tr"></div>
    </div>

    <h2>Grid Modules</h2>
    <div class="stage">
        <div class="module red"><h2>Square</h2><div class="big">□</div></div>
        <div class="module yellow"><h2>Circle</h2><div class="big">○</div></div>
        <div class="module blue"><h2>Triangle</h2><div class="big">△</div></div>
        <div class="module white"><h2>White</h2><div class="big">—</div></div>
        <div class="module blue"><h2>Blue</h2><div class="big">●</div></div>
        <div class="module red"><h2>Red</h2><div class="big">■</div></div>
    </div>
</div>
"""
    },
    {
        "id": "handdrawn",
        "name": "Hand-Drawn Sketch",
        "tagline": "Rough edges, paper texture, pencil marks.",
        "desc": "Everything looks like it was sketched on a napkin: wavy underlines, dashed borders, handwritten type, and a yellow tape strip holding it together.",
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
<div class="wrap">
    <h1>Hand-Drawn Sketch</h1>
    <p class="desc">Everything looks like it was sketched on a napkin: wavy underlines, dashed borders, handwritten type, and a yellow tape strip holding it together.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#f7f2e6;"><span>Paper</span></div>
        <div class="swatch" style="background:#3a3026;"><span style="color:#fff">Ink</span></div>
        <div class="swatch" style="background:#b45f06;"><span>Pencil</span></div>
    </div>

    <div class="napkin">
        <div class="tape"></div>
        <div class="row"><span>Display type</span><span>Patrick Hand</span></div>
        <div class="row"><span>UI type</span><span>Kalam</span></div>
        <div class="row"><span>Border style</span><span>Dashed / wavy</span></div>
        <div class="row"><span>Radius</span><span>Random organic</span></div>
    </div>

    <button class="sketch-btn">Save sketch</button>
    <button class="sketch-btn" style="background:#fffef8;">Erase</button>
</div>
"""
    },
    {
        "id": "artdeco",
        "name": "Art Deco Luxe",
        "tagline": "Gold, black, stepped geometry, fan patterns.",
        "desc": "Stepped forms, sunburst motifs, and gold on black. This direction trades utility for ceremony and turns every screen into a lobby.",
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
<div class="wrap">
    <div class="fan"></div>
    <h1>Art Deco Luxe</h1>
    <p class="desc">Stepped forms, sunburst motifs, and gold on black. This direction trades utility for ceremony and turns every screen into a lobby.</p>

    <h2 style="color:#c5a059; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.2em;">Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#050505;"><span style="color:#fff">Black</span></div>
        <div class="swatch" style="background:#c5a059;"><span>Gold</span></div>
        <div class="swatch" style="background:#f5e7c8;"><span>Cream</span></div>
    </div>

    <h2 style="color:#c5a059; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.2em;">Motifs</h2>
    <div class="shapes">
        <div class="diamond"></div>
        <div class="step"></div>
        <div class="diamond" style="background:#f5e7c8;"></div>
    </div>

    <div class="panel">
        <p style="font-size:1.3rem; margin:0 0 12px;">Your experience begins here.</p>
        <p style="color:#8a7e63; margin:0 0 24px;">Cinzel headings · Marcellus body · Gold accents</p>
        <button class="gold-btn">Enter</button>
    </div>
</div>
"""
    },
    {
        "id": "scrapbook",
        "name": "Scrapbook Collage",
        "tagline": "Washi tape, polaroids, layered paper, soft dopamine.",
        "desc": "Soft pastels, torn edges, polaroid frames, and yellow tape. A friendly, tactile collage that feels pinned up rather than rendered.",
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
<div class="wrap">
    <h1>Scrapbook Collage</h1>
    <p class="desc">Soft pastels, torn edges, polaroid frames, and yellow tape. A friendly, tactile collage that feels pinned up rather than rendered.</p>

    <h2>Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#e6f0e8;"><span>Mint</span></div>
        <div class="swatch" style="background:#e07050;"><span>Terracotta</span></div>
        <div class="swatch" style="background:#ffb74d;"><span>Tape</span></div>
    </div>

    <h2>Polaroids</h2>
    <div class="collage">
        <div class="polaroid"><div class="washi"></div><div class="img">🎨</div><p>Color study</p></div>
        <div class="polaroid"><div class="washi"></div><div class="img">✂️</div><p>Cut paper</p></div>
        <div class="polaroid"><div class="washi"></div><div class="img">📝</div><p>Hand note</p></div>
    </div>
</div>
"""
    },
    {
        "id": "japanese",
        "name": "Japanese Minimal",
        "tagline": "Space, ink, red seals, vertical rhythm.",
        "desc": "Ma — the power of empty space. A single red seal, vertical text, and ink-wash restraint turn silence into structure.",
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
<div class="wrap">
    <div class="vertical">間 · 2026</div>
    <h1>Japanese Minimal</h1>
    <p class="desc">Ma — the power of empty space. A single red seal, vertical text, and ink-wash restraint turn silence into structure.</p>

    <h2 style="font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase;">Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#f7f5f0;"><span>Paper</span></div>
        <div class="swatch" style="background:#2b2b2b;"><span style="color:#fff">Ink</span></div>
        <div class="swatch" style="background:#b02a2a;"><span style="color:#fff">Seal</span></div>
    </div>

    <div class="seal">美</div>

    <h2 style="font-size:0.75rem; letter-spacing:0.2em; text-transform:uppercase;">Type Rhythm</h2>
    <div class="type-line" style="font-size:2rem;">静かな余白</div>
    <div class="type-line" style="font-size:1.3rem;">Quiet white space</div>
    <div class="type-line" style="font-size:1rem;">Body text floats with generous leading.</div>
    <div class="type-line" style="font-size:0.75rem; color:#8c8c8c;">Caption — small, spaced, grey</div>
</div>
"""
    },
    {
        "id": "terminal",
        "name": "Retro Terminal",
        "tagline": "Monospace green, scanlines, CRT glow.",
        "desc": "A phosphor-green interface that feels like it boots from a 5.25-inch floppy. Scanlines, blinking cursor, and pure command-line romance.",
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
<div class="wrap">
    <h1>> RETRO_TERMINAL</h1>
    <p class="desc">A phosphor-green interface that feels like it boots from a 5.25-inch floppy. Scanlines, blinking cursor, and pure command-line romance.</p>

    <h2 style="font-size:1rem; color:#33ff00cc;">Palette</h2>
    <div class="swatches">
        <div class="swatch" style="background:#050a05;"><span style="color:#33ff00">Black</span></div>
        <div class="swatch" style="background:#33ff00;"><span style="color:#050a05">Green</span></div>
        <div class="swatch" style="background:#0f3d0f;"><span>Dim</span></div>
    </div>

    <h2 style="font-size:1rem; color:#33ff00cc;">Shapes</h2>
    <div class="shapes">
        <div class="bar"></div>
        <div class="bar" style="width:100px;"></div>
        <div class="grid2"></div>
    </div>

    <div class="log">
        <p><span class="prompt">$</span> load_ui --theme=terminal</p>
        <p>[OK] monospace loaded</p>
        <p>[OK] scanlines enabled</p>
        <p>[OK] 80 columns ready</p>
        <p><span class="prompt">$</span> run_presentation<span class="cursor">_</span></p>
    </div>
</div>
"""
    }
]

BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
__CSS__
</style>
</head>
<body>
<nav class="showcase-nav">
  <a href="index.html">← Showcase</a>
  <span>__NAME__</span>
  <a href="__NEXT__.html">Next →</a>
</nav>
__CONTENT__
<footer class="showcase-footer">UI Direction Showcase · __INDEX__ / __TOTAL__</footer>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UI Direction Showcase</title>
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
    <h1>UI Direction Showcase</h1>
    <p class="lead">Human, non-AI interface directions — one per page.</p>
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
        html = BASE
        html = html.replace("__TITLE__", f"{d['name']} — UI Direction")
        html = html.replace("__CSS__", d["css"])
        html = html.replace("__NAME__", d["name"])
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
