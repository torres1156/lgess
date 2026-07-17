# LG ESS Local

A fully local Home Assistant integration for LG ESS systems.

No cloud account is required. Communication takes place directly with the LG ESS over the local network.

---

## Features

- Local communication with LG ESS
- Home Assistant Config Flow
- Automatic device creation
- Real-time sensor updates
- Native Home Assistant device model
- Diagnostics support
- English and German translations
- HACS ready

---

## Supported sensors

- Battery SoC
- Battery Power
- Battery Status
- PV Power
- Home Load
- Grid Power
- Grid Import
- Grid Export

---

## Requirements

- Home Assistant 2026.7 or newer
- LG ESS connected to the local network
- IP address of the ESS

---

## Installation

### Manual

Copy

```
custom_components/lgess
```

into

```
config/custom_components
```

Restart Home Assistant.

Go to:

**Settings → Devices & Services → Add Integration**

Select:

```
LG ESS Local
```

Enter the IP address of the ESS.

---

### HACS

Support is planned.

---

## Roadmap

### Version 0.2.x

- Stable local integration
- Improved diagnostics
- Better logging
- Energy Dashboard support

### Version 0.3.x

- Additional LG ESS sensors
- Battery charge/discharge entities
- Daily energy statistics

### Version 0.4.x

- Services for ESS control (if supported)

### Version 1.0

- Production-ready HACS release
- Complete documentation
- Long-term maintenance

---

## License

MIT License
