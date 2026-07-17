"""Sensor platform for LG ESS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfPower,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import LGESSCoordinator
from .entity import LGESSEntity
from .models import LGESSData


@dataclass(frozen=True, kw_only=True)
class LGESSSensorDescription(SensorEntityDescription):
    """LG ESS sensor description."""

    value_fn: Callable[[LGESSData], Any]


SENSORS: tuple[LGESSSensorDescription, ...] = (

    LGESSSensorDescription(
        key="battery_soc",
        name="Battery SoC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        value_fn=lambda d: d.soc,
    ),

    LGESSSensorDescription(
        key="battery_power",
        name="Battery Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.battery_power,
    ),

    LGESSSensorDescription(
        key="battery_status",
        name="Battery Status",
        icon="mdi:battery-heart",
        value_fn=lambda d: d.battery_status,
    ),

    LGESSSensorDescription(
        key="pv_power",
        name="PV Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.pv_power,
    ),

    LGESSSensorDescription(
        key="home_load",
        name="Home Load",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.load_power,
    ),

    LGESSSensorDescription(
        key="grid_power",
        name="Grid Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.grid_power,
    ),

    LGESSSensorDescription(
        key="grid_import",
        name="Grid Import",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.grid_import,
    ),

    LGESSSensorDescription(
        key="grid_export",
        name="Grid Export",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda d: d.grid_export,
    ),

)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up LG ESS sensors."""

    coordinator: LGESSCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        LGESSSensor(coordinator, description)
        for description in SENSORS
    )


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
        return self.entity_description.value_fn(
            self.coordinator.data
        )