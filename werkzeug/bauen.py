"""Erzeugt alle Seiten der Website. Aufruf: python3 bauen.py (im Ordner werkzeug)."""
import html
import json
import os
import shutil
from basis import seite, uebung, REIHEN, REPO
import zeichnungen as Z

AFB_TEXT = {"I": "AFB I", "II": "AFB II", "III": "AFB III"}

# Freischaltung durch die Lehrkraft: freigabe.json im Hauptordner des Repositorys
with open(os.path.join(REPO, "freigabe.json"), encoding="utf-8") as _f:
    _FREI = json.load(_f)
FREI = {int(k.split()[-1]) for k, v in _FREI.items() if k.startswith("Reihe") and v is True}

# ======================================================================
# Daten der Reihen (bisher ausgearbeitet: Reihe 1)
# ======================================================================
import zeichnungen1 as Z1
from reihe1_texte import LERNTEXTE as LT1
from reihe1_rest import AUFGABEN as AUF1, UEBUNGEN as UEB1, MODELLE as MOD1, TRAINING as TRAIN1

FIGUREN = {}
FIGUREN.update(Z1.FIGUREN)
FERTIG = {1}


def figuren_einsetzen(text):
    for name, (fn, unterschrift) in FIGUREN.items():
        text = text.replace(f"<!--FIG:{name}-->", f'<figure class="breit"><div class="bild">{fn()}</div><figcaption>{unterschrift}</figcaption></figure>')
    return text


def reihenkopf(nr, name, text, bild):
    return f"""
<section class="reihe-kopf">
  <div class="huelle">
    <div>
      <span class="reihe-nr">Reihe {nr}</span>
      <h1>{html.escape(name)}</h1>
      <p>{text}</p>
    </div>
    {bild}
  </div>
</section>"""


def liste(eintraege, ordner, mit_nr=True):
    zeilen = []
    for i, e in enumerate(eintraege):
        nr = f'<span class="nr">{i + 1}</span>' if mit_nr else ""
        zeilen.append(f'<li><a href="{ordner}/{e["slug"]}.html"><span class="kachel">{Z.symbol(e["slug"])}{nr}</span>'
                      f'<span class="titel">{html.escape(e["titel"])}</span><span class="info">{html.escape(e["kurz"])}</span></a></li>')
    return '<ul class="liste zweispaltig">' + "".join(zeilen) + "</ul>"


def kurztitel(t):
    return t.split(": ", 1)[1] if ": " in t else t


def gesperrt(nr, text):
    ordner, name = REIHEN[nr]
    for unter in ("lerntexte", "aufgaben", "uebungen", "modelle"):
        shutil.rmtree(os.path.join(REPO, ordner, unter), ignore_errors=True)
    seite(f"{ordner}/index.html", name, reihenkopf(nr, name, text, Z.reihe_kopf(nr))
          + '<div class="huelle bereich"><p><a class="knopf" href="../index.html">Zurück zur Übersicht</a></p></div>',
          reihe=nr, krumen=[(name, None)], beschreibung=f"Unterrichtsreihe {name}")


def baue_reihe(nr, lerntexte, aufgaben, uebungen, modelle, kopftext, training=None, training_text="", vorwort="", training_titel="Wiederholen und vertiefen"):
    ordner, name = REIHEN[nr]
    alle_uebungen = uebungen + (training or [])
    if nr not in FREI:
        gesperrt(nr, "Diese Reihe ist noch nicht freigeschaltet. Deine Lehrkraft schaltet sie frei, sobald ihr im Unterricht damit anfangt.")
        return

    for i, lt in enumerate(lerntexte):
        vor = lerntexte[i - 1] if i > 0 else None
        nach = lerntexte[i + 1] if i < len(lerntexte) - 1 else None
        links = [f'<a href="{vor["slug"]}.html">Zurück: {html.escape(vor["titel"])}</a>' if vor else '<span></span>',
                 f'<a href="{nach["slug"]}.html">Weiter: {html.escape(nach["titel"])}</a>' if nach else '<a href="../index.html">Zur Übersicht der Reihe</a>']
        inhalt = f"""
<article class="spalte lerntext">
  <div class="lt-bild">{Z.lt_kopf(lt["slug"])}</div>
  <h1>{html.escape(lt["titel"])}</h1>
{figuren_einsetzen(lt["inhalt"])}
  <div class="knopfreihe">
    <a class="knopf" href="../aufgaben/{lt["slug"]}.html">Aufgaben zu diesem Text</a>
  </div>
  <nav class="weiter" aria-label="Weitere Lerntexte">{links[0]}{links[1]}</nav>
</article>"""
        seite(f"{ordner}/lerntexte/{lt['slug']}.html", lt["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Lerntext " + str(i + 1), None)], beschreibung=lt["kurz"])

    for i, lt in enumerate(lerntexte):
        items = []
        for afb, text, zeilen in aufgaben[lt["slug"]]:
            z = f'<div class="schreibzeilen" style="--zeilen:{zeilen}"></div>' if zeilen else ""
            items.append(f'<li><p>{html.escape(text)} <span class="afb" title="Anforderungsbereich {afb}">{AFB_TEXT[afb]}</span></p>{z}</li>')
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(lt["slug"])}<h1>Aufgaben: {html.escape(lt["titel"])}</h1></div>
  <p class="legende">Grundlage ist der Lerntext <a href="../lerntexte/{lt["slug"]}.html">{html.escape(lt["titel"])}</a>.
  AFB I = wiedergeben, AFB II = anwenden und erklären, AFB III = beurteilen und Stellung nehmen.</p>
  <div class="knopfreihe nicht-drucken">
    <button class="knopf leise" type="button" onclick="window.print()">Als Arbeitsblatt drucken</button>
  </div>
  <p class="nicht-drucken legende">Beim Drucken werden automatisch Schreiblinien eingefügt.</p>
  <p class="nur-druck">Name: ______________________________ &nbsp; Datum: ______________</p>
  <ol class="aufgaben">
    {''.join(items)}
  </ol>
  <nav class="weiter" aria-label="Navigation">
    <a href="../lerntexte/{lt["slug"]}.html">Zurück zum Lerntext</a>
    <a href="../index.html">Zur Übersicht der Reihe</a>
  </nav>
</article>"""
        seite(f"{ordner}/aufgaben/{lt['slug']}.html", "Aufgaben: " + lt["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Aufgaben " + str(i + 1), None)], beschreibung="Aufgaben zu " + lt["titel"])

    for u in alle_uebungen:
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(u["slug"])}<h1>{html.escape(u["titel"])}</h1></div>
  <p class="lead">{html.escape(u["anleitung"])}</p>
  {uebung(u["typ"], u["daten"])}
  <noscript><p>Für diese Übung muss JavaScript im Browser aktiviert sein.</p></noscript>
  <nav class="weiter" aria-label="Navigation"><a href="../index.html">Zur Übersicht der Reihe</a></nav>
</article>"""
        seite(f"{ordner}/uebungen/{u['slug']}.html", u["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Übung", None)], beschreibung=u["kurz"], skripte=["assets/uebungen.js"])

    for m in modelle:
        inhalt = f"""
<article class="spalte lerntext">
  <div class="uebung-kopf">{Z.symbol(m["slug"])}<h1>{html.escape(m["titel"])}</h1></div>
  {m["inhalt"]}
  <nav class="weiter" aria-label="Navigation"><a href="../index.html">Zur Übersicht der Reihe</a></nav>
</article>"""
        seite(f"{ordner}/modelle/{m['slug']}.html", m["titel"], inhalt, reihe=nr,
              krumen=[(name, "../index.html"), ("Modell", None)], beschreibung=m["kurz"], skripte=m.get("skripte", []))

    aufg = [{"slug": lt["slug"], "titel": lt["titel"], "kurz": f'{len(aufgaben[lt["slug"]])} Aufgaben, druckbar als Arbeitsblatt'} for lt in lerntexte]
    modelle_k = [dict(m, titel=kurztitel(m["titel"])) for m in modelle]
    training_html = ""
    if training:
        training_html = f"""
    <h3 class="unterteil">{training_titel}</h3>
    <p class="hinweis">{training_text}</p>
    {liste(training, "uebungen", mit_nr=False)}"""
    seite(f"{ordner}/index.html", name, reihenkopf(nr, name, kopftext, Z.reihe_kopf(nr)) + f"""
<div class="huelle">{vorwort}
  <section class="bereich" aria-labelledby="b-lt">
    <h2 id="b-lt">Lerntexte</h2>
    <p class="hinweis">In dieser Reihenfolge lesen. Jeder Text baut auf dem vorherigen auf.</p>
    {liste(lerntexte, "lerntexte")}
  </section>
  <section class="bereich" aria-labelledby="b-mo">
    <h2 id="b-mo">Modelle</h2>
    <p class="hinweis">Zum Ausprobieren und Verstehen.</p>
    {liste(modelle_k, "modelle", mit_nr=False)}
  </section>
  <section class="bereich" aria-labelledby="b-ue">
    <h2 id="b-ue">Übungen</h2>
    <p class="hinweis">Zum Üben und Wiederholen, mit sofortiger Rückmeldung.</p>
    {liste(uebungen, "uebungen", mit_nr=False)}{training_html}
  </section>
  <section class="bereich" aria-labelledby="b-au">
    <h2 id="b-au">Aufgaben</h2>
    <p class="hinweis">Passend zu den Lerntexten, für den Unterricht oder zu Hause.</p>
    {liste(aufg, "aufgaben")}
  </section>
</div>
""", reihe=nr, krumen=[(name, None)], beschreibung=f"Unterrichtsreihe {name}, Biologie Klasse 6")


# ======================================================================
# Startseite
# ======================================================================
beschr = {
    1: "Skelett, Knochen, Wirbelsäule, Gelenke und Muskeln und wie man sie gesund hält.",
    2: "Atmung, Herz und Blutkreislauf und wie die Organe des Körpers zusammenarbeiten.",
    3: "Nährstoffe, ausgewogene Ernährung und der Weg der Nahrung durch den Körper.",
    4: "Fotosynthese, Pflanzenzellen und wie Pflanzen und Tiere den Winter überstehen.",
    5: "Auge, Ohr und Haut, Reize und Reaktionen und die Sinne der Tiere.",
    6: "Pubertät, Geschlechtsorgane, Schwangerschaft und die ersten Lebensjahre.",
}
karten = []
for nr, (ordner, name) in REIHEN.items():
    fertig = nr in FERTIG and nr in FREI
    klasse = "reihe-karte" + ("" if fertig else " in-arbeit")
    stand = "Materialien ansehen" if fertig else ("Noch nicht freigeschaltet" if nr in FERTIG else "In Vorbereitung")
    karten.append(
        f'<li class="reihe-{nr}"><a class="{klasse}" href="{ordner}/index.html">'
        f'<div class="bildflaeche">{Z.karte_bild(nr)}</div>'
        f'<div class="karte-text"><span class="reihe-nr">Reihe {nr}</span><h2>{html.escape(name)}</h2><p>{beschr[nr]}</p><span class="stand">{stand}</span></div>'
        f'</a></li>')

seite("index.html", "Übersicht", f"""
<section class="buehne">
  <div class="huelle">
    <div>
      <p class="unterzeile">Biologie</p>
      <h1>Biologie<br>Klasse&nbsp;6</h1>
      <p class="einleitung">Lerntexte, Aufgaben, Übungen und Modelle zum Ausprobieren. Die sechs Unterrichtsreihen folgen der Reihenfolge im Schuljahr.</p>
    </div>
    {Z.hero_bild()}
  </div>
</section>
<div class="huelle">
  <ol class="reihen" aria-label="Unterrichtsreihen in der Reihenfolge des Schuljahres">
    {''.join(karten)}
  </ol>
</div>
""", beschreibung="Materialien für den Biologieunterricht, Klasse 6")

# ======================================================================
# Reihen bauen
# ======================================================================
baue_reihe(1, LT1, AUF1, UEB1, MOD1,
           "Wie Knochen, Gelenke und Muskeln zusammenarbeiten, damit wir uns bewegen können, und was wir tun können, damit unser Bewegungsapparat gesund bleibt.",
           training=TRAIN1,
           training_text="Wiederhole die wichtigsten Inhalte der Reihe: Fachbegriffe, Sportverletzungen und das Erklären in ganzen Sätzen.")

for _nr in (2, 3, 4, 5, 6):
    if _nr in FREI:
        gesperrt(_nr, "Diese Reihe wird gerade vorbereitet. Bald findest du hier Lerntexte, Übungen und Modelle.")
    else:
        gesperrt(_nr, "Diese Reihe ist noch nicht freigeschaltet. Deine Lehrkraft schaltet sie frei, sobald ihr im Unterricht damit anfangt.")
print("fertig")
