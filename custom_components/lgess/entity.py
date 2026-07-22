"""Base entity for LG ESS."""

from __future__ import annotations

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .coordinator import LGESSCoordinator
from .device import get_device_info


class LGESSEntity(CoordinatorEntity[LGESSCoordinator]):
    """Base class for all LG ESS entities."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: LGESSCoordinator) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)

    @property
    def device_info(self):
        """Return device information."""
        return get_device_info(self.coordinator)

    @property
    def available(self) -> bool:
        """Return whether the entity is available."""
        return self.coordinator.last_update_success
