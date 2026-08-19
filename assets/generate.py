# -*- coding: utf-8 -*-
"""Genere les visuels animes du profil : banniere, en-tetes, carte de chiffres, pied.
Tout est en SVG anime (CSS @keyframes), sans aucune dependance a un service externe."""
import os, math, random

BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE, "headers"), exist_ok=True)

BG, BG2 = "#0d1424", "#131d33"
AMBER, SKY, GREEN = "#f0b429", "#38bdf8", "#3fb950"
TXT, DIM = "#e8eef7", "#8fa0b8"
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"
MONO = "ui-monospace,'SF Mono',Menlo,Consolas,monospace"

COMMUN = """
    @keyframes leve   { from { opacity:0; transform:translateY(14px) } to { opacity:1; transform:translateY(0) } }
    @keyframes glisse { from { opacity:0; transform:translateX(-22px) } to { opacity:1; transform:translateX(0) } }
    @keyframes trace  { to { stroke-dashoffset:0 } }
    @keyframes pulse  { 0%,100% { opacity:.30 } 50% { opacity:1 } }
    @keyframes souffle{ 0%,100% { r:2.4 } 50% { r:4.2 } }
    @keyframes balaye { 0% { transform:translateX(-120%) } 60%,100% { transform:translateX(320%) } }
    @keyframes flotte { 0%,100% { transform:translateY(0) } 50% { transform:translateY(-7px) } }
    * { transform-box: fill-box; transform-origin: center; }
"""

def ecrire(chemin, contenu):
    open(os.path.join(BASE, chemin), "w", encoding="utf-8").write(contenu)


# ─────────────────────────── BANNIERE ───────────────────────────
def banner():
    W, H = 1200, 320
    random.seed(7)
    pts = []
    for i in range(38):
        a = i * 2.399963
        r = 9.2 * math.sqrt(i)
        pts.append((W - 245 + r * math.cos(a) * 1.72, H / 2 + r * math.sin(a) * 1.06))

    aretes = []
    for i, (x1, y1) in enumerate(pts):
        for j, (x2, y2) in enumerate(pts):
            if j <= i: continue
            d = math.hypot(x1 - x2, y1 - y2)
            if d < 64: aretes.append((x1, y1, x2, y2, d))

    css = COMMUN + f"""
    .lien   {{ stroke:{SKY}; stroke-width:1; fill:none; stroke-dasharray:90; stroke-dashoffset:90;
              animation: trace 1.5s ease-out forwards, pulse 5s ease-in-out infinite; }}
    .noeud  {{ opacity:0; animation: leve .5s ease-out forwards, souffle 4.5s ease-in-out infinite; }}
    .cle    {{ fill:{AMBER}; }}
    .nom    {{ opacity:0; animation: glisse .8s cubic-bezier(.2,.7,.3,1) .15s forwards; }}
    .regle  {{ transform:scaleX(0); transform-origin:left center; animation: etire .7s cubic-bezier(.2,.7,.3,1) .55s forwards; }}
    @keyframes etire {{ to {{ transform:scaleX(1) }} }}
    .l1     {{ opacity:0; animation: glisse .7s ease-out .75s forwards; }}
    .l2     {{ opacity:0; animation: glisse .7s ease-out .92s forwards; }}
    .l3     {{ opacity:0; animation: glisse .7s ease-out 1.09s forwards; }}
    .halo   {{ animation: pulse 6s ease-in-out infinite; }}
    .eclat  {{ animation: balaye 7s ease-in-out 1.6s infinite; }}
    """

    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-label="Ressane Messioughi, developpeur web full stack">',
         f'<style><![CDATA[{css}]]></style>', '<defs>',
         f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
         f'<stop offset="0" stop-color="{BG}"><animate attributeName="stop-color" '
         f'values="{BG};#101a2e;{BG}" dur="9s" repeatCount="indefinite"/></stop>'
         f'<stop offset="1" stop-color="{BG2}"><animate attributeName="stop-color" '
         f'values="{BG2};#0f1829;{BG2}" dur="9s" repeatCount="indefinite"/></stop></linearGradient>',
         f'<linearGradient id="ln" x1="0" y1="0" x2="1" y2="0">'
         f'<stop offset="0" stop-color="{AMBER}"/><stop offset="1" stop-color="{SKY}"/></linearGradient>',
         '<radialGradient id="glow" cx="50%" cy="50%">'
         f'<stop offset="0" stop-color="{SKY}" stop-opacity=".30"/>'
         f'<stop offset="1" stop-color="{SKY}" stop-opacity="0"/></radialGradient>',
         '<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">'
         '<stop offset="0" stop-color="#ffffff" stop-opacity="0"/>'
         '<stop offset=".5" stop-color="#ffffff" stop-opacity=".05"/>'
         '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>',
         f'<clipPath id="cadre"><rect width="{W}" height="{H}" rx="0"/></clipPath>',
         '</defs>',
         f'<g clip-path="url(#cadre)">',
         f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
         f'<circle class="halo" cx="{W-245}" cy="{H/2}" r="190" fill="url(#glow)"/>']

    for k, (x1, y1, x2, y2, d) in enumerate(aretes):
        s.append(f'<line class="lien" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke-opacity="{max(.07,.34-d/210):.2f}" style="animation-delay:{.5+k*.012:.2f}s,{2+k*.05:.2f}s"/>')
    for i, (x, y) in enumerate(pts):
        cle = i % 7 == 0
        s.append(f'<circle class="noeud{" cle" if cle else ""}" cx="{x:.1f}" cy="{y:.1f}" '
                 f'r="{3.6 if cle else 2.4}" fill="{AMBER if cle else SKY}" '
                 f'fill-opacity="{.95 if cle else .62}" style="animation-delay:{.35+i*.03:.2f}s,{1.6+i*.11:.2f}s"/>')

    s += [f'<text class="nom" x="70" y="128" font-family="{FONT}" font-size="47" font-weight="800" '
          f'fill="{TXT}" letter-spacing="-1">Ressane Messioughi</text>',
          f'<rect class="regle" x="70" y="149" width="92" height="4" rx="2" fill="url(#ln)"/>',
          f'<text class="l1" x="70" y="192" font-family="{FONT}" font-size="20" font-weight="600" '
          f'fill="{AMBER}">Développeur Web Full Stack</text>',
          f'<text class="l2" x="70" y="222" font-family="{MONO}" font-size="14" fill="{DIM}">'
          f'React · Node.js · Express · MySQL · Socket.IO</text>',
          f'<text class="l3" x="70" y="252" font-family="{FONT}" font-size="13.5" fill="{DIM}">'
          f'Reconversion · Titre professionnel DWWM · Lyon</text>',
          f'<rect class="eclat" x="-260" y="0" width="220" height="{H}" fill="url(#sweep)"/>',
          '</g></svg>']
    ecrire("banner.svg", "\n".join(s))


# ─────────────────────────── EN-TETES ───────────────────────────
def header(num, titre, fichier):
    W, H = 1200, 88
    css = COMMUN + f"""
    .barre {{ transform:scaleY(0); transform-origin:top center; animation: pousse .55s cubic-bezier(.2,.7,.3,1) forwards; }}
    @keyframes pousse {{ to {{ transform:scaleY(1) }} }}
    .num   {{ opacity:0; animation: leve .55s ease-out .12s forwards; }}
    .tit   {{ opacity:0; animation: glisse .6s cubic-bezier(.2,.7,.3,1) .22s forwards; }}
    .sep   {{ opacity:0; animation: leve .5s ease-out .3s forwards; }}
    .pois  {{ animation: pulse 2.6s ease-in-out infinite; }}
    """
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{num} — {titre}">',
         f'<style><![CDATA[{css}]]></style>',
         f'<defs><linearGradient id="g{num}" x1="0" y1="0" x2="1" y2="0">'
         f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="12" fill="url(#g{num})"/>',
         f'<rect class="barre" x="0" y="0" width="5" height="{H}" rx="2.5" fill="{AMBER}"/>',
         f'<text class="num" x="34" y="57" font-family="{MONO}" font-size="30" font-weight="700" '
         f'fill="{AMBER}" fill-opacity=".45">{num}</text>',
         f'<line class="sep" x1="86" y1="26" x2="86" y2="62" stroke="{DIM}" stroke-opacity=".3" stroke-width="1.5"/>',
         f'<text class="tit" x="108" y="55" font-family="{FONT}" font-size="24" font-weight="700" fill="{TXT}">{titre}</text>']
    for i in range(16):
        s.append(f'<circle class="pois" cx="{W-40-i*21}" cy="{H/2}" r="2.6" fill="{SKY}" '
                 f'fill-opacity="{max(.06,.42-i*.026):.2f}" style="animation-delay:{i*.09:.2f}s"/>')
    s.append('</svg>')
    ecrire(os.path.join("headers", fichier), "\n".join(s))


# ─────────────────── CARTE DE CHIFFRES (animee) ───────────────────
def stats():
    W, H = 1200, 215
    data = [("35", "composants"), ("11", "pages"), ("4 391", "lignes de code"),
            ("11", "tests"), ("72", "commits"), ("9", "versions taguées")]
    css = COMMUN + f"""
    .titre  {{ opacity:0; animation: glisse .6s ease-out forwards; }}
    .trait  {{ stroke-dasharray:1110; stroke-dashoffset:1110; animation: trace 1.1s ease-out .2s forwards; }}
    .col    {{ opacity:0; animation: leve .6s cubic-bezier(.2,.7,.3,1) forwards; }}
    .barrev {{ transform:scaleY(0); animation: pousseV .5s ease-out forwards; }}
    @keyframes pousseV {{ to {{ transform:scaleY(1) }} }}
    .pied   {{ opacity:0; animation: leve .6s ease-out 1.15s forwards; }}
    .lueur  {{ animation: balaye 6s ease-in-out 1.4s infinite; }}
    """
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="DevProject en chiffres">',
         f'<style><![CDATA[{css}]]></style>', '<defs>',
         f'<linearGradient id="sg" x1="0" y1="0" x2="1" y2="1">'
         f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient>',
         '<linearGradient id="sw2" x1="0" y1="0" x2="1" y2="0">'
         '<stop offset="0" stop-color="#ffffff" stop-opacity="0"/>'
         '<stop offset=".5" stop-color="#ffffff" stop-opacity=".055"/>'
         '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>',
         f'<clipPath id="cs"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>',
         '<g clip-path="url(#cs)">',
         f'<rect width="{W}" height="{H}" fill="url(#sg)"/>',
         f'<text class="titre" x="46" y="52" font-family="{FONT}" font-size="15" font-weight="700" '
         f'fill="{AMBER}" letter-spacing="1.6">DEVPROJECT EN CHIFFRES</text>',
         f'<line class="trait" x1="46" y1="70" x2="{W-46}" y2="70" stroke="{DIM}" stroke-opacity=".2" stroke-width="1"/>']
    cw = (W - 92) / 6
    for i, (v, k) in enumerate(data):
        cx = 46 + cw * i + cw / 2
        d = .35 + i * .11
        s.append(f'<g class="col" style="animation-delay:{d:.2f}s">'
                 f'<text x="{cx:.0f}" y="134" text-anchor="middle" font-family="{FONT}" font-size="43" '
                 f'font-weight="800" fill="{TXT}">{v}</text>'
                 f'<text x="{cx:.0f}" y="162" text-anchor="middle" font-family="{FONT}" font-size="13" '
                 f'fill="{DIM}">{k}</text></g>')
        if i:
            s.append(f'<line class="barrev" x1="{46+cw*i:.0f}" y1="98" x2="{46+cw*i:.0f}" y2="168" '
                     f'stroke="{DIM}" stroke-opacity=".14" stroke-width="1" style="animation-delay:{d:.2f}s"/>')
    s += [f'<text class="pied" x="{W/2}" y="195" text-anchor="middle" font-family="{MONO}" font-size="12" '
          f'fill="{DIM}">React 19 · Node.js · Express 5 · MySQL · Socket.IO — front et back développés seul</text>',
          f'<rect class="lueur" x="-250" y="0" width="200" height="{H}" fill="url(#sw2)"/>',
          '</g></svg>']
    ecrire("stats.svg", "\n".join(s))


# ─────────────────────────── PIED ───────────────────────────
def footer():
    W, H = 1200, 112
    css = COMMUN + f"""
    .onde {{ animation: flotte 3.4s ease-in-out infinite; }}
    .fil  {{ stroke:{SKY}; stroke-opacity:.16; stroke-width:1; stroke-dasharray:40; stroke-dashoffset:40;
            animation: trace 1.2s ease-out forwards; }}
    .mot  {{ opacity:0; animation: leve .8s ease-out .5s forwards; }}
    """
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Depuis Lyon">',
         f'<style><![CDATA[{css}]]></style>',
         f'<defs><linearGradient id="fg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BG}"/>'
         f'<stop offset=".5" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="12" fill="url(#fg)"/>']
    pos = [(60 + i * 24, H / 2 + math.sin(i * .42) * 18) for i in range(46)]
    for i, (x, y) in enumerate(pos):
        if i:
            px, py = pos[i - 1]
            s.append(f'<line class="fil" x1="{px}" y1="{py:.1f}" x2="{x}" y2="{y:.1f}" style="animation-delay:{i*.02:.2f}s"/>')
    for i, (x, y) in enumerate(pos):
        s.append(f'<circle class="onde" cx="{x}" cy="{y:.1f}" r="2.3" fill="{SKY}" fill-opacity=".32" '
                 f'style="animation-delay:{i*.07:.2f}s"/>')
    s += [f'<text class="mot" x="{W/2}" y="{H/2+6}" text-anchor="middle" font-family="{FONT}" font-size="17" '
          f'font-weight="600" fill="{TXT}">Depuis Lyon &#183; ouvert aux opportunités</text>', '</svg>']
    ecrire("footer.svg", "\n".join(s))


banner(); stats(); footer()
for n, t, f in [("01", "Qui je suis", "01-profil.svg"),
                ("02", "Projet principal", "02-projet.svg"),
                ("03", "Ma façon de travailler", "03-methode.svg"),
                ("04", "Stack technique", "04-stack.svg"),
                ("05", "DevProject en chiffres", "05-stats.svg"),
                ("06", "Me contacter", "06-contact.svg")]:
    header(n, t, f)

print("Visuels animés générés :")
for r, _, fs in os.walk(BASE):
    for f in sorted(fs):
        if f.endswith(".svg"):
            p = os.path.join(r, f)
            print(f"  {p.split('assets/')[1]:<34} {os.path.getsize(p):>7} o")
