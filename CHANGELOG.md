# Changelog

Alle wesentlichen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

## [0.2.0] - 2026-07-17

### Added
- Erste lauffähige Home-Assistant-Integration für LG ESS.
- Config Flow zur Einrichtung über die Benutzeroberfläche.
- Lokale Kommunikation mit dem ESS.
- Automatische Geräteerkennung.
- Live-Sensoren:
  - Battery Power
  - Battery SoC
  - Battery Status
  - Grid Export
  - Grid Import
  - Grid Power
  - Home Load
  - PV Power
- Deutsche und englische Übersetzungen.
- Geräteinformationen und Diagnoseschnittstelle.
- Grundlegende Testumgebung.

### Changed
- Projektstruktur für HACS und GitHub vorbereitet.
- Dokumentation überarbeitet.
- Entity- und Geräteverwaltung bereinigt.
- Verbesserte Parser- und Coordinator-Struktur.

### Fixed
- Korrekte Gerätezuordnung der Entitäten.
- Unterstützung für Dataclasses mit `slots=True`.
- Diverse kleinere Fehler im Config Flow und in der Diagnosefunktion.

## [0.1.0] - 2026-07-16

### Added
- Erster interner Prototyp.
- Grundlegende Kommunikation mit dem LG ESS.
