"""Parser for LG ESS API responses."""

from __future__ import annotations

from .models import LGESSData


class LGESSParser:
    """Convert LG ESS JSON responses into internal models."""

    @staticmethod
    def parse(
        home: dict,
        battery: dict,
    ) -> LGESSData:
        """Parse complete LG ESS response."""

        return LGESSData(
            home=home,
            battery=battery,
        )

    @staticmethod
    def as_int(
        value,
        default: int = 0,
    ) -> int:
        """Safely convert to int."""

        try:
            return int(float(value))
        except (TypeError, ValueError):
            return default

    @staticmethod
    def as_float(
        value,
        default: float = 0.0,
    ) -> float:
        """Safely convert to float."""

        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def as_bool(value) -> bool:
        """Convert LG ESS boolean values."""

        if isinstance(value, bool):
            return value

        return str(value).lower() in (
            "1",
            "true",
            "on",
            "yes",
        )
