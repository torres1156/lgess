from custom_components.lgess.models import LGESSData


def test_statistics_property_exists():
    assert hasattr(LGESSData, "statistics")
