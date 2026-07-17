"""LG ESS device information."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, MANUFACTURER
from .coordinator import LGESSCoordinator


def get_device_info(
    coordinator: LGESSCoordinator,
) -> DeviceInfo:
    """Return Home Assistant device information."""

    return DeviceInfo(
        identifiers={
            (
                DOMAIN,
                coordinator.api.unique_id,
            )
        },
        manufacturer=MANUFACTURER,
        model="ESS",
        name="LG ESS",
        configuration_url=f"https://{coordinator.api.host}",
        sw_version="Local API",
    )
