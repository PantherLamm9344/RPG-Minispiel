# RPG-Minispiel
Mit Python erstellte ich ein RPG Minispiel. Erkunde eine Mysteriöse Fantasy Welt und triff auf Verschiedenste Monster inklusive Loot.

# 🐉 Python Text-RPG: Fantasy World

## 📌 Projektübersicht
Ein modulares, textbasiertes Rollenspiel (RPG), das vollständig in Python als Konsolenanwendung entwickelt wurde. In dieser Simulation können Spieler eine Fantasy-Welt erkunden, strategische rundenbasierte Kämpfe führen, Ressourcen verwalten und mit verschiedenen NPCs handeln.

Dieses Projekt dient als praktischer Nachweis für fortgeschrittene Python-Kenntnisse, insbesondere im Bereich der **Softwarearchitektur**, des **State Managements** und der **logischen Strukturierung** von Backend-Prozessen.

---

## 🛠️ Technische Architektur (Separation of Concerns)

Das absolute Kernmerkmal dieses Projekts ist die strikte modulare Aufteilung. Anstatt die gesamte Logik monolithisch zu verwalten, ist das System in spezialisierte Skripte und Klassen unterteilt. Dies sorgt für hohe Skalierbarkeit und leichte Wartbarkeit des Codes.

**Die Struktur umfasst unter anderem:**
*   `/Scripts/Funktionen/`: Ausgelagerte Kernlogik (Berechnungen, Kampfsystem, Reisen, Menüsteuerung).
*   `/Scripts/Spieler/`: Verwaltung von Inventar, Ausrüstung und dynamischen Charakterwerten.
*   `/Scripts/Händler/`: Individuelle Handelslogiken für verschiedene NPCs (Emmil, Horus, Kastor).
*   `/Scripts/Gegner/ & /Gebiete/`: Modulare Datensätze zur Generierung der Spielwelt und Feinde.

---

## 🚀 Kern-Features
*   **Komplexes Kampfsystem:** Rundenbasierte Begegnungen mit dynamischer Schadensberechnung unter Einbezug von Charakterwerten, Ausrüstung und gegnerischen Stats.
*   **Wirtschafts- & Inventarsystem:** Ein vollständiges Array-basiertes Inventarsystem, das Ausrüstung, Tränke und Landkarten verwaltet. Spieler können Beute (Loot) sammeln und bei dedizierten Händlern verkaufen.
*   **Dynamische Welterkundung:** Verschiedene Gebiete mit ansteigendem Schwierigkeitsgrad und spezifischen Begegnungen.
*   **User Experience (UX):** Integriertes Screen-Clearing und strukturierte Konsolen-Menüs für eine saubere und übersichtliche Navigation.

---

## 💻 Lokale Ausführung

Da es sich um eine native Konsolenanwendung handelt, wird das Spiel direkt über das Terminal (Kommandozeile) gestartet. Es werden keine externen Bibliotheken benötigt (Zero Dependencies).

**Voraussetzungen:** 
*   Python 3.x

**Starten des Spiels:**
1. Lade dieses Repository herunter oder klone es via Git.
2. Öffne ein Terminal / Command Prompt im Hauptverzeichnis des Projekts.
3. Führe die Startdatei aus:
```bash
   python RPGminispiel.py

Copyright & Lizenz
Alle Rechte vorbehalten. Die Nutzung, Vervielfältigung oder Weiterverarbeitung dieses Codes ist ohne vorherige ausdrückliche Zustimmung nicht gestattet. Bei Interesse an einer Nutzung kontaktiere mich bitte direkt.
