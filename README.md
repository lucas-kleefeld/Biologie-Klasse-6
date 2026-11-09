# Biologie Klasse 6

Lernumgebung für den Biologieunterricht in Klasse 6 (Realschule NRW, Kernlehrplan Biologie, erste Progressionsstufe): Lerntexte, druckbare Aufgaben, interaktive Übungen und Modelle. Alle Texte und Zeichnungen sind selbst erstellt. Die Seiten laden nichts von außen und speichern keine Daten.

## Die sechs Reihen

1. **Bewegung und Gesundheit**: Skelett, Knochen, Wirbelsäule, Gelenke, Muskeln, Haltung und Sport *(fertig)*
2. **Herz, Lunge und weitere Organe**: Atmung, Herz und Blutkreislauf *(in Vorbereitung)*
3. **Nahrung und Verdauung**: Nährstoffe, Ernährungspyramide, Verdauung *(in Vorbereitung)*
4. **Pflanzen und Tiere im Jahreslauf**: Fotosynthese, Überwinterung *(in Vorbereitung)*
5. **Sinne und Wahrnehmung**: Auge, Ohr, Haut, Sinne der Tiere *(in Vorbereitung)*
6. **Sexualerziehung**: Pubertät, Geschlechtsorgane, Schwangerschaft *(in Vorbereitung)*

## Reihen freischalten

In `freigabe.json` steht für jede Reihe `true` (sichtbar) oder `false` (gesperrt). Datei auf GitHub bearbeiten, Wert ändern, speichern. Nach etwa zwei Minuten ist die Website aktualisiert. Gesperrte Reihen zeigen nur einen Hinweis, ihre Inhalte werden nicht veröffentlicht.

## Aufbau

- `werkzeug/bauen.py` erzeugt alle Seiten (`cd werkzeug && python3 bauen.py`).
- `werkzeug/reihe1_texte.py`: Lerntexte, `werkzeug/reihe1_rest.py`: Aufgaben, Übungen und Modellseiten, `werkzeug/zeichnungen*.py`: Zeichnungen.
- `assets/uebungen.js`: Übungstypen (Quiz, Zuordnen, Sortieren, Lückentext, Reihenfolge, Schreibtraining). Prüfen und Lösung sind erst möglich, wenn alles bearbeitet ist.
- `assets/reihe1.js`: Modelle der Reihe 1 (Skelett erkunden, Gelenktypen, Beuger und Strecker).
