"""Zeichnungen der Reihe 1: Bewegung und Gesundheit."""
import math
import zeichnungen as Z
from zeichnungen import svg, deko, text, pfeil, linie, blob, funkeln, knochen, muskel, arm, rippe


# ---------------------------------------------------------------- Knochenaufbau
def knochen_aufbau():
    i = ""
    # Außenform
    i += knochen(150, 150, 490, 150, 76, "f-weiss")
    # Knochenhaut entlang des Schafts
    i += '<path class="s k-rosa" stroke-width="3" fill="none" d="M196 108 H 444 M196 192 H 444"/>'
    # Markhöhle
    i += '<rect class="s f-gelb" x="214" y="130" width="212" height="40" rx="18"/>'
    i += "".join(f'<circle class="f-gelb-weich" cx="{x}" cy="{y}" r="4"/>' for x, y in [(240, 142), (268, 158), (300, 140), (334, 156), (370, 144), (404, 158)])
    # Knochenbälkchen in den Enden (Schwammknochen)
    for cx in (150, 490):
        i += f'<clipPath id="kb{cx}"><ellipse cx="{cx}" cy="150" rx="46" ry="52"/></clipPath>'
        striche = ""
        for k in range(-6, 7):
            striche += f'<path class="s2" fill="none" opacity=".75" d="M{cx - 60 + k * 12} 90 L {cx + 20 + k * 12} 210"/>'
            striche += f'<path class="s2" fill="none" opacity=".55" d="M{cx + 60 + k * 12} 90 L {cx - 20 + k * 12} 210"/>'
        i += f'<g clip-path="url(#kb{cx})">{striche}</g>'
    # Gelenkknorpel an den Enden
    i += '<path class="k-blau" stroke-width="9" stroke-linecap="round" fill="none" opacity=".75" d="M128 96 C 104 104, 98 140, 114 150 C 98 160, 104 196, 128 204"/>'
    i += '<path class="k-blau" stroke-width="9" stroke-linecap="round" fill="none" opacity=".75" d="M512 96 C 536 104, 542 140, 526 150 C 542 160, 536 196, 512 204"/>'
    # Beschriftung
    i += text(40, 40, "Gelenkknorpel", "hk", "start") + linie(98, 48, 112, 104)
    i += text(220, 40, "Knochenhaut", "hk", "start") + linie(260, 48, 262, 104)
    i += text(400, 40, "Knochenbälkchen", "hk", "start") + linie(450, 48, 478, 112)
    i += text(250, 266, "Markhöhle mit Knochenmark", "hk", "start") + linie(320, 248, 320, 166)
    i += text(470, 266, "feste Knochenrinde", "hk", "start") + linie(500, 248, 420, 182)
    return svg("0 0 640 280", i, "Aufbau eines Röhrenknochens im Längsschnitt",
               "Ein langer Knochen ist der Länge nach aufgeschnitten. Außen liegt die Knochenhaut, darunter die feste Knochenrinde. "
               "Innen ist die Markhöhle mit Knochenmark. Die verdickten Enden sind mit Knochenbälkchen gefüllt und mit Gelenkknorpel überzogen.")


def knochen_versuch():
    i = ""
    # Mitte: normaler Knochen
    i += blob(320, 120, 110, 80, "f-gruen-weich", 3)
    i += knochen(260, 120, 380, 120, 26)
    i += text(320, 186, "Kalk + Eiweißstoff", "hk") + text(320, 210, "hart und elastisch", "h")
    # Links: Essig
    i += '<path class="s f-blau-weich" d="M40 40 V 190 Q 40 204 54 204 H 166 Q 180 204 180 190 V 40"/>'
    i += '<path class="f-blau" opacity=".6" d="M42 90 V 190 Q 42 202 54 202 H 166 Q 178 202 178 190 V 90 Z"/>'
    i += '<path class="s2" fill="none" d="M42 90 H 178"/>'
    i += Z.rippe("M70 170 C 60 120, 120 130, 110 100 C 102 76, 150 70, 150 120", 14)
    i += text(110, 232, "in Essig: Kalk gelöst", "hk") + text(110, 256, "biegsam wie Gummi", "h")
    # Rechts: geglüht
    i += '<path class="s k-koralle" fill="none" d="M490 200 c -10 -20, 10 -24, 4 -44 c 14 10, 18 24, 14 36 M 540 200 c -8 -16, 8 -22, 2 -38 c 12 10, 14 22, 10 34 M 590 200 c -10 -18, 6 -22, 2 -36 c 12 8, 14 20, 10 32"/>'
    i += knochen(470, 120, 610, 120, 26, "f-sand")
    i += '<path class="s" fill="none" d="M510 107 l 8 10 l -6 6 l 8 10 M 566 108 l -6 8 l 8 8 l -6 10"/>'
    i += '<path class="s f-sand" d="M520 150 l 10 4 l -4 8 z M 556 150 l 8 -2 l 2 8 z"/>'
    i += text(540, 232, "stark erhitzt: Eiweiß verbrannt", "hk") + text(540, 256, "hart, aber spröde", "h")
    i += pfeil(200, 120, 248, 120, "s2", 0) + pfeil(392, 120, 452, 120, "s2", 0)
    return svg("0 0 650 270", i, "Versuch: Woraus besteht ein Knochen?",
               "Ein Knochen in Essig verliert seinen Kalk und wird biegsam. Ein stark erhitzter Knochen verliert seinen Eiweißstoff und wird spröde. "
               "Erst beides zusammen macht den Knochen hart und elastisch.")


# ---------------------------------------------------------------- Wirbelsäule
def _catmull(punkte, n):
    """Gleichmäßig viele Punkte entlang einer Catmull-Rom-Kurve."""
    roh = []
    p = [punkte[0]] + punkte + [punkte[-1]]
    for k in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[k - 1], p[k], p[k + 1], p[k + 2]
        for s in range(40):
            t = s / 40
            roh.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                     + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    roh.append(punkte[-1])
    laengen = [0]
    for a, b in zip(roh, roh[1:]):
        laengen.append(laengen[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    ges = laengen[-1]
    aus = []
    j = 0
    for k in range(n):
        ziel = ges * k / (n - 1)
        while j < len(laengen) - 2 and laengen[j + 1] < ziel:
            j += 1
        a, b = roh[j], roh[j + 1]
        f = (ziel - laengen[j]) / max(1e-6, laengen[j + 1] - laengen[j])
        x, y = a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f
        aus.append((x, y, math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))))
    return aus


def wirbelsaeule():
    # Seitenansicht: Bauch links, Rücken rechts. Doppel-S-Form.
    kurve = [(206, 40), (188, 82), (198, 124), (234, 200), (242, 240), (230, 292), (202, 334), (176, 386), (188, 430), (200, 446)]
    pts = _catmull(kurve, 26)
    bereiche = [("Halswirbel (7)", 7, "f-blau", 13), ("Brustwirbel (12)", 12, "f-gruen", 15), ("Lendenwirbel (5)", 5, "f-gelb", 18)]
    i = ""
    k = 0
    klammern = []
    for name, anz, fill, b in bereiche:
        start = k
        for _ in range(anz):
            x, y, w = pts[k]
            i += f'<g transform="translate({x:.1f} {y:.1f}) rotate({w - 90:.1f})"><rect class="s {fill}" x="{-b}" y="-7" width="{b * 2}" height="13" rx="4"/>'
            i += f'<path class="s2 {fill}" d="M{b - 2} -3 L {b + 12} 2 L {b - 2} 5 Z"/></g>'
            k += 1
        klammern.append((name, pts[start][1] - 6, pts[k - 1][1] + 6))
    # Kreuzbein und Steißbein
    x, y, w = pts[k]
    i += f'<path class="s f-sand" d="M{x - 18:.1f} {y - 6:.1f} C {x - 16:.1f} {y + 30:.1f}, {x - 4:.1f} {y + 52:.1f}, {x + 6:.1f} {y + 62:.1f} C {x + 16:.1f} {y + 50:.1f}, {x + 22:.1f} {y + 20:.1f}, {x + 20:.1f} {y - 6:.1f} Z"/>'
    i += f'<path class="s f-rosa" d="M{x + 2:.1f} {y + 64:.1f} q 4 10 0 22 q -2 4 -6 0 q 0 -12 6 -22 z"/>'
    klammern.append(("Kreuzbein", y - 4, y + 58))
    klammern.append(("Steißbein", y + 62, y + 88))
    for name, y1, y2 in klammern:
        i += f'<path class="s2" fill="none" d="M268 {y1:.1f} q 8 0 8 8 V {y2 - 8:.1f} q 0 8 -8 8 M 276 {(y1 + y2) / 2:.1f} h 8"/>'
        i += text(290, (y1 + y2) / 2 + 6, name, "hk", "start")
    i += text(150, 24, "Bauch", "hk", "end") + text(256, 24, "Rücken", "hk", "start")
    # Ausschnitt: zwei Wirbel mit Bandscheibe
    ox, oy = 470, 190
    i += f'<circle class="s2 gestrichelt" cx="{ox + 60}" cy="{oy + 10}" r="112" fill="none"/>'
    for dy in (-52, 52):
        i += f'<rect class="s f-gelb" x="{ox}" y="{oy + dy - 26}" width="80" height="50" rx="12"/>'
        i += f'<path class="s f-gelb" d="M{ox + 80} {oy + dy - 14} H {ox + 104} L {ox + 150} {oy + dy + 10} L {ox + 140} {oy + dy + 20} L {ox + 104} {oy + dy + 12} H {ox + 80}"/>'
    i += f'<rect class="s f-blau" x="{ox + 4}" y="{oy - 22}" width="72" height="44" rx="18"/>'
    i += f'<rect class="f-rosa-tief" x="{ox + 86}" y="{oy - 90}" width="14" height="180" rx="7" opacity=".85"/>'
    i += text(ox + 20, oy + 148, "Wirbelkörper", "hk") + linie(ox + 24, oy + 130, ox + 30, oy + 76)
    i += text(ox + 10, oy - 126, "Bandscheibe", "hk") + linie(ox + 14, oy - 118, ox + 30, oy - 20)
    i += text(ox + 150, oy - 126, "Rückenmark", "hk") + linie(ox + 140, oy - 118, ox + 96, oy - 80)
    i += text(ox + 170, oy + 148, "Dornfortsatz", "hk") + linie(ox + 160, oy + 130, ox + 140, oy + 72)
    return svg("0 0 680 560", i, "Die Wirbelsäule von der Seite und zwei Wirbel mit Bandscheibe",
               "Links: Die Wirbelsäule hat von der Seite die Form eines doppelten S. Sie besteht aus 7 Halswirbeln, 12 Brustwirbeln, 5 Lendenwirbeln, "
               "dem Kreuzbein und dem Steißbein. Rechts: Zwischen zwei Wirbelkörpern liegt eine Bandscheibe. Durch die Wirbel verläuft das Rückenmark.")


# ---------------------------------------------------------------- Gelenk
def gelenk_aufbau():
    i = ""
    # Gelenkkapsel (hinter den Knochen)
    i += '<path class="s k-rosa f-rosa-weich" d="M286 92 C 214 120, 214 270, 268 292 L 372 292 C 426 270, 426 120, 354 92 Z"/>'
    # oberer Knochen mit Gelenkkopf
    i += '<rect class="s f-weiss" x="292" y="0" width="56" height="140" />'
    i += '<circle class="s f-weiss" cx="320" cy="170" r="56"/>'
    i += '<rect class="f-weiss" x="294.5" y="0" width="51" height="140"/>'
    # Knorpel auf dem Kopf
    i += '<path class="k-blau" stroke-width="8" fill="none" opacity=".8" d="M273 197 A 54 54 0 0 0 367 197"/>'
    # unterer Knochen mit Pfanne
    i += '<path class="s f-weiss" d="M262 360 V 232 Q 262 218 277 220 A 66 66 0 0 0 363 220 Q 378 218 378 232 V 360"/>'
    i += '<path class="k-blau" stroke-width="7" fill="none" opacity=".8" d="M281 225 A 62 62 0 0 0 359 225"/>'
    # Gelenkschmiere im Spalt
    i += '<path class="k-bernstein" stroke-width="3" fill="none" stroke-dasharray="2 5" stroke-linecap="round" d="M277 216 A 60 60 0 0 0 363 216"/>'
    # Bänder
    i += '<path class="k-gruen" stroke-width="9" stroke-linecap="round" fill="none" d="M282 98 C 218 132, 218 262, 264 290 M 358 98 C 422 132, 422 262, 376 290"/>'
    # Beschriftung
    i += text(40, 60, "Knochen", "hk", "start") + linie(110, 54, 288, 50)
    i += text(40, 140, "Gelenkkopf", "hk", "start") + linie(132, 134, 290, 160)
    i += text(40, 214, "Gelenkknorpel", "hk", "start") + linie(156, 208, 278, 204)
    i += text(40, 300, "Gelenkpfanne", "hk", "start") + linie(150, 294, 284, 250)
    i += text(600, 120, "Bänder", "hk", "end") + linie(538, 114, 392, 170)
    i += text(600, 190, "Gelenkkapsel", "hk", "end") + linie(498, 184, 420, 200)
    i += text(600, 250, "Gelenkspalt mit", "hk", "end") + text(600, 272, "Gelenkschmiere", "hk", "end") + linie(470, 244, 360, 226)
    return svg("0 0 640 370", i, "Aufbau eines Gelenks (schematisch)",
               "Der Gelenkkopf des einen Knochens passt in die Gelenkpfanne des anderen. Beide sind mit glattem Gelenkknorpel überzogen. "
               "Dazwischen liegt der Gelenkspalt mit Gelenkschmiere. Die Gelenkkapsel umschließt das Gelenk, Bänder halten die Knochen zusammen.")


def _gelenk_symbol(art):
    """Schematische Gelenkmodelle für die Übersicht, Mitte (0, 0)."""
    if art == "kugel":
        return ('<path class="s f-weiss" d="M-40 40 V 14 A 40 40 0 0 0 40 14 V 40 Z"/>'
                '<circle class="s f-gelb" cx="0" cy="0" r="30"/><rect class="s f-gelb" x="-10" y="-80" width="20" height="56" rx="6"/>'
                + pfeil(-34, -64, -58, -40, "s2 k-koralle", 6) + pfeil(34, -64, 58, -40, "s2 k-koralle", -6)
                + '<path class="s2 k-koralle" fill="none" d="M-22 -92 A 24 8 0 1 0 22 -92"/>' + pfeil(18, -86, 24, -92, "s2 k-koralle"))
    if art == "scharnier":
        return ('<path class="s f-weiss" d="M-44 40 V 16 Q -44 -6 -22 -6 H 22 Q 44 -6 44 16 V 40 Z"/>'
                '<rect class="s f-gelb" x="-38" y="-30" width="76" height="34" rx="17"/><rect class="s f-gelb" x="-10" y="-90" width="20" height="62" rx="6"/>'
                + pfeil(-14, -82, -54, -54, "s2 k-koralle", 10) + pfeil(14, -82, 54, -54, "s2 k-koralle", -10))
    if art == "sattel":
        return ('<path class="s f-weiss" d="M-44 40 V 0 C -20 -20, 20 -20, 44 0 V 40 Z"/>'
                '<path class="s f-gelb" d="M-30 -2 C -10 18, 10 18, 30 -2 L 30 -20 C 10 -4, -10 -4, -30 -20 Z"/>'
                '<rect class="s f-gelb" x="-10" y="-80" width="20" height="62" rx="6"/>'
                + pfeil(-14, -72, -46, -50, "s2 k-koralle", 8) + pfeil(14, -72, 46, -50, "s2 k-koralle", -8)
                + '<path class="s2 k-koralle" fill="none" d="M0 -96 v -12"/>' + pfeil(0, -96, 10, -108, "s2 k-koralle"))
    return ('<rect class="s f-weiss" x="-40" y="0" width="80" height="40" rx="6"/><ellipse class="s f-papier" cx="0" cy="2" rx="22" ry="8"/>'
            '<rect class="s f-gelb" x="-10" y="-86" width="20" height="90" rx="6"/>'
            '<path class="s2 k-koralle" fill="none" d="M-30 -50 A 30 10 0 1 0 30 -50"/>' + pfeil(24, -46, 30, -50, "s2 k-koralle"))


GELENKTYPEN = [
    ("kugel", "Kugelgelenk", "in alle Richtungen", "Schulter, Hüfte"),
    ("scharnier", "Scharniergelenk", "in eine Richtung", "Ellenbogen, Finger"),
    ("sattel", "Sattelgelenk", "in zwei Richtungen", "Daumen"),
    ("dreh", "Drehgelenk", "drehen", "oberste Halswirbel"),
]


def gelenktypen():
    i = ""
    for k, (art, name, wie, wo) in enumerate(GELENKTYPEN):
        x = 90 + k * 170
        i += f'<rect class="s2 f-weiss" x="{x - 80}" y="6" width="160" height="276" rx="16"/>'
        i += f'<g transform="translate({x} 150)">{_gelenk_symbol(art)}</g>'
        i += text(x, 222, name, "h") + text(x, 246, wie, "hk") + text(x, 268, wo, "hk")
    return svg("0 0 680 290", i, "Vier Gelenktypen im Modell",
               "Kugelgelenk: Bewegung in alle Richtungen, zum Beispiel Schulter und Hüfte. Scharniergelenk: Bewegung in eine Richtung, zum Beispiel Ellenbogen, Knie und Finger. "
               "Sattelgelenk: Bewegung in zwei Richtungen, zum Beispiel im Daumen. Drehgelenk: Drehung, zum Beispiel zwischen dem ersten und zweiten Halswirbel.")


# ---------------------------------------------------------------- Muskeln
def _mitte(p, q, d, seite):
    L = math.hypot(q[0] - p[0], q[1] - p[1])
    nx, ny = -(q[1] - p[1]) / L * seite, (q[0] - p[0]) / L * seite
    return ((p[0] + q[0]) / 2 + nx * d * 0.7, (p[1] + q[1]) / 2 + ny * d * 0.7)


def gegenspieler():
    i = ""
    a1, h1, bz1, tz1 = arm((120, 70), (116, 220), 70, 22, 9)
    i += a1
    bm = _mitte((130, 78), bz1, 22, -1)
    tm = _mitte((110, 76), tz1, 9, 1)
    i += text(30, 34, "Arm beugen", "h", "start")
    i += text(250, 96, "Beuger (Bizeps)", "h", "start") + text(250, 120, "zieht sich zusammen:", "hk", "start") + text(250, 142, "kurz und dick", "hk", "start")
    i += linie(246, 108, bm[0] + 4, bm[1])
    i += text(14, 300, "Strecker (Trizeps)", "h", "start") + text(14, 324, "entspannt: lang und dünn", "hk", "start") + linie(60, 280, tm[0] - 2, tm[1])
    i += pfeil(300, 250, 262, 168, "s k-koralle", 24)
    ox = 420
    a2, h2, bz2, tz2 = arm((ox + 80, 70), (ox + 76, 220), 174, 10, 18)
    i += a2
    bm2 = _mitte((ox + 90, 78), bz2, 10, -1)
    tm2 = _mitte((ox + 70, 76), tz2, 18, 1)
    i += text(ox + 20, 34, "Arm strecken", "h", "start")
    i += text(ox + 140, 120, "Beuger (Bizeps)", "h", "start") + text(ox + 140, 144, "entspannt", "hk", "start") + linie(ox + 136, 128, bm2[0] + 3, bm2[1])
    i += text(ox + 140, 250, "Strecker (Trizeps)", "h", "start") + text(ox + 140, 274, "zieht sich zusammen", "hk", "start") + linie(ox + 136, 244, tm2[0] - 2, tm2[1] + 20)
    i += pfeil(ox + 40, 250, ox + 60, 330, "s k-koralle", -10)
    return svg("0 0 720 400", i, "Gegenspielerprinzip am Oberarm",
               "Links wird der Arm gebeugt: Der Beuger (Bizeps) zieht sich zusammen und wird kurz und dick, der Strecker (Trizeps) ist entspannt. "
               "Rechts wird der Arm gestreckt: Jetzt zieht sich der Strecker zusammen und der Beuger ist entspannt.")


def muskel_aufbau():
    i = ""
    i += knochen(40, 150, 600, 150, 30, "f-gelb-weich")
    i += '<path class="s f-rosa-tief" d="M170 120 C 220 70, 420 70, 470 120 C 420 140, 220 140, 170 120 Z"/>'
    i += '<path class="s2" fill="none" opacity=".5" d="M190 116 C 240 86, 400 86, 450 116 M 200 120 C 250 100, 390 100, 440 120"/>'
    i += '<path class="s f-weiss" d="M170 120 C 150 126, 130 134, 110 136 L 112 140 C 134 140, 156 132, 172 126 Z"/>'
    i += '<path class="s f-weiss" d="M470 120 C 490 126, 510 134, 530 136 L 528 140 C 506 140, 484 132, 468 126 Z"/>'
    # Faserbündel im Ausschnitt
    i += '<circle class="s2 gestrichelt" cx="330" cy="98" r="18" fill="none"/>' + linie(344, 86, 390, 40, "s2 gestrichelt")
    i += '<g transform="translate(440 40)"><ellipse class="s f-rosa-tief" cx="0" cy="0" rx="46" ry="26"/>' + "".join(
        f'<circle class="s2 f-rosa" cx="{x}" cy="{y}" r="7"/>' for x, y in [(-26, -6), (-12, 8), (0, -10), (14, 6), (28, -6), (-2, 12), (-18, -14), (22, 14)]) + '</g>'
    i += text(520, 30, "Muskelfaserbündel", "hk", "start")
    i += text(320, 220, "Muskel", "h") + linie(320, 202, 320, 136)
    i += text(110, 220, "Sehne", "h") + linie(110, 202, 130, 140)
    i += text(530, 220, "Sehne", "h") + linie(530, 202, 510, 140)
    i += text(40, 110, "Knochen", "hk", "start")
    return svg("0 0 680 240", i, "Ein Muskel ist über Sehnen am Knochen befestigt",
               "Der Muskel besteht aus vielen Faserbündeln. An beiden Enden geht er in feste Sehnen über, die am Knochen festgewachsen sind.")


# ---------------------------------------------------------------- Haltung und Sport
def _figur(huefte, schulter, kopf, knie, fuss, haende, fill="f-blau"):
    """Einfache Figur aus dicken Linien."""
    hx, hy = huefte
    sx, sy = schulter
    i = f'<path class="figur-rumpf" d="M{hx} {hy} Q {(hx + sx) / 2 + (sy - hy) * 0.08} {(hy + sy) / 2} {sx} {sy}" fill="none" style="stroke:var(--tinte)" stroke-width="16" stroke-linecap="round"/>'
    i += f'<path d="M{hx} {hy} L {knie[0]} {knie[1]} L {fuss[0]} {fuss[1]}" fill="none" style="stroke:var(--tinte)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    i += f'<path d="M{sx} {sy} L {haende[0]} {haende[1]}" fill="none" style="stroke:var(--tinte)" stroke-width="9" stroke-linecap="round"/>'
    i += f'<circle class="s {fill}" cx="{kopf[0]}" cy="{kopf[1]}" r="17"/>'
    return i


def heben():
    i = ""
    # falsch
    i += '<rect class="s2 f-rosa-weich" x="8" y="8" width="312" height="290" rx="18"/>'
    i += _figur((120, 160), (200, 128), (222, 112), (122, 220), (120, 270), (206, 252))
    i += '<path class="s k-koralle" stroke-width="4" fill="none" d="M126 150 Q 160 110 196 124"/>'
    i += '<rect class="s f-sand" x="186" y="246" width="56" height="38" rx="4"/>'
    i += text(164, 40, "So nicht!", "h") + text(164, 64, "runder Rücken, Beine gestreckt", "hk")
    i += '<path class="s k-koralle" stroke-width="5" d="M270 250 l 30 30 m 0 -30 l -30 30"/>'
    # richtig
    i += '<rect class="s2 f-gruen-weich" x="340" y="8" width="312" height="290" rx="18"/>'
    i += _figur((470, 206), (488, 130), (494, 104), (520, 214), (494, 274), (520, 232), "f-gruen")
    i += '<rect class="s f-sand" x="514" y="228" width="56" height="44" rx="4"/>'
    i += text(496, 40, "So ist es richtig", "h") + text(496, 64, "Knie beugen, Rücken gerade, Last nah", "hk")
    i += '<path class="s k-gruen" stroke-width="5" fill="none" d="M600 270 l 10 12 l 20 -26"/>'
    return svg("0 0 660 306", i, "Richtig und falsch heben",
               "Links: Wer mit rundem Rücken und gestreckten Beinen hebt, belastet die Bandscheiben stark. "
               "Rechts: Richtig ist es, in die Knie zu gehen, den Rücken gerade zu halten und die Last nah am Körper zu tragen.")


def pech():
    kacheln = [
        ("P", "Pause", "sofort aufhören", '<path class="s f-gelb" d="M-20 30 V -6 Q -20 -14 -12 -14 V -30 Q -12 -36 -6 -36 Q 0 -36 0 -30 V -14 V -34 Q 0 -40 6 -40 Q 12 -40 12 -34 V -12 V -28 Q 12 -34 18 -34 Q 24 -34 24 -28 V 10 Q 24 30 4 30 Z"/>'),
        ("E", "Eis", "kühlen, mit Tuch", '<rect class="s f-blau" x="-30" y="-24" width="60" height="44" rx="10"/><path class="s2" fill="none" d="M-18 -10 l 8 8 m 0 -8 l -8 8 M 6 -2 l 8 8 m 0 -8 l -8 8"/>'),
        ("C", "Compression", "leichter Druckverband", '<path class="s f-weiss" d="M-34 -20 H 34 V 20 H -34 Z"/><path class="s2" fill="none" d="M-34 -6 H 34 M -34 8 H 34 M -16 -20 V 20 M 6 -20 V 20"/>'),
        ("H", "Hochlagern", "über Herzhöhe legen", '<rect class="s f-sand" x="-6" y="0" width="48" height="24" rx="10"/><path d="M-52 22 L 30 -8" fill="none" style="stroke:var(--tinte)" stroke-width="12" stroke-linecap="round"/><path d="M30 -8 L 34 -26" fill="none" style="stroke:var(--tinte)" stroke-width="10" stroke-linecap="round"/>'),
    ]
    i = ""
    for k, (b, name, was, bild) in enumerate(kacheln):
        x = 85 + k * 165
        i += f'<rect class="s2 f-weiss" x="{x - 76}" y="6" width="152" height="214" rx="16"/>'
        i += f'<text class="h" x="{x}" y="52" text-anchor="middle" style="font-size:44px">{b}</text>'
        i += f'<g transform="translate({x} 110)">{bild}</g>'
        i += text(x, 172, name, "h") + text(x, 198, was, "hk")
    return svg("0 0 670 228", i, "Erste Hilfe bei Sportverletzungen: die PECH-Regel",
               "P wie Pause: sofort aufhören. E wie Eis: kühlen, aber nicht direkt auf die Haut. C wie Compression: leichter Druckverband. H wie Hochlagern: über Herzhöhe legen.")


FIGUREN = {
    "skelett": (lambda: Z.skelett(), "Das Skelett des Menschen. Ein Erwachsener hat etwa 206 Knochen."),
    "knochen_aufbau": (knochen_aufbau, "Aufbau eines Röhrenknochens, der Länge nach aufgeschnitten (schematisch)."),
    "knochen_versuch": (knochen_versuch, "Was im Knochen steckt: zwei Versuche mit Hühnerknochen."),
    "wirbelsaeule": (wirbelsaeule, "Die doppelt-S-förmige Wirbelsäule federt Stöße ab wie eine Sprungfeder."),
    "gelenk_aufbau": (gelenk_aufbau, "So ist ein Gelenk aufgebaut (schematisch)."),
    "gelenktypen": (gelenktypen, "Gelenke unterscheiden sich darin, wie sie sich bewegen lassen."),
    "muskel_aufbau": (muskel_aufbau, "Muskeln sind über Sehnen an den Knochen befestigt."),
    "gegenspieler": (gegenspieler, "Beuger und Strecker arbeiten als Gegenspieler."),
    "heben": (heben, "Beim Heben kommt es auf die Haltung an."),
    "pech": (pech, "Die PECH-Regel hilft bei Prellungen, Zerrungen und Verstauchungen."),
}


# ---------------------------------------------------------------- Kopfbilder und Symbole
def reihe1_kopf():
    a, _, _, _ = arm((120, 50), (110, 190), 75, 18, 8)
    i = (blob(270, 140, 250, 110, "f-blau-weich", -3)
         + a
         + f'<g transform="translate(300 10) scale(0.38)">{"".join(Z._skelett_teile().values())}</g>'
         + '<g transform="translate(450 150) scale(0.6)">' + _gelenk_symbol("kugel") + '</g>'
         + '<circle class="s f-gelb" cx="250" cy="70" r="18"/><path class="s2" fill="none" d="M236 62 q 14 8 28 0 M 236 78 q 14 -8 28 0"/>'
         + funkeln(500, 40, 0.9) + funkeln(60, 220, 0.7, "k-blau"))
    return deko("0 0 540 270", i, "ill kopf-bild")


def kopf(slug):
    h = blob(300, 112, 280, 96, "f-blau-weich", 2)
    if slug == "01-das-skelett":
        T = Z._skelett_teile()
        i = h + f'<g transform="translate(150 4) scale(0.33)">{"".join(T.values())}</g>' + f'<g transform="translate(360 4) scale(0.33)">{"".join(T.values())}</g>'
        i += knochen(250, 120, 340, 150, 14) + funkeln(560, 40, 0.8) + funkeln(60, 60, 0.7, "k-rosa")
    elif slug == "02-knochen":
        i = h + knochen(110, 110, 300, 110, 46, "f-weiss") + '<rect class="s f-gelb" x="160" y="98" width="90" height="24" rx="10"/>'
        i += '<path class="s f-blau-weich" d="M380 50 V 180 Q 380 190 390 190 H 470 Q 480 190 480 180 V 50"/><path class="f-blau" opacity=".5" d="M382 90 V 180 Q 382 188 390 188 H 470 Q 478 188 478 180 V 90 Z"/>'
        i += rippe("M410 170 C 400 130, 450 140, 444 110", 10) + text(430, 210, "Essig", "hk") + funkeln(540, 60, 0.8)
    elif slug == "03-wirbelsaeule":
        pts = _catmull([(170, 30), (160, 60), (180, 120), (176, 160), (164, 200)], 14)
        i = h + "".join(f'<g transform="translate({x + 130:.1f} {y:.1f}) rotate({w - 90:.1f})"><rect class="s f-gelb-weich" x="-14" y="-6" width="28" height="11" rx="4"/></g>' for x, y, w in pts)
        i += '<path class="s f-sand" d="M140 120 h 56 l -6 70 h -44 z"/><rect class="s f-blau" x="128" y="96" width="80" height="34" rx="6"/>'
        i += text(168, 118, "Ranzen", "hk") + pfeil(440, 60, 440, 170, "s k-koralle") + text(470, 120, "federt", "h", "start")
    elif slug == "04-gelenke":
        i = h
        for k, art in enumerate(["kugel", "scharnier", "sattel", "dreh"]):
            i += f'<g transform="translate({120 + k * 120} 150) scale(0.75)">{_gelenk_symbol(art)}</g>'
    elif slug == "05-muskeln":
        a, _, _, _ = arm((210, 30), (200, 160), 62, 20, 8)
        i = h + a + text(420, 90, "Bizeps", "h", "start") + text(420, 120, "Trizeps", "h", "start") + funkeln(540, 40, 0.8)
    else:
        i = h + _figur((210, 150), (226, 70), (232, 44), (250, 160), (236, 210), (290, 60), "f-gruen")
        i += _figur((380, 140), (420, 80), (436, 60), (360, 190), (330, 210), (470, 70), "f-gelb")
        i += '<rect class="s f-blau" x="480" y="140" width="70" height="44" rx="10"/><path class="s2" fill="none" d="M492 154 l 8 8 m 0 -8 l -8 8"/>'
        i += funkeln(560, 40, 0.8)
    return deko("0 0 600 220", i, "ill lt-kopf")


def _s(i):
    return i


SYMBOLE = {
    "01-das-skelett": '<g transform="translate(14 2) scale(0.1)">' + "".join(Z._skelett_teile().values()) + '</g>',
    "02-knochen": knochen(10, 32, 54, 32, 14, "f-weiss") + '<rect class="s f-gelb" x="22" y="27" width="20" height="10" rx="4"/>',
    "03-wirbelsaeule": "".join(f'<rect class="s f-gelb-weich" x="{24 + round(4 * math.sin(k / 1.4))}" y="{6 + k * 9}" width="16" height="7" rx="3"/>' for k in range(6)),
    "04-gelenke": f'<g transform="translate(32 44) scale(0.42)">{_gelenk_symbol("kugel")}</g>',
    "05-muskeln": muskel((10, 40), (54, 40), 12, "f-rosa-tief"),
    "06-haltung-und-sport": _figur((26, 44), (30, 22), (32, 12), (36, 50), (30, 60), (44, 18), "f-gruen").replace('stroke-width="16"', 'stroke-width="6"').replace('stroke-width="10"', 'stroke-width="4"').replace('stroke-width="9"', 'stroke-width="4"').replace('r="17"', 'r="6"'),
    "skelett-erkunden": '<g transform="translate(14 2) scale(0.1)">' + "".join(Z._skelett_teile().values()) + '</g>' + '<circle class="s2 k-koralle" cx="32" cy="10" r="9" fill="none"/>',
    "gelenk-modell": f'<g transform="translate(32 44) scale(0.42)">{_gelenk_symbol("scharnier")}</g>',
    "arm-modell": muskel((10, 46), (46, 18), 10, "f-rosa-tief") + knochen(8, 54, 56, 54, 7),
}
for _slug, _f in [("r1-skelett-zuordnen", Z.sym_zuordnen), ("r1-gelenke-sortieren", Z.sym_sortieren), ("r1-gelenk-lueckentext", Z.sym_luecke),
                  ("r1-arm-reihenfolge", Z.sym_reihenfolge), ("r1-ruecken-sortieren", Z.sym_sortieren), ("r1-quiz", Z.sym_quiz),
                  ("r1-fachbegriffe", Z.sym_training), ("r1-knochen-lueckentext", Z.sym_luecke), ("r1-schreiben", Z.sym_schreiben),
                  ("r1-verletzungen", Z.sym_zuordnen)]:
    SYMBOLE[_slug] = _f()

Z.SYMBOLE.update(SYMBOLE)
for _slug in ["01-das-skelett", "02-knochen", "03-wirbelsaeule", "04-gelenke", "05-muskeln", "06-haltung-und-sport"]:
    Z.KOEPFE[_slug] = (lambda s=_slug: kopf(s))
Z.KOPFBILDER[1] = reihe1_kopf
