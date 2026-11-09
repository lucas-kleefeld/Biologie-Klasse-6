/* Modelle der Reihe 1: Bewegung und Gesundheit. Ohne Datenspeicherung. */
(function () {
  "use strict";

  function $(id) { return document.getElementById(id); }
  function f(n) { return n.toFixed(1); }

  function knochen(x1, y1, x2, y2, w, fill) {
    fill = fill || "f-gelb-weich";
    var L = Math.hypot(x2 - x1, y2 - y1), a = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
    var h = w / 2, r = h * 0.95, o = h * 0.62, k = "";
    [[0, -o], [0, o], [L, -o], [L, o]].forEach(function (p) { k += '<circle class="s ' + fill + '" cx="' + f(p[0]) + '" cy="' + f(p[1]) + '" r="' + f(r) + '"/>'; });
    return '<g transform="translate(' + f(x1) + ' ' + f(y1) + ') rotate(' + f(a) + ')">' + k +
      '<rect class="' + fill + '" x="0" y="' + f(-h) + '" width="' + f(L) + '" height="' + f(w) + '"/>' +
      '<path class="s" fill="none" d="M' + f(r * 0.55) + ' ' + f(-h) + ' H' + f(L - r * 0.55) + ' M' + f(r * 0.55) + ' ' + f(h) + ' H' + f(L - r * 0.55) + '"/></g>';
  }

  function muskel(p1, p2, dicke, fill, seite) {
    var L = Math.hypot(p2[0] - p1[0], p2[1] - p1[1]);
    var ux = (p2[0] - p1[0]) / L, uy = (p2[1] - p1[1]) / L, nx = -uy * seite, ny = ux * seite;
    var s = Math.min(14, L * 0.12);
    var a = [p1[0] + ux * s, p1[1] + uy * s], b = [p2[0] - ux * s, p2[1] - uy * s];
    var m = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2];
    var c1 = [m[0] + nx * dicke * 1.3, m[1] + ny * dicke * 1.3], c2 = [m[0] - nx * dicke * 0.55, m[1] - ny * dicke * 0.55];
    return '<path class="s2" fill="none" d="M' + f(p1[0]) + ' ' + f(p1[1]) + ' L' + f(a[0]) + ' ' + f(a[1]) + ' M' + f(b[0]) + ' ' + f(b[1]) + ' L' + f(p2[0]) + ' ' + f(p2[1]) + '"/>' +
      '<path class="s ' + fill + '" d="M' + f(a[0]) + ' ' + f(a[1]) + ' Q' + f(c1[0]) + ' ' + f(c1[1]) + ' ' + f(b[0]) + ' ' + f(b[1]) + ' Q' + f(c2[0]) + ' ' + f(c2[1]) + ' ' + f(a[0]) + ' ' + f(a[1]) + ' Z"/>';
  }

  function text(x, y, t, kl, anker) { return '<text class="' + (kl || "hk") + '" x="' + f(x) + '" y="' + f(y) + '" text-anchor="' + (anker || "middle") + '">' + t + '</text>'; }

  function wahl(gruppe, attr, aufWahl) {
    var knoepfe = gruppe.querySelectorAll("button[" + attr + "]");
    knoepfe.forEach(function (b) {
      b.addEventListener("click", function () {
        knoepfe.forEach(function (k) { k.setAttribute("aria-pressed", k === b ? "true" : "false"); });
        aufWahl(b.getAttribute(attr));
      });
    });
  }

  /* ---------------------------------------------------------- Skelett erkunden */
  function skelettModell() {
    var box = $("sk"); if (!box) return;
    var info = {};
    document.querySelectorAll(".sk-liste li[data-teil]").forEach(function (li) {
      info[li.getAttribute("data-teil")] = { name: li.querySelector("strong").textContent, text: li.textContent.replace(/^[^:]*:\s*/, "") };
    });
    var teile = box.querySelectorAll(".sk-teil"), titel = $("sk-titel"), erkl = $("sk-erkl"), stand = $("sk-stand");
    var modus = "erkunden", reihe = [], pos = 0, fehler = 0;

    function leeren() { teile.forEach(function (t) { t.classList.remove("aktiv", "richtig", "falsch"); }); }
    function mischen(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
    function frage() {
      if (pos >= reihe.length) {
        titel.textContent = "Geschafft!";
        erkl.textContent = "Du hast alle " + reihe.length + " Knochen gefunden" + (fehler ? " und dich dabei " + fehler + "-mal vertippt." : ", ohne einen einzigen Fehler. Stark!");
        stand.textContent = "Klicke noch einmal auf „Suchspiel“, um neu zu starten.";
        return;
      }
      titel.textContent = "Finde: " + info[reihe[pos]].name;
      erkl.textContent = "Tippe im Skelett auf den passenden Knochen.";
      stand.textContent = "Knochen " + (pos + 1) + " von " + reihe.length + " · Fehler: " + fehler;
    }
    function start(m) {
      modus = m; leeren();
      if (m === "suchen") { reihe = mischen(Object.keys(info)); pos = 0; fehler = 0; frage(); }
      else { titel.textContent = "Tippe auf einen Knochen"; erkl.textContent = "Dann siehst du hier seinen Namen und seine Aufgabe."; stand.textContent = ""; }
    }
    function waehle(t) {
      var k = t.getAttribute("data-teil");
      if (modus === "erkunden") {
        leeren(); t.classList.add("aktiv");
        titel.textContent = info[k].name; erkl.textContent = info[k].text; return;
      }
      if (pos >= reihe.length) return;
      if (k === reihe[pos]) {
        t.classList.remove("falsch"); t.classList.add("richtig"); pos++; frage();
      } else if (!t.classList.contains("richtig")) {
        fehler++; t.classList.add("falsch");
        stand.textContent = "Das war: " + info[k].name + ". Versuch es noch einmal. · Fehler: " + fehler;
        setTimeout(function () { t.classList.remove("falsch"); }, 900);
      }
    }
    teile.forEach(function (t) {
      t.addEventListener("click", function () { waehle(t); });
      t.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); waehle(t); } });
    });
    wahl(box.querySelector(".wahl"), "data-modus", start);
  }

  /* ---------------------------------------------------------- Gelenktypen */
  var GELENKE = {
    kugel: { name: "Kugelgelenk", a: true, b: true, c: true, text: "Der kugelförmige Gelenkkopf liegt in einer runden Pfanne. Er kann sich in alle Richtungen bewegen und sich drehen. Beispiele: Schultergelenk und Hüftgelenk." },
    scharnier: { name: "Scharniergelenk", a: true, b: false, c: false, text: "Eine Walze liegt in einer Rinne, wie bei einem Türscharnier. Das Gelenk kann nur in einer Richtung gebeugt und gestreckt werden. Beispiele: Ellenbogen, Fingergelenke, vor allem auch das Knie." },
    sattel: { name: "Sattelgelenk", a: true, b: true, c: false, text: "Zwei sattelförmige Flächen liegen gekreuzt aufeinander, wie ein Reiter im Sattel. Das Gelenk bewegt sich in zwei Richtungen, kann sich aber kaum drehen. Beispiel: das Daumengelenk an der Handwurzel." },
    dreh: { name: "Drehgelenk", a: false, b: false, c: true, text: "Ein Zapfen dreht sich in einem Ring. Das Gelenk kann nur drehen. Beispiele: zwischen dem 1. und 2. Halswirbel (Kopf drehen) und zwischen Elle und Speiche." }
  };

  function gelenkModell() {
    var box = $("gm"); if (!box) return;
    var bild = $("gm-bild"), ra = $("gm-a"), rb = $("gm-b"), rc = $("gm-c"), typ = "kugel";

    function basis(t, x, y, ansicht) {
      if (t === "kugel") return '<path class="s f-weiss" d="M' + (x - 50) + ' ' + (y + 80) + ' V ' + (y + 10) + ' A 50 50 0 0 0 ' + (x + 50) + ' ' + (y + 10) + ' V ' + (y + 80) + ' Z"/>';
      if (t === "scharnier") return ansicht === "seite"
        ? '<path class="s f-weiss" d="M' + (x - 50) + ' ' + (y + 80) + ' V ' + (y + 6) + ' A 40 40 0 0 0 ' + (x + 50) + ' ' + (y + 6) + ' V ' + (y + 80) + ' Z"/>'
        : '<path class="s f-weiss" d="M' + (x - 70) + ' ' + (y + 80) + ' V ' + (y + 20) + ' H ' + (x + 70) + ' V ' + (y + 80) + ' Z"/>';
      if (t === "sattel") return ansicht === "seite"
        ? '<path class="s f-weiss" d="M' + (x - 55) + ' ' + (y + 80) + ' V ' + (y + 4) + ' C ' + (x - 20) + ' ' + (y + 34) + ' ' + (x + 20) + ' ' + (y + 34) + ' ' + (x + 55) + ' ' + (y + 4) + ' V ' + (y + 80) + ' Z"/>'
        : '<path class="s f-weiss" d="M' + (x - 55) + ' ' + (y + 80) + ' V ' + (y + 30) + ' C ' + (x - 20) + ' ' + (y + 4) + ' ' + (x + 20) + ' ' + (y + 4) + ' ' + (x + 55) + ' ' + (y + 30) + ' V ' + (y + 80) + ' Z"/>';
      return '<rect class="s f-weiss" x="' + (x - 55) + '" y="' + (y + 16) + '" width="110" height="64" rx="8"/><ellipse class="s f-papier" cx="' + x + '" cy="' + (y + 16) + '" rx="26" ry="9"/>';
    }
    function kopf(t, x, y, ansicht) {
      if (t === "kugel") return '<circle class="s f-gelb" cx="' + x + '" cy="' + y + '" r="40"/>';
      if (t === "scharnier") return ansicht === "seite" ? '<circle class="s f-gelb" cx="' + x + '" cy="' + y + '" r="34"/>' : '<rect class="s f-gelb" x="' + (x - 60) + '" y="' + (y - 30) + '" width="120" height="50" rx="22"/>';
      if (t === "sattel") return ansicht === "seite"
        ? '<path class="s f-gelb" d="M' + (x - 44) + ' ' + (y - 4) + ' C ' + (x - 16) + ' ' + (y + 26) + ' ' + (x + 16) + ' ' + (y + 26) + ' ' + (x + 44) + ' ' + (y - 4) + ' L ' + (x + 44) + ' ' + (y - 30) + ' C ' + (x + 16) + ' ' + (y - 4) + ' ' + (x - 16) + ' ' + (y - 4) + ' ' + (x - 44) + ' ' + (y - 30) + ' Z"/>'
        : '<path class="s f-gelb" d="M' + (x - 44) + ' ' + (y + 20) + ' C ' + (x - 16) + ' ' + (y - 4) + ' ' + (x + 16) + ' ' + (y - 4) + ' ' + (x + 44) + ' ' + (y + 20) + ' L ' + (x + 44) + ' ' + (y - 6) + ' C ' + (x + 16) + ' ' + (y - 30) + ' ' + (x - 16) + ' ' + (y - 30) + ' ' + (x - 44) + ' ' + (y - 6) + ' Z"/>';
      return '';
    }
    function ansicht(x, y, winkel, dreh, t, art, beschr) {
      var s = '<g>' + basis(t, x, y, art);
      // Knochen, der sich bewegt
      var rad = winkel * Math.PI / 180, L = 150;
      var ex = x + Math.sin(rad) * L, ey = y - Math.cos(rad) * L;
      s += '<g transform="rotate(' + f(winkel) + ' ' + x + ' ' + y + ')">';
      s += '<rect class="s f-gelb" x="' + (x - 16) + '" y="' + (y - L) + '" width="32" height="' + L + '" rx="10"/>';
      // aufgemalter Streifen zeigt das Drehen
      var off = Math.sin(dreh * Math.PI / 180) * 13, sichtbar = Math.cos(dreh * Math.PI / 180) > -0.2;
      if (art === "seite") { off = Math.sin((dreh + 90) * Math.PI / 180) * 13; sichtbar = Math.cos((dreh + 90) * Math.PI / 180) > -0.2; }
      if (sichtbar) s += '<rect class="f-rosa-tief" x="' + f(x + off - 3) + '" y="' + (y - L + 14) + '" width="6" height="' + (L - 50) + '" rx="3"/>';
      s += '</g>';
      s += kopf(t, x, y, art);
      if (t === "dreh") s += '<rect class="s f-gelb" x="' + (x - 16) + '" y="' + (y - 20) + '" width="32" height="40" rx="6"/>';
      s += '</g>';
      s += text(x, y + 112, beschr, "h");
      return s;
    }
    function zeichnen() {
      var g = GELENKE[typ];
      var a = g.a ? +ra.value : 0, b = g.b ? +rb.value : 0, c = g.c ? +rc.value : 0;
      bild.innerHTML = ansicht(170, 200, b, c, typ, "vorn", "von vorn") + ansicht(470, 200, a, c, typ, "seite", "von der Seite") +
        '<path class="s2 gestrichelt" d="M320 30 V 320"/>';
      var moeglich = [g.a ? "vor und zurück" : null, g.b ? "zur Seite" : null, g.c ? "drehen" : null].filter(Boolean);
      $("gm-hinweis").textContent = "Möglich: " + moeglich.join(", ") + ". " + (moeglich.length < 3 ? "Die anderen Regler sind bei diesem Gelenk gesperrt." : "");
    }
    function setzeTyp(t) {
      typ = t; var g = GELENKE[t];
      [[ra, g.a], [rb, g.b], [rc, g.c]].forEach(function (p) { p[0].disabled = !p[1]; if (!p[1]) p[0].value = 0; p[0].closest(".modell-steuerung").classList.toggle("gesperrt", !p[1]); });
      $("gm-titel").textContent = g.name; $("gm-text").textContent = g.text;
      zeichnen();
    }
    [ra, rb, rc].forEach(function (r) { r.addEventListener("input", zeichnen); });
    wahl(box.querySelector(".wahl"), "data-typ", setzeTyp);
    setzeTyp("kugel");
  }

  /* ---------------------------------------------------------- Armmodell */
  function armModell() {
    var box = $("am"); if (!box) return;
    var bild = $("am-bild"), regler = $("am-w"), last = $("am-last"), alt = +regler.value, richtung = 0;

    function zeichnen() {
      var w = +regler.value;
      if (w < alt) richtung = -1; else if (w > alt) richtung = 1;
      alt = w;
      $("am-w-t").textContent = w + "°";
      var sx = 250, sy = 50, ex = 244, ey = 220;
      var oa = Math.atan2(ey - sy, ex - sx), ua = oa - (180 - w) * Math.PI / 180, L = 170;
      var hx = ex + Math.cos(ua) * L, hy = ey + Math.sin(ua) * L;
      var t = (175 - w) / 135;            // 0 gestreckt … 1 stark gebeugt
      var bzD = 9 + t * 16, tzD = 9 + (1 - t) * 9;
      var bzO = [sx + 14, sy + 8], bzU = [ex + Math.cos(ua) * 38 + Math.cos(ua - Math.PI / 2) * 10, ey + Math.sin(ua) * 38 + Math.sin(ua - Math.PI / 2) * 10];
      var tzO = [sx - 14, sy + 6], tzU = [ex - Math.cos(ua) * 12 - 9, ey - Math.sin(ua) * 12 + 4];
      var bzAktiv = richtung < 0, tzAktiv = richtung > 0;
      var s = '<circle class="s f-gelb-weich" cx="' + sx + '" cy="' + sy + '" r="18"/>';
      s += knochen(sx, sy + 4, ex, ey, 18) + knochen(ex, ey, hx, hy, 14);
      s += '<g transform="translate(' + f(hx) + ' ' + f(hy) + ') rotate(' + f(ua * 180 / Math.PI) + ')"><path class="s f-gelb-weich" d="M2 -14 C 34 -18, 50 -6, 52 4 C 46 14, 22 16, 2 14 Z"/></g>';
      if (last.checked) {
        var bx = hx + Math.cos(ua) * 30, by = hy + Math.sin(ua) * 30;
        s += '<g transform="translate(' + f(bx) + ' ' + f(by) + ')"><rect class="s f-blau" x="-14" y="-10" width="28" height="64" rx="8"/><rect class="s f-weiss" x="-7" y="-20" width="14" height="12" rx="3"/></g>';
      }
      s += muskel(tzO, tzU, tzD, tzAktiv ? "f-rosa-tief" : "f-rosa", 1);
      s += muskel(bzO, bzU, bzD, bzAktiv ? "f-rosa-tief" : "f-rosa", -1);
      s += text(sx - 64, 140, "Trizeps", "h", "end") + text(sx + 70, 110, "Bizeps", "h", "start");
      s += '<path class="s2" fill="none" d="M' + (sx - 60) + ' 134 L ' + (sx - 18) + ' 130 M ' + (sx + 66) + ' 104 L ' + (sx + 22) + ' 112"/>';
      if (richtung) s += text(500, 40, richtung < 0 ? "Beugen" : "Strecken", "h");
      bild.innerHTML = s;

      var txt;
      if (!richtung) txt = "Bewege den Regler, um den Arm zu beugen oder zu strecken.";
      else if (richtung < 0) txt = "Der Arm wird gebeugt. Der Beuger (Bizeps) zieht sich zusammen: Er wird kürzer und dicker und zieht über seine Sehne den Unterarm nach oben. Der Strecker (Trizeps) ist entspannt und wird gedehnt.";
      else txt = "Der Arm wird gestreckt. Jetzt zieht sich der Strecker (Trizeps) zusammen und zieht den Unterarm nach unten. Der Bizeps entspannt sich und wird lang und dünn. Allein könnte er den Arm nicht strecken, denn Muskeln können nur ziehen.";
      if (last.checked) {
        var kraft = Math.round(5 * 8.5 * Math.sin(w * Math.PI / 180) / 5) * 5;
        txt += " Die Flasche wiegt etwa ein halbes Kilogramm und zieht mit etwa 5 Newton nach unten. Der Bizeps setzt etwa 8- bis 9-mal näher am Ellenbogen an als die Hand. Bei " + w + "° muss er deshalb mit ungefähr " + kraft + " Newton ziehen, um die Flasche zu halten.";
      }
      $("am-text").textContent = txt;
    }
    regler.addEventListener("input", zeichnen);
    last.addEventListener("change", zeichnen);
    zeichnen();
  }

  function start() { skelettModell(); gelenkModell(); armModell(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
