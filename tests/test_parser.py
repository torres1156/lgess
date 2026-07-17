"""Unit tests for parser helpers."""

from custom_components.lgess.parser import LGESSParser


def test_as_int() -> None:
    """Test integer conversion."""
    assert LGESSParser.as_int("42") == 42
    assert LGESSParser.as_int(None) == 0


def test_as_float() -> None:
    """Test float conversion."""
    assert LGESSParser.as_float("3.14") == 3.14
    assert LGESSParser.as_float(None) == 0.0


def test_as_bool() -> None:
    """Test boolean conversion."""
    assert LGESSParser.as_bool(True) is True
    assert LGESSParser.as_bool(False) is False
    assert LGESSParser.as_bool(1) is True
    assert LGESSParser.as_bool(0) is False
