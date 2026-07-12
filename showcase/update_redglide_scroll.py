#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

# Replace fixed rail CSS with a simple static logo-square
old_css = """.track-rail {
    position: fixed; top: 0; left: 0; width: 120px; height: 100vh;
    background: #1a1510; z-index: 100; pointer-events: none;
}
.track-line {
    position: absolute; top: 0; bottom: 0; width: 2px; background: #c5a059; opacity: 0.7;
}
.track-line.left { left: 20px; }
.track-line.right { left: 98px; }
.logo-square {
    position: absolute; left: 21px; top: 88px;
    width: 76px; height: 76px; background: #e42718; color: #1a1510;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 0.7rem; letter-spacing: 0.02em;
    font-weight: 700; text-transform: uppercase; text-align: center;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 160px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 160px; width: 100%; }
"""

new_css = """.logo-square {
    display: inline-flex; align-items: center; justify-content: center;
    width: 76px; height: 76px; background: #e42718; color: #1a1510;
    font-family: 'Cinzel', serif; font-size: 0.7rem; letter-spacing: 0.02em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    vertical-align: middle; margin: 0 16px 16px 0;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
"""

old_content = '<div class="track-rail"><div class="track-line left"></div><div class="track-line right"></div><div class="logo-square">Korvia</div></div>'
new_content = '<div class="logo-square">Korvia</div>'

old_footer = '.showcase-footer { padding: 20px 20px 20px 160px;'
new_footer = '.showcase-footer { padding: 20px;'

text = text.replace(old_css, new_css)
text = text.replace(old_content, new_content)
text = text.replace(old_footer, new_footer)

old_meta = '"tagline": "Direction 43 with a fixed Korvia square between two rail lines, moving against the scroll.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and pins a red Korvia square between two vertical rail lines on the left; the square stays fixed while the page scrolls, so it appears to glide past the content.",\n        "shapes": ["rail-lines", "logo-square", "red-bar"]'
new_meta = '"tagline": "Direction 43 with a static Korvia square that scrolls with the page.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and places a static red Korvia square in the page flow; it moves naturally as the user scrolls up and down.",\n        "shapes": ["logo-square", "peeling-gold", "red-bar"]'
text = text.replace(old_meta, new_meta)

target.write_text(text, encoding='utf-8')
print('Redglide now uses a static scrolling logo-square.')
