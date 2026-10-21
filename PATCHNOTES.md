# Patch Notes

## v68 — Besucher melden sich mit einer Marke

Händler, Boten und der Pfleger öffnen kein Fenster mehr mitten im Spiel. Stattdessen erscheint unten rechts eine kleine Marke.

- Marke antippen öffnet das Angebot. „Später“ schließt es wieder, die Marke bleibt.
- Händler und Boten der Städte: Marke bleibt 3 Spieltage, ein Balken zeigt die Restzeit. Danach zieht der Besucher ohne Folgen weiter.
- Pfleger und Bote des Grundherrn (rote Marke): bleiben 5 Spieltage. Ohne Antwort gilt es als Verweigern (gleiche Folgen wie der Knopf „Verweigern“).
- Solange eine Marke wartet, kommt kein weiterer Besucher.

## v67 — Dorfgeschichten

Ereignisse treffen jetzt einzelne Dorfbewohner und hängen von ihrer Eigenschaft ab. Jede Entscheidung erscheint als Fenster.

- Takt: alle 10 Tage mit 60 % Chance, danach mindestens 10 Tage Pause. Erst ab Tag 110 und ab 8 Einwohnern. Jede Person erlebt höchstens eine Geschichte pro Jahr. Es gibt immer eine Option ohne Kosten.
- Zwei neue Eigenschaften: trinkfest (etwas seltener krank) und streitsüchtig. Bestehende Bewohner behalten ihre Eigenschaft.
- Vier Geschichten: Händel im Wirtshaus (trinkfest/streitsüchtig, braucht Wirtshaus), Der Kränkliche im Winter (Bader, Kräutertee oder nichts tun), Ein Fleißiger will mehr (Aufstieg oder vertrösten; wer vertröstet wird, zieht mit 30 % in 20 Tagen weg), Ein gelehriges Kind (Schulfortschritt gegen Gulden).
- Weggang nur, wenn mindestens 6 Einwohner bleiben, die Person keine kleinen Kinder hat und nicht die einzige Kraft ihres Betriebs ist.
- Lebenslauf: Die Personenkarte zeigt bis zu 6 Einträge pro Person.

## v66 — Namen und Eigenschaften

Neue Dorfbewohner tragen Namen, wie sie um 1800 im Waldviertel üblich waren, und jeder hat eine Charaktereigenschaft.

- Namenslisten erweitert (Jodok, Korbinian, Apollonia, Kunigunde …; Familiennamen wie Weinstabl, Zeilinger, Müllner). Bestehende Bewohner behalten ihren Namen.
- Sechs Eigenschaften: fleißig (+10 % Tempo), gemächlich (−10 %), robust (selten krank), kränklich (öfter krank), gelehrig (Erfahrung +50 %), genügsam (weniger Hunger).
- Sichtbar in der Leute-Liste und auf der Personenkarte. Kinder erben mit 50 % die Eigenschaft eines Elternteils.
- Alte Spielstände: Bewohner bekommen beim Laden stabil eine Eigenschaft zugewiesen.

## v65 — Winter-Heimarbeit

Im Winter ruhen Felder, Sammler und Imker. Wer keine Winterstelle hat, stand
bisher herum. Jetzt arbeitet er zu Hause.

- **Dezember bis Februar:** Freie Erwachsene und Rentner gehen heim und
  spinnen oder weben. Aus **2 Flachs wird 1 Leinen**, aus **2 Wolle 1
  Wollstoff**. Dafür braucht es keine Weberei
- **Langsam und mit schlechter Ausbeute:** Eine Fuhre dauert etwa drei
  Spieltage, und die Weberei holt mehr heraus (4 Flachs ergeben dort
  3 Leinen). Heimarbeit ersetzt die Weberei also nicht, sie nutzt die Winterzeit
- **Die Weberei hat Vorrang:** Webt eine besetzte Weberei gerade Leinen,
  lässt die Heimarbeit den Flachs liegen (bei Wolle genauso). Es wird nichts
  schlechter verwertet als nötig
- Gearbeitet wird nur, solange der Rohstoff im Lager liegt und noch nicht
  40 Leinen oder 40 Wollstoff vorrätig sind
- Auf der Personenkarte steht „Heimarbeit“. Die Leute verschwinden dabei im
  Haus
- Im März meldet das Spiel, was über den Winter entstanden ist
- Kinder, Kranke und Leute mit Stelle sind nicht betroffen
- Das Hauptmenü zeigt „Version 65“

## v64 — Spielstand als Datei sichern und laden

Bisher lag der Spielstand nur im Speicher des Browsers. Wer die Browserdaten
löscht, das Handy wechselt oder die App neu installiert, hat sein Dorf
verloren. Jetzt gibt es eine Sicherung als Datei, auf Handy und PC.

- **Hauptmenü, bei jedem Spielstand:** „Sichern (Datei)“ lädt eine Datei
  `Dorf-am-Kamp_Spielstand1_2026-10-19.json` herunter (Dorf, Leute, Lager,
  Gulden, Aufträge, Sättigung, alles)
- **„Aus Datei laden“** liest so eine Datei in den gewählten Spielstand.
  Ist der Platz belegt, fragt das Spiel vorher „Wirklich überschreiben?“.
  Danach auf „Spielen“ tippen
- Die Datei wird vorher geprüft. Ist es keine gültige Spielstand-Datei
  (falsches Format, kaputt, zu groß), steht eine Meldung im Menü und der
  Spielstand bleibt unangetastet
- Wird in den Spielstand geladen, in dem man gerade spielt, ersetzt der
  geladene Stand das laufende Dorf. Das alte Dorf überschreibt ihn nicht
- Sichern und Laden gehen auch zwischen Handy und PC, zum Beispiel per
  Cloud-Ordner oder Mail an dich selbst
- Das Hauptmenü zeigt „Version 64“

## v63 — Händler-Aufkauf folgt der Sättigung

Seit v62 drückt man den Preis, wenn man immer dasselbe in dieselbe Stadt
liefert. Wer die Ware stattdessen dem Wanderhändler gab, umging das. Das ist
jetzt zu.

- **Der Händler trägt die Ware in die Stadt mit der besten Nachfrage**
  (Krems, Zwettl oder Horn, je nachdem, wo der Preis gerade am wenigsten
  gedrückt ist). Sein Angebot wird um denselben Abschlag gekürzt und trägt
  ihn am Knopf, z. B. „(−27 %)“
- **Die verkaufte Menge zählt zur Sättigung** dieser Stadt. Wer dem Händler
  dreimal Holz gibt, bekommt später auch am Handelshaus weniger dafür
- Die Nachfrage erholt sich wie bisher (rund drei Wochen zur Hälfte)
- Der Händler zahlt weiterhin nur einen Bruchteil des Handelshaus-Preises
  und kauft nur, was im Lager reichlich da ist (ab 60). Er bleibt also
  Notverkauf, kein Gewinnweg
- **Marktstand unverändert:** Dort kaufen die Dorfbewohner, es fließt kein
  Geld von außen herein. Eine Sättigung wäre dort unlogisch
- Das Hauptmenü zeigt „Version 63“

## v62 — Handels-Sättigung: Wer immer dasselbe liefert, drückt den Preis

Bisher brachte jede Fuhre denselben Preis, egal wie oft man dieselbe Ware in
dieselbe Stadt schickte. Das machte Handel zum Dauerklick. Jetzt reagiert der
Markt der Stadt.

- **Preis fällt mit der gelieferten Menge**, je Stadt und je Ware
  (Faktor 1/(1 + Sättigung/80), nie unter 30 % des Grundpreises)
- **Erholung:** Die Sättigung baut sich um 3 % pro Tag ab, nach etwa
  23 Tagen ist die Hälfte weg
- **Am Knopf sichtbar:** Der Abschlag steht direkt dabei, z. B. „(−11 %)“.
  Bereits eingeplante Fuhren zählen mit, die Zahlung wird beim Beladen
  neu berechnet
- Der Spielstand speichert die Sättigung mit
- Bestellungen, Marktstand und Händlerbesuche sind unverändert (der
  Händler-Aufkauf hat weiter feste Preise)
- **Fix:** „tr is not a function“ beim Einplanen einer Fuhre (die Variable
  `tr` verdeckte die Übersetzungsfunktion, jetzt `trb`)
- **Fix:** Das Hauptmenü zeigt jetzt die richtige Versionsnummer (stand
  noch auf 58)

## v61 — Soldaten, Boten und Händler kommen sichtbar ins Dorf

Bisher ploppte bei Pfleger, Händler und Bestellung einfach ein Fenster auf.
Jetzt kommen die Leute zu Fuß oder mit Wagen von außerhalb ins Dorf, und das
Fenster öffnet sich erst, wenn sie am Lager (Händler: Handelshaus/Markt)
stehen.

- **Pfleger im Oktober:** Offizier und zwei Soldaten marschieren ein.
  Zehent, Robot und Ablöse laufen wie bisher. Wer **verweigert** und
  dadurch unter 25 Gunst fällt, bekommt (70 %) die Soldaten ins Lager:
  sie nehmen ein Viertel der Nahrung und des Getreides und ziehen mit dem
  Sack ab. Unter 12 Gunst steckt zusätzlich ein Soldat mit der Fackel ein
  Gebäude an (nie Wohnhäuser, Lager, Kapelle, Friedhof)
- **Neu: Forderung des Grundherrn** (ab 1801, ab 10 Leuten, nicht bei sehr
  hoher Gunst, höchstens etwa ein- bis zweimal im Jahr): Ein Bote bringt
  eine Lieferung (Getreide, Holz oder Stein) mit 25 Tagen Frist. Zusagen,
  mit Gulden ablösen oder verweigern. Nach Ablauf holen Soldaten die Ware
  aus dem Lager, Erinnerung 10 und 3 Tage vorher. Fehlt etwas, nehmen sie,
  was da ist, die Gunst sinkt stark, und bei Gunst unter 30 wird ein
  Gebäude angezündet
- **Händler** kommen mit Wagen und Pferd, ein Fußgänger mit Kraxe geht mit
- **Boten** der Städte (Bestellungen) laufen schnell ins Dorf
- Besucher kommen vom **Kartenrand** und gehen am selben Rand wieder ab. Lange Wege laufen sie schneller, damit die Ankunft nach etwa 20 Sekunden passiert
- Es gibt immer nur einen Besuch gleichzeitig. Ist kein Weg zum Lager frei
  oder läuft schon ein Besuch, kommt das Fenster sofort wie früher. Nichts
  kann hängen bleiben (Zeitsicherung 2 Minuten)
- Besucher werden nicht gespeichert. Lädt man mitten im Besuch, kommt das
  Ereignis einfach am nächsten Tag wieder
- Gunst und Forderung werden gespeichert. Das Oktober-Jahr des Pflegers
  wurde bisher gespeichert und geladen, jetzt auch die Forderung
- Sieben neue Figuren, englische Texte

**Ehrlich dazu:** Die Soldaten sind keine Kampfeinheit. Man kann sie nicht
aufhalten, nur mit Gunst vermeiden. Das Feuer löschen die Dorfleute wie jedes
andere.

### Gemessen

Testdorf: Pfleger mit Plünderung und Brandstiftung, Forderung erfüllt und
nicht erfüllt, Händler, Bote, 3 Jahre Dauerlauf mit Zufallsantworten:
keine Konsolenfehler, jeder Besuch endet nach höchstens 26 Sekunden.

## v60 — Honig ist eine eigene Ware

Die Imkerei lieferte bisher einfach „Nahrung“. Jetzt liefert sie **Honig**,
eine eigene Ware im Lager (Gruppe Nahrung und Futter).

- **Gegessen:** je acht Leute ein Glas im Monat. Jedes Glas sättigt wie
  3 Nahrung, und Honig zählt als **eigene Nahrungsquelle** für die
  Abwechslung (Stimmung, Auftrag „4 Nahrungsquellen“)
- **Verkauf:** Überschuss kauft das Handelshaus (Grundpreis 3 Gulden, wie
  Bier und Nahrung — bewusst nicht mehr, du hast ohnehin viel Geld)
- Imkerei, Ertrag und Jahreszeiten sind unverändert; Honig gibt es nur im
  Frühling und Sommer
- Neues Honigglas als Tragebild, Hilfe-Absatz, englische Texte

**Ehrlich dazu:** Eine Imkerei füllt dadurch die Vorratskammer weniger als
vorher, weil Honig nur monatlich in kleinen Mengen gegessen wird. Wer sich
auf sie verlassen hat, braucht ein Feld mehr. Dafür taugt sie jetzt als
Handelsware und Abwechslung.

### Gemessen

Testdorf, 150 Tage: 45 Honig im Lager, der Verbrauch läuft alle 10 Tage,
die Quelle „Imkerei“ bleibt als Abwechslung aktiv, keine Konsolenfehler.

## v59 — Hopfengarten, und die Brauerei braucht jetzt Hopfen

### Hopfen

Neues Gebäude **Hopfengarten** (Nahrung, ab Dorf, 4×4, 12 Holz, 2 Arbeiter).
Der Hopfen rankt an Stangen, wird gesät und im Spätsommer geerntet; ein
Garten liefert rund 40 Hopfen je Ernte.

- **Brauerei:** 3 Getreide + 1 Hopfen = 4 Bier
- **Ohne Hopfen:** nur Dünnbier, 2 Bier aus 3 Getreide. Die Brauerei steht
  also nie still, alte Spielstände laufen weiter
- **Handel:** Hopfen gibt es auch von den Händlern aus Böhmen und Bayern
  (20 Stück für 18 Gulden)
- Die Brauerei meldet im Status, ob sie Bier oder Dünnbier braut
- Hilfe: neuer Absatz zum Bier unter „Woher kommen Rohstoffe?“

### Gemessen

Testdorf, 210 Tage: im Lager lagen mit Hopfengarten 346 Bier, ohne 208
(gebraut: 416 gegen 278). Hopfen wächst, wird geerntet und verbraucht, keine
Konsolenfehler.

### Noch offen

Der Hopfengarten wird vorerst vom Code gezeichnet (Stange und Laub). Die
gemalten Feldbilder `f_hopfen` und `f_hopfenreif` fehlen noch; sobald sie da
sind, übernimmt das Spiel sie automatisch.

### Behoben

Die englischen Texte „Genug Scheitholz auf Lager“ und „Brennholz · Gewand“
aus v57/v58 griffen nie, weil die Schlüssel falsch geschrieben waren.

## v58 — Scheitholz als eigene Ware, und ein richtiger Hilfe-Guide

### Scheitholz

Du wolltest Brennholz als eigene Sache, also ist es jetzt eine eigene Ware.
Das Sägewerk ist der Umwandler: aus Rundholz wird **entweder Bauholz
(Bretter) oder Brennholz (Scheitholz)**. Damit stimmt deine ursprüngliche
Formulierung wieder — Bretter, Brennholz oder nach Bedarf.

Drei Betriebsarten:

- **Nach Bedarf** (neue Grundeinstellung) — sägt Bretter, solange eine
  Baustelle wartet oder unter 20 Bretter im Lager liegen, und hackt sonst
  Scheitholz für den Winter
- **Bretter** — immer Bretter, bis 80 auf Lager
- **Scheitholz** — immer Scheitholz, bis 140 auf Lager

**Geheizt wird mit Scheitholz. Rundholz geht auch, aber schlecht: davon
braucht ein Haus das Doppelte.** Das ist der eigentliche Unterschied und der
Grund, die Säge im Herbst umzustellen. Gemessen: Mit Scheitholz verbraucht
das Testdorf 44 Einheiten je Heiztag, mit Rundholz 88.

Am Marktstand kaufen die Haushalte zuerst Scheitholz (⅞ Gulden), sonst
Rundholz (⅖) — und davon dann eben doppelt so viel. Die Städte bestellen
Scheitholz auch.

**Dein Spielstand bleibt heil:** Beim Laden bekommst du 0 Scheitholz, und
weil Rundholz weiter heizt, friert niemand. Du merkst es nur daran, dass
mehr Holz draufgeht, bis du die Säge umstellst.

### Hilfe-Guide (Punkt 26)

Im Menü unter Hilfe stehen jetzt vier Abschnitte vorne, mit den echten
Bedingungen aus dem Code statt vager Tipps:

- **Woher kommen Leute?** Kinder brauchen Paar, eigenes Haus, freies Bett,
  Stimmung ab 50 und Vorrat im Lager. Zuzug ab Stimmung 70 plus Polster, je
  besser der Ruf desto öfter. Anwerben als Notlösung. Heiraten nur mit
  Pfarrer.
- **Woher kommen Rohstoffe?** Was aus der Landschaft kommt, was verarbeitet
  wird, was nachwächst und was man zukaufen muss.
- **Woher kommen Gulden?** Steuer, Zunftabgabe, Marktstand, Bestellungen —
  und der Hinweis, dass Bestellungen das einzige Geld von außen sind. Dazu
  die wichtigste Regel: Lohnsumme über Einnahmen führt zum Streik.
- **Handel.** Wanderhändler, Handelshaus, was welche Stadt zahlt, wie
  Bestellungen und Ruf zusammenhängen.

**Zum Testen:** Menü → Hilfe. Und stell dein Sägewerk auf „Nach Bedarf", dann
legt es im Herbst von selbst Scheitholz an.

## v57 — Maifest, Erntedank und die Säge mit Wahl

### Maifest und Erntedankfest (Punkt 22)

Die Bilder lagen seit v49 im Spiel und hatten nichts zu tun außer Dorfschönheit.
Jetzt haben sie einen Zweck:

- **Maifest** am 1. Mai, wenn ein **Maibaum** steht. Bis zu zehn Leute legen die
  Arbeit nieder und tanzen einen Tag lang.
- **Erntedank** am 1. Oktober, wenn eine **Erntekrone** steht. Bis zu zwölf
  Leute. Ist das Lager voll, fällt das Fest größer aus; ist es mager, wird
  trotzdem gefeiert, nur bescheidener.

Gefeiert wird an der Festtafel, sonst am Dorfplatz, sonst beim Zierstück selbst.
Jedes Fest gibt es einmal im Jahr und es steht in der Chronik.

Gemessen: Maifest hebt die Stimmung von 53 auf 61, Erntedank bei vollem Lager
von 61 auf 69.

### Sägewerk mit Wahl (Punkt 18)

Drei Einstellungen, wie beim Schlachthaus und der Schmiede:

- **Immer sägen** — wie bisher, bis 80 Bretter auf Lager
- **Nach Bedarf** — sägt nur, wenn eine Baustelle Bretter braucht oder der
  Vorrat unter 20 fällt
- **Holz schonen** — sägt gar nicht

**Eine Anmerkung dazu, weil du „Brennholz" geschrieben hast:** Im Spiel ist
Holz zugleich Bauholz und Brennholz, es gibt keine getrennte Ressource.
„Brennholz machen" kann also nur heißen: nicht sägen, damit der Vorrat fürs
Heizen bleibt. Genau das macht „Holz schonen" — im Winter der Unterschied
zwischen warm und kalt. Wenn du wirklich zwei getrennte Waren willst
(Scheitholz und Bauholz), sag Bescheid, das ist aber ein größerer Umbau an
jeder Stelle, die Holz anfasst.

**Zum Testen:** Sägewerk antippen, umstellen, im Statustext schauen was es
sagt. Und bau einen Maibaum, wenn keiner steht — im Mai passiert dann was.

## v56 — Der Bestellungs-Motor

Das ist der Punkt 13 aus deiner Liste: „Nach dem Markt wird es monoton." Und
gleichzeitig die Lösung für dein Geldproblem, weil Bestellungen das einzige
sind, was Geld von außen ins Dorf bringt. Alles andere schiebt nur zwischen
Gemeindekasse und Haushalten hin und her.

### Mehrere Bestellungen gleichzeitig

Bisher: eine offene Bestellung, Prüfung alle 10 Tage, 45 Tage Sperrfrist,
dann 50 Prozent Chance. Macht rund zwei Bestellungen im Jahr — die halbe
Spielzeit ohne Auftrag.

Jetzt: bis zu drei offen (eine bis zum Dorf, zwei ab Dorf, drei ab Markt),
Prüfung zweimal je zehn Tage, 15 Tage Sperrfrist. Gemessen im Testdorf:
**vier Bestellungen in 70 Tagen** statt zwei im Jahr.

### Jede Stadt bestellt, was sie braucht

Die Preistabelle der drei Städte lag schon im Code, wurde aber nie benutzt —
alle zahlten gleich viel. Jetzt bestellt jede Stadt bevorzugt das, wofür sie
gut zahlt, und zahlt auch danach:

- **Krems** an der Donau: Bauholz, Bretter, Stein, Leinen
- **Zwettl** im Westen: Getreide, Nahrung, Bier
- **Horn** im Norden: Stein, Werkzeug, Nägel

Zwettl zahlt für Getreide das 1,4-fache, Horn für Stein das 1,6-fache. Es
lohnt sich also zu schauen, wer gerade fragt.

### Schwankende Preise

Jeder Bote bringt einen anderen Preis mit, plus/minus rund 20 Prozent. Im Text
steht, woran du bist: „Sie zahlen heuer gut dafür" oder „Der Preis ist mager,
die Stadt hat selber genug." Damit ist Ablehnen eine echte Entscheidung und
nicht nur Rufverlust.

### Kürzere Fristen

Vorher pauschal 60 Tage. Jetzt 25 bis 45 Tage, je nach Menge. Große
Bestellungen geben mehr Zeit, kleine müssen flott gehen.

### Ruf wirkt jetzt wirklich

Ablehnen kostet 3 Ansehen (vorher 2), Frist verpassen 10, Liefern bringt 6.
Der Ruf bestimmt nicht nur den Preis, sondern auch **wie oft** sich die Städte
überhaupt melden. Wer verlässlich liefert, bekommt mehr und besser bezahlte
Aufträge.

### Anzeige

Das Auftragsfenster zeigt alle offenen Bestellungen nach Frist sortiert, jede
mit eigenem Liefern-Knopf, Lagerstand und Resttagen. Die Leiste oben zeigt die
fertige zuerst, sonst die dringendste, und wie viele offen sind.

**Dein Spielstand:** Die laufende Bestellung wandert beim Laden automatisch ins
neue System, da geht nichts verloren.

**Zum Testen — und da brauche ich dich:** Ich weiß nicht, ob die Bezahlung
passt. Im Testdorf kamen über 70 Tage rund 1.400 Gulden herein, aber ich habe
das Lager vorher vollgefüllt und musste nichts produzieren. Bei dir muss das
Zeug erst hergestellt werden, das ist der eigentliche Bremsklotz. Sag mir nach
ein paar Spieljahren, ob es zu leicht oder zu knapp ist — dann drehe ich an
den Preisen, nicht vorher auf Verdacht.

## v55 — Geldbuch oben in der Leiste, und der Schuldschein

### Geldbuch beim Gulden-Feld

Deine Idee, und die bessere Platzierung: Das Gulden-Feld in der oberen Leiste
öffnet jetzt die Gemeindekasse, genau wie das Lager-Feld das Lagerfenster.
Drin stehen Kassenstand, Lohnsumme je zehn Tage, die Einnahmen der letzten
Abrechnung und das volle Geldbuch. Im Rathaus bleibt es zusätzlich stehen.

Neu dabei: Liegt die Lohnsumme über den Einnahmen, steht es rot da. Und bei
Streik steht dort auch, wie du wieder herauskommst.

### Lohnwarnung, bevor es zu spät ist

Bisher hast du erst gemerkt, dass die Kasse nicht reicht, als der erste
Zahltag ausgefallen ist. Jetzt sagt es dir das Spiel eine Abrechnung vorher:
„Die Lohnsumme liegt über den Einnahmen." Da ist noch Zeit, Betriebe zu
leeren oder mehr Ware an den Stand zu bringen.

### Schuldschein beim Grundherrn

Das war eine Sackgasse, und zwar eine, in der du gerade steckst: Leere Kasse
heißt kein voller Lohn, kein voller Lohn heißt Streik, Streik heißt weniger
Produktion, weniger Produktion heißt noch weniger Einnahmen. Einmal drin,
kommst du aus eigener Kraft kaum wieder heraus.

Reicht die Kasse am Zahltag nicht, bietet der Grundherr jetzt einen
Schuldschein an. Die Summe deckt etwa drei Zahltage. Zurück müssen 25 Prozent
mehr, in acht Raten, fällig bei jeder Abrechnung — und zwar nach den Löhnen,
nicht davor, sonst nimmt die Rate genau das Geld weg, das den Streik beenden
soll.

Kein Geschenk, sondern eine Entscheidung: Du kannst auch ablehnen und den
Streik in Kauf nehmen. Wer eine Rate nicht in Gulden zahlen kann, bei dem
holen sich die Leute des Grundherrn Vorräte aus dem Lager, und die Stimmung
sinkt. Neuer Schuldschein erst 30 Tage nach der Tilgung.

**Getestet:** Dorf mit leerer Kasse und 54 Gulden Lohn. Angebot kommt am
Zahltag, nach Annahme werden die Löhne voll bezahlt (37 von 37, kein Streik),
die 125 Gulden werden über acht Abrechnungen getilgt, die Einwohnerzahl bleibt
stabil bei 41.

**Zum Testen:** Oben auf Gulden tippen. Und schau, ob bei deinem Spielstand
die Lohnwarnung kommt — bei 135 Lohn gegen 86 Einnahmen sollte sie sofort da
sein.

## v54 — Das Geldbuch und zwei Sackgassen beim Wasser

### Geldbuch im Rathaus

Du hast 15 Gulden bei 55 Leuten, 113 rein und 135 raus. Statt blind am
Steuersatz zu drehen, siehst du jetzt selbst, wo es hingeht: Das Rathaus
zeigt Einnahmen und Ausgaben der letzten zehn Tage, aufgeschlüsselt nach
Steuer, Zunftabgabe, Marktstand, Bestellungen, Löhnen, Handel, Grund und
Anwerbungen — und unterm Strich, ob die Kasse wächst oder schrumpft.

**Zum Testen:** Rathaus antippen, zum „Geldbuch der letzten zehn Tage"
scrollen. Schick mir einen Screenshot davon, dann sehe ich deine Zahlen.

### Zunftabgabe — und warum sie dein Problem nicht löst

Handwerk und Handel zahlen jetzt zusätzlich eine Zunftabgabe, gestaffelt nach
Ertrag (Wirtshaus und Handel am meisten, Köhler und Dachdecker am wenigsten).
Historisch sauber, aber ich sage es offen: **Das schließt deine Lücke nicht.**
Gemessen bringt sie 3 bis 9 Gulden. Sie zieht aus derselben Haushaltskasse wie
die Kopfsteuer und teilt nur eine Basis, die ohnehin leer läuft.

In meinem Testdorf fallen die Haushaltskassen von 220 auf 35 Gulden, und die
Steuer bricht von 81 auf 13 ein — bei gleichbleibender Einwohnerzahl. Das ist
dein Muster. Der echte Hebel ist Geld von außen: Bestellungen aus der Stadt.
Das ist der nächste Bau, und es behebt die Monotonie gleich mit.

### Hortungssteuer verschärft

Wer mehr als 25 Gulden hortet, gibt 18 Prozent davon ab (vorher ab 40 Gulden
zehn Prozent). Geld, das in Haushalten liegen bleibt, fehlt im Kreislauf.

### Wasser: zwei Wege, die in den Tod führten

**Kranke konnten sich kein Wasser mehr holen.** Wer vom Durst krank wurde, war
damit vom Wasserholen ausgeschlossen — und drei Trinktage später tot. Waren
alle im Haus krank, ging niemand mehr zum Brunnen. Eine Einbahn ohne Ausweg.
Jetzt tragen Nachbarn die Eimer hin, so wie das am Land üblich war. Getestet
mit drei Häusern voll Dauerkranker: nach 56 Tagen leben alle acht noch, die
Fässer werden immer wieder nachgefüllt.

**Der nächste Brunnen war nicht immer der erreichbare.** Die Leute suchten den
Brunnen mit der kürzesten Luftlinie und prüften nie, ob ein Weg hinführt. Stand
ein Haus im Weg, scheiterte der Gang stumm — und sie verdursteten neben zwei
anderen, erreichbaren Brunnen. Jetzt werden die nächsten vier Wasserstellen
durchprobiert.

**Verbauter Heimweg.** Kam jemand mit vollem Eimer nicht mehr heim, wurde das
Wasser weggeschüttet und das Ganze begann von vorn — endlos, bis die Leute
starben. Jetzt stellt er den Eimer beim nächsten Nachbarn ab, der ihn braucht.
Und nach dem dritten Fehlschlag bekommst du eine Warnung: „Haushalte kommen
nicht zum Brunnen — der Weg ist verbaut." Dann kannst du einen Brunnen näher
setzen oder ein Gebäude abreißen, statt dass das Dorf stumm ausstirbt.

**Zum Testen:** Spiel normal weiter und schau, ob dir eine Wasserwarnung
begegnet. Wenn ja, schick mir einen Screenshot — dann will ich wissen, wo.

## v53 — Der Geisterklick

Du hattest einen Fehler gefunden, den ich in sechs Versuchen nicht nachstellen
konnte: Steuersatz oder Betriebsart springen zurück, „als ob es wer anders
umstellt". Dein Bildschirmvideo hat ihn verraten.

**Was passiert ist:** Die Karte reagiert auf das Loslassen des Fingers. Der
Browser schickt danach aber noch einen Klick an dieselbe Stelle hinterher — und
dort steht inzwischen das Fenster, das gerade aufgegangen ist. Dein Finger
drückt also den Knopf mit, der zufällig unter ihm erscheint. Beim Rathaus ist
das die Steuerzeile, beim Schlachthaus die Tierart.

Du hast nie etwas zurückgestellt. Dein eigener Tipp, mit dem du das Gebäude
angetippt hast, hat zweimal gewirkt: einmal zum Öffnen, einmal auf den Knopf.

**Nachgestellt:** Rathaus auf Steuer „Hoch" gestellt, Fenster zu, Gebäude
wieder angetippt — vorher sprang es auf „Niedrig", jetzt bleibt es auf „Hoch".

**Behoben:** Knopfdrücke im Infofenster werden in den ersten knapp einer halben
Sekunde nach dem Öffnen nicht angenommen. Lang genug für den Geisterklick, kurz
genug, dass man es beim Bedienen nicht merkt. Das gilt für alle Knöpfe im
Fenster, also auch Schlachthaus, Schmiede, Weberei, Schneider, Bergwerk und
Handelsposten.


## v52 — Die Festtafel war so groß wie ein Haus

Du hast recht gehabt, und es war schlimmer als es aussah: nachgerechnet wurde
die Tafel 56 × 46 Pixel gezeichnet, ein Wohnhaus 54 × 47. Sie war also nicht
ungefähr so groß wie ein Haus, sondern exakt. Jetzt ist sie 36 × 29, also gut
halb so hoch wie ein Haus — eine Tafel, an der zwölf Leute sitzen, neben einem
Haus, in dem eine Familie wohnt.

Erntekrone und Maibaum habe ich gegengeprüft, die stimmen.


## v51 — Das Lager zeigt, was drin ist

Der Knopf **Lager** oben links öffnet jetzt ein richtiges Fenster statt einer
Zeile mit sieben Zahlen. Darin steht jede Ware mit Balken und Zahl, dazu wie
viel Platz noch ist:

- **Nahrung und Futter** — Nahrung, Getreide, Heu, Bier
- **Bauen** — Holz, Bretter, Stein, Nägel, Stroh, Schilf, nasses Schilf, Lehm, Ziegel
- **Handwerk und Gewand** — Werkzeug, Erz, Eisen, Holzkohle, Flachs, Leinen,
  Wolle, Wollstoff, Sommer- und Wintergewand

Oben steht, wie viele Lager, Speicher und Heustadel stehen und was wohin geht:
Das Lager fasst Baustoffe und Waren (250 je Lager), der Speicher nur Nahrung
und Getreide (400 je Speicher, dazu 100 je Lager), der Heustadel nur Heu
(300 je Stadel). Wird eine Ware knapp am Anschlag, färbt sich ihr Balken.

Wer gerade etwas trägt, das noch nicht im Lager liegt, wird unten mitgezählt —
dann weißt du, dass noch etwas unterwegs ist.

Nebenbei: In der Kopfzeile stand bei Dezember und September „Tag 6 von 10"
über den Rand hinaus. Jetzt steht dort nur noch der Tag.


## v51 — Das Lagerfenster

Der Lager-Knopf oben klappt nicht mehr nur eine Zeile Kacheln auf, sondern
öffnet ein eigenes Fenster mit allem, was im Dorf liegt.

**Jede Ware mit Balken und Grenze.** Du siehst nicht nur, wie viel Holz da ist,
sondern auch, wie nah es an der Kapazität ist. Was fast voll ist, wird rot —
dann lohnt ein zweites Lager, bevor die Träger vor vollen Regalen stehen.

**Drei Gruppen**, damit man nicht sucht:

- Nahrung und Futter: Nahrung, Getreide, Heu, Bier
- Bauen: Holz, Bretter, Stein, Nägel, Stroh, Schilf, nasses Schilf, Lehm, Ziegel
- Handwerk und Gewand: Werkzeug, Erz, Eisen, Holzkohle, Flachs, Leinen, Wolle,
  Wollstoff, Sommer- und Wintergewand

Oben steht, wie viele Lager, Speicher und Heustadel stehen und was wohin geht:
das Lager fasst Baustoffe und Waren, der Speicher nur Nahrung und Getreide, der
Heustadel nur Heu. Darum hat jede Ware ihre eigene Grenze — Nahrung 500 mit
einem Speicher, Heu 300 je Heustadel, alles andere 250 je Lager.

Unten steht, wie viele Leute gerade etwas tragen, das noch nicht angekommen ist.

**Die Lager-Kachel selbst** zeigt jetzt die Nahrung und daneben, für wie viele
Tage sie reicht. Vorher stand dort die Summe aus Holz, Brettern und Stein, die
nichts aussagte, und die Tagesanzeige war seit dem Umbau der Kopfleiste
verschwunden. Das war ein Rückschritt, der ist behoben.

## v50 — Das Dorf steht am Grab

Stirbt jemand, legen die Angehörigen die Arbeit nieder und gehen zum Friedhof.
Sie stehen beisammen am Rand, ein gutes Stück eines Spieltages lang, dann geht
jeder zurück an seine Arbeit.

**Wer kommt:** Ehepartner, Eltern, Kinder und Geschwister, dazu der Pfarrer,
wenn einer im Dorf ist. Kinder unter sechs bleiben daheim. In einem Dorf mit
höchstens vierzehn Leuten kommen auch zwei Nachbarn mit, weil dort jeder jeden
kennt.

**Höchstens sechs Leute** gehen hin. Sonst stünde bei einer Seuche das halbe
Dorf auf dem Friedhof und die Arbeit läge still — das wäre eine Strafe auf die
Strafe.

Ein Begräbnis mit Pfarrer tröstet das Dorf ein wenig, die Stimmung sinkt nicht
so tief. Ohne Friedhof werden die Toten weiterhin in Gföhl begraben, dann
bleibt auch der Trauerzug aus. Der Friedhof hat damit einen zweiten Grund
dazubekommen.

Nachgeprüft: Ehemann und Tochter gehen zum Grab, stehen nebeneinander und
nehmen danach ihre Arbeit wieder auf. Keine Fehlermeldungen.


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
