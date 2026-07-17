"""Shared pytest fixtures."""

import pytest


@pytest.fixture
def sample_host() -> str:
    """Return a sample LG ESS host."""
    return "192.168.1.10"
