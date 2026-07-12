#!/usr/bin/env python3
"""Append 20 QR-inspired wordmark logo concepts (106-125)."""
from pathlib import Path

THEMES = [
    {
        "id": "qrkblock",
        "name": "QR K Block",
        "tagline": "The letter K built from QR modules.",
        "desc": "The Korvia wordmark with the K constructed from black-and-white QR code blocks.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "qr-k", "modules"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; display: inline-block; }
.logo-wordmark .k { display: inline-block; width: 1.1em; height: 1.1em; background: #f8fafc; position: relative; vertical-align: middle; margin-right: 0.1em; }
.logo-wordmark .k::before { content: ""; position: absolute; inset: 0; background-image: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrofinder",
        "name": "QR Finder O",
        "tagline": "The O in Korvia becomes a QR finder pattern.",
        "desc": "A wordmark where the letter O is replaced by a QR code finder square.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "finder-o", "square"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark .o { display: inline-block; width: 0.85em; height: 0.85em; border: 4px solid #f8fafc; border-radius: 0; position: relative; vertical-align: middle; margin: 0 0.05em; }
.logo-wordmark .o::before { content: ""; position: absolute; inset: 6px; border: 3px solid #f8fafc; }
.logo-wordmark .o::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 12px; height: 12px; background: #f8fafc; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "pixelkorvia",
        "name": "Pixel Korvia",
        "tagline": "Korvia rendered as crisp QR pixels.",
        "desc": "The wordmark uses a pixel-grid font treatment reminiscent of QR module arrays.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "pixel", "grid"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; text-shadow: 4px 4px 0 rgba(192,192,192,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrcorners",
        "name": "QR Corners",
        "tagline": "Three QR finder corners frame the wordmark.",
        "desc": "The Korvia wordmark is framed by the three signature QR finder-pattern corners.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "corners", "frame"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 18px; }
.logo-wrap::before, .logo-wrap::after, .logo-wrap .corner-br { content: ""; position: absolute; width: 28px; height: 28px; border-color: #C0C0C0; border-style: solid; }
.logo-wrap::before { top: 0; left: 0; border-width: 4px 0 0 4px; }
.logo-wrap::after { top: 0; right: 0; border-width: 4px 4px 0 0; }
.logo-wrap .corner-br { bottom: 0; right: 0; border-width: 0 4px 4px 0; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "scanframe",
        "name": "Scan Frame",
        "tagline": "A phone-style QR scanner frame around Korvia.",
        "desc": "The wordmark sits inside a pulsating QR scanner frame with corner brackets.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "scanner", "frame"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 24px 48px; border: 1px dashed rgba(192,192,192,0.4); }
.logo-wrap::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: #C0C0C0; animation: scan 2.5s ease-in-out infinite; }
@keyframes scan { 0%,100% { transform: translateY(0); opacity: 0.3; } 50% { transform: translateY(80px); opacity: 1; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "dotmatrix",
        "name": "Dot Matrix",
        "tagline": "Korvia dotted like a thermal QR printer.",
        "desc": "The wordmark is built from a dense dot matrix, evoking QR code modules.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "dots", "matrix"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; }
.logo-wordmark::after { content: ""; position: absolute; inset: -10px; background: radial-gradient(circle, rgba(192,192,192,0.3) 1px, transparent 1px); background-size: 6px 6px; opacity: 0.4; pointer-events: none; mask-image: linear-gradient(90deg, transparent, black 10%, black 90%, transparent); -webkit-mask-image: linear-gradient(90deg, transparent, black 10%, black 90%, transparent); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrmosaic",
        "name": "QR Mosaic",
        "tagline": "The letters emerge from a mosaic of QR modules.",
        "desc": "A mosaic of small squares forms the negative space around the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "mosaic", "modules"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 20px 40px; background: linear-gradient(90deg, transparent 0%, rgba(20,30,50,0.85) 20%, rgba(20,30,50,0.85) 80%, transparent 100%); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wrap::before { content: ""; position: absolute; inset: 0; background-image: repeating-linear-gradient(0deg, rgba(192,192,192,0.15) 0px, rgba(192,192,192,0.15) 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, rgba(192,192,192,0.15) 0px, rgba(192,192,192,0.15) 4px, transparent 4px, transparent 8px); pointer-events: none; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "stylizedk",
        "name": "Stylized K",
        "tagline": "A single lettermark K made of QR modules.",
        "desc": "A bold K lettermark built entirely from QR-style squares, paired with a clean Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lettermark", "k", "modules"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-mark { display: inline-block; width: 1.2em; height: 1.2em; background: #f8fafc; vertical-align: middle; margin-right: 0.15em; position: relative; }
.logo-mark::before { content: ""; position: absolute; inset: 0; background: #0a0f1e; clip-path: polygon(20% 0%, 40% 0%, 40% 40%, 70% 0%, 100% 0%, 55% 55%, 100% 100%, 70% 100%, 40% 60%, 40% 100%, 20% 100%, 20% 20%, 0% 40%, 0% 20%); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "concentricqr",
        "name": "Concentric QR",
        "tagline": "Concentric square rings echo QR finder patterns.",
        "desc": "The Korvia wordmark is paired with a concentric square ring mark inspired by QR finder patterns.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "rings", "finder"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 64px; height: 64px; border: 3px solid #f8fafc; display: grid; place-items: center; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 8px; border: 2px solid #f8fafc; }
.logo-mark::after { content: ""; width: 14px; height: 14px; background: #f8fafc; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "fragmentedqr",
        "name": "Fragmented QR",
        "tagline": "Korvia with fragmented QR blocks breaking away.",
        "desc": "The wordmark features small QR-style squares that appear to fragment and scatter.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "fragments", "scatter"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.fragment { position: absolute; width: 8px; height: 8px; background: #C0C0C0; }
.fragment:nth-child(1) { top: 10%; right: -20px; }
.fragment:nth-child(2) { top: 40%; right: -35px; }
.fragment:nth-child(3) { bottom: 15%; right: -18px; }
.fragment:nth-child(4) { top: 20%; left: -25px; }
.fragment:nth-child(5) { bottom: 25%; left: -30px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "scanline",
        "name": "Scan Line",
        "tagline": "A horizontal laser scan line crosses Korvia.",
        "desc": "A glowing horizontal scan line moves across the wordmark like a QR scanner.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "scan", "laser"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.logo-wordmark::after { content: ""; position: absolute; left: 0; right: 0; height: 2px; background: #C0C0C0; box-shadow: 0 0 10px #C0C0C0; animation: scanline 2s ease-in-out infinite; }
@keyframes scanline { 0%,100% { top: 0; } 50% { top: 100%; } }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrspacing",
        "name": "QR Spacing",
        "tagline": "The letters are spaced by tiny QR modules.",
        "desc": "Small square modules separate the letters of Korvia, creating a QR-like rhythm.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "spacing", "modules"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
.logo-wordmark::after { content: ""; display: block; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 6px, transparent 6px, transparent 12px); margin-top: 8px; opacity: 0.7; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "finderdots",
        "name": "Finder Dots",
        "tagline": "The i-dots become QR finder squares.",
        "desc": "A subtle wordmark treatment where the dot of the i is a QR finder pattern square.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "dots", "finder"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark .dot { display: inline-block; width: 0.18em; height: 0.18em; background: #f8fafc; vertical-align: super; margin-left: -0.05em; position: relative; }
.logo-wordmark .dot::before { content: ""; position: absolute; inset: 3px; border: 1px solid #0a0f1e; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "modulargrid",
        "name": "Modular Grid",
        "tagline": "Each letter sits on a modular QR grid.",
        "desc": "The Korvia letters each rest inside their own square module cell.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "grid", "cells"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-wordmark span { display: inline-block; width: 1.1em; height: 1.1em; line-height: 1.1em; text-align: center; border: 1px solid rgba(192,192,192,0.3); margin: 0 2px; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrshadow",
        "name": "QR Shadow",
        "tagline": "The Korvia wordmark casts a QR module shadow.",
        "desc": "A clean wordmark with a shadow made of QR-style squares.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "shadow", "squares"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; text-shadow: 8px 8px 0 rgba(192,192,192,0.15); }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrshimmer",
        "name": "QR Shimmer",
        "tagline": "QR modules shimmer across the wordmark.",
        "desc": "The Korvia wordmark has a subtle animated shimmer of QR modules moving across it.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "shimmer", "animation"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; display: inline-block; }
.logo-wordmark::before { content: ""; position: absolute; inset: -10px; background: repeating-linear-gradient(90deg, transparent, transparent 10px, rgba(192,192,192,0.15) 10px, rgba(192,192,192,0.15) 14px); animation: shimmer 3s linear infinite; pointer-events: none; }
@keyframes shimmer { from { transform: translateX(-20px); } to { transform: translateX(20px); } }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qr3d",
        "name": "3D QR Block",
        "tagline": "A dimensional QR block sits beside Korvia.",
        "desc": "A 3D-style QR cube mark paired with the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "cube", "3d"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 60px; height: 60px; background: #f8fafc; position: relative; transform: rotateX(15deg) rotateY(-15deg); box-shadow: 8px 8px 0 rgba(192,192,192,0.3); flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 6px; background: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 5px, transparent 5px, transparent 10px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 5px, transparent 5px, transparent 10px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "circularqr",
        "name": "Circular QR",
        "tagline": "QR modules arranged in a circle around Korvia.",
        "desc": "A circular ring of QR-style modules surrounds the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "circle", "ring"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding: 30px; }
.logo-wrap::before { content: ""; position: absolute; inset: 0; border-radius: 50%; border: 2px dashed rgba(192,192,192,0.4); }
.logo-wrap::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 90%; border-radius: 50%; border: 8px dotted rgba(192,192,192,0.5); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; position: relative; z-index: 1; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrmerge",
        "name": "QR Merge",
        "tagline": "The QR pattern merges into the Korvia letterforms.",
        "desc": "A gradient transition where QR modules dissolve into the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "merge", "transition"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; background: linear-gradient(90deg, rgba(192,192,192,0.2) 0%, #f8fafc 30%, #f8fafc 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "minimalqr",
        "name": "Minimal QR",
        "tagline": "The smallest possible QR nod in a clean wordmark.",
        "desc": "A minimal, refined Korvia wordmark with a single subtle QR square accent.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "minimal", "square"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: 0.12em; text-transform: uppercase; }
.logo-wordmark::after { content: ""; display: inline-block; width: 10px; height: 10px; background: #C0C0C0; margin-left: 8px; vertical-align: super; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrtag",
        "name": "QR Tag",
        "tagline": "Korvia sits on a price-tag-shaped QR plate.",
        "desc": "The wordmark is paired with a QR code tag shape reminiscent of retail and hospitality labels.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "tag", "label"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 56px; height: 80px; background: #f8fafc; clip-path: polygon(0 0, 100% 0, 100% 75%, 50% 100%, 0 75%); position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; top: 8px; left: 50%; transform: translateX(-50%); width: 8px; height: 8px; border-radius: 50%; background: #0a0f1e; }
.logo-mark::after { content: ""; position: absolute; top: 24px; left: 8px; right: 8px; bottom: 18px; background: repeating-linear-gradient(0deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px), repeating-linear-gradient(90deg, #0a0f1e 0px, #0a0f1e 4px, transparent 4px, transparent 8px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrbadge",
        "name": "QR Badge",
        "tagline": "A circular badge with a QR pattern holds the K.",
        "desc": "A circular badge containing a QR pattern and the letter K, next to the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "badge", "circle"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 70px; height: 70px; border-radius: 50%; background: #f8fafc; display: grid; place-items: center; font-family: 'Cinzel', serif; font-size: 1.8rem; font-weight: 700; color: #0a0f1e; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 6px; border-radius: 50%; border: 2px dashed #0a0f1e; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "binaryqr",
        "name": "Binary QR",
        "tagline": "Binary code streams into the Korvia wordmark.",
        "desc": "A tech-forward wordmark with binary digits and QR modules flowing behind the text.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "binary", "stream"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; }
.logo-wrap::before { content: "10110010 01101011 01101111 01110010 01110110 01101001 01100001"; position: absolute; top: -14px; left: 0; font-family: monospace; font-size: 0.55rem; color: rgba(192,192,192,0.35); letter-spacing: 0.1em; white-space: nowrap; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrpath",
        "name": "QR Path",
        "tagline": "A path of QR modules leads to Korvia.",
        "desc": "Small QR squares form a dotted path leading into the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "path", "trail"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { position: relative; display: inline-block; padding-left: 50px; }
.logo-wrap::before { content: ""; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 40px; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 6px, transparent 6px, transparent 12px); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrstack",
        "name": "QR Stack",
        "tagline": "Stacked QR squares form a monogram beside Korvia.",
        "desc": "A monogram of stacked QR squares sits next to the Korvia wordmark.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "stack", "monogram"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { display: grid; grid-template-columns: repeat(2, 18px); gap: 4px; flex-shrink: 0; }
.logo-mark span { width: 18px; height: 18px; background: #f8fafc; }
.logo-mark span:nth-child(2), .logo-mark span:nth-child(3) { background: rgba(192,192,192,0.4); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qrkmonogram",
        "name": "QR K Monogram",
        "tagline": "A monogram where K and QR become one shape.",
        "desc": "A compact monogram combining the letter K with a QR finder pattern.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["monogram", "k", "finder"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wrap { display: inline-flex; align-items: center; gap: 16px; }
.logo-mark { width: 64px; height: 64px; border: 4px solid #f8fafc; display: grid; place-items: center; font-family: 'Cinzel', serif; font-size: 1.6rem; font-weight: 700; color: #f8fafc; position: relative; flex-shrink: 0; }
.logo-mark::before { content: ""; position: absolute; inset: 8px; border: 3px solid #f8fafc; }
.logo-mark::after { content: ""; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 12px; height: 12px; background: #f8fafc; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
    {
        "id": "qroutline",
        "name": "QR Outline",
        "tagline": "The Korvia letters are outlined with QR module corners.",
        "desc": "An outline wordmark where each letter is traced by QR-style corner brackets.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["wordmark", "outline", "corners"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; -webkit-text-stroke: 1px #f8fafc; color: transparent; }
.showcase-nav { display: flex; justify-content: space-between; align-items: center; padding: 18px 24px; background: rgba(10,15,30,0.8); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 700; }
.showcase-nav a { color: #C0C0C0; text-decoration: none; }
.wrap { flex: 1; max-width: 1000px; margin: 0 auto; padding: 48px 24px; width: 100%; }
h1 { font-family: 'Cinzel', serif; font-size: clamp(2rem, 5vw, 3.5rem); margin: 0 0 12px; }
.desc { color: #cbd5e1; margin-bottom: 40px; max-width: 560px; }
.decay-card { background: rgba(20,30,50,0.85); padding: 28px; margin-bottom: 16px; position: relative; border-left: 6px solid #C0C0C0; clip-path: polygon(0% 2%, 100% 0%, 98% 100%, 2% 98%); }
.gold-btn { display: inline-block; padding: 14px 28px; background: #C0C0C0; color: #0a0f1e; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 700; cursor: pointer; border: none; }
.grid-line { height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0, #C0C0C0 20px, transparent 20px, transparent 30px); margin-bottom: 24px; }
.showcase-footer { padding: 20px; background: rgba(10,15,30,0.8); color: #94a3b8; text-align: center; }
        """,
    },
]

CONTENT = """
<style>
.portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin: 24px 0; }
a { text-decoration: none; color: inherit; }
</style>
<div class="wrap">
<div style="text-align:right;margin-bottom:16px;"><button class="gold-btn">Options</button></div>
<div class="logo-wrap"><span class="logo-mark"></span><span class="logo-wordmark">Korvia</span></div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">QR-inspired wordmark concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Logo accent</h2>
<div class="grid-line" style="width:80%"></div>
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
    print(f"Appended {len(THEMES)} QR wordmark logo concepts.")

if __name__ == "__main__":
    main()
