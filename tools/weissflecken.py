#!/usr/bin/env python3
"""Sucht in den schon eingebauten Gebaeudebildern nach vergessenen
Hintergrundresten und macht sie durchsichtig.

    python3 tools/weissflecken.py --zeigen    # nur berichten, nichts aendern
    python3 tools/weissflecken.py             # aendern

Gemeint sind Stellen wie das weisse Dreieck zwischen Dach und Pfosten beim
Brunnen: eingeschlossene Flaechen, an die beim Freistellen niemand herankam.

Angefasst wird nur, was alle vier Pruefungen besteht:
  - eingeschlossen, also vom durchsichtigen Rand aus nicht erreichbar
  - hell (Mittel ab 235)
  - neutral grau-weiss (R, G und B liegen dicht beieinander)
  - klein im Verhaeltnis zur Figur (hoechstens 4 Prozent)

Gekalkter Putz faellt durch: der ist warm getoent, bei den Haeusern liegt
Rot rund 18 Stufen ueber Blau. Grosse helle Flaechen wie der Marterl-Schaft
fallen ueber die Groessengrenze durch.
"""
import base64
import io
import os
import re
import sys

try:
    import numpy as np
    from PIL import Image
    from scipy import ndimage
except ImportError:
    sys.exit("Fehlt. Installieren mit: pip install --break-system-packages pillow numpy scipy")

HTML = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
HELLMITTEL = 235     # ab diesem Mittelwert gilt eine Flaeche als hell
NEUTRAL = 12         # hoechster Abstand zwischen staerkstem und schwaechstem Kanal
ANTEIL = 0.04        # hoechstens so viel der Figur darf eine Flaeche ausmachen
MINPX = 20           # kleiner lohnt nicht


def pruefen(im):
    """Gibt die Maske der zu entfernenden Flaechen zurueck."""
    a = np.asarray(im).astype(int)
    rgb, alpha = a[:, :, :3], a[:, :, 3]
    fest = alpha > 160
    if not fest.any():
        return None, []

    # was vom durchsichtigen Rand aus erreichbar ist, ist schon Hintergrund
    frei = ~fest
    hell = (rgb.mean(axis=2) >= HELLMITTEL - 20) & ((rgb.max(axis=2) - rgb.min(axis=2)) <= NEUTRAL + 6) & fest
    lab, n = ndimage.label(hell)
    weg = np.zeros(hell.shape, bool)
    bericht = []
    grenze = fest.sum() * ANTEIL
    for i in range(1, n + 1):
        m = lab == i
        gr = m.sum()
        if gr < MINPX or gr > grenze:
            continue
        # beruehrt die Flaeche den durchsichtigen Bereich, war sie schon offen
        rand = ndimage.binary_dilation(m, np.ones((3, 3), bool)) & ~m
        if frei[rand].any():
            continue
        px = rgb[m]
        mittel = px.mean(axis=0)
        if mittel.mean() < HELLMITTEL:
            continue
        if mittel.max() - mittel.min() > NEUTRAL:
            continue
        weg |= m
        bericht.append((int(gr), mittel.round(0).astype(int).tolist()))
    return weg, bericht


def main(argv):
    nur_zeigen = "--zeigen" in argv
    with io.open(HTML, encoding="utf8") as f:
        s = f.read()
    i = s.index("const BSPR=")
    j = s.index("};", i)
    block = s[i:j + 1]

    muster = re.compile(r'"(\w+)":\s*\{"w":\s*(\d+),\s*"h":\s*(\d+),\s*"src":\s*"data:image/webp;base64,([A-Za-z0-9+/=]+)"\}')
    geaendert = []
    neu_block = block
    for m in muster.finditer(block):
        k = m.group(1)
        im = Image.open(io.BytesIO(base64.b64decode(m.group(4)))).convert("RGBA")
        weg, bericht = pruefen(im)
        if weg is None or not weg.any():
            continue
        a = np.asarray(im).copy()
        a[:, :, 3][weg] = 0
        geaendert.append((k, sum(b[0] for b in bericht), bericht))
        if nur_zeigen:
            continue
        out = Image.fromarray(a, "RGBA")
        kasten = out.getbbox()
        if kasten:
            out = out.crop(kasten)
        puffer = io.BytesIO()
        out.save(puffer, "WEBP", quality=88, method=6)
        neu = '"%s": {"w": %d, "h": %d, "src": "data:image/webp;base64,%s"}' % (
            k, out.width, out.height, base64.b64encode(puffer.getvalue()).decode())
        neu_block = neu_block.replace(m.group(0), neu, 1)

    if not geaendert:
        print("Keine Hintergrundreste gefunden.")
        return
    for k, gesamt, bericht in sorted(geaendert, key=lambda t: -t[1]):
        print("  %-12s %5d px in %d Flaeche(n): %s" % (
            k, gesamt, len(bericht), ", ".join("%dpx %s" % (g, f) for g, f in bericht[:3])))
    if nur_zeigen:
        print("\nNur gezeigt, nichts geaendert. Ohne --zeigen wird eingebaut.")
        return
    with io.open(HTML, "w", encoding="utf8") as f:
        f.write(s[:i] + neu_block + s[j + 1:])
    print("\n%d Bilder bereinigt. Cache-Namen in sw.js hochzaehlen." % len(geaendert))


if __name__ == "__main__":
    main(sys.argv[1:])
