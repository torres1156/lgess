"""Shared pytest fixtures."""

import pytest

@pytest.fixture
def sample_host():
    return "192.168.1.10"
