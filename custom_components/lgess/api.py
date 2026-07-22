"""Async LG ESS local API."""

from __future__ import annotations

from datetime import date
from typing import Any

from aiohttp import ClientError, ClientSession


class LGESSApiError(Exception):
    """Base API error."""


class LGESSAuthenticationError(LGESSApiError):
    """Authentication failed."""


class LGESSApi:
    """LG ESS local API."""

    def __init__(
        self,
        session: ClientSession,
        host: str,
        password: str,
    ) -> None:
        self._session = session
        self._host = host
        self._password = password
        self._auth_key: str | None = None

    @property
    def host(self) -> str:
        return self._host

    @property
    def unique_id(self) -> str:
        return self._host

    @property
    def base_url(self) -> str:
        return f"https://{self._host}"

    async def _login(self) -> None:
        try:
            async with self._session.put(
                f"{self.base_url}/v1/login",
                ssl=False,
                json={"password": self._password},
                timeout=10,
            ) as response:
                response.raise_for_status()
                data = await response.json()
        except ClientError as err:
            raise LGESSApiError(err) from err

        if data.get("status") != "success":
            raise LGESSAuthenticationError()

        self._auth_key = data["auth_key"]

    async def _request(
        self,
        endpoint: str,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if self._auth_key is None:
            await self._login()

        body = {"auth_key": self._auth_key}

        if payload:
            body.update(payload)

        try:
            async with self._session.post(
                self.base_url + endpoint,
                ssl=False,
                json=body,
                timeout=10,
            ) as response:
                response.raise_for_status()
                data = await response.json()
        except ClientError as err:
            raise LGESSApiError(err) from err

        if data.get("auth") == "auth_key failed":
            self._auth_key = None
            await self._login()
            return await self._request(endpoint, payload)

        return data

    async def async_get_home(self) -> dict[str, Any]:
        return await self._request("/v1/user/essinfo/home")

    async def async_get_battery(self) -> dict[str, Any]:
        return await self._request("/v1/user/setting/batt")

    async def async_get_graph_day(
        self,
        day: date,
    ) -> dict[str, Any]:
        return await self._request(
            "/v1/user/graph/pv/day",
            {"year_month_day": day.strftime("%Y%m%d")},
        )

    async def async_get_graph_week(
        self,
        day: date,
    ) -> dict[str, Any]:
        return await self._request(
            "/v1/user/graph/pv/week",
            {"year_month_day": day.strftime("%Y%m%d")},
        )

    async def async_get_graph_month(
        self,
        day: date,
    ) -> dict[str, Any]:
        return await self._request(
            "/v1/user/graph/pv/month",
            {"year_month": day.strftime("%Y%m")},
        )

    async def async_get_graph_year(
        self,
        day: date,
    ) -> dict[str, Any]:
        return await self._request(
            "/v1/user/graph/pv/year",
            {"year": day.strftime("%Y")},
        )
