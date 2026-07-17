"""Config flow for LG ESS."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from aiohttp import ClientSession
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PASSWORD
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import (
    LGESSApi,
    LGESSApiError,
    LGESSAuthenticationError,
)
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class LGESSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ):
        """Handle the initial step."""

        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                session: ClientSession = async_get_clientsession(self.hass)

                api = LGESSApi(
                    session=session,
                    host=user_input[CONF_HOST],
                    password=user_input[CONF_PASSWORD],
                )

                await api.login()

            except LGESSAuthenticationError:
                errors["base"] = "invalid_auth"

            except LGESSApiError:
                errors["base"] = "cannot_connect"

            except Exception:  # noqa: BLE001
                _LOGGER.exception("Unexpected exception during config flow")
                errors["base"] = "unknown"

            else:
                await self.async_set_unique_id(user_input[CONF_HOST])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"LG ESS ({user_input[CONF_HOST]})",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )
