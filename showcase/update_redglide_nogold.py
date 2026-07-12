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
    padding: 18px 24px; background: #120e0a;
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
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
.showcase-footer { padding: 20px; background: #120e0a; color: #6b5b3e; text-align: center; }
        """

text = text.replace(old_css, new_css)

old_meta = '"tagline": "Direction 43 with a static Korvia square that scrolls with the page.",\n        "desc": "Red Deco Glide keeps the rotting gold and Swiss-red spine of Direction 43 and places a static red Korvia square in the page flow; it moves naturally as the user scrolls up and down.",\n        "palette": ["#1A1510", "#C5A059", "#E42718"],\n        "shapes": ["logo-square", "peeling-gold", "red-bar"]'
new_meta = '"tagline": "Direction 43 stripped to a red Korvia square and no gold lines.",\n        "desc": "Red Deco Glide takes Direction 43 and removes all gold lines, leaving a clean dark canvas with a static red Korvia square that scrolls with the page.",\n        "palette": ["#1A1510", "#E42718"],\n        "shapes": ["logo-square", "red-bar"]'
text = text.replace(old_meta, new_meta)

target.write_text(text, encoding='utf-8')
print('Removed gold lines from redglide.')
