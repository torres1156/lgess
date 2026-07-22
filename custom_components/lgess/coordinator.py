"""Coordinator for LG ESS."""

from __future__ import annotations

import logging
from datetime import date, datetime, timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import LGESSApi, LGESSApiError
from .models import (
    LGESSData,
    LGESSGraphDay,
    LGESSGraphWeek,
    LGESSGraphMonth,
    LGESSGraphYear,
)
from .parser import LGESSParser

_LOGGER = logging.getLogger(__name__)

UPDATE_INTERVAL = timedelta(seconds=10)
GRAPH_UPDATE_INTERVAL = timedelta(minutes=5)


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

        self.graph_day: LGESSGraphDay | None = None
        self.graph_week: LGESSGraphWeek | None = None
        self.graph_month: LGESSGraphMonth | None = None
        self.graph_year: LGESSGraphYear | None = None
        self._graph_dates = {
            "day": None,
            "week": None,
            "month": None,
            "year": None,
        }

        self._graph_updated = {
            "day": None,
            "week": None,
            "month": None,
            "year": None,
        }

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

            today = date.today()
            now = datetime.now()

            if (
                self.graph_day is None
                or self._graph_dates["day"] != today
                or self._graph_updated["day"] is None
                or now - self._graph_updated["day"] >= GRAPH_UPDATE_INTERVAL
            ):
                graph = await self.api.async_get_graph_day(today)
                self.graph_day = LGESSParser.parse_graph_day(graph)
                self._graph_dates["day"] = today
                self._graph_updated["day"] = now

            if (
                self.graph_week is None
                or self._graph_dates["week"] != today
                or self._graph_updated["week"] is None
                or now - self._graph_updated["week"] >= GRAPH_UPDATE_INTERVAL
            ):
                graph = await self.api.async_get_graph_week(today)
                self.graph_week = LGESSParser.parse_graph_week(graph)
                self._graph_dates["week"] = today
                self._graph_updated["week"] = now

            if (
                self.graph_month is None
                or self._graph_dates["month"] != today
                or self._graph_updated["month"] is None
                or now - self._graph_updated["month"] >= GRAPH_UPDATE_INTERVAL
            ):
                graph = await self.api.async_get_graph_month(today)
                self.graph_month = LGESSParser.parse_graph_month(graph)
                self._graph_dates["month"] = today
                self._graph_updated["month"] = now

            if (
                self.graph_year is None
                or self._graph_dates["year"] != today
                or self._graph_updated["year"] is None
                or now - self._graph_updated["year"] >= GRAPH_UPDATE_INTERVAL
            ):
                graph = await self.api.async_get_graph_year(today)
                self.graph_year = LGESSParser.parse_graph_year(graph)
                self._graph_dates["year"] = today
                self._graph_updated["year"] = now


            return LGESSData(
                home=home,
                battery=battery,
            )

        except LGESSApiError as err:
            raise UpdateFailed(
                f"LG ESS communication failed: {err}"
            ) from err
