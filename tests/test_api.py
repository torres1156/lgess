"""Tests for the LG ESS API."""

from custom_components.lgess.api import LGESSApi


def test_api_class_exists() -> None:
    """Verify that the API class exists."""
    assert LGESSApi is not None
