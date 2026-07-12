#!/usr/bin/env python3
"""Append 17 creative color/filter variations of Direction 53 (slides 69-85)."""
from pathlib import Path

THEMES = [
    {
        "id": "duotone",
        "name": "Duotone Fire",
        "tagline": "High-contrast black and red duotone burn.",
        "desc": "Duotone Fire pushes the Direction 53 layout into a stark black-and-red duotone with boosted contrast.",
        "palette": ["#000000", "#FF2200", "#FFFFFF"],
        "shapes": ["logo-square", "red-dot", "contrast-boost"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #000; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF2200; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #000; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF2200; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; filter: contrast(1.25); }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0a0a0a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF2200; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF2200; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF2200, #FF2200 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0a0a0a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF2200; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #000; color: #777; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: #FF2200; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "noisefield",
        "name": "Noise Field",
        "tagline": "Analog noise over a red-black signal.",
        "desc": "Noise Field layers analog film grain over the Direction 53 layout for a textured, broadcast feel.",
        "palette": ["#0A0A0A", "#E42718", "#444"],
        "shapes": ["logo-square", "noise-overlay", "red-bar"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #f4f3ef; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.12'/%3E%3C/svg%3E"); pointer-events: none; z-index: 200; opacity: 0.35; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #f4f3ef; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a89f7e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #1a1a1a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #e42718; color: #1a1510; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #1a1a1a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #6b5b3e; text-align: center; }
.dopamine { width: 120px; height: 16px; background: #e42718; opacity: 0.8; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "glassmorphism",
        "name": "Glassmorphism",
        "tagline": "Frosted glass cards over a red glow.",
        "desc": "Glassmorphism turns the Direction 53 cards into translucent frosted panels with a soft red aura.",
        "palette": ["#0F0505", "#E42718", "#FFFFFF"],
        "shapes": ["logo-square", "glass-card", "red-glow"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 20% 20%, #2a0a0a 0%, #0a0505 60%); color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(255,255,255,0.06); backdrop-filter: blur(10px); color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid rgba(228,39,24,0.85); clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 8px 32px rgba(228,39,24,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,5,5,0.6); backdrop-filter: blur(8px); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d4c5a9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(255,255,255,0.05); backdrop-filter: blur(12px); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid rgba(228,39,24,0.8); clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: rgba(228,39,24,0.9); color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, rgba(228,39,24,0.8), rgba(228,39,24,0.8) 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(255,255,255,0.05); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid rgba(228,39,24,0.6); z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,5,5,0.6); color: #a89f7e; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: rgba(228,39,24,0.25); backdrop-filter: blur(6px); border: 1px solid rgba(228,39,24,0.5); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "halftone",
        "name": "Halftone Hero",
        "tagline": "Comic-book halftone dots over red ink.",
        "desc": "Halftone Hero prints the Direction 53 layout like a comic cover with red halftone dots and bold contrast.",
        "palette": ["#F4F3EF", "#E42718", "#111"],
        "shapes": ["logo-square", "halftone-dots", "red-ink"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #f4f3ef; color: #111; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle, #e42718 1px, transparent 1.5px); background-size: 10px 10px; opacity: 0.12; pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #111; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #e42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #e42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #e42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #e42718, #e42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #e42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #777; text-align: center; }
.dopamine { width: 80px; height: 80px; border-radius: 50%; background: radial-gradient(circle, #e42718 20%, transparent 25%); background-size: 8px 8px; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "crtlines",
        "name": "CRT Lines",
        "tagline": "Retro CRT scanlines with a red cursor.",
        "desc": "CRT Lines renders the Direction 53 layout on an old monitor with scanlines and a glowing red accent.",
        "palette": ["#050505", "#FF2A2A", "#33FF33"],
        "shapes": ["logo-square", "scanlines", "red-cursor"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #e8ffe8; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,0,0,0.4) 2px, rgba(0,0,0,0.4) 4px); pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #0a0a0a; color: #33ff33; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF2A2A; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; text-shadow: 0 0 6px #33ff33; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #080808; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF2A2A; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 0 0 8px #33ff33; }
.desc { color: #7f9e7f; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0d0d0d; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF2A2A; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF2A2A; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF2A2A, #FF2A2A 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d0d0d; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF2A2A; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #080808; color: #4a6b4a; text-align: center; }
.dopamine { width: 14px; height: 70px; background: #33ff33; box-shadow: 0 0 10px #33ff33; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "vhs",
        "name": "VHS Glitch",
        "tagline": "Tracking error colors and chromatic drift.",
        "desc": "VHS Glitch smears the Direction 53 layout with cyan/magenta drift and tracking-bar energy.",
        "palette": ["#0A0A0A", "#00F0FF", "#FF00AA"],
        "shapes": ["logo-square", "tracking-bar", "chromatic-drift"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #111; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #00F0FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; text-shadow: 3px 0 #FF00AA, -3px 0 #00F0FF; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00F0FF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 3px 0 #FF00AA, -3px 0 #00F0FF; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #00F0FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #00F0FF; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #00F0FF, #00F0FF 20px, #FF00AA 20px, #FF00AA 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF00AA; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #777; text-align: center; }
.dopamine { width: 120px; height: 10px; background: linear-gradient(90deg, #00F0FF, #FF00AA); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "aurora",
        "name": "Aurora Borealis",
        "tagline": "Slow-moving northern lights behind the layout.",
        "desc": "Aurora Borealis places the Direction 53 layout over a shifting green-purple-blue glow.",
        "palette": ["#0A0F14", "#2DD4BF", "#A855F7"],
        "shapes": ["logo-square", "aurora-glow", "shimmer-pill"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0f14; color: #e6fffa; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(120deg, #0a0f14, #2dd4bf33, #a855f733, #0a0f14); background-size: 300% 300%; animation: aurora 10s ease infinite; pointer-events: none; z-index: -1; }
@keyframes aurora { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(10,15,20,0.8); color: #e6fffa; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #2DD4BF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,20,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #2DD4BF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #9bd5c9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(10,15,20,0.75); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #2DD4BF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #2DD4BF; color: #0a0f14; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #2DD4BF, #2DD4BF 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(10,15,20,0.75); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #A855F7; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,20,0.7); color: #7aa3a8; text-align: center; }
.dopamine { width: 90px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #2DD4BF, #A855F7); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "pasteldream",
        "name": "Pastel Dream",
        "tagline": "Soft gradients for a calm dopamine hit.",
        "desc": "Pastel Dream wraps the Direction 53 layout in lavender, blush, and mint gradients for a gentle feel.",
        "palette": ["#FFF0F5", "#FFB7B2", "#B5EAD7"],
        "shapes": ["logo-square", "pastel-pill", "soft-glow"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #fff0f5 0%, #e0f7fa 100%); color: #4a3b3b; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #4a3b3b; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFB7B2; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 6px 18px rgba(255,183,178,0.3); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF8A80; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #8a7070; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFB7B2; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); box-shadow: 0 4px 14px rgba(255,183,178,0.2); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFB7B2; color: #4a3b3b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFB7B2, #FFB7B2 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; box-shadow: 0 4px 14px rgba(181,234,215,0.3); }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B5EAD7; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.7); color: #9e8585; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: linear-gradient(135deg, #FFB7B2, #B5EAD7); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "highcontrast",
        "name": "High Contrast",
        "tagline": "Black, white, and one red accent only.",
        "desc": "High Contrast strips the Direction 53 layout to pure black, pure white, and a single red accent.",
        "palette": ["#000000", "#FFFFFF", "#E42718"],
        "shapes": ["logo-square", "red-slash", "white-card"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #000; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #000; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; color: #fff; }
.desc { color: #ccc; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; color: #000; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #555; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 35px solid transparent; border-right: 35px solid transparent; border-bottom: 70px solid #E42718; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "neongrid",
        "name": "Neon Grid",
        "tagline": "Red square locked inside a glowing grid.",
        "desc": "Neon Grid lays a glowing red wireframe behind the Direction 53 layout.",
        "palette": ["#050505", "#E42718", "#330a0a"],
        "shapes": ["logo-square", "neon-grid", "red-wire"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #050505; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(90deg, rgba(228,39,24,0.15) 1px, transparent 1px), linear-gradient(rgba(228,39,24,0.15) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #0a0a0a; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 0 20px rgba(228,39,24,0.4); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #080808; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #aaa; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #0d0d0d; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #000; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #0d0d0d; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #080808; color: #777; text-align: center; }
.dopamine { width: 60px; height: 60px; background: #0a0a0a; border: 2px solid #E42718; box-shadow: 0 0 12px #E42718; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "sunsetbleed",
        "name": "Sunset Bleed",
        "tagline": "Warm sunset tones bleeding across the page.",
        "desc": "Sunset Bleed washes the Direction 53 layout in orange, coral, and plum gradients.",
        "palette": ["#2A0F0F", "#FF6B35", "#5C2A32"],
        "shapes": ["logo-square", "sunset-gradient", "coral-pill"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #2a0f0f 0%, #4a1a1a 50%, #5c2a32 100%); color: #fff5f0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(40,15,15,0.85); color: #fff5f0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF6B35; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(30,10,10,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF6B35; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #e8b8a8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(40,15,15,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF6B35; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF6B35; color: #2a0f0f; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF6B35, #FF6B35 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(40,15,15,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF6B35; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(30,10,10,0.8); color: #b5857a; text-align: center; }
.dopamine { width: 90px; height: 90px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #FF6B35, #5c2a32); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "noirfilm",
        "name": "Noir Film",
        "tagline": "Black-and-white cinema with one red accent.",
        "desc": "Noir Film turns the Direction 53 layout into a grayscale movie frame with a single red accent.",
        "palette": ["#0A0A0A", "#E42718", "#D4D4D4"],
        "shapes": ["logo-square", "film-grain", "red-accent"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #d4d4d4; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; filter: grayscale(100%); }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #d4d4d4; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #999; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #E42718; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #777; text-align: center; }
.dopamine { width: 100px; height: 12px; background: #E42718; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "popartfilter",
        "name": "Pop Art Filter",
        "tagline": "Bold primary colors and comic energy over the final layout.",
        "desc": "Pop Art gives the Direction 53 layout a Roy Lichtenstein treatment with primary colors and Ben-Day dots.",
        "palette": ["#FFFBEA", "#E42718", "#3B82F6"],
        "shapes": ["logo-square", "ben-day-dots", "primary-burst"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #fffbea; color: #111; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle, #3b82f6 1.5px, transparent 2px); background-size: 12px 12px; opacity: 0.12; pointer-events: none; z-index: 200; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #111; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; border: 3px solid #111; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; border-bottom: 3px solid #111; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; border: 3px solid #111; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: 3px solid #111; }
.grid-line { height: 4px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, #3B82F6 20px, #3B82F6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; border: 3px solid #111; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; background: #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; border-top: 3px solid #111; color: #555; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle, #E42718 25%, transparent 30%); background-size: 10px 10px; border: 3px solid #111; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "acidinvert",
        "name": "Acid Invert",
        "tagline": "Inverted acid green with a black accent.",
        "desc": "Acid Invert flips the Direction 53 layout into a toxic green world with black cutouts.",
        "palette": ["#CCFF00", "#000000", "#1A1A1A"],
        "shapes": ["logo-square", "acid-green", "black-cutout"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #CCFF00; color: #000; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #000; color: #CCFF00; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #fff; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #b8e600; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #000; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #333; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #000; color: #CCFF00; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #fff; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #000; color: #CCFF00; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: 2px solid #000; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #000, #000 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #000; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #fff; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #b8e600; color: #333; text-align: center; }
.dopamine { width: 80px; height: 80px; background: #000; clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "sepiawarm",
        "name": "Sepia Warm",
        "tagline": "Old photograph warmth with a red seal.",
        "desc": "Sepia Warm gives the Direction 53 layout an aged-photo feel with brown tones and a red wax seal accent.",
        "palette": ["#2A1F18", "#E42718", "#C5A059"],
        "shapes": ["logo-square", "sepia-filter", "wax-seal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1f18; color: #f4e4d4; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; filter: sepia(0.4); }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3a2a20; color: #f4e4d4; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #221712; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c9b49e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3a2a20; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C5A059; color: #2a1f18; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C5A059, #C5A059 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3a2a20; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #221712; color: #a08b76; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: #E42718; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "bluemonotone",
        "name": "Blue Monotone",
        "tagline": "Every tone is a shade of blue.",
        "desc": "Blue Monotone dyes the entire Direction 53 layout in a single blue family.",
        "palette": ["#0A1628", "#3B82F6", "#93C5FD"],
        "shapes": ["logo-square", "blue-wash", "monotone-bar"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a1628; color: #dbeafe; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #112240; color: #dbeafe; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #3B82F6; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #081020; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #3B82F6; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; filter: saturate(0.7); }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #93c5fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #112240; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #3B82F6; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #3B82F6, #3B82F6 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #112240; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #3B82F6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #081020; color: #93c5fd; text-align: center; }
.dopamine { width: 100px; height: 12px; background: linear-gradient(90deg, #3B82F6, #93C5FD); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "holographic",
        "name": "Holographic",
        "tagline": "Iridescent shimmer over dark chrome.",
        "desc": "Holographic coats the Direction 53 layout in shifting rainbow sheen and silver type.",
        "palette": ["#0A0A0A", "#C0C0C0", "#E42718"],
        "shapes": ["logo-square", "holo-sheen", "chrome-text"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #e0e0e0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(120deg, rgba(255,0,85,0.15), rgba(0,240,255,0.15), rgba(120,255,120,0.15), rgba(255,0,85,0.15)); background-size: 300% 300%; animation: holo 6s linear infinite; pointer-events: none; z-index: -1; }
@keyframes holo { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #e0e0e0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #E42718; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; background: linear-gradient(90deg, #c0c0c0, #fff, #c0c0c0); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.desc { color: #999; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #151515; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #E42718; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: linear-gradient(90deg, #c0c0c0, #fff, #c0c0c0); color: #0a0a0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #E42718, #E42718 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #151515; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #E42718; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #888; text-align: center; }
.dopamine { width: 90px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #ff0055, #00f0ff, #78ff78, #ff0055); background-size: 200% auto; animation: holo 3s linear infinite; display: inline-block; margin-right: 16px; }
        """,
    },
]

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
    return f'''    {{
        "id": "{t['id']}",
        "name": "{t['name']}",
        "tagline": "{t['tagline']}",
        "desc": "{t['desc']}",
        "palette": {t['palette']},
        "shapes": {t['shapes']},
        "css": """
{t['css']}
        """,
        "content": """
{CONTENT}
        """
    }},'''

def main():
    target = Path("showcase/generate_showcase.py")
    text = target.read_text(encoding="utf-8")
    marker = "    },\n]\n\nBASE = \"\"\""
    if marker not in text:
        print("Marker not found")
        return
    insert = "\n".join(build_entry(t) for t in THEMES).rstrip() + "\n"
    new_text = text.replace(marker, "    },\n" + insert + "]\n\nBASE = \"\"\"")
    target.write_text(new_text, encoding="utf-8")
    print(f"Appended {len(THEMES)} creative color directions.")

if __name__ == "__main__":
    main()
