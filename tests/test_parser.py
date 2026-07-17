"""Unit tests for parser helpers."""

from custom_components.lgess.parser import as_bool, as_float, as_int


def test_as_int() -> None:
    assert as_int("42") == 42
    assert as_int(None) == 0


def test_as_float() -> None:
    assert as_float("3.14") == 3.14
    assert as_float(None) == 0.0


def test_as_bool() -> None:
    assert as_bool(True) is True
    assert as_bool(False) is False
    assert as_bool(1) is True
    assert as_bool(0) is False
