#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

# Replace the fixed logo-square CSS block with a railway track + moving train
old_css = """.logo-square {
    position: fixed; top: 88px; left: 24px; width: 120px; height: 120px;
    background: #e42718; color: #1a1510;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1.05rem; letter-spacing: 0.08em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    z-index: 100; pointer-events: none;
}
.logo-square::after {
    content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px;
    border: 1px solid #c5a059; opacity: 0.6; z-index: -1;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 168px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 168px; width: 100%; }
"""

new_css = """.track-rail {
    position: fixed; top: 0; left: 0; width: 120px; height: 100vh;
    background: #1a1510; z-index: 100; overflow: hidden;
}
.track-line {
    position: absolute; top: 0; bottom: 0; width: 2px; background: #c5a059; opacity: 0.7;
}
.track-line.left { left: 20px; }
.track-line.right { left: 98px; }
.logo-train {
    position: absolute; left: 21px; top: 0;
    width: 76px; height: 76px; background: #e42718; color: #1a1510;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 0.7rem; letter-spacing: 0.02em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    animation: train 7s linear infinite;
}
@keyframes train {
    0% { transform: translateY(-76px); }
    100% { transform: translateY(calc(100vh + 76px)); }
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 160px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 160px; width: 100%; }
"""

old_content = '<div class="logo-square">Korvia</div>'
new_content = '<div class="track-rail"><div class="track-line left"></div><div class="track-line right"></div><div class="logo-train">Korvia</div></div>'

old_footer = '.showcase-footer { padding: 20px 20px 20px 168px;'
new_footer = '.showcase-footer { padding: 20px 20px 20px 160px;'

text = text.replace(old_css, new_css)
text = text.replace(old_content, new_content)
text = text.replace(old_footer, new_footer)

old_meta = '"tagline": "Direction 43 with a fixed red Korvia square that moves against the scroll.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and pins a red square logo holder to the left; as the page scrolls, the square stays fixed and appears to glide past the content.",\n        "shapes": ["logo-square", "peeling-gold", "red-bar"]'
new_meta = '"tagline": "Direction 43 with a Korvia train gliding between two rail lines on the left.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and runs a red square logo carriage between two vertical rail lines on the left, so Korvia glides up and down like a train on a track.",\n        "shapes": ["rail-lines", "logo-train", "red-bar"]'
text = text.replace(old_meta, new_meta)

target.write_text(text, encoding='utf-8')
print('Updated redglide to railway train.')
