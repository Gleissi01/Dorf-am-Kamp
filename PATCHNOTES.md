# Patch Notes

## Gegen die Wölfe kann man jetzt etwas tun

Dein ältester Kritikpunkt. Drei Wege, die sich ergänzen:

**Die Hundehütte** — neu in der Vieh-Leiste, 1x1, 6 Holz, 3 Bretter, 1 Nagel,
niemand muss eingeteilt werden. Der Hofhund deckt alles im Umkreis von 8
Feldern ab. Wölfe gehen eine bewachte Weide gar nicht erst an, und wer dem
Hund zu nahe kommt, dreht ab und zieht sich zurück.

**Die Treibjagd** — beim Wolfsereignis steht jetzt eine echte Entscheidung
statt eines "Verstanden"-Knopfes:

| | |
|---|---|
| Treibjagd ansetzen | braucht 4 Männer zwischen 18 und 60. Jeder Wolf wird zu 70 % erlegt, der Rest zieht ab. Das Fleisch kommt ins Lager, 4 Nahrung je Wolf. Zu 25 % kommt einer verletzt heim und liegt sechs Tage. |
| Abwarten | wie bisher |

**Der Jäger** nimmt weiter die Fährte auf, das war schon drin.

Der Ereignistext sagt jetzt auch, was du hast: ob ein Jäger besetzt ist und
wie viele Hofhunde stehen.

Dazu: der Steinhaufen auf der Baustelle ist da. Ein Ziegelhaus bekommt jetzt
Steine und Mörtel, ein Wohnhaus Bretter und Strohbunde.

## Gerüst, Bretter, Mörtel — echte Bilder auf der Baustelle

Vier neue Bilder, die auf jeder Baustelle gleich aussehen und deshalb nicht
je Gebäude gezeichnet werden müssen:

- **Gerüst** aus Rundhölzern mit Seilbünden, ersetzt die gezeichneten
  Stangen. Eines ab 30 %, das zweite ab 62 %.
- **Bretterstapel**, **Strohbund** und **Mörtelkübel mit Leiter** liegen vor
  dem Bau — und zwar das, was für dieses Gebäude tatsächlich geliefert
  wurde. Ein Ziegelhaus bekommt den Mörtel, ein Wohnhaus Bretter und Stroh.

Zusammen 30 KB. Die Datei liegt jetzt bei 2,56 MB.

Nicht gemacht: Mauern und Dächer je Bauabschnitt als Bild. Das wären drei
Bilder mal 55 Gebäude, rund 860 KB, und sie müssten pixelgenau zum fertigen
Gebäude passen. Der Dachstuhl kommt weiter aus dem fertigen Bild.

## Baustellen bauen jetzt in Abschnitten

Eine Baustelle war ein brauner Fleck mit gestricheltem Rahmen. Jetzt
entsteht das Haus so, wie es gebaut wird:

| Fortschritt | was zu sehen ist |
|---|---|
| bis 12 % | abgesteckt, Boden aufgegraben, Fundamentsteine am Rand |
| 12–50 % | **Rohbau**: die Mauern wachsen aus dem Boden, oben die rohe Mauerkrone |
| 50–72 % | **Dachstuhl**: Sparren und First stehen frei, Traufbalken quer |
| 72–100 % | **Dach decken**: das Dach schließt von der Traufe nach oben |

Die Dachform ist nicht geraten: das Spiel liest die Traufe und den Umriss
aus dem Gebäudebild selbst, indem es die breiteste Zeile sucht. Darum passt
der Dachstuhl zu jedem Gebäude, auch zu neuen.

Dazu: das gelieferte Material liegt als Bretterstapel und Steinhaufen auf
der Baustelle, das Gerüst steht seitlich statt quer über dem Dach, und die
Grube verschwindet, sobald die Mauern stehen.

## 10. Oktober 1800 — Vieh, Dächer, Winter

### Vieh

**Jedes Tier hat jetzt ein Geschlecht.** Stier und Kühe, Widder und
Mutterschafe, Eber und Sauen, Hahn und Hennen. Ohne beide kein Nachwuchs.
Eier und Milch kommen weiter ohne Männchen, nur die Vermehrung steht still.
Im Stallfenster steht die ganze Herde: „1 Stier, 3 Kühe, 2 Kälber".

**Nachwuchs kommt als Jungtier.** Küken brauchen 18 Tage, Ferkel 25, Lämmer
30, Kälber 40, bis sie erwachsen sind. Solange geben sie nichts und zeugen
nichts. Der Fleischhauer lässt sie stehen, Wolf und Hunger nicht.

**Zwölf neue Tierbilder** — Stier, Kuh, Kalb, Widder, Mutterschaf, Lamm,
Eber, Sau, Ferkel, Hahn, Henne, Küken. Die Kuh ist auf Waldviertler
Blondvieh umgestellt, damit eine Rasse im Zaun steht.

**Neu: die Schafweide.** 4×4, 8 Holz und 3 Nägel, gehört zum Schafstall in
der Nähe. Von Frühling bis Herbst steht die Herde draußen, die Wolle wächst
um die Hälfte schneller.

**Der Viehtreiber zeigt seine ganze Herde.** Du suchst aus, was du brauchst,
statt zu nehmen, was er zufällig dabeihat. Gekaufte Tiere gehen in den Stall
mit dem meisten Platz.

### Behoben

- **Schweine und Hühner waren unsichtbar.** Sie wurden im Zweig für Gebäude
  ohne Bild gezeichnet; seit die Ställe Bilder haben, lief der nie.
- **Der Händler kam ein- bis zweimal im Jahr.** Er hing im selben Topf wie
  Feuer und Seuche und nur im Sommerhalbjahr. Jetzt kommt er unabhängig
  davon, rund fünfmal im Jahr, bei Viehnot öfter.
- **Hunger hat sofort getötet.** Jetzt zählt jeder Stall seine Hungertage:
  erst beim zweiten Mal ohne Futter geht ein Tier ab, und das letzte
  Zuchtpaar hält neun Fütterungen durch. Im November sagt das Spiel, wie
  viel Heu und Getreide das Vieh über den Winter braucht.
- **Kaputte Dächer** waren sechs graue Rechtecke. Jetzt wird die Dachfläche
  aus dem Gebäudebild gesucht: vergrautes Stroh, Mulden, offene Löcher mit
  ausgefransten Halmen.
- **Schnee lag als Rechteck** über Häusern, Gärten, Weiden, Teich und
  Friedhof. Jetzt folgt er dem Umriss.
- **Winterwege** lagen heller als der Boden und sahen aus wie hingelegte
  Rechtecke. Jetzt deckt sie der Schnee zu.
- **Winter lief mit 22 statt 61 Bildern je Sekunde.** Über jedem Gebäude lag
  ein Filter, jedes Bild neu gerechnet. Wird jetzt einmal je Gebäudeart
  gerechnet und gemerkt.

### Für dein laufendes Spiel

Ställe mit mindestens zwei Tieren bekommen beim Laden ein Zuchtpaar
zugewiesen. Leere Ställe gelten als Viehnot — der Viehtreiber kommt dann
bald vorbei.
