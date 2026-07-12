#!/usr/bin/env python3
from pathlib import Path

target = Path('~/github-recovery/korvia/showcase/generate_showcase.py').expanduser()
text = target.read_text(encoding='utf-8')

old_css = """.logo-square::after {
    content: ""; position: absolute;
    top: 10px; left: 10px; right: -10px; bottom: -10px;
    background: rgba(0,0,0,0.35); z-index: -1;
}
"""

new_css = """.logo-square::after {
    content: ""; position: absolute;
    top: 8px; left: 8px; right: -8px; bottom: -8px;
    background: #111; z-index: -1;
}
"""

text = text.replace(old_css, new_css)

target.write_text(text, encoding='utf-8')
print('Made the duplicate shadow a solid black rectangle.')
