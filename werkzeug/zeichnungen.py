"""Eigene Zeichnungen im Skizzenbuch-Stil (wie Biologie Klasse 8). Farben kommen über CSS-Klassen
(siehe style.css, Abschnitt Zeichnungen), damit sie im hellen und dunklen Modus funktionieren.

Klassen:  s = Tintenlinie, s2 = dünne Linie, d = Tintenfläche
          f-blau, f-rosa, f-gruen, f-gelb, f-sand, f-weiss, f-papier (+ -weich/-tief) = Füllfarben
          k-blau, k-rosa, k-gruen, k-bernstein, k-koralle, k-violett = farbige Linien
          h = Handschrift-Beschriftung, hk = kleine Handschrift
"""
import math
import hashlib


def svg(viewbox, inhalt, titel, beschreibung="", klasse="ill"):
    vid = "i" + hashlib.md5(titel.encode()).hexdigest()[:8]
    desc = f'<desc id="{vid}d">{beschreibung}</desc>' if beschreibung else ""
    lab = f'{vid}t {vid}d' if beschreibung else f'{vid}t'
    return (f'<svg class="{klasse}" viewBox="{viewbox}" role="img" aria-labelledby="{lab}" xmlns="http://www.w3.org/2000/svg">'
            f'<title id="{vid}t">{titel}</title>{desc}{inhalt}</svg>')


def deko(viewbox, inhalt, klasse="ill"):
    return f'<svg class="{klasse}" viewBox="{viewbox}" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">{inhalt}</svg>'


# ---------------------------------------------------------------- Grundbausteine
def text(x, y, t, klasse="h", anker="middle", drehung=0):
    rot = f' transform="rotate({drehung} {x} {y})"' if drehung else ""
    return f'<text class="{klasse}" x="{x}" y="{y}" text-anchor="{anker}"{rot}>{t}</text>'


def pfeil(x1, y1, x2, y2, klasse="s2", bogen=0):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - bogen
    ang = math.atan2(y2 - my, x2 - mx)
    a1 = (x2 - 9 * math.cos(ang - 0.45), y2 - 9 * math.sin(ang - 0.45))
    a2 = (x2 - 9 * math.cos(ang + 0.45), y2 - 9 * math.sin(ang + 0.45))
    return (f'<path class="{klasse}" fill="none" d="M{x1} {y1} Q{mx} {my} {x2} {y2}"/>'
            f'<path class="{klasse}" fill="none" d="M{a1[0]:.1f} {a1[1]:.1f} L{x2} {y2} L{a2[0]:.1f} {a2[1]:.1f}"/>')


def linie(x1, y1, x2, y2, klasse="s2"):
    return f'<path class="{klasse}" fill="none" d="M{x1} {y1} L{x2} {y2}"/>'


def funkeln(x, y, s=1.0, klasse="k-bernstein"):
    return f'<path transform="translate({x} {y}) scale({s})" class="s2 {klasse}" d="M0 -8 V8 M-8 0 H8 M-5 -5 L5 5 M5 -5 L-5 5" fill="none"/>'


def blob(x, y, rx, ry, fill, drehung=0):
    return (f'<path transform="translate({x} {y}) rotate({drehung})" class="{fill}" '
            f'd="M{-rx} 0 C {-rx} {-ry * 0.9:.1f}, {-rx * 0.3:.1f} {-ry}, {rx * 0.2:.1f} {-ry} C {rx * 0.9:.1f} {-ry}, {rx} {-ry * 0.4:.1f}, {rx} {ry * 0.1:.1f} '
            f'C {rx} {ry * 0.8:.1f}, {rx * 0.4:.1f} {ry}, {-rx * 0.1:.1f} {ry} C {-rx * 0.8:.1f} {ry}, {-rx} {ry * 0.6:.1f}, {-rx} 0 Z"/>')


def tropfen(x, y, s=1.0, fill="f-blau"):
    return f'<path transform="translate({x} {y}) scale({s})" class="s {fill}" d="M0 -14 C 6 -5, 10 0, 10 5 A 10 10 0 0 1 -10 5 C -10 0, -6 -5, 0 -14 Z"/>'


def herz(x, y, s=1.0, fill="f-rosa-tief"):
    return (f'<path transform="translate({x} {y}) scale({s})" class="s {fill}" '
            'd="M0 18 C -22 4, -26 -12, -14 -18 C -6 -22, 0 -16, 0 -10 C 0 -16, 6 -22, 14 -18 C 26 -12, 22 4, 0 18 Z"/>')


def sonne(x, y, r=16):
    strahlen = "".join(f'<line class="s2 k-bernstein" x1="{x + math.cos(math.radians(a)) * (r + 6):.1f}" y1="{y + math.sin(math.radians(a)) * (r + 6):.1f}" '
                       f'x2="{x + math.cos(math.radians(a)) * (r + 13):.1f}" y2="{y + math.sin(math.radians(a)) * (r + 13):.1f}"/>' for a in range(0, 360, 45))
    return strahlen + f'<circle class="s f-gelb" cx="{x}" cy="{y}" r="{r}"/>'


def blatt(x, y, s=1.0, drehung=0, fill="f-gruen"):
    return (f'<g transform="translate({x} {y}) rotate({drehung}) scale({s})"><path class="s {fill}" d="M0 30 C -22 10, -20 -20, 0 -34 C 20 -20, 22 10, 0 30 Z"/>'
            '<path class="s2 k-gruen" fill="none" d="M0 34 V -26 M0 0 L -10 -10 M0 12 L 10 2 M 0 -12 L 8 -20"/></g>')


def auge(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-weiss" d="M-30 0 C -16 -18, 16 -18, 30 0 C 16 18, -16 18, -30 0 Z"/>'
            '<circle class="s f-blau" r="10"/><circle class="d" r="4.5"/><circle class="f-weiss" cx="3" cy="-3" r="1.8"/></g>')


def apfel(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path class="s f-rosa-tief" d="M0 -14 C -8 -22, -26 -18, -26 0 C -26 18, -12 28, 0 22 C 12 28, 26 18, 26 0 C 26 -18, 8 -22, 0 -14 Z"/>'
            '<path class="s2" fill="none" d="M0 -14 C 0 -20, 2 -26, 6 -30"/>' + blatt(10, -26, 0.32, 60) + '</g>')


# ---------------------------------------------------------------- Knochen
def knochen(x1, y1, x2, y2, w=10, fill="f-gelb-weich", extra=""):
    """Knochen mit verdickten Enden (Gelenkköpfe) zwischen zwei Punkten."""
    L = math.hypot(x2 - x1, y2 - y1)
    a = math.degrees(math.atan2(y2 - y1, x2 - x1))
    h = w / 2
    r = h * 0.95
    o = h * 0.62
    k = "".join(f'<circle class="s {fill} kf" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/>' for cx, cy in [(0, -o), (0, o), (L, -o), (L, o)])
    schaft = f'<rect class="{fill} kf" x="0" y="{-h:.1f}" width="{L:.1f}" height="{w:.1f}"/>'
    kanten = (f'<path class="s" fill="none" d="M{r * 0.55:.1f} {-h:.1f} H{L - r * 0.55:.1f} M{r * 0.55:.1f} {h:.1f} H{L - r * 0.55:.1f}"/>')
    return f'<g transform="translate({x1:.1f} {y1:.1f}) rotate({a:.2f})"{extra}>{k}{schaft}{kanten}</g>'


def rippe(d, dicke=6):
    """Knochen als gebogene Linie (Rippe): dunkler Rand mit heller Füllung."""
    return (f'<path d="{d}" fill="none" style="stroke:var(--tinte)" stroke-width="{dicke + 4.4}" stroke-linecap="round"/>'
            f'<path class="kf-s" d="{d}" fill="none" style="stroke:var(--ill-gelb-weich)" stroke-width="{dicke}" stroke-linecap="round"/>')


def spiegel(inhalt, achse):
    return f'<g transform="translate({2 * achse} 0) scale(-1 1)">{inhalt}</g>'


# ---------------------------------------------------------------- Skelett
# Teile mit Namen und kurzer Erklärung (auch für das Modell „Skelett erkunden“)
SKELETT_TEILE = [
    ("schaedel", "Schädel", "Der Schädel schützt das Gehirn. Nur der Unterkiefer ist beweglich, die übrigen Schädelknochen sind fest miteinander verwachsen."),
    ("wirbelsaeule", "Wirbelsäule", "Die Wirbelsäule trägt den Oberkörper und den Kopf. In ihr verläuft geschützt das Rückenmark. Sie besteht aus vielen Wirbeln."),
    ("brustkorb", "Brustkorb (Rippen und Brustbein)", "Zwölf Rippenpaare und das Brustbein bilden einen Korb. Er schützt Herz und Lunge und bewegt sich beim Atmen mit."),
    ("schluesselbein", "Schlüsselbein", "Das Schlüsselbein verbindet das Brustbein mit der Schulter. Bei Stürzen auf die Schulter bricht es leicht."),
    ("oberarm", "Oberarmknochen", "Der Oberarmknochen reicht von der Schulter bis zum Ellenbogen. An ihm setzen die Muskeln an, die den Arm beugen und strecken."),
    ("unterarm", "Elle und Speiche", "Im Unterarm liegen zwei Knochen: die Elle und die Speiche. Weil sich die Speiche um die Elle drehen kann, kannst du die Hand drehen."),
    ("hand", "Handknochen", "Die Hand hat 27 Knochen: Handwurzel, Mittelhand und Finger. So kann sie greifen, halten und feine Bewegungen machen."),
    ("becken", "Becken", "Das Becken trägt den Oberkörper und die Bauchorgane. An ihm sind die Beine über das Hüftgelenk befestigt."),
    ("oberschenkel", "Oberschenkelknochen", "Der Oberschenkelknochen ist der längste und kräftigste Knochen des Körpers."),
    ("kniescheibe", "Kniescheibe", "Die Kniescheibe liegt vorn auf dem Kniegelenk und schützt es. Sie ist in eine Sehne eingebettet."),
    ("unterschenkel", "Schienbein und Wadenbein", "Im Unterschenkel liegen das kräftige Schienbein und das dünne Wadenbein. Das Schienbein trägt fast das ganze Gewicht."),
    ("fuss", "Fußknochen", "Der Fuß hat 26 Knochen. Sie bilden ein Gewölbe, das beim Gehen und Springen federt."),
]


def _skelett_teile():
    """Gibt {name: svg} für ein Skelett von vorn zurück (Koordinaten 0..320 x 0..640, Mitte x = 160)."""
    T = {}
    M = 160
    # Schädel
    T["schaedel"] = ('<path class="s f-gelb-weich kf" d="M124 58 C 122 16, 198 16, 196 58 C 196 80, 190 92, 184 98 L 182 112 C 176 122, 144 122, 138 112 L 136 98 C 130 92, 124 80, 124 58 Z"/>'
                     '<ellipse class="d" cx="146" cy="66" rx="9" ry="10"/><ellipse class="d" cx="174" cy="66" rx="9" ry="10"/>'
                     '<path class="d" d="M160 76 L 154 90 H 166 Z"/>'
                     '<path class="s2" fill="none" d="M142 104 H 178 M148 100 V 108 M154 100 V 109 M160 100 V 109 M166 100 V 109 M172 100 V 108"/>')
    # Wirbelsäule (Hals sichtbar, unten Lendenwirbel)
    ws = ""
    for k, y in enumerate(range(122, 336, 12)):
        b = 13 if y < 150 else (15 if y < 300 else 19)
        ws += f'<rect class="s f-gelb-weich kf" x="{M - b / 2}" y="{y}" width="{b}" height="9" rx="3"/>'
    T["wirbelsaeule"] = ws
    # Brustkorb: Rippen links (gespiegelt rechts) und Brustbein
    rp = ""
    for i in range(10):
        y = 150 + i * 11
        if i < 7:
            W = 30 + min(i, 4) * 5
            d = f"M{M - 7} {y} C {M - 30} {y - 8}, {M - W - 8} {y - 2}, {M - W - 6} {y + 16} C {M - W - 4} {y + 26}, {M - W + 6} {y + 30}, {M - W + 14} {y + 28}"
        else:
            W = 52 - (i - 7) * 5
            d = f"M{M - 10 - (i - 6) * 7} {y + 4} C {M - 34} {y}, {M - W - 4} {y + 4}, {M - W - 2} {y + 18}"
        rp += rippe(d, 4.4)
    T["brustkorb"] = rp + spiegel(rp, M) + f'<rect class="s f-gelb-weich kf" x="{M - 7}" y="142" width="14" height="78" rx="5"/>'
    T["schluesselbein"] = knochen(M - 6, 140, 112, 134, 7) + knochen(M + 6, 140, 208, 134, 7)
    ob = knochen(112, 142, 102, 250, 12)
    T["oberarm"] = ob + spiegel(ob, M)
    ua = knochen(98, 256, 90, 350, 7) + knochen(108, 258, 104, 350, 6)
    T["unterarm"] = ua + spiegel(ua, M)
    hd = '<path class="s f-gelb-weich kf" d="M86 352 C 86 346, 110 346, 110 352 L 112 368 C 106 372, 90 372, 84 368 Z"/>'
    for fx, ex in [(84, 74), (90, 84), (97, 96), (104, 108), (110, 118)]:
        hd += knochen(fx, 370, ex, 404 if ex not in (74, 118) else 394, 4.2)
    T["hand"] = hd + spiegel(hd, M)
    T["becken"] = (f'<path class="s f-gelb-weich kf" d="M{M} 320 C 140 312, 110 312, 106 332 C 102 352, 116 362, 126 372 L 140 378 C 146 368, 152 362, {M} 362 '
                   f'C 168 362, 174 368, 180 378 L 194 372 C 204 362, 218 352, 214 332 C 210 312, 180 312, {M} 320 Z"/>'
                   '<ellipse class="f-papier" cx="138" cy="356" rx="9" ry="7"/><ellipse class="f-papier" cx="182" cy="356" rx="9" ry="7"/>'
                   '<path class="s2" fill="none" d="M126 338 C 136 344, 148 346, 160 346 C 172 346, 184 344, 194 338"/>')
    os_ = knochen(130, 374, 138, 488, 13)
    T["oberschenkel"] = os_ + spiegel(os_, M)
    T["kniescheibe"] = '<circle class="s f-gelb-weich kf" cx="139" cy="494" r="7.5"/>' + spiegel('<circle class="s f-gelb-weich kf" cx="139" cy="494" r="7.5"/>', M)
    us = knochen(138, 504, 140, 598, 10) + knochen(152, 508, 150, 596, 5)
    T["unterschenkel"] = us + spiegel(us, M)
    fs = ('<path class="s f-gelb-weich kf" d="M126 604 C 128 600, 152 600, 154 604 L 158 618 C 150 622, 132 622, 122 618 Z"/>'
          + "".join(knochen(x, 620, x - 4 + j, 634, 4.2) for j, x in enumerate([124, 132, 140, 147, 154])))
    T["fuss"] = fs + spiegel(fs, M)
    return T


def skelett(beschriften=True, interaktiv=False):
    T = _skelett_teile()
    reihen = ["wirbelsaeule", "brustkorb", "schluesselbein", "becken", "oberschenkel", "unterschenkel", "kniescheibe", "fuss", "oberarm", "unterarm", "hand", "schaedel"]
    namen = {k: n for k, n, _ in SKELETT_TEILE}
    teile = ""
    for k in reihen:
        if interaktiv:
            teile += f'<g class="sk-teil" data-teil="{k}" tabindex="0" role="button" aria-label="{namen[k]}">{T[k]}</g>'
        else:
            teile += f'<g>{T[k]}</g>'
    ox = 160
    inhalt = f'<g transform="translate({ox} 0)">{teile}</g>'
    if beschriften:
        links = [("Schädel", 70, 128), ("Schlüsselbein", 138, 116 + ox - 36), ("Oberarmknochen", 196, 106), ("Elle und Speiche", 300, 96),
                 ("Handknochen", 388, 90), ("Oberschenkelknochen", 432, 132), ("Schienbein und Wadenbein", 552, 140)]
        rechts = [("Wirbelsäule", 128, 166), ("Brustkorb", 186, 204), ("Brustbein", 226, 166), ("Becken", 340, 212),
                  ("Kniescheibe", 494, 186), ("Fußknochen", 620, 190)]
        b = ""
        for t, y, zx in links:
            b += text(16, y + 6, t, "hk", "start") + linie(16 + len(t) * 8.4, y, zx + ox if zx < 200 else zx, y, "s2 gestrichelt")
        for t, y, zx in rechts:
            b += text(624, y + 6, t, "hk", "end") + linie(zx + ox, y, 624 - len(t) * 8.6, y, "s2 gestrichelt")
        inhalt += b
        return svg("0 0 640 650", inhalt, "Das Skelett des Menschen von vorn",
                   "Schematische Zeichnung des Skeletts mit Schädel, Wirbelsäule, Brustkorb mit Rippen und Brustbein, Schlüsselbein, Oberarmknochen, "
                   "Elle und Speiche, Handknochen, Becken, Oberschenkelknochen, Kniescheibe, Schienbein und Wadenbein sowie Fußknochen.")
    if interaktiv:
        return f'<svg class="ill sk-bild" viewBox="150 0 340 650" role="group" aria-label="Skelett zum Anklicken" xmlns="http://www.w3.org/2000/svg">{inhalt}</svg>'
    return deko("150 0 340 650", inhalt)


# ---------------------------------------------------------------- Muskel und Arm
def muskel(p1, p2, dicke, fill="f-rosa-tief", seite=1, klasse_extra=""):
    """Spindelförmiger Muskel zwischen p1 und p2 mit kurzen Sehnen an den Enden."""
    (x1, y1), (x2, y2) = p1, p2
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy * seite, ux * seite
    s = min(14, L * 0.12)
    a = (x1 + ux * s, y1 + uy * s)
    b = (x2 - ux * s, y2 - uy * s)
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    c1 = (m[0] + nx * dicke * 1.3, m[1] + ny * dicke * 1.3)
    c2 = (m[0] - nx * dicke * 0.55, m[1] - ny * dicke * 0.55)
    d = (f"M{a[0]:.1f} {a[1]:.1f} Q{c1[0]:.1f} {c1[1]:.1f} {b[0]:.1f} {b[1]:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {a[0]:.1f} {a[1]:.1f} Z")
    sehnen = f'<path class="s2 sehne" fill="none" d="M{x1:.1f} {y1:.1f} L{a[0]:.1f} {a[1]:.1f} M{b[0]:.1f} {b[1]:.1f} L{x2:.1f} {y2:.1f}"/>'
    linien = f'<path class="s2" fill="none" opacity=".45" d="M{a[0]:.1f} {a[1]:.1f} Q{m[0] + nx * dicke * 0.5:.1f} {m[1] + ny * dicke * 0.5:.1f} {b[0]:.1f} {b[1]:.1f}"/>'
    return f'<g class="muskel{klasse_extra}">{sehnen}<path class="s {fill}" d="{d}"/>{linien}</g>'


def arm(schulter, ellbogen, winkel, bizeps_dick, trizeps_dick, beschriftung=True):
    """Arm von der Seite. winkel = Winkel im Ellenbogen (180 = gestreckt). Unterarm zeigt nach rechts oben beim Beugen."""
    sx, sy = schulter
    ex, ey = ellbogen
    oa = math.atan2(ey - sy, ex - sx)
    knick = math.radians(180 - winkel)
    ua = oa - knick
    L = 150
    hx, hy = ex + math.cos(ua) * L, ey + math.sin(ua) * L
    # Ansatzpunkte
    bz_oben = (sx + 14, sy + 8)
    bz_unten = (ex + math.cos(ua) * 34 + math.cos(ua - math.pi / 2) * 10, ey + math.sin(ua) * 34 + math.sin(ua - math.pi / 2) * 10)
    tz_oben = (sx - 14, sy + 6)
    tz_unten = (ex - math.cos(ua) * 12 - 9, ey - math.sin(ua) * 12 + 4)
    i = ""
    i += f'<circle class="s f-gelb-weich" cx="{sx}" cy="{sy}" r="16"/>'
    i += knochen(sx, sy + 4, ex, ey, 16)
    i += knochen(ex, ey, hx, hy, 13)
    i += f'<g transform="translate({hx:.1f} {hy:.1f}) rotate({math.degrees(ua):.1f})"><path class="s f-gelb-weich" d="M2 -12 C 30 -16, 44 -6, 46 4 C 40 12, 20 14, 2 12 Z"/>'
    i += '<path class="s2" fill="none" d="M18 -12 V 10 M 30 -11 V 10"/></g>'
    i += muskel(tz_oben, tz_unten, trizeps_dick, "f-rosa", 1)
    i += muskel(bz_oben, bz_unten, bizeps_dick, "f-rosa-tief", -1)
    return i, (hx, hy), bz_unten, tz_unten


# ---------------------------------------------------------------- Startseite und Karten
LOGO_INHALT = ('<path class="s f-gruen" d="M8 30 C 4 18, 12 6, 22 5 C 34 4, 38 16, 33 26 C 29 34, 14 36, 8 30 Z"/>'
               '<path class="s2 k-gruen" fill="none" d="M10 31 C 16 24, 22 18, 30 10"/>'
               '<circle class="s f-rosa-tief" cx="30" cy="30" r="6"/>')


def hero_bild():
    T = _skelett_teile()
    sk = '<g transform="translate(70 18) scale(0.5)">' + "".join(T.values()) + '</g>'
    inhalt = (blob(300, 175, 250, 160, "f-blau-weich", 6)
              + sk
              + herz(330, 100, 2.0)
              + apfel(450, 120, 1.5)
              + '<g transform="translate(330 262)">' + blatt(0, 0, 1.3, -20) + blatt(42, 6, 1.0, 30) + '</g>'
              + sonne(470, 255, 22)
              + auge(220, 300, 1.2)
              + funkeln(520, 40, 0.9) + funkeln(250, 30, 0.7, "k-rosa") + funkeln(560, 180, 0.7, "k-blau"))
    return deko("0 0 600 360", inhalt, "ill hero-bild")


def karte_bild(nr):
    if nr == 1:
        arm_i, _, _, _ = arm((70, 30), (70, 112), 70, 13, 7)
        i = (arm_i + knochen(150, 40, 230, 110, 12) + '<circle class="s f-gelb" cx="218" cy="40" r="15"/>'
             + '<path class="s2" fill="none" d="M206 30 q 12 6 24 0 M 206 50 q 12 -6 24 0"/>' + funkeln(196, 120, 0.6))
    elif nr == 2:
        i = (herz(80, 70, 2.4)
             + '<path class="s f-rosa-weich" d="M150 30 C 130 30, 126 60, 128 90 C 130 116, 152 118, 160 104 L 166 40 C 164 32, 158 30, 150 30 Z"/>'
             + '<path class="s f-rosa-weich" d="M204 30 C 224 30, 228 60, 226 90 C 224 116, 202 118, 194 104 L 188 40 C 190 32, 196 30, 204 30 Z"/>'
             + '<path class="s2" fill="none" d="M177 10 V 46 M177 46 L 166 60 M 177 46 L 188 60"/>'
             + pfeil(30, 128, 120, 128, "s2 k-rosa") + funkeln(20, 20, 0.6))
    elif nr == 3:
        i = (apfel(60, 80, 1.6)
             + '<path class="s f-sand" d="M110 40 C 150 30, 200 34, 210 60 C 218 84, 186 92, 160 86 C 132 82, 120 100, 150 112 C 180 124, 220 114, 228 128"/>'
             + '<path class="s f-gelb" d="M120 108 C 130 100, 150 100, 160 110 C 150 122, 130 122, 120 108 Z"/>'
             + '<rect class="s f-gelb-weich" x="168" y="94" width="36" height="22" rx="8"/>' + funkeln(220, 24, 0.7))
    elif nr == 4:
        i = (sonne(46, 40, 18) + blatt(120, 76, 1.4, -10) + blatt(158, 92, 1.0, 34)
             + '<path class="s f-sand" d="M190 112 C 186 96, 196 84, 212 86 C 228 82, 238 98, 232 112 Z"/><circle class="d" cx="222" cy="96" r="2.2"/>'
             + '<path class="s2" fill="none" d="M0 126 C 60 118, 120 134, 240 122"/>'
             + "".join(f'<path class="s2 k-blau" fill="none" d="M{x} {y} l 4 4 m 0 -4 l -4 4"/>' for x, y in [(20, 96), (70, 110), (210, 40), (180, 60), (90, 26)]))
    elif nr == 5:
        i = (auge(80, 70, 1.8)
             + '<path class="s f-rosa-weich" d="M170 30 C 200 24, 222 50, 214 80 C 208 100, 194 98, 190 112 C 186 126, 168 128, 162 116 C 172 108, 178 98, 172 90 C 160 84, 156 40, 170 30 Z"/>'
             + '<path class="s2" fill="none" d="M180 50 C 196 50, 200 70, 188 76"/>'
             + "".join(f'<path class="s2 k-violett" fill="none" d="M{132 - k * 8} {50 - k * 8} q -{8 + k * 6} 20 0 {40 + k * 16}"/>' for k in range(3)))
    else:
        i = ('<circle class="s f-gelb" cx="60" cy="48" r="20"/><path class="s f-gelb" d="M30 120 C 30 84, 90 84, 90 120 Z"/>'
             '<circle class="s f-blau" cx="180" cy="44" r="22"/><path class="s f-blau" d="M146 120 C 146 80, 214 80, 214 120 Z"/>'
             + herz(120, 60, 1.0, "f-rosa-tief")
             + '<path class="s2 k-violett" fill="none" d="M100 104 C 110 96, 130 96, 140 104"/>' + funkeln(226, 20, 0.6, "k-violett"))
    return deko("0 0 240 140", i, "ill karte-bild")


# ---------------------------------------------------------------- Symbole für Listen
def sym_quiz():
    return ('<path class="s f-gelb" d="M10 14 Q 10 8 16 8 H 48 Q 54 8 54 14 V 38 Q 54 44 48 44 H 28 L 18 54 L 20 44 H 16 Q 10 44 10 38 Z"/>'
            '<text class="h" x="32" y="36" text-anchor="middle">?</text>')


def sym_training():
    return ('<rect class="s f-weiss" x="12" y="8" width="40" height="50" rx="5"/><rect class="s f-sand" x="22" y="4" width="20" height="9" rx="3"/>'
            '<path class="s2 k-gruen" fill="none" d="M18 24 l 4 4 l 7 -8 M 18 38 l 4 4 l 7 -8"/><path class="s2" d="M33 26 H 46 M 33 40 H 46 M 18 52 H 42"/>')


def sym_reihenfolge():
    return ('<rect class="s f-blau" x="10" y="8" width="44" height="12" rx="4"/><rect class="s f-rosa" x="10" y="26" width="44" height="12" rx="4"/>'
            '<rect class="s f-gelb" x="10" y="44" width="44" height="12" rx="4"/><text class="hk" x="16" y="18" style="font-size:12px">1</text>'
            '<text class="hk" x="16" y="36" style="font-size:12px">2</text><text class="hk" x="16" y="54" style="font-size:12px">3</text>')


def sym_schreiben():
    return ('<rect class="s f-weiss" x="8" y="10" width="38" height="46" rx="4"/><path class="s2" d="M14 22 H 38 M 14 32 H 38 M 14 42 H 30"/>'
            '<g transform="rotate(35 46 32)"><rect class="s f-gelb" x="42" y="6" width="9" height="40" rx="2"/><path class="s f-sand" d="M42 46 L 46.5 56 L 51 46 Z"/></g>')


def sym_sortieren():
    return ('<path class="s f-gruen" d="M8 30 H 28 V 54 H 8 Z"/><path class="s f-rosa" d="M36 30 H 56 V 54 H 36 Z"/>'
            '<rect class="s f-weiss" x="12" y="8" width="16" height="12" rx="3"/><rect class="s f-weiss" x="36" y="8" width="16" height="12" rx="3"/>'
            + pfeil(20, 20, 18, 28, "s2") + pfeil(44, 20, 46, 28, "s2"))


def sym_zuordnen():
    return ('<circle class="s f-blau" cx="14" cy="18" r="6"/><circle class="s f-rosa" cx="14" cy="46" r="6"/><rect class="s f-weiss" x="40" y="12" width="16" height="12" rx="3"/>'
            '<rect class="s f-weiss" x="40" y="40" width="16" height="12" rx="3"/><path class="s2" fill="none" d="M20 18 C 30 18, 30 46, 40 46 M 20 46 C 30 46, 30 18, 40 18"/>')


def sym_luecke():
    return ('<rect class="s f-weiss" x="8" y="10" width="48" height="44" rx="5"/><path class="s2" d="M14 22 H 28 M 44 22 H 50 M 14 34 H 22 M 38 34 H 50 M 14 46 H 34"/>'
            '<rect class="s2 f-gelb" x="30" y="16" width="12" height="11" rx="2"/><rect class="s2 f-gelb" x="24" y="28" width="12" height="11" rx="2"/>')


SYMBOLE = {}   # wird von den Reihen-Modulen gefüllt: slug -> svg-Inhalt (64 x 64)
KOEPFE = {}    # slug -> Funktion, die das Kopfbild eines Lerntextes liefert
KOPFBILDER = {}  # Reihennummer -> Kopfbild der Reihenübersicht


def symbol(name):
    return deko("0 0 64 64", SYMBOLE.get(name, ""), "ill symbol")


def lt_kopf(slug):
    f = KOEPFE.get(slug)
    return f() if f else ""


def reihe_kopf(nr):
    if nr in KOPFBILDER:
        return KOPFBILDER[nr]()
    return deko("0 0 240 140", karte_bild(nr)[karte_bild(nr).index(">") + 1:-6], "ill kopf-bild")
