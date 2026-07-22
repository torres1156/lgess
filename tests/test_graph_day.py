"""Test für den PV-Tagesverlauf ohne Home Assistant."""

from __future__ import annotations

import importlib.util
import json
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# Dummy-Paketstruktur anlegen, damit relative Importe funktionieren
# ------------------------------------------------------------------

custom_components = types.ModuleType("custom_components")
custom_components.__path__ = [str(ROOT / "custom_components")]

lgess = types.ModuleType("custom_components.lgess")
lgess.__path__ = [str(ROOT / "custom_components" / "lgess")]

sys.modules["custom_components"] = custom_components
sys.modules["custom_components.lgess"] = lgess


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)

    assert spec is not None
    assert spec.loader is not None

    sys.modules[name] = module
    spec.loader.exec_module(module)

    return module


load_module(
    "custom_components.lgess.models",
    ROOT / "custom_components" / "lgess" / "models.py",
)

parser = load_module(
    "custom_components.lgess.parser",
    ROOT / "custom_components" / "lgess" / "parser.py",
)

LGESSParser = parser.LGESSParser


def test_parse_graph_day() -> None:
    """PV-Tageshistorie wird korrekt eingelesen."""

    data = json.loads(
        (ROOT / "tests" / "data" / "graph_day.json").read_text(
            encoding="utf-8"
        )
    )

    graph = LGESSParser.parse_graph_day(data)

    assert len(graph.points) == len(data["loginfo"])

    first = graph.points[0]
    last = graph.points[-1]

    assert first.generation == 0
    assert first.feed_in == 0

    assert last.generation == int(data["loginfo"][-1]["generation"])
    assert last.feed_in == int(data["loginfo"][-1]["feed_in"])
    assert (
        last.total_generation
        == int(data["loginfo"][-1]["total_generation"])
    )
