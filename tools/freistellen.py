#!/usr/bin/env python3
"""Schneidet den Hintergrund aus einem Bild heraus.

    python3 tools/freistellen.py roh/wegkreuz.jpg bilder/

Gedacht fuer Bilder aus einer Bilder-KI, die trotz Anweisung einen weissen
Hintergrund oder ein eingemaltes Karomuster liefert.

So geht es vor:
  - faengt an allen Bildraendern an und frisst sich nach innen, solange die
    Farbe hell und farblos ist (Weiss bis helles Grau, auch Karomuster)
  - haelt an der ersten Kante an, die dunkler oder farbig ist
  - weiche Kante: Pixel am Rand bekommen Teil-Transparenz, damit nichts
    ausfranst

Weil nur vom Rand her gearbeitet wird, bleiben weisse Stellen IM Motiv
erhalten: der gekalkte Putz am Marterl, weisse Blueten, helle Baender.
"""
import os
import sys
from collections import deque

try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("Fehlt. Installieren mit: pip install --break-system-packages pillow numpy")

HELL = 200      # ab dieser Helligkeit gilt ein Pixel als moeglicher Hintergrund
BUNT = 26       # so farbig darf er hoechstens sein (max-min der Kanaele)
WEICH = 190     # ab dieser Helligkeit wird die Kante weich ausgeblendet


def freistellen(pfad, ziel):
    im = Image.open(pfad).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w = a.shape[:2]

    hell = a.max(axis=2) >= HELL
    flau = (a.max(axis=2) - a.min(axis=2)) <= BUNT
    kandidat = hell & flau

    # vom Rand nach innen fluten
    bg = np.zeros((h, w), dtype=bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if kandidat[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if kandidat[y, x] and not bg[y, x]:
                bg[y, x] = True
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and kandidat[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True
                q.append((ny, nx))

    # Eingeschlossene Hintergrundflecken: die Luecken zwischen den Zaunlatten,
    # das Dreieck unterm Dach des Wegkreuzes. Dorthin kommt die Flutung vom
    # Rand nicht. Weggenommen wird nur, was die GLEICHEN Farben hat wie der
    # Hintergrund am Bildrand. Damit faellt auch ein eingemaltes Karomuster
    # weg, waehrend getoenter Putz, ein helles Schild, Blueten und Baender
    # erhalten bleiben: die sind merklich dunkler oder waermer als der Grund.
    innen = kandidat & ~bg
    if innen.any() and bg.any():
        from scipy import ndimage
        # Vergleichsfarben nur aus dem Inneren des Hintergrunds nehmen. Direkt
        # am Motivrand sitzt ein JPG-Saum mit Grauwerten bis hinunter zu 200;
        # waere der dabei, wuerde spaeter heller Putz faelschlich mitgeloescht.
        kern = ndimage.binary_erosion(bg, np.ones((9, 9), bool))
        quelle = bg if not kern.any() else kern
        randfarben = np.unique(a[quelle].reshape(-1, 3) // 6 * 6, axis=0)
        lab, k = ndimage.label(innen)
        for i in range(1, k + 1):
            m = lab == i
            if m.sum() < 6:   # auch die winzigen Luecken zwischen Blaettern
                continue
            px = a[m]
            nah = (np.abs(px[:, None, :] - randfarben[None, :, :]).max(axis=2) <= 13).any(axis=1)
            if nah.mean() >= 0.85:
                bg |= m

    alpha = np.where(bg, 0, 255).astype(np.uint8)

    # weiche Kante: helle Pixel direkt am Hintergrund teilweise durchsichtig
    rand = np.zeros((h, w), dtype=bool)
    rand[1:, :] |= bg[:-1, :]
    rand[:-1, :] |= bg[1:, :]
    rand[:, 1:] |= bg[:, :-1]
    rand[:, :-1] |= bg[:, 1:]
    rand &= ~bg
    hellwert = a.max(axis=2)
    weich = rand & (hellwert >= WEICH)
    if weich.any():
        anteil = np.clip((255 - hellwert) / max(1, 255 - WEICH), 0, 1)
        alpha[weich] = (anteil[weich] * 255).astype(np.uint8)

    out = Image.fromarray(np.dstack([np.asarray(im).astype(np.uint8), alpha]), "RGBA")
    kasten = out.getbbox()
    if kasten:
        out = out.crop(kasten)

    os.makedirs(os.path.dirname(ziel) or ".", exist_ok=True)
    out.save(ziel)
    anteil_weg = bg.mean() * 100
    return out.size, anteil_weg


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    *quellen, zielordner = argv
    for q in quellen:
        name = os.path.splitext(os.path.basename(q))[0] + ".png"
        ziel = os.path.join(zielordner, name)
        (bw, bh), weg = freistellen(q, ziel)
        print("  %-14s -> %4d x %-4d  %4.1f %% Hintergrund entfernt" % (name, bw, bh, weg))


if __name__ == "__main__":
    main(sys.argv[1:])
