"""LG ESS data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class LGESSData:
    """Complete LG ESS state."""

    home: dict[str, Any]
    battery: dict[str, Any]

    @property
    def statistics(self) -> dict[str, Any]:
        """Return statistics section."""
        return self.home.get("statistics", {})

    @property
    def direction(self) -> dict[str, Any]:
        """Return direction section."""
        return self.home.get("direction", {})

    @property
    def operation(self) -> dict[str, Any]:
        """Return operation section."""
        return self.home.get("operation", {})

    def statistic(self, key: str, default: Any = 0) -> Any:
        """Return a statistic value."""
        return self.statistics.get(key, default)

    def direction_flag(self, key: str) -> bool:
        """Return a direction flag.

        Supports both firmware variants:

            is_grid_buying
            is_grid_buying_
        """

        value = self.direction.get(key)

        if value is None:
            value = self.direction.get(f"{key}_")

        return str(value) == "1"

    def operation_value(self, key: str, default: Any = None) -> Any:
        """Return an operation value."""
        return self.operation.get(key, default)

    def power(self, key: str) -> int:
        """Return a power value in W."""

        try:
            return int(self.statistic(key, 0))
        except (TypeError, ValueError):
            return 0

    def energy(self, key: str) -> float:
        """Return an energy value in kWh."""

        try:
            return float(self.statistic(key, 0))
        except (TypeError, ValueError):
            return 0.0

    @property
    def battery_status(self) -> str:
        """Return battery status."""

        if self.direction_flag("is_battery_charging"):
            return "Charging"

        if self.direction_flag("is_battery_discharging"):
            return "Discharging"

        return "Idle"

    @property
    def battery_power(self) -> int:
        """Return signed battery power."""

        power = self.power("batconv_power")

        if self.direction_flag("is_battery_discharging"):
            return -power

        return power

    @property
    def grid_import(self) -> int:
        """Return grid import power."""

        if self.direction_flag("is_grid_buying"):
            return self.power("grid_power")

        return 0

    @property
    def grid_export(self) -> int:
        """Return grid export power."""

        if self.direction_flag("is_grid_selling"):
            return self.power("grid_power")

        return 0