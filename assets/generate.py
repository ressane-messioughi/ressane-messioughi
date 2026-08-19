# -*- coding: utf-8 -*-
import os, math, random
BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE, "headers"), exist_ok=True)

BG, BG2 = "#0d1424", "#131d33"
AMBER, SKY, GREEN, TXT, DIM = "#f0b429", "#38bdf8", "#3fb950", "#e8eef7", "#8fa0b8"
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"

# ── Banniere : reseau de noeuds relies (equipe + temps reel) ──────────────
def banner():
    W, H = 1200, 300
    random.seed(7)
    pts = []
    for i in range(34):
        a = i * 2.399963
        r = 9.5 * math.sqrt(i)
        pts.append((W - 250 + r * math.cos(a) * 1.65, H / 2 + r * math.sin(a) * 1.0))
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Ressane Messioughi, developpeur web full stack">',
         '<defs>',
         f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>',
         f'<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{AMBER}"/><stop offset="1" stop-color="{SKY}"/></linearGradient>',
         '<radialGradient id="glow" cx="50%" cy="50%"><stop offset="0" stop-color="#38bdf8" stop-opacity=".28"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>',
         '</defs>',
         f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
         f'<circle cx="{W-250}" cy="{H/2}" r="185" fill="url(#glow)"/>']
    for i, (x1, y1) in enumerate(pts):
        for j, (x2, y2) in enumerate(pts):
            if j <= i: continue
            d = math.hypot(x1 - x2, y1 - y2)
            if d < 62:
                s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{SKY}" stroke-opacity="{max(.06,.34-d/210):.2f}" stroke-width="1"/>')
    for i, (x, y) in enumerate(pts):
        c = AMBER if i % 7 == 0 else SKY
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{3.6 if i%7==0 else 2.4}" fill="{c}" fill-opacity="{.95 if i%7==0 else .62}"/>')
    s += [f'<text x="70" y="122" font-family="{FONT}" font-size="46" font-weight="800" fill="{TXT}" letter-spacing="-1">Ressane Messioughi</text>',
          f'<rect x="70" y="142" width="86" height="4" rx="2" fill="url(#ln)"/>',
          f'<text x="70" y="184" font-family="{FONT}" font-size="20" font-weight="600" fill="{AMBER}">Développeur Web Full Stack</text>',
          f'<text x="70" y="214" font-family="{MONO}" font-size="14" fill="{DIM}">React · Node.js · Express · MySQL · Socket.IO</text>',
          f'<text x="70" y="243" font-family="{FONT}" font-size="13.5" fill="{DIM}">Reconversion · Titre professionnel DWWM · Lyon</text>',
          '</svg>']
    open(os.path.join(BASE, "banner.svg"), "w", encoding="utf-8").write("\n".join(s))

# ── En-tetes de section ──────────────────────────────────────────────────
def header(num, titre, fichier):
    W, H = 1200, 88
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{num} — {titre}">',
         f'<defs><linearGradient id="g{num}" x1="0" y1="0" x2="1" y2="0">'
         f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="12" fill="url(#g{num})"/>',
         f'<rect x="0" y="0" width="5" height="{H}" rx="2.5" fill="{AMBER}"/>',
         f'<text x="34" y="57" font-family="{MONO}" font-size="30" font-weight="700" fill="{AMBER}" fill-opacity=".45">{num}</text>',
         f'<line x1="86" y1="26" x2="86" y2="62" stroke="{DIM}" stroke-opacity=".3" stroke-width="1.5"/>',
         f'<text x="108" y="55" font-family="{FONT}" font-size="24" font-weight="700" fill="{TXT}">{titre}</text>']
    for i in range(16):
        x = W - 40 - i * 21
        s.append(f'<circle cx="{x}" cy="{H/2}" r="2.6" fill="{SKY}" fill-opacity="{max(.05, .40 - i*.026):.2f}"/>')
    s.append('</svg>')
    open(os.path.join(BASE, "headers", fichier), "w", encoding="utf-8").write("\n".join(s))

# ── Pied de page ─────────────────────────────────────────────────────────
def footer():
    W, H = 1200, 110
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Depuis Lyon">',
         f'<defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BG}"/><stop offset=".5" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="12" fill="url(#fg)"/>']
    for i in range(46):
        x = 60 + i * 24
        y = H / 2 + math.sin(i * .42) * 17
        s.append(f'<circle cx="{x}" cy="{y:.1f}" r="2.3" fill="{SKY}" fill-opacity=".30"/>')
        if i: 
            px, py = 60 + (i-1) * 24, H / 2 + math.sin((i-1) * .42) * 17
            s.append(f'<line x1="{px}" y1="{py:.1f}" x2="{x}" y2="{y:.1f}" stroke="{SKY}" stroke-opacity=".14" stroke-width="1"/>')
    s += [f'<text x="{W/2}" y="{H/2+6}" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="600" fill="{TXT}">Depuis Lyon &#183; ouvert aux opportunités</text>',
          '</svg>']
    open(os.path.join(BASE, "footer.svg"), "w", encoding="utf-8").write("\n".join(s))

banner(); footer()
for n, t, f in [("01","Qui je suis","01-profil.svg"),
                ("02","Projet principal","02-projet.svg"),
                ("03","Ma façon de travailler","03-methode.svg"),
                ("04","Stack technique","04-stack.svg"),
                ("05","Statistiques","05-stats.svg"),
                ("06","Contributions","06-contributions.svg"),
                ("07","Me contacter","07-contact.svg")]:
    header(n, t, f)
print("SVG générés :")
for r, _, fs in os.walk(BASE):
    for f in sorted(fs): print("  ", os.path.join(r, f).split("assets/")[1], os.path.getsize(os.path.join(r, f)), "o")

# ── Carte de statistiques du projet (auto-hebergee : aucun service externe) ──
def stats():
    W, H = 1200, 210
    data = [("35", "composants"), ("11", "pages"), ("4 391", "lignes de code"),
            ("11", "tests"), ("72", "commits"), ("9", "versions taguées")]
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DevProject en chiffres">',
         f'<defs><linearGradient id="sg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="14" fill="url(#sg)"/>',
         f'<text x="46" y="52" font-family="{FONT}" font-size="15" font-weight="700" fill="{AMBER}" letter-spacing="1.6">DEVPROJECT EN CHIFFRES</text>',
         f'<line x1="46" y1="70" x2="{W-46}" y2="70" stroke="{DIM}" stroke-opacity=".2" stroke-width="1"/>']
    cw = (W - 92) / 6
    for i, (v, k) in enumerate(data):
        cx = 46 + cw * i + cw / 2
        s.append(f'<text x="{cx:.0f}" y="132" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="800" fill="{TXT}">{v}</text>')
        s.append(f'<text x="{cx:.0f}" y="160" text-anchor="middle" font-family="{FONT}" font-size="13" fill="{DIM}">{k}</text>')
        if i: s.append(f'<line x1="{46+cw*i:.0f}" y1="98" x2="{46+cw*i:.0f}" y2="166" stroke="{DIM}" stroke-opacity=".14" stroke-width="1"/>')
    s.append(f'<text x="{W/2}" y="191" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{DIM}">React 19 · Node.js · Express 5 · MySQL · Socket.IO — front et back développés seul</text>')
    s.append('</svg>')
    open(os.path.join(BASE, "stats.svg"), "w", encoding="utf-8").write("\n".join(s))

stats()
header("05", "DevProject en chiffres", "05-stats.svg")
header("06", "Me contacter", "06-contact.svg")
for vieux in ("06-contributions.svg", "07-contact.svg"):
    p = os.path.join(BASE, "headers", vieux)
    if os.path.exists(p): os.remove(p)
print("→ stats.svg généré, en-têtes 05/06 refaits, 06-contributions et 07-contact supprimés")
