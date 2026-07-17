"""Tests for the LG ESS config flow."""

from custom_components.lgess.config_flow import LGESSConfigFlow


def test_config_flow_class_exists() -> None:
    """Verify that the config flow class exists."""
    assert LGESSConfigFlow is not None
