#!/usr/bin/env python3
"""Append 25 Korvia logo + tagline lockup concepts (133-157)."""
from pathlib import Path

THEMES = [
    {
        "id": "stackedtagline",
        "name": "Stacked Tagline",
        "tagline": "Korvia sits above Karibu, tukuhudumie in a clean stack.",
        "desc": "A vertical lockup with Korvia wordmark above the Swahili tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "stacked", "tagline"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; display: inline-block; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: clamp(0.9rem, 2.5vw, 1.3rem); letter-spacing: 0.25em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; }
.logo-lockup::after { content: ""; display: block; width: 60px; height: 2px; background: #C0C0C0; margin: 16px auto 0; }
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
        "id": "horizontallockup",
        "name": "Horizontal Lockup",
        "tagline": "Korvia and tagline sit on one line.",
        "desc": "A horizontal logo lockup with the tagline separated by a vertical rule.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "horizontal", "rule"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; align-items: center; gap: 20px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }
.logo-rule { width: 2px; height: 40px; background: #C0C0C0; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase; color: #94a3b8; line-height: 1.4; }
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
        "id": "framedlockup",
        "name": "Framed Lockup",
        "tagline": "Korvia and tagline inside a QR-corner frame.",
        "desc": "The logo and tagline are enclosed by QR finder-pattern corner brackets.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "frame", "corners"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 50px; }
.logo-lockup::before, .logo-lockup::after, .logo-lockup .corner-br { content: ""; position: absolute; width: 24px; height: 24px; border-color: #C0C0C0; border-style: solid; }
.logo-lockup::before { top: 0; left: 0; border-width: 4px 0 0 4px; }
.logo-lockup::after { top: 0; right: 0; border-width: 4px 4px 0 0; }
.logo-lockup .corner-br { bottom: 0; right: 0; border-width: 0 4px 4px 0; }
.logo-lockup .corner-bl { position: absolute; bottom: 0; left: 0; width: 24px; height: 24px; border-color: #C0C0C0; border-style: solid; border-width: 0 0 4px 4px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.8rem, 9vw, 5.5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; }
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
        "id": "badgelockup",
        "name": "Badge Lockup",
        "tagline": "Korvia inside a circular badge with tagline ribbon.",
        "desc": "A circular badge containing the Korvia wordmark with a ribbon-style tagline below.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "badge", "ribbon"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; flex-direction: column; align-items: center; }
.logo-badge { width: 160px; height: 160px; border-radius: 50%; border: 2px solid #C0C0C0; display: grid; place-items: center; position: relative; }
.logo-badge::before { content: ""; position: absolute; inset: 8px; border-radius: 50%; border: 1px dashed rgba(192,192,192,0.5); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: 1.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }
.logo-ribbon { background: #C0C0C0; color: #0a0f1e; padding: 8px 24px; font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; margin-top: -14px; z-index: 1; }
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
        "id": "twolinetagline",
        "name": "Two-Line Tagline",
        "tagline": "Karibu on one line, tukuhudumie on the next.",
        "desc": "The tagline is split into two lines for a more dramatic lockup.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "two-line", "dramatic"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; margin-bottom: 12px; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: clamp(0.8rem, 2vw, 1.1rem); letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; display: block; }
.logo-tagline span { display: block; }
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
        "id": "qrfullframe",
        "name": "QR Full Frame",
        "tagline": "The entire logo lockup sits inside a QR scanner frame.",
        "desc": "A full scanner frame with corner brackets encloses the Korvia wordmark and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "scanner", "frame"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 40px 60px; border: 1px dashed rgba(192,192,192,0.4); }
.logo-lockup::before { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: #C0C0C0; animation: scan 2.5s ease-in-out infinite; }
@keyframes scan { 0%,100% { transform: translateY(0); opacity: 0.3; } 50% { transform: translateY(110px); opacity: 1; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; text-align: center; }
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
        "id": "monogramlockup",
        "name": "Monogram Lockup",
        "tagline": "A K monogram anchors the full Korvia wordmark and tagline.",
        "desc": "A K monogram sits above or beside the full Korvia name and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "monogram", "k"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-flex; align-items: center; gap: 20px; }
.logo-monogram { width: 80px; height: 80px; background: #f8fafc; color: #0a0f1e; font-family: 'Cinzel', serif; font-size: 2.5rem; font-weight: 700; display: grid; place-items: center; }
.logo-text { display: flex; flex-direction: column; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2rem, 6vw, 4rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 4px; }
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
        "id": "swahilifirst",
        "name": "Swahili First",
        "tagline": "Karibu, tukuhudumie leads, Korvia follows.",
        "desc": "A reverse lockup where the Swahili tagline is primary and Korvia is secondary.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "swahili", "reverse"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-tagline { font-family: 'Cinzel', serif; font-size: clamp(1.4rem, 4vw, 2.5rem); font-weight: 400; letter-spacing: 0.12em; text-transform: uppercase; color: #C0C0C0; display: block; margin-bottom: 8px; }
.logo-wordmark { font-family: 'Inter', sans-serif; font-size: clamp(0.9rem, 2.5vw, 1.2rem); letter-spacing: 0.4em; text-transform: uppercase; color: #94a3b8; display: block; }
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
        "id": "qrruled",
        "name": "QR Ruled",
        "tagline": "Ruled lines connect the wordmark and tagline like a form.",
        "desc": "A technical, ruled layout with Korvia above and tagline below, connected by vertical lines.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "ruled", "technical"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-grid; grid-template-columns: 1fr auto 1fr; gap: 12px; align-items: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; grid-column: 1 / -1; text-align: center; border-bottom: 1px solid rgba(192,192,192,0.4); padding-bottom: 12px; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase; color: #94a3b8; grid-column: 1 / -1; text-align: center; padding-top: 8px; }
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
        "id": "qrmicro",
        "name": "QR Micro Tagline",
        "tagline": "The tagline is rendered in tiny QR modules.",
        "desc": "Korvia in full size with the tagline spelled out in small square modules below.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "micro", "modules"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.65rem; letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; }
.logo-tagline::after { content: ""; display: block; width: 100%; height: 6px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 4px, transparent 4px, transparent 8px); margin-top: 8px; opacity: 0.5; }
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
        "id": "ticketlockup",
        "name": "Ticket Lockup",
        "tagline": "Korvia and tagline on a hospitality ticket shape.",
        "desc": "A ticket-shaped container holds the Korvia wordmark and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "ticket", "hospitality"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; background: rgba(20,30,50,0.85); border: 1px solid rgba(192,192,192,0.3); padding: 24px 48px; position: relative; }
.logo-lockup::before, .logo-lockup::after { content: ""; position: absolute; top: 50%; transform: translateY(-50%); width: 20px; height: 20px; border-radius: 50%; background: #0a0f1e; border: 1px solid rgba(192,192,192,0.3); }
.logo-lockup::before { left: -10px; }
.logo-lockup::after { right: -10px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; text-align: center; }
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
        "id": "africanpattern",
       "name": "East African Pattern",
        "tagline": "A subtle kanga-pattern accent under the lockup.",
        "desc": "Korvia wordmark and tagline with a subtle East African geometric pattern band.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "pattern", "african"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-pattern { height: 12px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 8px, transparent 8px, transparent 16px, #C0C0C0 16px, #C0C0C0 20px, transparent 20px, transparent 28px); margin: 12px 0; opacity: 0.6; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; display: block; }
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
        "id": "moonandqr",
        "name": "Moon and QR",
        "tagline": "A crescent moon cradles the Korvia lockup.",
        "desc": "The Moonlight theme is echoed by a crescent shape behind the wordmark and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "moon", "crescent"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 50px; }
.logo-lockup::before { content: ""; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); width: 120px; height: 120px; border-radius: 50%; box-shadow: inset -20px 0 0 0 rgba(192,192,192,0.15); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; position: relative; z-index: 1; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; position: relative; z-index: 1; }
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
        "id": "glasscard",
        "name": "Glass Card",
        "tagline": "The lockup floats on a frosted glass card.",
        "desc": "Korvia and tagline on a translucent frosted card with a subtle QR grid behind.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "glass", "card"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; background: rgba(20,30,50,0.6); backdrop-filter: blur(8px); border: 1px solid rgba(192,192,192,0.2); padding: 36px 56px; border-radius: 4px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #cbd5e1; margin-top: 12px; display: block; text-align: center; }
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
        "id": "ruledbackground",
        "name": "Ruled Background",
        "tagline": "The lockup sits on the ruled Moonlight grid.",
        "desc": "Korvia and tagline aligned to a subtle ruled grid background.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "ruled", "grid"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; padding: 24px 0; border-top: 1px solid rgba(192,192,192,0.3); border-bottom: 1px solid rgba(192,192,192,0.3); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.25em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; }
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
        "id": "animatedscanlockup",
        "name": "Animated Scan Lockup",
        "tagline": "A scanning line animates across the full lockup.",
        "desc": "The Korvia wordmark and tagline with a continuous scanning animation.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "animation", "scan"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; text-align: center; }
.logo-lockup::after { content: ""; position: absolute; left: 0; right: 0; height: 2px; background: #C0C0C0; box-shadow: 0 0 8px #C0C0C0; animation: scanlock 2.5s ease-in-out infinite; }
@keyframes scanlock { 0%,100% { top: 0; } 50% { top: 100%; } }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; }
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
        "id": "minimaltagline",
        "name": "Minimal Tagline",
        "tagline": "The simplest possible Korvia + tagline treatment.",
        "desc": "A minimal lockup with generous spacing and a delicate tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "minimal", "spacious"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: 0.15em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.7rem; letter-spacing: 0.3em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; }
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
        "id": "boldtagline",
        "name": "Bold Tagline",
        "tagline": "A heavy, confident Korvia with a bold tagline.",
        "desc": "A bold, high-impact lockup with thick lettering and a strong tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "bold", "heavy"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3.2rem, 11vw, 7rem); font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; display: block; -webkit-text-stroke: 1px #f8fafc; color: transparent; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.85rem; letter-spacing: 0.2em; text-transform: uppercase; color: #C0C0C0; margin-top: 12px; display: block; font-weight: 700; }
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
        "id": "editoriallockup",
        "name": "Editorial Lockup",
        "tagline": "A magazine-style Korvia headline with tagline.",
        "desc": "An editorial layout with Korvia as a headline and the tagline as a byline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "editorial", "headline"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: left; max-width: 600px; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 400; letter-spacing: -0.02em; text-transform: uppercase; display: block; line-height: 0.95; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.9rem; letter-spacing: 0.1em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; font-style: italic; }
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
        "id": "stamplockup",
        "name": "Stamp Lockup",
        "tagline": "Korvia stamped in a rectangular seal with tagline.",
        "desc": "A stamp-like rectangular seal containing the Korvia wordmark and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "stamp", "seal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { display: inline-block; border: 3px solid #C0C0C0; padding: 20px 40px; position: relative; transform: rotate(-2deg); }
.logo-lockup::before { content: ""; position: absolute; inset: 4px; border: 1px solid #C0C0C0; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(2.5rem, 8vw, 5rem); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 8px; display: block; text-align: center; }
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
        "id": "neonlockup",
        "name": "Neon Lockup",
        "tagline": "Korvia and tagline glow like a neon sign.",
        "desc": "A neon-style treatment with glowing outlines for both wordmark and tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "neon", "glow"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; color: #f8fafc; text-shadow: 0 0 10px #C0C0C0, 0 0 20px #C0C0C0; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.25em; text-transform: uppercase; color: #C0C0C0; margin-top: 12px; display: block; text-shadow: 0 0 6px #C0C0C0; }
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
        "id": "embossedlockup",
        "name": "Embossed Lockup",
        "tagline": "Korvia and tagline look pressed into metal.",
        "desc": "An embossed effect with subtle highlights and shadows on the lockup.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "embossed", "metal"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; color: #e2e8f0; text-shadow: 1px 1px 0 rgba(255,255,255,0.2), -1px -1px 0 rgba(0,0,0,0.3); }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 12px; display: block; text-shadow: 1px 1px 0 rgba(255,255,255,0.1); }
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
        "id": "pixellockup",
        "name": "Pixel Lockup",
        "tagline": "Korvia and tagline in a pixelated arcade style.",
        "desc": "A pixelated treatment for both the wordmark and the tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "pixel", "arcade"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Press+Start+2P&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Press Start 2P', cursive; font-size: clamp(1.8rem, 6vw, 3.5rem); letter-spacing: 0.04em; text-transform: uppercase; display: block; line-height: 1.4; }
.logo-tagline { font-family: 'Press Start 2P', cursive; font-size: 0.55rem; letter-spacing: 0.1em; text-transform: uppercase; color: #94a3b8; margin-top: 16px; display: block; line-height: 1.6; }
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
        "id": "geometriclockup",
        "name": "Geometric Lockup",
        "tagline": "Korvia and tagline locked in a geometric construction.",
        "desc": "A geometric frame of circles and lines contains the Korvia lockup.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "geometric", "construction"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; padding: 30px 60px; }
.logo-lockup::before { content: ""; position: absolute; top: 0; bottom: 0; left: 20px; width: 1px; background: rgba(192,192,192,0.3); }
.logo-lockup::after { content: ""; position: absolute; top: 0; bottom: 0; right: 20px; width: 1px; background: rgba(192,192,192,0.3); }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; text-align: center; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; text-align: center; }
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
        "id": "signaturelockup",
        "name": "Signature Lockup",
        "tagline": "Korvia as a signature with a handwritten tagline.",
        "desc": "A signature-style wordmark with an elegant script tagline.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "signature", "script"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Dancing+Script:wght@700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { text-align: center; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; }
.logo-tagline { font-family: 'Dancing Script', cursive; font-size: clamp(1.2rem, 3vw, 2rem); color: #C0C0C0; margin-top: 4px; display: block; }
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
        "id": "qrradiant",
        "name": "QR Radiant",
        "tagline": "QR modules radiate outward from Korvia.",
        "desc": "The lockup sits at the center with radiating QR module lines.",
        "palette": ["#0A0F1E", "#C0C0C0", "#1E3A8A"],
        "shapes": ["lockup", "radiant", "lines"],
        "css": """

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Cinzel:wght@400;700&display=swap');
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Inter', sans-serif; background: radial-gradient(circle at 80% 20%, #1e3a8a 0%, #0a0f1e 40%); color: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
body::before { content: ""; position: fixed; top: 8%; right: 10%; width: 120px; height: 120px; border-radius: 50%; background: radial-gradient(circle, #e2e8f0 40%, transparent 45%); box-shadow: 0 0 60px rgba(226,232,240,0.3); pointer-events: none; z-index: -1; }
.logo-lockup { position: relative; display: inline-block; text-align: center; padding: 20px 40px; }
.logo-lockup::before { content: ""; position: absolute; top: 50%; left: -80px; right: -80px; height: 1px; background: repeating-linear-gradient(90deg, #C0C0C0 0px, #C0C0C0 4px, transparent 4px, transparent 8px); transform: translateY(-50%); opacity: 0.4; z-index: -1; }
.logo-wordmark { font-family: 'Cinzel', serif; font-size: clamp(3rem, 10vw, 6rem); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; display: block; position: relative; z-index: 1; }
.logo-tagline { font-family: 'Inter', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; text-transform: uppercase; color: #94a3b8; margin-top: 10px; display: block; position: relative; z-index: 1; }
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
<div class="logo-lockup">
  <span class="logo-wordmark">Korvia</span>
  <span class="logo-tagline">Karibu, tukuhudumie</span>
</div>
<h1>Korvia</h1>
<p class="desc">Karibu, tukuhudumie</p>
<p style="margin:0 0 32px; font-size:1.05rem; opacity:.85; max-width:640px;">Logo + tagline lockup concept.</p>
<h2>Choose your portal</h2>
<div class="portal-grid">
<a href="#client" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">👤</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Client</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Discover restaurants, hotels, and events using Korvia.</p></a>
<a href="#restaurant" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🍽️</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Restaurant</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">QR menus, table ordering, and live kitchen display.</p></a>
<a href="#hotel" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🏨</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Hotel</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Room service, amenities, and guest requests.</p></a>
<a href="#events" class="decay-card" style="text-align:center;display:block;"><div style="font-size:1.8rem;margin-bottom:8px;">🎉</div><h3 style="margin:0 0 6px;font-size:1.15rem;">Events</h3><p style="margin:0;font-size:.9rem;line-height:1.4;opacity:.9;">Weddings, parties, and conference ordering.</p></a>
</div>
<div style="margin:24px 0;"><a href="#" class="gold-btn">Scan QR to order</a><a href="#" class="gold-btn" style="margin-left:12px;">Open dashboard</a></div>
<h2>Lockup accent</h2>
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
    print(f"Appended {len(THEMES)} logo + tagline lockup concepts.")

if __name__ == "__main__":
    main()
