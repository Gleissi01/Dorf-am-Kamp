# Patch Notes

## v49 — Fünf neue Wildarten, der Damm und zwei Stücke Zierde

Deine acht Bilder sind drin. Gemini hat sie in drei Dateien gepackt, ich habe
sie auseinandergeschnitten — beim Hasen hing der Schweineschwanz am Ohr, das
musste von Hand weg.

**Im Wald leben jetzt sechs Arten statt einer.** Bisher gab es nur das Reh.
Dazu kommen Feldhase, Fuchs, Dachs, Wildschwein und Hirsch. Jede Art hat ihren
eigenen Platz:

| Tier | Fleisch | wo es steht | wie oft |
|---|---|---|---|
| Feldhase | 2 | auch am Feldrand, braucht kaum Wald | sehr oft |
| Reh | 5 | im lichten Wald | oft |
| Fuchs | 1 | am Waldrand | mittel |
| Dachs | 2 | im dichteren Wald | selten |
| Wildschwein | 7 | im Dickicht | selten |
| Hirsch | 9 | tief im Wald | am seltensten |

Der Jäger bringt also nicht mehr immer dieselben fünf Nahrung heim. Ein Hirsch
lohnt den weiten Weg, ein Fuchs kaum. Bei starker Beute kommt eine Meldung.
Die Wölfe reißen alles Wild, nicht mehr nur Rehe, und der Hase flieht am
schnellsten.

**Der Fuchs holt sich Hühner.** Steht ein Hühnerstall ohne Hofhund in der Nähe,
schleicht er sich an und nimmt sich eines. Mit Hundehütte traut er sich nicht
heran. Das ist die einzige neue Mechanik, die ich dazugebaut habe — ein Fuchs,
der nur herumsteht, wäre Deko gewesen.

**Der Damm ist jetzt gemalt.** Das Bild zeigte ein längliches Stück von schräg
oben, das sich nicht aneinanderreihen ließ: drei Dämme nebeneinander ergaben
drei einzelne Haufen. Ich habe aus der Mitte ein kachelbares Stück Schüttung
herausgeschnitten. Jetzt ergibt eine Reihe Dämme eine durchgehende Böschung,
egal in welche Richtung du baust, und nach außen franst sie unregelmäßig ins
Gras aus statt an einer geraden Kante aufzuhören. Im Winter liegt Schnee darauf.

**Festtafel und Erntekrone** stehen in der Zierde-Leiste:

- Festtafel, 2×1, aus 4 Holz, 6 Brettern und 2 Nägeln, Zierwert 3
- Erntekrone, 1×1, aus 8 Getreide und 3 Holz, Zierwert 4

Beide zählen auf die Dorfschönheit. Wenn wir Maifest und Erntedankfest bauen,
sind sie der Platz, an dem sich die Leute sammeln — dafür fehlt noch die
Spiellogik, die Bilder stehen aber schon bereit.

Nachgeprüft: alle acht Bilder laden, sechs Wildarten tauchen im Wald auf und
wandern, keine Fehlermeldungen über fünf Spieljahre.


## v48 — Die sieben Fehler aus deinem Test

**Der Jäger erlegt jetzt wirklich Wölfe.** Das war kaputt, und zwar schlimmer
als gedacht: Im Test vor der Änderung hat ein Jäger in zwanzig Spieltagen
keinen einzigen von drei Wölfen erlegt. Er ist dorthin gelaufen, wo der Wolf
war, als er losging — bis er ankam, war das Rudel weiter, und das ging endlos
so. Die Wölfe verschwanden irgendwann von allein, nicht durch ihn.

Jetzt schießt er, statt hinterherzulaufen: ein Steinschlossgewehr trägt rund
sieben Felder weit, und auf dem Weg pirscht er sich in kurzen Etappen an, statt
quer über die Karte zu marschieren. Nachgeprüft: drei von drei Wölfen erlegt,
auch wenn man die Wölfe unsterblich macht, damit nur der Jäger sie entfernen
kann.

**Getreide bleibt für das Vieh liegen.** Bäcker und Brauer haben aus demselben
Topf genommen wie die Tiere, wer zuerst kam. Für Brennholz gab es längst eine
Winterreserve, für Futter nicht. Ab Herbst wird jetzt zurückgehalten, was
Schweine, Schafe und Rinder über den Winter brauchen — Heu im Stadel wird
gegengerechnet. Nachgeprüft: acht Kühe und sechs Schweine ohne Heu sperren 66
Getreide, der Bäcker schreibt dann "Hält 66 Getreide als Winterfutter für das
Vieh zurück". Mit vollem Heustadel fällt die Reserve auf null.

**Nicht mehr nur die Ruhr.** Es gab schon drei Ursachen — Ruhr, verdorbenes
Wasser, Frieren ohne Wintergewand — aber jeder Tote hieß "an der Ruhr
gestorben". Darum wirkte es wie eine einzige Krankheit. Jetzt hat jede
Krankheit ihren Namen und ihr eigenes Risiko: Ruhr 12 %, Wechselfieber 7 %,
verdorbenes Wasser 6 %, Lungenentzündung 5 %, Grippe 2 %, eine Wunde von der
Treibjagd tötet nicht mehr. Ein Ausbruch trifft auch nicht mehr jeden Fünften,
sondern 10 bis 16 Prozent, mit Bader deutlich weniger. Im Testlauf über fünf
Jahre kamen alle vier Arten vor.

**Die Bildung kann nicht mehr aussterben.** Das war deine Sackgasse: Die
Volksschule brauchte selbst einen Volksschulabschluss. Stirbt der letzte
Absolvent, ist sie nie wieder besetzbar, es gibt nie wieder Absolventen, und
irgendwann steht auch das Rathaus leer. Zwei Änderungen:

- Bäcker, Brauerei, Schmiede, Wagnerei, Weberei, Bader, Spital, Wirtshaus und
  Handelsposten brauchen gar keinen Abschluss mehr. Nur Rathaus (Hauptschule)
  und die Schulen verlangen noch einen.
- Hat im ganzen Dorf niemand den Abschluss, darf ein Ungelernter übernehmen.
  In der Schule lernen die Kinder dann halb so schnell — es geht weiter, aber
  schlechter. Wer einen Abschluss hat, wird weiterhin zuerst genommen.

**Die Kinder laufen nicht mehr vor und zurück.** Am Jahreswechsel kippten
Erntezeit und Notlage im Takt hin und her, und mit jedem Takt wurden die Kinder
zugeteilt und wieder abgezogen. Wer heute hilft, bleibt jetzt bis zum
Tagesende dabei.

**Der Holzfäller nimmt den nächsten Baum.** Markierte Bäume hatten immer
Vorrang, egal wie weit weg sie standen — eine Markierung am anderen Ende der
Karte hat ihn quer durchs Dorf geschickt. Jetzt gewinnt der nächste Baum, und
markierte zählen nur als sechs Felder näher.

**Der Damm ist zu sehen.** Er war ein brauner Fleck mit drei Pünktchen. Jetzt
ist er eine geschüttete Steinwehr: Bruchsteine mit Gras in den Fugen, mehrere
Dammstücke gehen ineinander über, im Winter liegt Schnee darauf. Das ist
gezeichnet, kein gemaltes Bild wie bei den Gebäuden — wenn du eins willst,
sag Bescheid, dann schreibe ich dir den Prompt dafür.

### Dazu die optischen Sachen

**Die obere Leiste hat nur noch fünf Felder:** Lager, Gulden, Leute,
Meilensteine, Dorfstufe. Die Rohstoffe stecken hinter "Lager" — antippen, dann
klappt die Zeile mit Holz, Brettern, Nägeln, Dach, Stein, Nahrung, Werkzeug
und den freien Leuten auf. "Meilensteine" zeigt den Stand und führt in die
Übersicht.

**Die Gebäudeleiste lässt sich wegklappen** über den Knopf "Bauen" rechts
unten, damit man die Karte ganz sieht.

**Betriebe ohne Arbeiter stehen oben in der Liste**, mit einer Zeile darüber:
"Ohne Arbeiter: Jäger, Sägewerk (verfällt), Schmiede". Auf der Karte bleiben
sie kalt — kein Rauch mehr aus dem Kamin — und sie verfallen doppelt so
schnell, weil niemand mehr das Dach flickt.

**Das Jahr läuft in Monaten.** Oben steht jetzt "März 1800 · Tag 2 von 10"
statt der Jahreszeit.

Noch nicht drin, weil dafür Bilder aus Gemini fehlen: Maifest und
Erntedankfest zum Zuschauen, mehr Waldtiere.


## Die Hundehütte hat ihr Bild

Bis jetzt war die Hundehütte gezeichnet: ein brauner Kasten mit Dach. Jetzt
steht eine echte Holzhütte mit Schindeldach, davor liegt der Hofhund an der
Kette.

- Gleiche Größe wie bisher (1×1), etwas größer gezeichnet, damit sie neben
  Weide und Stall nicht verschwindet
- Im Winter bekommt sie Schnee aufs Dach wie jedes andere Gebäude
- An der Wirkung ändert sich nichts: 8 Felder Umkreis, Wölfe drehen ab

Nachgeprüft: Wolf neben dem Hund wird verjagt, bewachte Weide wird nicht
angegangen, Händler, Vieh, Baustellen und Bildrate (55–61) unverändert.

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
