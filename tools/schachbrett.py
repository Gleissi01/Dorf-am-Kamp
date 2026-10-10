#!/usr/bin/env python3
"""Stellt Bilder frei, die auf weissem Grund oder auf dem Schachbrettmuster
liegen, das Bildgeneratoren statt Transparenz ausgeben.

Aufruf:
    python3 tools/schachbrett.py bilder/roh/*.jpg
    python3 tools/schachbrett.py bilder/roh/ --ziel bilder/

Warum eigens dafuer und nicht freistellen.py: dort ist der Hintergrund immer
hell (Schwelle 200). Das Schachbrett kann auch dunkelgrau sein, und es
besteht aus zwei Toenen statt einem. Hier werden die Hintergrundtoene darum
aus dem Bildrand gelesen, statt sie vorauszusetzen.

Verfahren:
  - Am Rand die Grautoene einsammeln (nur neutrale, also R=G=B)
  - Als Hintergrund gilt, was neutral ist und zwischen diesen Toenen liegt
  - Von allen vier Raendern durchfluten, damit Weiss im Tier stehen bleibt
  - Eingeschlossene Flaechen (zwischen den Beinen) genauso pruefen
  - Den Rand weich auslaufen lassen, sonst bleibt der JPEG-Saum stehen
"""
import os
import sys

try:
    import numpy as np
    from PIL import Image
    from scipy import ndimage
except ImportError:
    sys.exit("Fehlt: pip install --break-system-packages pillow numpy scipy")

NEUTRAL = 16     # erlaubter Abstand zwischen den Kanaelen
RAND = 3         # wie viele Pixel am Bildrand gelesen werden
LUFT = 14        # Spielraum um die gefundenen Hintergrundtoene
WEICH = 1.6      # Breite des weichen Saums in Pixeln
MIN_LOCH = 25    # kleinere eingeschlossene Flecken bleiben stehen


def freistellen(pfad, ziel):
    im = Image.open(pfad).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape

    spread = a.max(axis=2) - a.min(axis=2)
    lum = a.mean(axis=2)
    neutral = spread <= NEUTRAL

    # Hintergrundtoene aus dem Rand lesen
    rand = np.zeros((h, w), bool)
    rand[:RAND, :] = rand[-RAND:, :] = True
    rand[:, :RAND] = rand[:, -RAND:] = True
    toene = lum[rand & neutral]
    if toene.size < 50:
        print("  %s: kein neutraler Rand gefunden, uebersprungen" % os.path.basename(pfad))
        return False
    lo, hi = np.percentile(toene, 2) - LUFT, np.percentile(toene, 98) + LUFT

    kandidat = neutral & (lum >= lo) & (lum <= hi)

    # von den Raendern durchfluten
    saat = np.zeros((h, w), bool)
    saat[0, :] = saat[-1, :] = True
    saat[:, 0] = saat[:, -1] = True
    saat &= kandidat
    marken, _ = ndimage.label(kandidat)
    aussen = set(np.unique(marken[saat])) - {0}
    bg = np.isin(marken, list(aussen))

    # eingeschlossene Flaechen: zwischen den Beinen, unter dem Bauch
    innen, nz = ndimage.label(kandidat & ~bg)
    for k in range(1, nz + 1):
        m = innen == k
        if m.sum() < MIN_LOCH:
            continue
        bg |= m

    # weicher Saum: der JPEG-Uebergang wird halbdurchsichtig
    dist = ndimage.distance_transform_edt(~bg)
    alpha = np.clip((dist - 0.2) / WEICH, 0, 1)
    alpha[bg] = 0

    out = np.dstack([np.asarray(im), (alpha * 255).astype(np.uint8)])
    bild = Image.fromarray(out, "RGBA")
    k = bild.getbbox()
    if k:
        bild = bild.crop(k)
    bild.save(ziel)
    anteil = 100.0 * bg.sum() / (h * w)
    print("  %-10s %4dx%-4d  Hintergrund %4.1f %%  Toene %d-%d"
          % (os.path.basename(ziel), bild.width, bild.height, anteil, int(lo), int(hi)))
    return True


def main(argv):
    ziel_ordner = None
    if "--ziel" in argv:
        i = argv.index("--ziel")
        ziel_ordner = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if not argv:
        sys.exit(__doc__)

    pfade = []
    for p in argv:
        if os.path.isdir(p):
            pfade += [os.path.join(p, f) for f in sorted(os.listdir(p))
                      if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
        else:
            pfade.append(p)

    for p in pfade:
        name = os.path.splitext(os.path.basename(p))[0] + ".png"
        ziel = os.path.join(ziel_ordner or os.path.dirname(p), name)
        freistellen(p, ziel)


if __name__ == "__main__":
    main(sys.argv[1:])
