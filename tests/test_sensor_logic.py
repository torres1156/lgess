"""Tests for LG ESS sensor logic."""

from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

from custom_components.lgess.models import (
    LGESSData,
    LGESSGraphDay,
    LGESSGraphPoint,
)
from custom_components.lgess.sensor import SENSORS


def test_sensor_definitions():
    """Verify that all expected sensors exist."""

    keys = [sensor.key for sensor in SENSORS]

    assert len(keys) == 11

    assert "battery_soc" in keys
    assert "battery_power" in keys
    assert "battery_status" in keys
    assert "pv_power" in keys
    assert "home_load" in keys
    assert "grid_power" in keys
    assert "grid_import" in keys
    assert "grid_export" in keys

    assert "pv_generation_today" in keys
    assert "pv_feed_in_today" in keys
    assert "pv_direct_consumption_today" in keys


def test_graph_day_sensor_values():
    """Verify graph day sensors return kWh values."""

    graph_day = LGESSGraphDay(
        points=[
            LGESSGraphPoint(
                time=datetime(2026, 7, 19, 12, 0),
                generation=250,
                feed_in=100,
                self_consumption=150.0,
                total_generation=12345,
                total_feed_in=4567,
                total_direct_consumption=7778,
            )
        ]
    )

    dummy = SimpleNamespace(
        data=SimpleNamespace(),
        graph_day=graph_day,
    )

    values = {
        sensor.key: sensor.value_fn(dummy)
        for sensor in SENSORS
        if sensor.key.startswith("pv_")
        and sensor.key.endswith("_today")
    }

    assert values["pv_generation_today"] == 12.345
    assert values["pv_feed_in_today"] == 4.567
    assert values["pv_direct_consumption_today"] == 7.778
