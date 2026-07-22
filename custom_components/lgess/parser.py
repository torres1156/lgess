"""Parser for LG ESS API responses."""

from __future__ import annotations

from datetime import datetime

from .models import (
    LGESSData,
    LGESSGraphDay,
    LGESSGraphWeek,
    LGESSGraphMonth,
    LGESSGraphYear,
    LGESSGraphPoint,
)


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
    def parse_graph_day(data: dict) -> LGESSGraphDay:
        """Parse PV day history."""

        points: list[LGESSGraphPoint] = []

        for item in data.get("loginfo", []):
            points.append(
                LGESSGraphPoint(
                    time=datetime.strptime(
                        item["time"],
                        "%Y%m%d%H%M%S",
                    ),
                    generation=LGESSParser.as_int(item.get("generation")),
                    feed_in=LGESSParser.as_int(item.get("feed_in")),
                    self_consumption=LGESSParser.as_float(
                        item.get("self_consum")
                    ),
                    total_generation=LGESSParser.as_int(
                        item.get("total_generation")
                    ),
                    total_feed_in=LGESSParser.as_int(
                        item.get("total_Feed_in")
                    ),
                    total_direct_consumption=LGESSParser.as_int(
                        item.get("total_pv_direct_consumption_energy")
                    ),
                )
            )

        return LGESSGraphDay(points=points)

    @staticmethod
    def parse_graph_week(data: dict) -> LGESSGraphWeek:
        """Parse PV week history."""

        points: list[LGESSGraphPoint] = []

        for item in data.get("loginfo", []):
            points.append(
                LGESSGraphPoint(
                    time=datetime.strptime(
                        item["time"],
                        "%Y%m%d%H%M%S",
                    ),
                    generation=LGESSParser.as_int(item.get("generation")),
                    feed_in=LGESSParser.as_int(item.get("feed_in")),
                    self_consumption=LGESSParser.as_float(
                        item.get("self_consum")
                    ),
                    total_generation=LGESSParser.as_int(
                        item.get("total_generation")
                    ),
                    total_feed_in=LGESSParser.as_int(
                        item.get("total_Feed_in")
                    ),
                    total_direct_consumption=LGESSParser.as_int(
                        item.get("total_pv_direct_consumption_energy")
                    ),
                )
            )

        return LGESSGraphWeek(points=points)

    @staticmethod
    def parse_graph_month(data: dict) -> LGESSGraphMonth:
        """Parse PV month history."""

        points: list[LGESSGraphPoint] = []

        for item in data.get("loginfo", []):
            points.append(
                LGESSGraphPoint(
                    time=datetime.strptime(
                        item["time"],
                        "%Y%m%d%H%M%S",
                    ),
                    generation=LGESSParser.as_int(item.get("generation")),
                    feed_in=LGESSParser.as_int(item.get("feed_in")),
                    self_consumption=LGESSParser.as_float(
                        item.get("self_consum")
                    ),
                    total_generation=LGESSParser.as_int(
                        item.get("total_generation")
                    ),
                    total_feed_in=LGESSParser.as_int(
                        item.get("total_Feed_in")
                    ),
                    total_direct_consumption=LGESSParser.as_int(
                        item.get("total_pv_direct_consumption_energy")
                    ),
                )
            )

        return LGESSGraphMonth(points=points)

    @staticmethod
    def parse_graph_year(data: dict) -> LGESSGraphYear:
        """Parse PV year history."""

        points: list[LGESSGraphPoint] = []

        for item in data.get("loginfo", []):
            points.append(
                LGESSGraphPoint(
                    time=datetime.strptime(
                        item["time"],
                        "%Y%m%d%H%M%S",
                    ),
                    generation=LGESSParser.as_int(item.get("generation")),
                    feed_in=LGESSParser.as_int(item.get("feed_in")),
                    self_consumption=LGESSParser.as_float(
                        item.get("self_consum")
                    ),
                    total_generation=LGESSParser.as_int(
                        item.get("total_generation")
                    ),
                    total_feed_in=LGESSParser.as_int(
                        item.get("total_Feed_in")
                    ),
                    total_direct_consumption=LGESSParser.as_int(
                        item.get("total_pv_direct_consumption_energy")
                    ),
                )
            )

        return LGESSGraphYear(points=points)

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
