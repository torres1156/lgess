# Changelog

All notable changes to this project are documented in this file.

## [0.2.0] - 2026-07-21

### Added
- Local Home Assistant integration for LG ESS.
- Config Flow for UI-based setup.
- Automatic device creation.
- Diagnostics support.
- English and German translations.
- Home Assistant Energy Dashboard support.
- Day, Week, Month and Year energy statistics.
- New graph API support for:
  - Day
  - Week
  - Month
  - Year
- New energy sensors for:
  - PV Generation
  - Direct Consumption
  - Grid Feed-In
- New `battery_power_flow` sensor for Power Flow Card Plus.

### Changed
- Extended API, parser, models and coordinator for historical energy data.
- Improved sensor structure and entity handling.
- Updated documentation for version 0.2.0.

### Fixed
- Correct battery power direction for Power Flow Card Plus using a dedicated flow sensor.
- Various parser and coordinator improvements.
- Minor stability and logging fixes.

## [0.1.0] - 2026-07-16

### Added
- Initial prototype.
- Local communication with LG ESS.
