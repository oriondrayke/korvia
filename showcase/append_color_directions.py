#!/usr/bin/env python3
"""Append 15 color variations of the final Direction 53 design."""
from pathlib import Path

THEMES = [
    {
        "id": "neonglitch",
        "name": "Neon Glitch",
        "tagline": "Black canvas split by cyan and magenta dopamine rails.",
        "desc": "Neon Glitch takes the Direction 53 layout and pumps it with cyan voltage and magenta static.",
        "palette": ["#050505", "#00F0FF", "#FF00AA"],
        "shapes": ["logo-square", "cyan-bar", "magenta-dot"],
        "body1": "#050505", "body2": "#0a0a12",
        "nav": "#08080f", "card": "#0d0d14", "text": "#e6f7ff",
        "muted": "#7aa7b5", "accent": "#00F0FF", "accent2": "#FF00AA", "btn_text": "#000",
        "dopamine": "width:120px;height:16px;background:linear-gradient(90deg,#00F0FF,#FF00AA);display:inline-block;margin-right:16px;"
    },
    {
        "id": "sunsetpop",
        "name": "Sunset Pop",
        "tagline": "Warm gradient dusk with tangerine energy.",
        "desc": "Sunset Pop soaks the Direction 53 layout in tangerine, amber, and deep plum shadows.",
        "palette": ["#2A1515", "#FF6B35", "#F7C548"],
        "shapes": ["logo-square", "orange-bar", "gold-pill"],
        "body1": "#2A1515", "body2": "#3D1E1E",
        "nav": "#1f0f0f", "card": "#241313", "text": "#fff0e6",
        "muted": "#c98d75", "accent": "#FF6B35", "accent2": "#F7C548", "btn_text": "#1a0a05",
        "dopamine": "width:80px;height:80px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#F7C548,#FF6B35);display:inline-block;margin-right:16px;"
    },
    {
        "id": "mintchoco",
        "name": "Mint Choco",
        "tagline": "Dark chocolate softened by electric mint.",
        "desc": "Mint Choco pairs the Direction 53 grid with rich chocolate browns and a fresh mint accent.",
        "palette": ["#1F1612", "#7FFFD4", "#5C4033"],
        "shapes": ["logo-square", "mint-stripe", "choco-dot"],
        "body1": "#1F1612", "body2": "#2a1e18",
        "nav": "#16100d", "card": "#261c17", "text": "#f0fff7",
        "muted": "#8fb8a8", "accent": "#7FFFD4", "accent2": "#5C4033", "btn_text": "#000",
        "dopamine": "width:100px;height:12px;background:repeating-linear-gradient(90deg,#7FFFD4,#7FFFD4 10px,transparent 10px,transparent 18px);display:inline-block;margin-right:16px;"
    },
    {
        "id": "lavenderhaze",
        "name": "Lavender Haze",
        "tagline": "Deep purple calm with a lavender spark.",
        "desc": "Lavender Haze drapes the Direction 53 layout in midnight violet and soft lavender highlights.",
        "palette": ["#1A1025", "#B18CFF", "#7C3AED"],
        "shapes": ["logo-square", "lavender-bar", "haze-glow"],
        "body1": "#1A1025", "body2": "#241338",
        "nav": "#120a1a", "card": "#1e1229", "text": "#f3e8ff",
        "muted": "#9b8db5", "accent": "#B18CFF", "accent2": "#7C3AED", "btn_text": "#1a1025",
        "dopamine": "width:64px;height:64px;border-radius:12px;background:linear-gradient(135deg,#B18CFF,#7C3AED);display:inline-block;margin-right:16px;"
    },
    {
        "id": "olivegold",
        "name": "Olive Gold",
        "tagline": "Military olive charged with gold voltage.",
        "desc": "Olive Gold gives the Direction 53 layout an underground bunker feel with olive drab and antique gold.",
        "palette": ["#1A1A10", "#B5BD68", "#D4AF37"],
        "shapes": ["logo-square", "olive-bar", "gold-tick"],
        "body1": "#1A1A10", "body2": "#252516",
        "nav": "#11110a", "card": "#202013", "text": "#f4f3d9",
        "muted": "#9ea36b", "accent": "#B5BD68", "accent2": "#D4AF37", "btn_text": "#1a1a10",
        "dopamine": "width:90px;height:90px;background:repeating-linear-gradient(45deg,#B5BD68,#B5BD68 4px,#202013 4px,#202013 8px);display:inline-block;margin-right:16px;"
    },
    {
        "id": "berrycream",
        "name": "Berry Cream",
        "tagline": "Dark berry base with a cream swirl.",
        "desc": "Berry Cream softens the Direction 53 layout with plum darkness, cream text, and a ripe berry accent.",
        "palette": ["#1F0F1A", "#D81B60", "#FFF5E6"],
        "shapes": ["logo-square", "berry-bar", "cream-pill"],
        "body1": "#1F0F1A", "body2": "#2a1522",
        "nav": "#150a12", "card": "#241220", "text": "#FFF5E6",
        "muted": "#c9929e", "accent": "#D81B60", "accent2": "#FFF5E6", "btn_text": "#fff5e6",
        "dopamine": "width:120px;height:14px;border-radius:7px;background:linear-gradient(90deg,#D81B60,#FFF5E6);display:inline-block;margin-right:16px;"
    },
    {
        "id": "tealdusk",
        "name": "Teal Dusk",
        "tagline": "Night dive into saturated teal.",
        "desc": "Teal Dusk pulls the Direction 53 layout under deep water with dark teal depths and a bright surface accent.",
        "palette": ["#0F1F1F", "#2DD4BF", "#115E59"],
        "shapes": ["logo-square", "teal-bar", "dusk-wave"],
        "body1": "#0F1F1F", "body2": "#142b2b",
        "nav": "#0a1616", "card": "#132525", "text": "#e6fffa",
        "muted": "#6abfb5", "accent": "#2DD4BF", "accent2": "#115E59", "btn_text": "#000",
        "dopamine": "width:0;height:0;border-left:40px solid transparent;border-right:40px solid transparent;border-bottom:70px solid #2DD4BF;display:inline-block;margin-right:16px;"
    },
    {
        "id": "cobaltrush",
        "name": "Cobalt Rush",
        "tagline": "Midnight blue lit by cobalt lightning.",
        "desc": "Cobalt Rush runs the Direction 53 layout through a deep-blue hour with electric cobalt edges.",
        "palette": ["#0A1220", "#3B82F6", "#60A5FA"],
        "shapes": ["logo-square", "cobalt-bar", "rush-bolt"],
        "body1": "#0A1220", "body2": "#0f1a2e",
        "nav": "#060c16", "card": "#0d1626", "text": "#e8f1ff",
        "muted": "#7ca1d8", "accent": "#3B82F6", "accent2": "#60A5FA", "btn_text": "#fff",
        "dopamine": "width:12px;height:80px;background:#3B82F6;box-shadow:0 0 12px #60A5FA;display:inline-block;margin-right:16px;"
    },
    {
        "id": "rosewood",
        "name": "Rosewood",
        "tagline": "Polished dark wood with a rose highlight.",
        "desc": "Rosewood warms the Direction 53 layout with dark rosewood grain tones and a dusty-rose accent.",
        "palette": ["#2A1518", "#FF6F91", "#5C2A32"],
        "shapes": ["logo-square", "rose-bar", "wood-dot"],
        "body1": "#2A1518", "body2": "#351a1e",
        "nav": "#1e0f12", "card": "#30181c", "text": "#fff0f3",
        "muted": "#c98a97", "accent": "#FF6F91", "accent2": "#5C2A32", "btn_text": "#2a1518",
        "dopamine": "width:70px;height:70px;border-radius:50%;background:#FF6F91;opacity:.85;display:inline-block;margin-right:16px;"
    },
    {
        "id": "limewire",
        "name": "Lime Wire",
        "tagline": "Dark forest floor wired with lime.",
        "desc": "Lime Wire roots the Direction 53 layout in dark green soil and threads it with acid lime.",
        "palette": ["#0F1A0F", "#84CC16", "#3F6212"],
        "shapes": ["logo-square", "lime-bar", "wire-zig"],
        "body1": "#0F1A0F", "body2": "#152415",
        "nav": "#0a120a", "card": "#132113", "text": "#f0ffe6",
        "muted": "#8fb86e", "accent": "#84CC16", "accent2": "#3F6212", "btn_text": "#0f1a0f",
        "dopamine": "width:100px;height:8px;background:#84CC16;border-radius:4px;box-shadow:0 0 10px #84CC16;display:inline-block;margin-right:16px;"
    },
    {
        "id": "coralreef",
        "name": "Coral Reef",
        "tagline": "Deep navy reef with living coral.",
        "desc": "Coral Reef sinks the Direction 53 layout into deep navy water and lets coral accents glow.",
        "palette": ["#0F172A", "#FF7F50", "#1E293B"],
        "shapes": ["logo-square", "coral-bar", "reef-bubble"],
        "body1": "#0F172A", "body2": "#162033",
        "nav": "#0a101f", "card": "#121b2e", "text": "#fff3ef",
        "muted": "#c99a8a", "accent": "#FF7F50", "accent2": "#1E293B", "btn_text": "#0f172a",
        "dopamine": "width:60px;height:60px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#FF7F50,#c94f28);display:inline-block;margin-right:16px;"
    },
    {
        "id": "icebreaker",
        "name": "Ice Breaker",
        "tagline": "Near-black frost with an ice-blue crack.",
        "desc": "Ice Breaker freezes the Direction 53 layout in near-black ice and fractures it with a cold blue accent.",
        "palette": ["#111827", "#93C5FD", "#1E3A8A"],
        "shapes": ["logo-square", "ice-bar", "frost-ring"],
        "body1": "#111827", "body2": "#182435",
        "nav": "#0c111b", "card": "#151d2b", "text": "#eff6ff",
        "muted": "#8ba6c7", "accent": "#93C5FD", "accent2": "#1E3A8A", "btn_text": "#111827",
        "dopamine": "width:90px;height:90px;border:2px solid #93C5FD;border-radius:50%;display:inline-block;margin-right:16px;position:relative;"
    },
    {
        "id": "ambernight",
        "name": "Amber Night",
        "tagline": "Pitch black warmed by glowing amber.",
        "desc": "Amber Night keeps the Direction 53 layout in pure darkness and lights it with molten amber.",
        "palette": ["#1F140A", "#F59E0B", "#78350F"],
        "shapes": ["logo-square", "amber-bar", "night-glow"],
        "body1": "#1F140A", "body2": "#2a1b0e",
        "nav": "#150d06", "card": "#24170c", "text": "#fffbeb",
        "muted": "#cfa876", "accent": "#F59E0B", "accent2": "#78350F", "btn_text": "#1f140a",
        "dopamine": "width:120px;height:14px;background:linear-gradient(90deg,#F59E0B,#78350F);border-radius:7px;display:inline-block;margin-right:16px;"
    },
    {
        "id": "bubblegumgrunge",
        "name": "Bubblegum Grunge",
        "tagline": "Charcoal concrete splashed with bubblegum and cyan.",
        "desc": "Bubblegum Grunge smears the Direction 53 layout with hot pink and cyan against dirty charcoal.",
        "palette": ["#1F1A24", "#EC4899", "#22D3EE"],
        "shapes": ["logo-square", "pink-bar", "cyan-splash"],
        "body1": "#1F1A24", "body2": "#28222e",
        "nav": "#17131c", "card": "#221d27", "text": "#fff0f8",
        "muted": "#c996b3", "accent": "#EC4899", "accent2": "#22D3EE", "btn_text": "#1f1a24",
        "dopamine": "width:80px;height:80px;background:linear-gradient(135deg,#EC4899,#22D3EE);clip-path:polygon(50% 0%,100% 50%,50% 100%,0% 50%);display:inline-block;margin-right:16px;"
    },
    {
        "id": "forestfunk",
        "name": "Forest Funk",
        "tagline": "Dark forest floor with moss and earth sparks.",
        "desc": "Forest Funk grounds the Direction 53 layout in dark forest green and accents it with moss and stone.",
        "palette": ["#0F1F15", "#86EFAC", "#A8A29E"],
        "shapes": ["logo-square", "moss-bar", "stone-dot"],
        "body1": "#0F1F15", "body2": "#152a1d",
        "nav": "#0a160f", "card": "#12241a", "text": "#f0fdf4",
        "muted": "#8fb89d", "accent": "#86EFAC", "accent2": "#A8A29E", "btn_text": "#0f1f15",
        "dopamine": "width:100px;height:14px;border-radius:7px;background:repeating-linear-gradient(90deg,#86EFAC,#86EFAC 8px,#A8A29E 8px,#A8A29E 16px);display:inline-block;margin-right:16px;"
    },
]

def build_css(t):
    return f"""

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* {{ box-sizing: border-box; }}
body {{
    margin: 0; font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, {t['body1']} 0%, {t['body2']} 100%);
    color: {t['text']};
    min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden;
}}
.logo-square {{
    position: fixed; top: 24px; left: 24px;
    width: 110px; height: 110px; background: {t['card']}; color: {t['text']};
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em;
    font-weight: 700; text-transform: uppercase; text-align: center;
    border-left: 6px solid {t['accent']};
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
    z-index: 100; pointer-events: none;
}}
.showcase-nav {{
    display: flex; justify-content: space-between; align-items: center;
    padding: 18px 24px 18px 154px; background: {t['nav']};
    font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700;
}}
.showcase-nav a {{ color: {t['accent']}; text-decoration: none; }}
.wrap {{ flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }}
h1 {{ font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }}
.desc {{ color: {t['muted']}; margin-bottom: 40px; max-width: 560px; }}
.decay-card {{
    background: {t['card']}; padding: 28px; margin-bottom: 16px;
    position: relative; border-left: 6px solid {t['accent']};
    clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%);
}}
.gold-btn {{
    display: inline-block; padding: 14px 28px; background: {t['accent']};
    color: {t['btn_text']}; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none;
}}
.grid-line {{ height: 1px; background: repeating-linear-gradient(90deg, {t['accent']}, {t['accent']} 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }}
.peel {{ width: 100px; height: 100px; background: {t['card']}; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }}
.peel::after {{ content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid {t['accent']}; z-index: -1; opacity: 0.6; }}
.showcase-footer {{ padding: 20px 20px 20px 154px; background: {t['nav']}; color: {t['muted']}; text-align: center; }}
.dopamine {{ {t['dopamine']} }}
        """

CONTENT = """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="logo-square">Korvia</div>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Welcome. Order, pay, and manage — all through one QR ecosystem.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Direction accent</h2>
<div class="grid-line" style="width:80%"></div><div class="peel"></div><div class="dopamine"></div>
</div>
"""

def build_entry(t):
    css = build_css(t)
    return f'''    {{
        "id": "{t['id']}",
        "name": "{t['name']}",
        "tagline": "{t['tagline']}",
        "desc": "{t['desc']}",
        "palette": {t['palette']},
        "shapes": {t['shapes']},
        "css": """
{css}
        """,
        "content": """
{CONTENT}
        """
    }},'''

def main():
    target = Path("showcase/generate_showcase.py")
    text = target.read_text(encoding="utf-8")
    marker = "    }\n]\n\nBASE = \"\"\""
    if marker not in text:
        print("Marker not found")
        return
    insert = "\n".join(build_entry(t) for t in THEMES).rstrip() + "\n"
    new_text = text.replace(marker, "    },\n" + insert + "]\n\nBASE = \"\"\"")
    target.write_text(new_text, encoding="utf-8")
    print(f"Appended {len(THEMES)} color directions.")

if __name__ == "__main__":
    main()
