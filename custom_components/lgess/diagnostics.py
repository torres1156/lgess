"""Diagnostics support for LG ESS."""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry

from .const import DOMAIN

TO_REDACT = {
    "auth_key",
    "password",
    "installer_password",
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: ConfigEntry,
    device: DeviceEntry | None = None,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""

    coordinator = hass.data[DOMAIN][entry.entry_id]

    return {
        "entry": async_redact_data(dict(entry.data), TO_REDACT),
        "data": async_redact_data(
            {
                "home": coordinator.data.home,
                "battery": coordinator.data.battery,
            },
            TO_REDACT,
        ),
    }
