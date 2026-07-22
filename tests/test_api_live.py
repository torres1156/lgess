"""Live test against a real LG ESS."""

from __future__ import annotations

import json
import os
from datetime import date

import aiohttp
import pytest

from custom_components.lgess.api import LGESSApi


@pytest.mark.asyncio
async def test_graph_day_live() -> None:
    """Read graph/day from a real LG ESS."""

    host = os.environ["LGESS_HOST"]
    password = os.environ["LGESS_PASSWORD"]

    async with aiohttp.ClientSession() as session:
        api = LGESSApi(session, host, password)

        data = await api.async_get_graph_day(date.today())

        print("\n=== GRAPH DAY RESPONSE ===")
        print(json.dumps(data, indent=2, sort_keys=True))
        print("==========================\n")

        assert isinstance(data, dict)
