#!/usr/bin/env python3
"""Baut Gebaeudebilder in index.html ein.

Aufruf:
    python3 tools/add-sprite.py bilder/wegkreuz.png bilder/marterl.png
    python3 tools/add-sprite.py bilder/           # alle PNG im Ordner

Der Dateiname ohne Endung ist der Gebaeudeschluessel, so wie er in DEF steht
(wegkreuz, marterl, maibaum, blumen, obstbaum, zaun, ...).

Was das Werkzeug macht:
  - laedt das Bild, schneidet durchsichtige Raender weg
  - skaliert auf 256 Pixel Breite (kleinere Bilder bleiben, wie sie sind)
  - speichert als WebP mit Transparenz
  - traegt den Eintrag in BSPR ein oder ersetzt einen vorhandenen

Den Schatten und das Laden erledigt das Spiel selbst.
Nach dem Lauf: den Cache-Namen in sw.js hochzaehlen, sonst sehen
Spieler mit installierter App weiter die alte Fassung.
"""
import base64
import io
import os
import re
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow fehlt. Installieren mit: pip install --break-system-packages pillow")

HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
BREITE = 256
QUALITAET = 88


def bild_einlesen(pfad):
    im = Image.open(pfad).convert("RGBA")
    rand = im.getbbox()
    if rand:
        im = im.crop(rand)
    if im.width > BREITE:
        h = max(1, round(im.height * BREITE / im.width))
        im = im.resize((BREITE, h), Image.LANCZOS)
    puffer = io.BytesIO()
    im.save(puffer, "WEBP", quality=QUALITAET, method=6, lossless=False)
    roh = puffer.getvalue()
    return im.width, im.height, "data:image/webp;base64," + base64.b64encode(roh).decode(), len(roh)


def eintrag(schluessel, w, h, src):
    return '"%s": {"w": %d, "h": %d, "src": "%s"}' % (schluessel, w, h, src)


def main(argv):
    if not argv:
        sys.exit(__doc__)

    pfade = []
    for a in argv:
        if os.path.isdir(a):
            pfade += [os.path.join(a, f) for f in sorted(os.listdir(a))
                      if f.lower().endswith((".png", ".webp"))]
        else:
            pfade.append(a)
    if not pfade:
        sys.exit("Keine Bilder gefunden.")

    with io.open(HTML, encoding="utf8") as f:
        s = f.read()

    i = s.index("const BSPR=")
    j = s.index("};", i)
    block = s[i + len("const BSPR="):j + 1]

    vorhanden = set(re.findall(r'"(\w+)":\s*\{"w":', block))
    def_keys = set(re.findall(r"^\s{0,4}(\w+):\s*\{n:tr`", s, re.M))

    neu, ersetzt = [], []
    for p in pfade:
        k = os.path.splitext(os.path.basename(p))[0]
        if k not in def_keys:
            print("  uebersprungen: %s — kein Gebaeude mit diesem Schluessel in DEF" % k)
            continue
        w, h, src, roh = bild_einlesen(p)
        e = eintrag(k, w, h, src)
        if k in vorhanden:
            block = re.sub(r'"%s":\s*\{"w":\s*\d+,\s*"h":\s*\d+,\s*"src":\s*"[^"]*"\}' % k,
                           lambda m: e, block, count=1)
            ersetzt.append(k)
        else:
            block = block[:-1].rstrip().rstrip(",") + ",\n" + e + "}"
            neu.append(k)
        print("  %-12s %3d x %-3d  %6.1f KB" % (k, w, h, roh / 1024))

    if not neu and not ersetzt:
        sys.exit("Nichts eingebaut.")

    s = s[:i] + "const BSPR=" + block + s[j + 1:]
    with io.open(HTML, "w", encoding="utf8") as f:
        f.write(s)

    print("\nNeu: %s" % (", ".join(neu) or "keins"))
    print("Ersetzt: %s" % (", ".join(ersetzt) or "keins"))
    print("index.html ist jetzt %.1f MB." % (len(s) / 1024 / 1024))
    print("Nicht vergessen: Cache-Namen in sw.js hochzaehlen.")


if __name__ == "__main__":
    main(sys.argv[1:])
