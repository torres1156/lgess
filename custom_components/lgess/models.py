"""LG ESS data models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from datetime import datetime


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
    def soc(self) -> float:
        """Battery state of charge (%)."""
        return self.energy("bat_user_soc")

    @property
    def pv_power(self) -> int:
        """Current PV power (W)."""
        return self.power("pcs_pv_total_power")

    @property
    def load_power(self) -> int:
        """Current house load (W)."""
        return self.power("load_power")

    @property
    def grid_power(self) -> int:
        """Current grid power (W)."""
        return self.power("grid_power")

    @property
    def pv_generation_today(self) -> float:
        """Today's PV generation."""
        return self.energy("current_pv_generation_sum")

    @property
    def pv_feed_in_today(self) -> float:
        """Today's grid feed-in."""
        return self.energy("current_grid_feed_in_energy")

    @property
    def pv_direct_consumption_today(self) -> float:
        """Today's direct self-consumption."""
        return self.energy("current_day_self_consumption")

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


@dataclass(slots=True)
class LGESSGraphPoint:
    """Ein 15-Minuten-Datenpunkt der PV-Tageshistorie."""

    time: datetime
    generation: int
    feed_in: int
    self_consumption: float
    total_generation: int
    total_feed_in: int
    total_direct_consumption: int


@dataclass(slots=True)
class LGESSGraphDay:
    """PV-Tageshistorie."""

    points: list[LGESSGraphPoint]


@dataclass(slots=True)
class LGESSGraphWeek:
    """PV-Wochenhistorie."""

    points: list[LGESSGraphPoint]


@dataclass(slots=True)
class LGESSGraphMonth:
    """PV-Monatshistorie."""

    points: list[LGESSGraphPoint]


@dataclass(slots=True)
class LGESSGraphYear:
    """PV-Jahreshistorie."""

    points: list[LGESSGraphPoint]
