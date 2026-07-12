#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

old_css = """.logo-square {
    display: inline-flex; align-items: center; justify-content: center;
    width: 76px; height: 76px; background: #e42718; color: #1a1510;
    font-family: 'Cinzel', serif; font-size: 0.7rem; letter-spacing: 0.02em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    vertical-align: middle; margin: 0 16px 16px 0;
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px; background: #120e0a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
"""

new_css = """.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #e42718; color: #1a1510;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    z-index: 100; pointer-events: none;
    box-shadow: 0 6px 18px rgba(0,0,0,0.45);
}
.showcase-nav {
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: #120e0a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
"""

old_footer = '.showcase-footer { padding: 20px; background: #120e0a; color: #6b5b3e; text-align: center; }'
new_footer = '.showcase-footer { padding: 20px 20px 20px 154px; background: #120e0a; color: #6b5b3e; text-align: center; }'

text = text.replace(old_css, new_css)
text = text.replace(old_footer, new_footer)

old_meta = '"tagline": "Direction 43 stripped to a red Korvia square and no gold lines.",\n        "desc": "Red Deco Glide takes Direction 43 and removes all gold lines, leaving a clean dark canvas with a static red Korvia square that scrolls with the page."'
new_meta = '"tagline": "Direction 43 with a larger fixed Korvia square that moves against the scroll.",\n        "desc": "Red Deco Glide takes Direction 43, removes the gold lines, and pins a larger red Korvia square to the top-left. The square stays fixed while the page scrolls, so it appears to move relative to the content, and it carries a soft shadow like the portal cards."'
text = text.replace(old_meta, new_meta)

target.write_text(text, encoding='utf-8')
print('Updated redglide: bigger fixed square with shadow, moves against scroll.')
