"""Coordinator for LG ESS."""

from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import LGESSApi, LGESSApiError
from .models import LGESSData

_LOGGER = logging.getLogger(__name__)

UPDATE_INTERVAL = timedelta(seconds=10)


class LGESSCoordinator(DataUpdateCoordinator[LGESSData]):
    """Coordinate LG ESS updates."""

    def __init__(
        self,
        hass: HomeAssistant,
        host: str,
        password: str,
    ) -> None:
        self.api = LGESSApi(
            async_get_clientsession(hass),
            host,
            password,
        )

        super().__init__(
            hass,
            _LOGGER,
            name="LG ESS",
            update_interval=UPDATE_INTERVAL,
        )

    async def _async_update_data(self) -> LGESSData:
        """Fetch the latest data."""

        try:
            home = await self.api.async_get_home()
            battery = await self.api.async_get_battery()

            return LGESSData(
                home=home,
                battery=battery,
            )

        except LGESSApiError as err:
            raise UpdateFailed(
                f"LG ESS communication failed: {err}"
            ) from err
