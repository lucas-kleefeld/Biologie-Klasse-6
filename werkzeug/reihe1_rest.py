"""Reihe 1: Aufgaben, Übungen und Modellseiten."""
import zeichnungen as Z

AUFGABEN = {
"01-das-skelett": [
 ("I", "Nenne die vier Aufgaben des Skeletts und gib zu jeder ein Beispiel.", 5),
 ("I", "Beschrifte ein Skelett (Arbeitsblatt oder Zeichnung) mit den Namen der wichtigsten Knochen.", 0),
 ("II", "Vergleiche den Bau von Arm und Bein. Beschreibe Gemeinsamkeiten und Unterschiede.", 5),
 ("II", "Erkläre, warum der Brustkorb aus vielen einzelnen Rippen besteht und nicht aus einer festen Knochenplatte. Denke an das Atmen.", 4),
 ("III", "Ein Neugeborenes hat über 300 Knochen, ein Erwachsener etwa 206. Erkläre, wie das sein kann.", 3),
],
"02-knochen": [
 ("I", "Beschreibe mithilfe der Abbildung den Aufbau eines Röhrenknochens von außen nach innen.", 5),
 ("I", "Nenne die beiden Stoffe, aus denen ein Knochen besteht, und ihre Eigenschaften.", 3),
 ("II", "Erkläre den Versuch mit dem Knochen in Essig. Gehe auf Durchführung, Beobachtung und Erklärung ein.", 6),
 ("II", "Erkläre, warum Röhrenknochen leicht und trotzdem stabil sind. Nutze ein Beispiel aus der Technik.", 4),
 ("II", "Erkläre, warum Kinder sich seltener die Knochen brechen als alte Menschen.", 3),
 ("III", "Ein Mitschüler sagt: „Knochen sind doch tot, die verändern sich nicht.“ Nimm Stellung.", 4),
],
"03-wirbelsaeule": [
 ("I", "Nenne die Abschnitte der Wirbelsäule von oben nach unten mit der Zahl ihrer Wirbel.", 4),
 ("I", "Beschreibe den Aufbau eines Wirbels und die Aufgabe der Bandscheiben.", 5),
 ("II", "Erkläre, warum die Wirbelsäule die Form eines doppelten S hat. Baut dazu ein Modell aus einem geraden und einem gebogenen Draht und lasst ein Gewicht darauf fallen.", 5),
 ("II", "Erkläre, warum man morgens etwas größer ist als abends.", 3),
 ("II", "Erkläre, warum die Lendenwirbel größer sind als die Halswirbel.", 3),
 ("III", "Beurteile, warum eine Verletzung der Wirbelsäule besonders gefährlich sein kann.", 4),
],
"04-gelenke": [
 ("I", "Beschrifte die Teile eines Gelenks und nenne ihre Aufgaben.", 6),
 ("I", "Nenne die vier Gelenktypen mit je einem Beispiel aus deinem Körper.", 4),
 ("II", "Teste an deinem eigenen Körper: In welche Richtungen kannst du Schulter, Ellenbogen, Daumen und Kopf bewegen? Ordne die Gelenke den Gelenktypen zu.", 5),
 ("II", "Erkläre, welche Aufgabe die Gelenkschmiere hat. Vergleiche mit einem Beispiel aus der Technik.", 3),
 ("II", "Erkläre den Unterschied zwischen einer Verstauchung und einer Verrenkung.", 3),
 ("III", "Baut aus Alltagsgegenständen (zum Beispiel Tischtennisball, Joghurtbecher, Pappe, Musterbeutelklammer) Modelle von zwei Gelenktypen. Zeigt, was die Modelle gut darstellen und wo sie vom echten Gelenk abweichen.", 0),
],
"05-muskeln": [
 ("I", "Beschreibe, wie ein Muskel am Knochen befestigt ist.", 3),
 ("I", "Erkläre den Begriff Gegenspielerprinzip am Beispiel des Oberarms.", 5),
 ("II", "Erkläre, warum ein einzelner Muskel ein Gelenk nicht beugen und wieder strecken kann.", 3),
 ("II", "Baut ein Armmodell aus Pappe, Musterbeutelklammern und Gummibändern oder Schnüren. Zeigt damit das Beugen und Strecken und beschreibt, welcher „Muskel“ jeweils zieht.", 0),
 ("II", "Beim Kniebeugen arbeiten an der Vorderseite und an der Rückseite des Oberschenkels zwei Muskeln. Beschreibe, welcher beim Aufstehen und welcher beim Beugen arbeitet.", 4),
 ("III", "Erkläre mit der Hebelwirkung, warum man ein schweres Buch mit gestrecktem Arm kaum halten kann, mit angewinkeltem Arm dicht am Körper aber gut.", 5),
],
"06-haltung-und-sport": [
 ("I", "Nenne drei Haltungsschäden und beschreibe sie kurz.", 4),
 ("I", "Erkläre die PECH-Regel.", 4),
 ("II", "Wiege deinen Schulranzen und dich selbst. Berechne, wie viel Prozent deines Körpergewichts der Ranzen wiegt, und bewerte das Ergebnis.", 4),
 ("II", "Führt in Partnerarbeit richtiges und falsches Heben einer Kiste vor. Die anderen beschreiben, was richtig und was falsch ist, und begründen es.", 0),
 ("II", "Erstelle ein Bewegungstagebuch für eine Woche. Werte aus, an wie vielen Tagen du auf 60 Minuten Bewegung gekommen bist.", 0),
 ("III", "Gestalte ein Plakat für deine Klasse mit Tipps für einen gesunden Rücken. Begründe jeden Tipp mit deinem Wissen über die Wirbelsäule.", 0),
],
}

UEBUNGEN = [
{
"slug": "r1-skelett-zuordnen",
"titel": "Zuordnen: Knochen und ihre Aufgaben",
"kurz": "Wichtige Teile des Skeletts und was sie leisten",
"typ": "zuordnen",
"anleitung": "Wähle für jeden Teil des Skeletts die passende Beschreibung. Prüfen kannst du, wenn alles zugeordnet ist.",
"daten": {"paare": [
 {"links": "Schädel", "rechts": "schützt das Gehirn"},
 {"links": "Brustkorb", "rechts": "schützt Herz und Lunge"},
 {"links": "Wirbelsäule", "rechts": "trägt den Oberkörper und schützt das Rückenmark"},
 {"links": "Becken", "rechts": "trägt die Bauchorgane und verbindet die Beine mit dem Rumpf"},
 {"links": "Schlüsselbein", "rechts": "verbindet das Brustbein mit der Schulter"},
 {"links": "Oberschenkelknochen", "rechts": "längster und kräftigster Knochen"},
 {"links": "Elle und Speiche", "rechts": "zwei Knochen im Unterarm, ermöglichen das Drehen der Hand"},
 {"links": "Kniescheibe", "rechts": "liegt vorn auf dem Kniegelenk und schützt es"}
]}
},
{
"slug": "r1-knochen-lueckentext",
"titel": "Lückentext: Aufbau eines Knochens",
"kurz": "Knochenhaut, Markhöhle, Kalk und Eiweißstoff",
"typ": "lueckentext",
"anleitung": "Fülle die Lücken mit den Wörtern aus dem Wortspeicher. Groß- und Kleinschreibung ist egal.",
"daten": {"text": "<p>Lange Knochen wie der Oberschenkelknochen heißen [[Röhrenknochen]]. Außen liegt die [[Knochenhaut]] mit Blutgefäßen und Nerven. Darunter folgt die feste Knochenrinde. Im Inneren liegt die [[Markhöhle]] mit dem Knochenmark. Die Enden bestehen aus feinen [[Knochenbälkchen]] und sind mit glattem [[Gelenkknorpel|Knorpel]] überzogen.</p><p>[[Kalk]] macht den Knochen hart, ein [[Eiweißstoff]] macht ihn elastisch. Legt man einen Knochen in [[Essig]], wird er biegsam. In die Länge wachsen Knochen an den [[Wachstumsfugen]].</p>"}
},
{
"slug": "r1-gelenke-sortieren",
"titel": "Sortieren: Welcher Gelenktyp ist das?",
"kurz": "Gelenke im Körper den Gelenktypen zuordnen",
"typ": "sortieren",
"anleitung": "Ordne jedes Gelenk dem passenden Gelenktyp zu. Probiere die Bewegung ruhig an deinem eigenen Körper aus.",
"daten": {"kategorien": ["Kugelgelenk", "Scharniergelenk", "Sattelgelenk", "Drehgelenk"], "eintraege": [
 {"text": "Schultergelenk", "kategorie": "Kugelgelenk"},
 {"text": "Hüftgelenk", "kategorie": "Kugelgelenk"},
 {"text": "Ellenbogengelenk zwischen Oberarm und Elle", "kategorie": "Scharniergelenk"},
 {"text": "Gelenke zwischen den Fingergliedern", "kategorie": "Scharniergelenk"},
 {"text": "Daumengelenk an der Handwurzel", "kategorie": "Sattelgelenk"},
 {"text": "Gelenk zwischen dem 1. und 2. Halswirbel", "kategorie": "Drehgelenk"},
 {"text": "Gelenk zwischen Elle und Speiche", "kategorie": "Drehgelenk"}
]}
},
{
"slug": "r1-gelenk-lueckentext",
"titel": "Lückentext: Aufbau eines Gelenks",
"kurz": "Gelenkkopf, Gelenkpfanne und Gelenkschmiere",
"typ": "lueckentext",
"anleitung": "Fülle die Lücken mit den Wörtern aus dem Wortspeicher. Groß- und Kleinschreibung ist egal.",
"daten": {"text": "<p>An einem Gelenk passt der gewölbte [[Gelenkkopf]] des einen Knochens in die [[Gelenkpfanne]] des anderen Knochens. Beide sind mit glattem [[Gelenkknorpel|Knorpel]] überzogen. Dazwischen liegt der [[Gelenkspalt]]. Er ist mit [[Gelenkschmiere]] gefüllt, damit die Knochen leicht gleiten.</p><p>Die [[Gelenkkapsel]] umschließt das Gelenk. Feste [[Bänder]] halten die Knochen zusammen. Werden sie beim Umknicken überdehnt, spricht man von einer [[Verstauchung]].</p>"}
},
{
"slug": "r1-arm-reihenfolge",
"titel": "Reihenfolge: So wird der Arm gebeugt",
"kurz": "Vom Signal im Gehirn bis zur Bewegung",
"typ": "reihenfolge",
"anleitung": "Bringe die Schritte in die richtige Reihenfolge. Beginne mit dem Gehirn.",
"daten": {"schritte": [
 "Das Gehirn schickt über Nerven ein Signal an den Bizeps.",
 "Der Bizeps zieht sich zusammen und wird kurz und dick.",
 "Die Sehne zieht am Unterarm unterhalb des Ellenbogens.",
 "Der Unterarm dreht sich im Ellenbogengelenk nach oben: Der Arm wird gebeugt.",
 "Dabei entspannt sich der Trizeps und wird gedehnt.",
 "Zum Strecken zieht sich nun der Trizeps zusammen."
]}
},
{
"slug": "r1-ruecken-sortieren",
"titel": "Sortieren: Gut oder schlecht für den Rücken?",
"kurz": "Alltagssituationen beurteilen",
"typ": "sortieren",
"anleitung": "Ist das Verhalten gut oder schlecht für deinen Rücken und deine Gelenke? Ordne zu und prüfe.",
"daten": {"kategorien": ["gut für den Rücken", "schlecht für den Rücken"], "eintraege": [
 {"text": "Eine Kiste mit gebeugten Knien und geradem Rücken anheben", "kategorie": "gut für den Rücken"},
 {"text": "Den Schulranzen auf beiden Schultern tragen", "kategorie": "gut für den Rücken"},
 {"text": "Beim Hausaufgabenmachen zwischendurch aufstehen und sich strecken", "kategorie": "gut für den Rücken"},
 {"text": "Jeden Tag mit dem Fahrrad zur Schule fahren", "kategorie": "gut für den Rücken"},
 {"text": "Eine schwere Tasche mit gestreckten Beinen und rundem Rücken vom Boden heben", "kategorie": "schlecht für den Rücken"},
 {"text": "Den vollen Ranzen nur über eine Schulter hängen", "kategorie": "schlecht für den Rücken"},
 {"text": "Stundenlang mit gesenktem Kopf aufs Handy schauen", "kategorie": "schlecht für den Rücken"},
 {"text": "Alle Bücher der Woche täglich im Ranzen mitschleppen", "kategorie": "schlecht für den Rücken"}
]}
},
{
"slug": "r1-quiz",
"titel": "Quiz: Bewegung und Gesundheit",
"kurz": "12 Fragen quer durch die ganze Reihe",
"typ": "quiz",
"anleitung": "Klicke jeweils auf die Antwort, die du für richtig hältst. Du bekommst sofort eine Rückmeldung.",
"daten": {"fragen": [
 {"frage": "Wie viele Knochen hat ein erwachsener Mensch ungefähr?", "optionen": ["206", "52", "650", "1000"], "richtig": 0, "erklaerung": "Über 650 ist die Zahl der Muskeln."},
 {"frage": "Welche Aufgabe hat der Brustkorb?", "optionen": ["Er schützt Herz und Lunge.", "Er schützt das Gehirn.", "Er bildet die Gelenkschmiere.", "Er verbindet die Beine mit dem Rumpf."], "richtig": 0, "erklaerung": "Er besteht aus Rippen, Brustbein und Brustwirbeln."},
 {"frage": "Was macht einen Knochen hart?", "optionen": ["Kalk", "der Eiweißstoff", "das Knochenmark", "die Knochenhaut"], "richtig": 0, "erklaerung": "Der Eiweißstoff macht ihn elastisch."},
 {"frage": "Was passiert mit einem Knochen, der einige Tage in Essig liegt?", "optionen": ["Er wird biegsam.", "Er wird spröde.", "Er wird schwerer.", "Nichts."], "richtig": 0, "erklaerung": "Der Essig löst den Kalk heraus, übrig bleibt der elastische Eiweißstoff."},
 {"frage": "Wo entstehen Blutzellen?", "optionen": ["im roten Knochenmark", "im Gelenkknorpel", "in den Sehnen", "in der Gelenkkapsel"], "richtig": 0, "erklaerung": "Blutbildung ist eine der Aufgaben des Skeletts."},
 {"frage": "Wie viele Halswirbel hat der Mensch?", "optionen": ["7", "5", "12", "24"], "richtig": 0, "erklaerung": "Dazu kommen 12 Brustwirbel und 5 Lendenwirbel."},
 {"frage": "Warum hat die Wirbelsäule die Form eines doppelten S?", "optionen": ["Sie federt Stöße ab.", "Sie passt so besser in den Körper.", "Sie wächst schief, weil wir sitzen.", "Damit das Rückenmark länger ist."], "richtig": 0, "erklaerung": "Sie wirkt wie eine Sprungfeder."},
 {"frage": "Was liegt zwischen den Wirbelkörpern?", "optionen": ["Bandscheiben", "Sehnen", "Kniescheiben", "Rippen"], "richtig": 0, "erklaerung": "Sie dämpfen Stöße und machen die Wirbelsäule beweglich."},
 {"frage": "Welches Gelenk ist ein Kugelgelenk?", "optionen": ["Schultergelenk", "Ellenbogengelenk", "Fingergelenk", "Daumengelenk"], "richtig": 0, "erklaerung": "Auch das Hüftgelenk ist ein Kugelgelenk."},
 {"frage": "Wozu dient die Gelenkschmiere?", "optionen": ["Die Knochen gleiten leicht aneinander vorbei.", "Sie verbindet Muskel und Knochen.", "Sie macht Knochen hart.", "Sie bildet Blutzellen."], "richtig": 0, "erklaerung": "Sie wirkt wie Öl in einem Lager."},
 {"frage": "Was verbindet einen Muskel mit dem Knochen?", "optionen": ["eine Sehne", "ein Band", "Knorpel", "die Gelenkkapsel"], "richtig": 0, "erklaerung": "Bänder verbinden dagegen Knochen mit Knochen."},
 {"frage": "Warum braucht ein Gelenk zwei Muskeln als Gegenspieler?", "optionen": ["Muskeln können nur ziehen, nicht drücken.", "Ein Muskel allein ist zu schwach.", "Damit der Arm doppelt so schnell ist.", "Weil ein Muskel immer schläft."], "richtig": 0, "erklaerung": "Der Beuger beugt, der Strecker streckt."}
]}
},
]

TRAINING = [
{
"slug": "r1-fachbegriffe",
"titel": "Fachbegriffe: Bewegung und Gesundheit",
"kurz": "Die wichtigsten Begriffe der Reihe zuordnen",
"typ": "zuordnen",
"anleitung": "Wähle für jeden Fachbegriff die passende Erklärung. Die Lösung kannst du ansehen, sobald alles zugeordnet ist.",
"daten": {"paare": [
 {"links": "Skelett", "rechts": "alle Knochen des Körpers zusammen"},
 {"links": "Knochenmark", "rechts": "Gewebe im Knocheninneren, in dem Blutzellen entstehen"},
 {"links": "Bandscheibe", "rechts": "Polster zwischen zwei Wirbelkörpern"},
 {"links": "Rückenmark", "rechts": "Nervenstrang im Wirbelkanal"},
 {"links": "Gelenkknorpel", "rechts": "glatte, elastische Schicht auf den Knochenenden"},
 {"links": "Band", "rechts": "verbindet zwei Knochen an einem Gelenk"},
 {"links": "Sehne", "rechts": "verbindet einen Muskel mit einem Knochen"},
 {"links": "Beuger", "rechts": "Muskel, der ein Gelenk beugt, zum Beispiel der Bizeps"},
 {"links": "Strecker", "rechts": "Muskel, der ein Gelenk streckt, zum Beispiel der Trizeps"},
 {"links": "Haltungsschaden", "rechts": "dauerhafte Verformung durch jahrelange falsche Haltung"}
]}
},
{
"slug": "r1-verletzungen",
"titel": "Zuordnen: Sportverletzungen",
"kurz": "Verletzungen erkennen und die PECH-Regel anwenden",
"typ": "zuordnen",
"anleitung": "Ordne jeder Verletzung oder jedem Buchstaben der PECH-Regel die passende Beschreibung zu.",
"daten": {"paare": [
 {"links": "Prellung", "rechts": "durch einen Stoß gequetscht, es entsteht ein blauer Fleck"},
 {"links": "Zerrung", "rechts": "ein Muskel wurde überdehnt"},
 {"links": "Verstauchung", "rechts": "die Bänder eines Gelenks wurden überdehnt"},
 {"links": "Knochenbruch", "rechts": "der Knochen ist gebrochen, oft mit Fehlstellung"},
 {"links": "P", "rechts": "Pause: sofort mit dem Sport aufhören"},
 {"links": "E", "rechts": "Eis: die Stelle kühlen, nicht direkt auf die Haut"},
 {"links": "C", "rechts": "Compression: einen leichten Druckverband anlegen"},
 {"links": "H", "rechts": "Hochlagern: über Herzhöhe legen"}
]}
},
{
"slug": "r1-schreiben",
"titel": "Schreibtraining: Erklären in ganzen Sätzen",
"kurz": "Gegenspielerprinzip und Wirbelsäule erklären",
"typ": "schreiben",
"anleitung": "Beantworte die Aufgaben in ganzen Sätzen. Erst wenn du genug geschrieben hast, kannst du deinen Text mit einer Musterlösung vergleichen.",
"daten": {"aufgaben": [
 {"frage": "Erkläre das Gegenspielerprinzip am Beispiel des Oberarms. Verwende die Begriffe Beuger, Strecker, Sehne, zusammenziehen und entspannen.",
  "hinweis": "Tipp: Beschreibe zuerst das Beugen, dann das Strecken. Erkläre am Ende, warum man zwei Muskeln braucht.",
  "minWoerter": 40,
  "checkliste": ["Ich habe beschrieben, dass Muskeln über Sehnen am Knochen befestigt sind.", "Ich habe das Beugen mit dem Bizeps erklärt.", "Ich habe das Strecken mit dem Trizeps erklärt.", "Ich habe beschrieben, dass sich der Gegenspieler jeweils entspannt.", "Ich habe erklärt, dass Muskeln nur ziehen können."],
  "muster": "Am Oberarm liegen zwei Muskeln, die über Sehnen an den Knochen befestigt sind. Der Bizeps liegt auf der Vorderseite und ist der Beuger. Wenn er sich zusammenzieht, wird er kürzer und dicker und zieht über seine Sehne am Unterarm. Dadurch wird der Arm im Ellenbogen gebeugt. Gleichzeitig entspannt sich der Trizeps auf der Rückseite und wird gedehnt. Zum Strecken zieht sich der Trizeps zusammen, er ist der Strecker. Jetzt entspannt sich der Bizeps. Man braucht zwei Muskeln, weil ein Muskel nur ziehen und nicht drücken kann. Deshalb arbeiten Beuger und Strecker als Gegenspieler."},
 {"frage": "Erkläre, wie die Wirbelsäule gebaut ist und wie sie den Körper vor Stößen schützt.",
  "hinweis": "Tipp: Nenne die Abschnitte, beschreibe die Bandscheiben und erkläre die doppelte S-Form.",
  "minWoerter": 40,
  "checkliste": ["Ich habe die Abschnitte der Wirbelsäule genannt.", "Ich habe die Bandscheiben und ihre Aufgabe beschrieben.", "Ich habe die doppelte S-Form erklärt.", "Ich habe den Vergleich mit einer Feder verwendet.", "Ich habe das Rückenmark erwähnt."],
  "muster": "Die Wirbelsäule besteht aus 7 Halswirbeln, 12 Brustwirbeln und 5 Lendenwirbeln. Unten folgen das Kreuzbein und das Steißbein. Zwischen den Wirbelkörpern liegen Bandscheiben. Sie wirken wie kleine Kissen, dämpfen Stöße und machen die Wirbelsäule beweglich. Von der Seite hat die Wirbelsäule die Form eines doppelten S. Dadurch federt sie beim Gehen, Laufen und Springen wie eine Sprungfeder, und die Stöße kommen nicht ungebremst am Kopf an. Außerdem schützt die Wirbelsäule das Rückenmark, das im Wirbelkanal verläuft."}
]}
},
]

# ---------------------------------------------------------------- Modellseiten
_info = "".join(f'<li data-teil="{k}"><strong>{n}</strong>: {t}</li>' for k, n, t in Z.SKELETT_TEILE)

SKELETT = f"""
<p class="lead">Tippe auf einen Knochen, um seinen Namen und seine Aufgabe zu sehen. Im Suchspiel nennt das Modell einen Knochen, und du findest ihn im Skelett.</p>
<div class="modell sk-modell" id="sk">
  <div class="wahl" role="group" aria-label="Modus wählen">
    <button type="button" data-modus="erkunden" aria-pressed="true">Erkunden</button>
    <button type="button" data-modus="suchen" aria-pressed="false">Suchspiel</button>
  </div>
  <div class="sk-flaeche">
    {Z.skelett(beschriften=False, interaktiv=True)}
    <div class="schritt-text sk-text" aria-live="polite"><h3 id="sk-titel">Tippe auf einen Knochen</h3><p id="sk-erkl">Du kannst auch mit der Tab-Taste von Knochen zu Knochen springen und mit der Eingabetaste auswählen.</p><p id="sk-stand" class="legende"></p></div>
  </div>
</div>
<details class="sk-liste"><summary>Alle Knochen als Liste</summary><ul>{_info}</ul></details>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Erkunde das Skelett. Schreibe zu fünf Knochen auf, welche Aufgabe sie haben.</li>
  <li>Spiele das Suchspiel, bis du alle zwölf Knochen ohne Fehler findest.</li>
  <li>Taste an deinem eigenen Körper nach: Welche Knochen kannst du unter der Haut fühlen?</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Das Skelett ist stark vereinfacht. Viele kleine Knochen, zum Beispiel in Hand, Fuß und Schädel, sind zusammengefasst, und die Schulterblätter fehlen, weil sie von vorn verdeckt sind. Die Formen der Knochen sind schematisch gezeichnet.</p>
"""

GELENK = """
<p class="lead">Wähle einen Gelenktyp und bewege den Knochen mit den Reglern. Welche Bewegungen sind möglich und welche nicht?</p>
<div class="modell" id="gm">
  <div class="wahl" role="group" aria-label="Gelenktyp wählen">
    <button type="button" data-typ="kugel" aria-pressed="true">Kugelgelenk</button>
    <button type="button" data-typ="scharnier" aria-pressed="false">Scharniergelenk</button>
    <button type="button" data-typ="sattel" aria-pressed="false">Sattelgelenk</button>
    <button type="button" data-typ="dreh" aria-pressed="false">Drehgelenk</button>
  </div>
  <svg id="gm-bild" class="ill" viewBox="0 0 640 340" role="img" aria-label="Modell eines Gelenks, dessen Knochen sich mit den Reglern bewegen lässt"></svg>
  <div class="modell-steuerung"><label for="gm-a">vor und zurück</label><input type="range" id="gm-a" min="-60" max="60" value="0" class="breit-regler"></div>
  <div class="modell-steuerung"><label for="gm-b">zur Seite</label><input type="range" id="gm-b" min="-60" max="60" value="0" class="breit-regler"></div>
  <div class="modell-steuerung"><label for="gm-c">drehen</label><input type="range" id="gm-c" min="-90" max="90" value="0" class="breit-regler"></div>
  <div class="schritt-text" aria-live="polite"><h3 id="gm-titel"></h3><p id="gm-text"></p><p id="gm-hinweis" class="legende"></p></div>
</div>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Probiere bei jedem Gelenktyp alle drei Regler aus. Lege eine Tabelle an: Welche Bewegungen sind möglich?</li>
  <li>Finde an deinem Körper zu jedem Gelenktyp ein Beispiel und überprüfe die Bewegungen.</li>
  <li>Erkläre, warum das Schultergelenk beweglicher ist als das Ellenbogengelenk.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Das Modell zeigt nur den Knochen und die Grundform des Gelenks. Gelenkkapsel, Bänder und Muskeln fehlen, obwohl gerade sie die Bewegungen im Körper begrenzen. Echte Gelenke können sich auch nicht so weit bewegen, wie die Regler es erlauben, und manche, etwa das Knie, sind Mischformen.</p>
"""

ARM = """
<p class="lead">Bewege den Unterarm mit dem Regler. Beobachte, welcher Muskel sich zusammenzieht und welcher sich entspannt.</p>
<div class="modell" id="am">
  <svg id="am-bild" class="ill" viewBox="0 0 640 400" role="img" aria-label="Arm mit Bizeps und Trizeps, der sich mit dem Regler beugen und strecken lässt"></svg>
  <div class="modell-steuerung"><label for="am-w">Winkel im Ellenbogen: <strong id="am-w-t"></strong></label><input type="range" id="am-w" min="40" max="175" value="160" class="breit-regler"></div>
  <div class="modell-steuerung">
    <label class="schalter"><input type="checkbox" id="am-last"> Wasserflasche in der Hand</label>
  </div>
  <div class="schritt-text" aria-live="polite"><p id="am-text"></p></div>
</div>
<h2>Arbeitsaufträge</h2>
<ol>
  <li>Beuge den Arm langsam. Beschreibe, wie sich Form und Länge von Bizeps und Trizeps verändern.</li>
  <li>Strecke den Arm wieder. Erkläre, welcher Muskel jetzt arbeitet und warum der Bizeps das nicht allein schafft.</li>
  <li>Schalte die Wasserflasche ein. Erkläre mit der Hebelwirkung, warum der Bizeps viel mehr Kraft braucht, als die Flasche wiegt.</li>
</ol>
<h3>Grenzen des Modells</h3>
<p>Im echten Arm arbeiten noch weitere Muskeln mit, und die Muskeln liegen nicht frei neben dem Knochen, sondern sind von Haut, Fett und Bindegewebe umgeben. Die Kraftangaben sind grob gerundet und sollen nur das Prinzip des Hebels zeigen.</p>
"""

MODELLE = [
 {"slug": "skelett-erkunden", "titel": "Modell: Das Skelett erkunden", "kurz": "Knochen antippen, Namen und Aufgaben lernen, Suchspiel", "inhalt": SKELETT, "skripte": ["assets/reihe1.js"]},
 {"slug": "gelenk-modell", "titel": "Modell: Gelenktypen ausprobieren", "kurz": "Kugel-, Scharnier-, Sattel- und Drehgelenk bewegen", "inhalt": GELENK, "skripte": ["assets/reihe1.js"]},
 {"slug": "arm-modell", "titel": "Modell: Beuger und Strecker", "kurz": "Den Arm beugen und strecken und die Muskeln beobachten", "inhalt": ARM, "skripte": ["assets/reihe1.js"]},
]
