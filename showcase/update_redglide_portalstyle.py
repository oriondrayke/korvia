#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

old_css = """.logo-square {
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

new_css = """.logo-square {
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: #201a12; color: #d4c5a9;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid #e42718;
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}
"""

text = text.replace(old_css, new_css)

target.write_text(text, encoding='utf-8')
print('Styled logo-square exactly like the portal rectangles.')
