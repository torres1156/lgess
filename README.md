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
- Home Assistant Energy Dashboard support
- Day / Week / Month / Year energy statistics
- Power Flow Card Plus support

---

## Supported sensors

### Live sensors

- Battery SoC
- Battery Power
- Battery Power Flow
- Battery Status
- PV Power
- Home Load
- Grid Power
- Grid Import
- Grid Export

### Energy statistics

- PV Generation (Day / Week / Month / Year)
- Direct Consumption (Day / Week / Month / Year)
- Grid Feed-In (Day / Week / Month / Year)

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

## Power Flow Card Plus

For the battery entity use:

```
sensor.lg_ess_battery_power_flow
```

This sensor uses the sign convention expected by Power Flow Card Plus.
The original `sensor.lg_ess_battery_power` sensor remains unchanged and
provides the raw battery power reported by the LG ESS.

---

## Roadmap

### Version 0.3.x

- Additional LG ESS sensors
- Services for ESS control (if supported)

### Version 1.0

- Production-ready HACS release
- Complete documentation
- Long-term maintenance

---

## License

MIT License
