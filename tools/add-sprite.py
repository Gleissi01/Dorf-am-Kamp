#!/usr/bin/env python3
"""Baut Gebaeudebilder in index.html ein.

Aufruf:
    python3 tools/add-sprite.py bilder/wegkreuz.png bilder/marterl.png
    python3 tools/add-sprite.py bilder/           # alle PNG im Ordner
    python3 tools/add-sprite.py --trage bilder/wasser.png   # Tragegut
    python3 tools/add-sprite.py --natur bilder/schaf.png    # Tier oder Natur

Der Dateiname ohne Endung ist der Gebaeudeschluessel, so wie er in DEF steht
(wegkreuz, marterl, maibaum, blumen, obstbaum, zaun, ...).

Mit --trage landet das Bild stattdessen in CSPR, der Tabelle fuer das, was
die Leute in der Hand tragen (wasser, holz, stein, nahrung, ...). Tragegut
wird auf 48 Pixel skaliert statt auf 256, weil es im Spiel nur rund 10 Pixel
breit erscheint.

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
BREITE_BAU = 256
BREITE_TRAGE = 48
BREITE_NATUR = 96
NATUR_NEU = {"schaf", "widder", "schwein", "eber", "huhn", "hahn", "stier", "ziege", "gans"}
QUALITAET = 88


def bild_einlesen(pfad, breite):
    im = Image.open(pfad).convert("RGBA")
    rand = im.getbbox()
    if rand:
        im = im.crop(rand)
    if im.width > breite:
        h = max(1, round(im.height * breite / im.width))
        im = im.resize((breite, h), Image.LANCZOS)
    puffer = io.BytesIO()
    im.save(puffer, "WEBP", quality=QUALITAET, method=6, lossless=False)
    roh = puffer.getvalue()
    return im.width, im.height, "data:image/webp;base64," + base64.b64encode(roh).decode(), len(roh)


def eintrag(schluessel, w, h, src):
    return '"%s": {"w": %d, "h": %d, "src": "%s"}' % (schluessel, w, h, src)


def main(argv):
    trage = "--trage" in argv
    natur = "--natur" in argv
    argv = [a for a in argv if a not in ("--trage", "--natur")]
    if not argv:
        sys.exit(__doc__)
    breite = BREITE_NATUR if natur else BREITE_TRAGE if trage else BREITE_BAU
    tabelle = "const NSPR=" if natur else "const CSPR=" if trage else "const BSPR="

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

    i = s.index(tabelle)
    j = s.index("};", i)
    block = s[i + len(tabelle):j + 1]

    vorhanden = set(re.findall(r'"(\w+)":\s*\{"w":', block))
    if natur:
        # Tiere und Natur: was schon drin ist, dazu die geplanten neuen
        def_keys = set(vorhanden) | NATUR_NEU
    elif trage:
        # Tragegut: erlaubt ist alles, was eine Tragefarbe hat (CARRYCOL),
        # dazu die Warennamen aus RN. Wasser steht nur in CARRYCOL, weil es
        # keine Lagerware ist, sondern im Haus steht.
        def_keys = set(vorhanden)
        for muster in (r"const CARRYCOL=\{(.*?)\};", r"const RN=\{(.*?)\};"):
            r = re.search(muster, s, re.S)
            if r:
                def_keys |= set(re.findall(r"(\w+)\s*:", r.group(1)))
    else:
        # nur der DEF-Block, sonst zaehlen auch Haendlerwaren (WARE) als Gebaeude
        i0 = s.index("const DEF={")
        i1 = s.index("\n};", i0)
        def_keys = set(re.findall(r"^\s{0,4}(\w+):\s*\{n:tr`", s[i0:i1], re.M))

    neu, ersetzt = [], []
    for p in pfade:
        k = os.path.splitext(os.path.basename(p))[0]
        if k not in def_keys:
            print("  uebersprungen: %s — diesen Schluessel gibt es nicht" % k)
            continue
        w, h, src, roh = bild_einlesen(p, breite)
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

    s = s[:i] + tabelle + block + s[j + 1:]
    with io.open(HTML, "w", encoding="utf8") as f:
        f.write(s)

    print("\nNeu: %s" % (", ".join(neu) or "keins"))
    print("Ersetzt: %s" % (", ".join(ersetzt) or "keins"))
    print("index.html ist jetzt %.1f MB." % (len(s) / 1024 / 1024))
    print("Nicht vergessen: Cache-Namen in sw.js hochzaehlen.")


if __name__ == "__main__":
    main(sys.argv[1:])
