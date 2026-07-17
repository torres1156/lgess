"""Basic smoke tests for the LG ESS integration."""

from importlib import import_module


def test_import_integration() -> None:
    """Verify that the integration package can be imported."""

    import_module("custom_components.lgess")
