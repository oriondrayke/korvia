#!/usr/bin/env python3
"""Append 20 creative, less-red madness directions (86-105)."""
from pathlib import Path

THEMES = [
    {
        "id": "fireflies",
        "name": "Fireflies",
        "tagline": "Glowing fireflies drift through a warm night.",
        "desc": "Fireflies fills the Direction 53 layout with slow-moving yellow-green glow orbs in a dark meadow.",
        "palette": ["#0F1A0F", "#ADFF2F", "#1A2E1A"],
        "shapes": ["logo-square", "firefly-orb", "meadow"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 50% 100%, #1a2e1a 0%, #0f1a0f 60%); color: #f0ffe6; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 20% 60%, rgba(173,255,47,0.2) 0%, transparent 3%), radial-gradient(circle at 70% 30%, rgba(173,255,47,0.25) 0%, transparent 4%), radial-gradient(circle at 40% 80%, rgba(173,255,47,0.15) 0%, transparent 2%); animation: drift 8s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes drift { from { transform: translate(0,0); } to { transform: translate(20px,-15px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #162b16; color: #f0ffe6; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #ADFF2F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #121f12; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #ADFF2F; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b8e08a; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #162b16; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #ADFF2F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #ADFF2F; color: #0f1a0f; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #ADFF2F, #ADFF2F 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #162b16; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #ADFF2F; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #121f12; color: #8fb86e; text-align: center; }
.dopamine { width: 16px; height: 16px; border-radius: 50%; background: #ADFF2F; box-shadow: 0 0 12px #ADFF2F; animation: pulse 2s infinite; display: inline-block; margin-right: 16px; }
@keyframes pulse { 0%,100% { opacity: 0.6; } 50% { opacity: 1; } }
        """,
    },
    {
        "id": "blinkingstars",
        "name": "Blinking Stars",
        "tagline": "A navy sky full of twinkling stars.",
        "desc": "Blinking Stars places the Direction 53 layout under a deep navy sky with twinkling star dots.",
        "palette": ["#0A0F1E", "#FFE4B5", "#1E293B"],
        "shapes": ["logo-square", "twinkle-star", "night-sky"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(ellipse at bottom, #1e293b 0%, #0a0f1e 100%); color: #fffbeb; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background-image: radial-gradient(#ffe4b5 1px, transparent 1px), radial-gradient(#ffe4b5 1px, transparent 1px); background-size: 60px 60px, 100px 100px; background-position: 0 0, 30px 30px; opacity: 0.25; animation: twinkle 3s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes twinkle { from { opacity: 0.15; } to { opacity: 0.35; } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(20,30,50,0.9); color: #fffbeb; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFE4B5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFE4B5; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #c4b5fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFE4B5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFE4B5; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFE4B5, #FFE4B5 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(20,30,50,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFE4B5; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,30,0.8); color: #a5b4fc; text-align: center; }
.dopamine { width: 24px; height: 24px; background: #FFE4B5; clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%); animation: twinkle 1.5s infinite alternate; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "wildflowers",
        "name": "Wildflowers",
        "tagline": "A soft meadow of colorful blooms.",
        "desc": "Wildflowers spreads a gentle green meadow behind the Direction 53 layout with scattered flower accents.",
        "palette": ["#F0FDF4", "#FF69B4", "#86EFAC"],
        "shapes": ["logo-square", "flower", "meadow"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #f0fdf4 0%, #dcfce7 100%); color: #14532d; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 15% 85%, rgba(255,105,180,0.25) 0%, transparent 6%), radial-gradient(circle at 75% 80%, rgba(250,204,21,0.25) 0%, transparent 5%), radial-gradient(circle at 45% 90%, rgba(139,92,246,0.2) 0%, transparent 7%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #14532d; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF69B4; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF69B4; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #3f6212; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF69B4; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #86EFAC; color: #14532d; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF69B4, #FF69B4 20px, #86EFAC 20px, #86EFAC 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #86EFAC; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #3f6212; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #FF69B4 30%, #86EFAC 31%, #86EFAC 45%, #FACC15 46%, #FACC15 55%, transparent 56%); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "lavablob",
        "name": "Lava Blob",
        "tagline": "Gooey lava-lamp blobs floating behind the cards.",
        "desc": "Lava Blob gives the Direction 53 layout a classic lava lamp feel with slow purple and orange blobs.",
        "palette": ["#1A0A1A", "#FF8C00", "#8B5CF6"],
        "shapes": ["logo-square", "blob", "lava"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0a1a; color: #fff7ed; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 30% 30%, rgba(255,140,0,0.35) 0%, transparent 25%), radial-gradient(circle at 70% 70%, rgba(139,92,246,0.35) 0%, transparent 25%); filter: blur(30px); animation: blobmove 10s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes blobmove { from { transform: scale(1) translate(0,0); } to { transform: scale(1.2) translate(-30px, 30px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a122a; color: #fff7ed; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f0f1f; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF8C00; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d8b4fe; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a122a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #8B5CF6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF8C00, #FF8C00 20px, #8B5CF6 20px, #8B5CF6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a122a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #8B5CF6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f0f1f; color: #c4b5fd; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #FF8C00, #8B5CF6); filter: blur(2px); animation: blobmove 4s ease-in-out infinite alternate; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "woodgrain",
        "name": "Wood Grain",
        "tagline": "Polished timber and warm copper hardware.",
        "desc": "Wood Grain gives the Direction 53 layout a rich timber surface with copper accents.",
        "palette": ["#3E2723", "#B87333", "#8D6E63"],
        "shapes": ["logo-square", "timber", "copper"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #3e2723; color: #efebe9; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(90deg, rgba(0,0,0,0.1) 0px, transparent 2px, rgba(255,255,255,0.05) 4px, transparent 8px); background-size: 60px 100%; opacity: 0.4; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #4e342e; color: #efebe9; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #B87333; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #2d1b18; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #B87333; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #d7ccc8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #4e342e; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #B87333; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #B87333; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #B87333, #B87333 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #4e342e; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #B87333; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #2d1b18; color: #a1887f; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #B87333, #5d4037); box-shadow: inset 0 0 10px rgba(0,0,0,0.5); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "brushedmetal",
        "name": "Brushed Metal",
        "tagline": "Cool steel with machined highlights.",
        "desc": "Brushed Metal turns the Direction 53 layout into a sheet of steel with a machined accent.",
        "palette": ["#212121", "#C0C0C0", "#607D8B"],
        "shapes": ["logo-square", "steel", "rivet"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #424242 0%, #212121 100%); color: #eceff1; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(255,255,255,0.05) 2px, rgba(255,255,255,0.05) 4px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #616161; color: #eceff1; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #212121; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #b0bec5; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #424242; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #212121; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #424242; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #C0C0C0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #212121; color: #90a4ae; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #E0E0E0, #616161); box-shadow: inset 0 0 8px rgba(0,0,0,0.5); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "glassblocks",
        "name": "Glass Blocks",
        "tagline": "Frosted glass bricks with cool light.",
        "desc": "Glass Blocks stacks translucent panels behind the Direction 53 layout with a soft blue glow.",
        "palette": ["#0A1A2E", "#87CEEB", "#1E3A8A"],
        "shapes": ["logo-square", "glass-brick", "blue-light"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a1a2e; color: #e0f2fe; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(90deg, rgba(135,206,235,0.1) 1px, transparent 1px), linear-gradient(rgba(135,206,235,0.1) 1px, transparent 1px); background-size: 80px 80px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(135,206,235,0.1); backdrop-filter: blur(8px); color: #e0f2fe; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #87CEEB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,26,46,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #87CEEB; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #bae6fd; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(135,206,235,0.1); backdrop-filter: blur(8px); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #87CEEB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #87CEEB; color: #0a1a2e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #87CEEB, #87CEEB 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(135,206,235,0.1); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #87CEEB; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,26,46,0.8); color: #bae6fd; text-align: center; }
.dopamine { width: 70px; height: 70px; background: rgba(135,206,235,0.2); backdrop-filter: blur(4px); border: 1px solid #87CEEB; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "shutters",
        "name": "Shutters",
        "tagline": "Sunlight cuts through window shutters.",
        "desc": "Shutters casts warm golden slats of light across the Direction 53 layout.",
        "palette": ["#2A1B0A", "#FFD700", "#8B4513"],
        "shapes": ["logo-square", "shutter-slat", "sunbeam"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1b0a; color: #fff8e1; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(75deg, rgba(255,215,0,0.15) 0px, rgba(255,215,0,0.15) 20px, transparent 20px, transparent 60px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3e2723; color: #fff8e1; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFD700; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f1408; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFD700; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #ffe082; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3e2723; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFD700; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFD700; color: #2a1b0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFD700, #FFD700 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3e2723; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFD700; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f1408; color: #c9a66b; text-align: center; }
.dopamine { width: 100px; height: 10px; background: #FFD700; box-shadow: 0 0 10px #FFD700; transform: rotate(-10deg); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "candlelight",
        "name": "Candlelight",
        "tagline": "Warm amber flicker in a dark room.",
        "desc": "Candlelight gives the Direction 53 layout a cozy, flickering amber glow.",
        "palette": ["#1A0F0A", "#FFAE42", "#5D4037"],
        "shapes": ["logo-square", "flame", "flicker"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0f0a; color: #fff3e0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 10%; left: 30%; width: 300px; height: 300px; border-radius: 50%; background: radial-gradient(circle, rgba(255,174,66,0.25) 0%, transparent 60%); animation: flicker 0.1s infinite alternate; pointer-events: none; z-index: -1; }
@keyframes flicker { from { opacity: 0.8; transform: scale(1); } to { opacity: 1; transform: scale(1.05); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a1a10; color: #fff3e0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFAE42; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1a0f0a; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFAE42; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #ffcc80; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a1a10; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFAE42; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFAE42; color: #1a0f0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFAE42, #FFAE42 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a1a10; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFAE42; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1a0f0a; color: #c7a07a; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-bottom: 60px solid #FFAE42; border-radius: 50%; filter: drop-shadow(0 0 8px #FFAE42); animation: flicker 0.2s infinite alternate; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "moonlight",
        "name": "Moonlight",
        "tagline": "Silver moon glow on a dark blue canvas.",
        "desc": "Moonlight washes the Direction 53 layout in cool silver moonbeams.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["logo-square", "crescent", "moonbeam"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(20,30,50,0.9); color: #f8fafc; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(20,30,50,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #C0C0C0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; box-shadow: inset -12px -5px 0 0 #C0C0C0; display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "rainonwindow",
        "name": "Rain on Window",
        "tagline": "Droplets sliding down dark glass.",
        "desc": "Rain on Window puts the Direction 53 layout behind a wet pane with sliding raindrops.",
        "palette": ["#0F172A", "#5F9EA0", "#334155"],
        "shapes": ["logo-square", "raindrop", "wet-glass"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); color: #e2e8f0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.08) 0%, transparent 3%), radial-gradient(circle at 70% 60%, rgba(255,255,255,0.06) 0%, transparent 2%), radial-gradient(circle at 50% 80%, rgba(255,255,255,0.07) 0%, transparent 4%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(30,41,59,0.9); color: #e2e8f0; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #5F9EA0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(15,23,42,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #5F9EA0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #94a3b8; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(30,41,59,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #5F9EA0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #5F9EA0; color: #0f172a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #5F9EA0, #5F9EA0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(30,41,59,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #5F9EA0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(15,23,42,0.8); color: #94a3b8; text-align: center; }
.dopamine { width: 20px; height: 30px; border-radius: 50%; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); box-shadow: inset 0 -5px 5px rgba(255,255,255,0.2); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "sunbeams",
        "name": "Sunbeams",
        "tagline": "Golden light rays cutting through dust.",
        "desc": "Sunbeams shoots warm light rays across the Direction 53 layout.",
        "palette": ["#2A1B0A", "#FFFACD", "#DAA520"],
        "shapes": ["logo-square", "ray", "dust"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #2a1b0a; color: #fffbe6; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: -50%; left: -20%; width: 140vw; height: 140vh; background: conic-gradient(from 0deg at 50% 0%, transparent 0deg, rgba(255,250,205,0.1) 20deg, transparent 40deg, rgba(255,250,205,0.08) 60deg, transparent 80deg); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #3e2c14; color: #fffbe6; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFFACD; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f1508; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFFACD; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #f3e5ab; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #3e2c14; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFFACD; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #DAA520; color: #2a1b0a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFFACD, #FFFACD 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #3e2c14; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #DAA520; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f1508; color: #c9a66b; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 15px solid transparent; border-right: 15px solid transparent; border-bottom: 100px solid rgba(255,250,205,0.3); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "confetti",
        "name": "Confetti",
        "tagline": "Colorful paper falling in celebration.",
        "desc": "Confetti rains bright colored paper over the Direction 53 layout.",
        "palette": ["#FFFFFF", "#FF00FF", "#00BFFF"],
        "shapes": ["logo-square", "confetti-piece", "celebration"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #fff; color: #222; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: linear-gradient(45deg, rgba(255,0,255,0.1) 25%, transparent 25%, transparent 50%, rgba(0,191,255,0.1) 50%, rgba(0,191,255,0.1) 75%, transparent 75%); background-size: 40px 40px; pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #f8f8f8; color: #222; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF00FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #fff; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00BFFF; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #555; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF00FF; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #00BFFF; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF00FF, #FF00FF 20px, #00BFFF 20px, #00BFFF 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF00FF; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #fff; color: #777; text-align: center; }
.dopamine { width: 16px; height: 8px; background: #FF00FF; transform: rotate(15deg); box-shadow: 20px 10px 0 #00BFFF, -10px 25px 0 #FFD700; display: inline-block; margin-right: 40px; }
        """,
    },
    {
        "id": "neonlightsign",
        "name": "Neon Light Sign",
        "tagline": "A pink neon tube hums behind the cards.",
        "desc": "Neon Light Sign gives the Direction 53 layout a buzzing pink neon glow against dark brick.",
        "palette": ["#1A0A14", "#FF10F0", "#2A1B1B"],
        "shapes": ["logo-square", "neon-tube", "brick"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #1a0a14; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: repeating-linear-gradient(0deg, rgba(255,16,240,0.05) 0px, transparent 2px, transparent 80px, rgba(255,16,240,0.05) 82px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #2a1224; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF10F0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; box-shadow: 0 0 20px rgba(255,16,240,0.3); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #1f0f1a; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FF10F0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; text-shadow: 0 0 12px #FF10F0; }
.desc { color: #f9a8d4; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #2a1224; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF10F0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FF10F0; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF10F0, #FF10F0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #2a1224; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FF10F0; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #1f0f1a; color: #f9a8d4; text-align: center; }
.dopamine { width: 100px; height: 8px; border-radius: 4px; background: #FF10F0; box-shadow: 0 0 12px #FF10F0; animation: buzz 1.5s infinite alternate; display: inline-block; margin-right: 16px; }
@keyframes buzz { from { opacity: 0.8; } to { opacity: 1; } }
        """,
    },
    {
        "id": "cherryblossom",
        "name": "Cherry Blossom",
        "tagline": "Pink petals drift across a soft sky.",
        "desc": "Cherry Blossom showers the Direction 53 layout with falling pink petals.",
        "palette": ["#FFF0F5", "#FFB7C5", "#FBCFE8"],
        "shapes": ["logo-square", "petal", "blossom"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #fff0f5 0%, #fce7f3 100%); color: #831843; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 20% 20%, #ffb7c5 0%, transparent 4%), radial-gradient(circle at 70% 40%, #fbcfe8 0%, transparent 3%), radial-gradient(circle at 40% 70%, #ffb7c5 0%, transparent 5%); opacity: 0.6; animation: fall 8s linear infinite; pointer-events: none; z-index: -1; }
@keyframes fall { 0% { transform: translateY(-20px) rotate(0deg); } 100% { transform: translateY(20px) rotate(10deg); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #831843; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFB7C5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #DB2777; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #be185d; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFB7C5; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #FFB7C5; color: #831843; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFB7C5, #FFB7C5 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #FFB7C5; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #be185d; text-align: center; }
.dopamine { width: 30px; height: 30px; border-radius: 50% 0 50% 50%; background: #FFB7C5; transform: rotate(-45deg); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "tropicalfruit",
        "name": "Tropical Fruit",
        "tagline": "Juicy citrus and berry colors.",
        "desc": "Tropical Fruit squeezes bright orange, lime, and berry juice into the Direction 53 layout.",
        "palette": ["#FFFBEB", "#FF8C00", "#84CC16"],
        "shapes": ["logo-square", "citrus", "juice"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 10% 20%, #fffbeb 0%, #fef3c7 100%); color: #451a03; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(circle at 80% 80%, rgba(255,140,0,0.15) 0%, transparent 25%), radial-gradient(circle at 20% 80%, rgba(132,204,22,0.15) 0%, transparent 25%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #451a03; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #84CC16; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #92400e; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FF8C00; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #84CC16; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FF8C00, #FF8C00 20px, #84CC16 20px, #84CC16 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #84CC16; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.8); color: #92400e; text-align: center; }
.dopamine { width: 70px; height: 70px; border-radius: 50%; background: repeating-conic-gradient(#FF8C00 0deg 10deg, #fff 10deg 20deg, #84CC16 20deg 30deg); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "northernlights",
        "name": "Northern Lights",
        "tagline": "Green and violet aurora waves.",
        "desc": "Northern Lights paints the Direction 53 layout with slow aurora ribbons.",
        "palette": ["#0A0F14", "#00FF7F", "#8B5CF6"],
        "shapes": ["logo-square", "aurora-ribbon", "wave"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0f14; color: #e6fffa; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; inset: 0; background: radial-gradient(ellipse at 50% 100%, rgba(0,255,127,0.25) 0%, transparent 40%), radial-gradient(ellipse at 30% 100%, rgba(139,92,246,0.2) 0%, transparent 35%); filter: blur(20px); animation: aurora 8s ease-in-out infinite alternate; pointer-events: none; z-index: -1; }
@keyframes aurora { 0% { transform: scaleY(1) translateY(0); } 100% { transform: scaleY(1.1) translateY(-20px); } }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: rgba(10,20,30,0.9); color: #e6fffa; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #00FF7F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(10,15,20,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #00FF7F; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #a7f3d0; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(10,20,30,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #00FF7F; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #8B5CF6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #00FF7F, #00FF7F 20px, #8B5CF6 20px, #8B5CF6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: rgba(10,20,30,0.85); display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #8B5CF6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(10,15,20,0.8); color: #a7f3d0; text-align: center; }
.dopamine { width: 100px; height: 14px; border-radius: 7px; background: linear-gradient(90deg, #00FF7F, #8B5CF6); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "citylights",
        "name": "City Lights",
        "tagline": "Bokeh skyline at night.",
        "desc": "City Lights blurs a distant downtown skyline behind the Direction 53 layout.",
        "palette": ["#0A0A0A", "#FFA500", "#3B82F6"],
        "shapes": ["logo-square", "bokeh", "skyline"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: #0a0a0a; color: #fff; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; bottom: 0; left: 0; right: 0; height: 50vh; background: radial-gradient(circle at 20% 80%, rgba(255,165,0,0.3) 0%, transparent 15%), radial-gradient(circle at 50% 70%, rgba(59,130,246,0.25) 0%, transparent 12%), radial-gradient(circle at 80% 85%, rgba(255,255,255,0.2) 0%, transparent 10%); filter: blur(15px); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #151515; color: #fff; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #FFA500; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: #0d0d0d; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #FFA500; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #fde68a; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #1a1a1a; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #FFA500; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #3B82F6; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #FFA500, #FFA500 20px, #3B82F6 20px, #3B82F6 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #1a1a1a; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #3B82F6; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: #0d0d0d; color: #93c5fd; text-align: center; }
.dopamine { width: 20px; height: 20px; border-radius: 50%; background: #FFA500; box-shadow: 0 0 12px #FFA500, 25px 10px 0 #3B82F6, -15px 20px 0 #fff; filter: blur(2px); display: inline-block; margin-right: 40px; }
        """,
    },
    {
        "id": "sanddunes",
        "name": "Sand Dunes",
        "tagline": "Warm desert curves and shadows.",
        "desc": "Sand Dunes shapes the Direction 53 layout from warm desert gradients and soft shadows.",
        "palette": ["#EDC9AF", "#D2691E", "#F4A460"],
        "shapes": ["logo-square", "dune", "desert"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: linear-gradient(180deg, #edc9af 0%, #d2691e 100%); color: #4a2511; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; bottom: 0; left: 0; right: 0; height: 60vh; background: radial-gradient(ellipse at 30% 100%, rgba(244,164,96,0.5) 0%, transparent 50%), radial-gradient(ellipse at 70% 100%, rgba(210,105,30,0.4) 0%, transparent 50%); pointer-events: none; z-index: -1; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #f5e6d3; color: #4a2511; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #D2691E; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(245,230,211,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #D2691E; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #7c3d16; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #f5e6d3; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #D2691E; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #D2691E; color: #fff; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #D2691E, #D2691E 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #f5e6d3; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #F4A460; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(245,230,211,0.8); color: #7c3d16; text-align: center; }
.dopamine { width: 0; height: 0; border-left: 60px solid transparent; border-right: 60px solid transparent; border-bottom: 30px solid rgba(210,105,30,0.4); display: inline-block; margin-right: 16px; }
        """,
    },
    {
        "id": "watercolor",
        "name": "Watercolor",
        "tagline": "Soft paint washes bleeding into each other.",
        "desc": "Watercolor softens the Direction 53 layout with pastel washes and gentle splashes.",
        "palette": ["#FDF2F8", "#9370DB", "#87CEFA"],
        "shapes": ["logo-square", "paint-splash", "wash"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700\u0026family=Cinzel:wght@400;700\u0026display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 20% 30%, rgba(147,112,219,0.2) 0%, transparent 30%), radial-gradient(circle at 80% 70%, rgba(135,206,250,0.25) 0%, transparent 35%), #fdf2f8; color: #4c1d95; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
.logo-square { position: fixed; top: 24px; left: 24px; width: 110px; height: 110px; background: #fff; color: #4c1d95; display: flex; align-items: center; justify-content: center; font-family: 'Cinzel', serif; font-size: 1rem; letter-spacing: 0.04em; font-weight: 700; text-transform: uppercase; text-align: center; border-left: 6px solid #9370DB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); z-index: 100; pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px 18px 154px; background: rgba(255,255,255,0.7); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #9370DB; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px 48px 154px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 7vw, 5rem); margin: 0 0 12px; }
.desc { color: #6d28d9; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: #fff; padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #9370DB; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #87CEFA; color: #1e3a8a; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #9370DB, #9370DB 20px, #87CEFA 20px, #87CEFA 40px); margin-bottom: 24px; }
.peel { width: 100px; height: 100px; background: #fff; display: inline-block; margin-right: 16px; margin-bottom: 24px; position: relative; }
.peel::after { content: ""; position: absolute; top: 8px; left: 8px; right: -8px; bottom: -8px; border: 1px solid #87CEFA; z-index: -1; opacity: 0.6; }
.showcase-footer { padding: 20px 20px 20px 154px; background: rgba(255,255,255,0.7); color: #6d28d9; text-align: center; }
.dopamine { width: 60px; height: 60px; border-radius: 50%; background: radial-gradient(circle, #9370DB 30%, #87CEFA 70%); filter: blur(2px); display: inline-block; margin-right: 16px; }
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
    print(f"Appended {len(THEMES)} pure-madness directions.")

if __name__ == "__main__":
    main()
