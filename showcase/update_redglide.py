#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

# Replace glide CSS block with fixed logo-square block
old_css = """.glide-rail {
    position: fixed; top: 0; left: 0; width: 72px; height: 100vh;
    background: #e42718; color: #1a1510; overflow: hidden;
    display: flex; align-items: center; justify-content: center; z-index: 100;
}
.glide-track {
    display: flex; flex-direction: column; align-items: center;
    animation: glide 5s linear infinite;
}
.glide-word {
    writing-mode: vertical-rl; text-orientation: mixed;
    font-family: 'Cinzel', serif; font-size: 1.5rem; letter-spacing: 0.28em;
    font-weight: 700; text-transform: uppercase; padding: 32px 0;
}
@keyframes glide { 0% { transform: translateY(-50%); } 100% { transform: translateY(0%); } }
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 96px; background: #120e0a; border-bottom: 1px solid #6b5b3e;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 96px; width: 100%; }
"""

new_css = """.logo-square {
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

old_content = '<div class="glide-rail"><div class="glide-track"><div class="glide-word">Korvia</div><div class="glide-word">Korvia</div></div></div>'
new_content = '<div class="logo-square">Korvia</div>'

old_footer = '.showcase-footer { padding: 20px 20px 20px 96px;'
new_footer = '.showcase-footer { padding: 20px 20px 20px 168px;'

text = text.replace(old_css, new_css)
text = text.replace(old_content, new_content)
text = text.replace(old_footer, new_footer)

# Update description / tagline / shapes to match
old_meta = '"tagline": "Direction 43 with a moving logo rail on the left.",\n        "desc": "Red Deco Glide takes the rotting gold and Swiss-red spine of Direction 43 and adds a fixed left rail where the Korvia wordmark glides vertically.",\n        "palette": ["#1A1510", "#C5A059", "#E42718"],\n        "shapes": ["glide-rail", "peeling-gold", "red-bar"]'
new_meta = '"tagline": "Direction 43 with a fixed red Korvia square that moves against the scroll.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and pins a red square logo holder to the left; as the page scrolls, the square stays fixed and appears to glide past the content.",\n        "palette": ["#1A1510", "#C5A059", "#E42718"],\n        "shapes": ["logo-square", "peeling-gold", "red-bar"]'
text = text.replace(old_meta, new_meta)

target.write_text(text, encoding='utf-8')
print('Updated redglide entry.')
