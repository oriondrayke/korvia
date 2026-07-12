#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

old_css = """.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #e42718; color: #1a1510;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    z-index: 100; pointer-events: none;
}
.logo-square::after {
    content: ""; position: absolute;
    top: 8px; left: 8px; right: -8px; bottom: -8px;
    background: #111; z-index: -1;
}
"""

new_css = """.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #111; color: #e42718;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    z-index: 100; pointer-events: none;
}
.logo-square::after {
    content: ""; position: absolute;
    top: 8px; left: 8px; right: -8px; bottom: -8px;
    background: #e42718; z-index: -1;
}
"""

text = text.replace(old_css, new_css)

target.write_text(text, encoding='utf-8')
print('Swapped logo square colors: black front, red shadow.')
