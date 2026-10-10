# Gebäudebilder

## Stand

49 von 66 Gebäuden haben ein gemaltes Bild. Die 17 ohne Bild teilen sich so auf:

**Richtig so, brauchen keins** (werden als Bodenfläche gezeichnet, kein aufrecht stehendes Ding):
Feld, Erdäpfelacker, Flachsfeld, Weide, Heuwiese, Karpfenteich, Damm, Friedhof

**Keine Gebäude:** Horn, Krems, Zwettl (das sind die Städte für den Handel)

**Fehlen wirklich** — die Zierde aus v44, derzeit mit Zeichencode gemalt:

| Schlüssel | Gebäude | Dringlichkeit |
|---|---|---|
| `wegkreuz` | Wegkreuz | hoch, steht aufrecht neben gemalten Häusern |
| `marterl` | Marterl | hoch |
| `maibaum` | Maibaum | hoch |
| `obstbaum` | Obstbaum | mittel |
| `zaun` | Zaun | niedrig |
| `blumen` | Blumenbeet | niedrig, liegt flach am Boden |

## Stil der vorhandenen Bilder

- Leicht schräge Aufsicht von vorne oben, etwa 3/4-Ansicht, immer dieselbe Blickrichtung
- Gemalt/gerendert, nicht Pixelgrafik, aber mit weicher Körnung
- Durchsichtiger Hintergrund, kein Boden, kein Schatten im Bild (den Schatten rechnet das Spiel selbst)
- Gedeckte Erdfarben: Stroh, verwittertes Holz, Kalkputz, grauer Granit
- Waldviertel um 1800: Strohdach, Schindel, Bruchstein, Lehm
- 256 Pixel breit, Höhe je nach Motiv

Zum Vergleich ansehen: Wohnhaus, Brunnen und Bank sind im Spiel die klarsten Beispiele.

## Vorlagen für die Bilderzeugung

Jeweils anhängen: *„Dreiviertelansicht leicht von oben, durchsichtiger Hintergrund,
kein Boden und kein Schatten, gemalte Spielgrafik, gedeckte Erdfarben,
Waldviertel um 1800, 256 Pixel breit."*

- **wegkreuz** — Hölzernes Wegkreuz am Feldrand, dunkel verwittertes Eichenholz, kleines Schindeldachl über dem Querbalken, schlichte helle Figur oder Tafel in der Mitte, etwas Gras am Fuß.
- **marterl** — Gemauerter Bildstock, weiß gekalkter Putz auf Bruchsteinsockel, eine Nische mit kleinem Heiligenbild, oben ein rotes Ziegeldach mit Giebel, schmal und mannshoch.
- **maibaum** — Hoher schlanker Fichtenstamm, geschält, mit grünem Kranz knapp unter der Spitze, bunte Bänder in Rot, Blau, Gelb und Weiß hängen herab, Fuß in Steinen verkeilt.
- **obstbaum** — Einzelner junger Apfelbaum mit dünnem Stamm, runde Krone, ein paar rote Äpfel.
- **zaun** — Kurzes gerades Stück Lattenzaun aus verwittertem Holz, drei Pfosten, zwei Querlatten, von vorne.
- **blumen** — Kleines rechteckiges Beet mit niedriger Holzeinfassung, bunte Bauerngartenblumen, flach von schräg oben gesehen.

## Einbauen

```
python3 tools/add-sprite.py bilder/wegkreuz.png bilder/marterl.png
python3 tools/add-sprite.py bilder/          # alles aus dem Ordner
```

Der Dateiname ohne Endung ist der Schlüssel aus der Tabelle oben.
Das Werkzeug schneidet durchsichtige Ränder weg, skaliert auf 256 Pixel Breite,
wandelt in WebP und trägt den Eintrag in `BSPR` ein. Ein vorhandener Eintrag
wird ersetzt, man kann also gefahrlos mehrmals laufen lassen.

Das Spiel nimmt das Bild automatisch, sobald es da ist, und fällt ohne Bild
auf die gezeichnete Fassung zurück. Es muss also nichts im Code geändert werden.

Danach:
1. Den Cache-Namen in `sw.js` hochzählen, sonst sehen Spieler mit installierter App weiter die alte Fassung
2. Im Spiel nachsehen, ob die Größe passt — wenn nicht, den Faktor in `BSC` setzen
   (`BSC={bank:.55, brunnen:.8, ...}`, Standard ist 1)
