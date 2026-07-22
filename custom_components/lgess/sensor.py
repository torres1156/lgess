"""Sensor platform for LG ESS."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import LGESSCoordinator
from .entity import LGESSEntity


@dataclass(frozen=True, kw_only=True)
class LGESSSensorDescription(SensorEntityDescription):
    """LG ESS sensor description."""

    value_fn: Callable[[LGESSCoordinator], Any]


SENSORS: tuple[LGESSSensorDescription, ...] = (
    LGESSSensorDescription(
        key="battery_soc",
        name="Battery SoC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        value_fn=lambda c: c.data.soc,
    ),
    LGESSSensorDescription(
        key="battery_power",
        name="Battery Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.battery_power,
    ),
    LGESSSensorDescription(
        key="battery_power_flow",
        name="Battery Power Flow",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: -c.data.battery_power,
    ),

    LGESSSensorDescription(
        key="battery_status",
        name="Battery Status",
        icon="mdi:battery-heart",
        value_fn=lambda c: c.data.battery_status,
    ),
    LGESSSensorDescription(
        key="pv_power",
        name="PV Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.pv_power,
    ),
    LGESSSensorDescription(
        key="home_load",
        name="Home Load",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.load_power,
    ),
    LGESSSensorDescription(
        key="grid_power",
        name="Grid Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.grid_power,
    ),
    LGESSSensorDescription(
        key="grid_import",
        name="Grid Import",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.grid_import,
    ),
    LGESSSensorDescription(
        key="grid_export",
        name="Grid Export",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda c: c.data.grid_export,
    ),
    LGESSSensorDescription(
        key="pv_generation_today",
        name="PV Generation Today",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_day is None or not c.graph_day.points
            else c.graph_day.points[-1].total_generation / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_feed_in_today",
        name="PV Feed-In Today",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_day is None or not c.graph_day.points
            else c.graph_day.points[-1].total_feed_in / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_direct_consumption_today",
        name="PV Direct Consumption Today",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_day is None or not c.graph_day.points
            else c.graph_day.points[-1].total_direct_consumption / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_generation_week",
        name="PV Generation Week",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_week is None or not c.graph_week.points
            else c.graph_week.points[-1].total_generation / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_feed_in_week",
        name="PV Feed-In Week",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_week is None or not c.graph_week.points
            else c.graph_week.points[-1].total_feed_in / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_direct_consumption_week",
        name="PV Direct Consumption Week",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_week is None or not c.graph_week.points
            else c.graph_week.points[-1].total_direct_consumption / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_generation_month",
        name="PV Generation Month",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_month is None or not c.graph_month.points
            else c.graph_month.points[-1].total_generation / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_feed_in_month",
        name="PV Feed-In Month",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_month is None or not c.graph_month.points
            else c.graph_month.points[-1].total_feed_in / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_direct_consumption_month",
        name="PV Direct Consumption Month",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_month is None or not c.graph_month.points
            else c.graph_month.points[-1].total_direct_consumption / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_generation_year",
        name="PV Generation Year",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_year is None or not c.graph_year.points
            else c.graph_year.points[-1].total_generation / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_feed_in_year",
        name="PV Feed-In Year",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_year is None or not c.graph_year.points
            else c.graph_year.points[-1].total_feed_in / 1000
        ),
    ),
    LGESSSensorDescription(
        key="pv_direct_consumption_year",
        name="PV Direct Consumption Year",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL,
        value_fn=lambda c: (
            None
            if c.graph_year is None or not c.graph_year.points
            else c.graph_year.points[-1].total_direct_consumption / 1000
        ),
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up LG ESS sensors."""

    import logging

    logger = logging.getLogger(__name__)

    logger.warning("LGESS SENSOR: async_setup_entry() gestartet")

    coordinator: LGESSCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities = [LGESSSensor(coordinator, description) for description in SENSORS]

    logger.warning(
        "LGESS SENSOR: async_add_entities() mit %d Sensoren",
        len(entities),
    )

    async_add_entities(entities)

    logger.warning("LGESS SENSOR: async_setup_entry() beendet")


class LGESSSensor(LGESSEntity, SensorEntity):
    """Representation of an LG ESS sensor."""

    entity_description: LGESSSensorDescription

    def __init__(
        self,
        coordinator: LGESSCoordinator,
        description: LGESSSensorDescription,
    ) -> None:
        super().__init__(coordinator)

        self.entity_description = description
        self._attr_unique_id = (
            f"{coordinator.api.unique_id}_{description.key}"
        )
        self._attr_has_entity_name = True

    @property
    def native_value(self):
        """Return sensor value."""
        return self.entity_description.value_fn(self.coordinator)
