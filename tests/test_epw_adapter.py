import pytest
from perma3d.adapters.epw_adapter import EPWAdapter
from perma3d.models import ClimateData


def test_epw_loads_climate_data(epw_file):
    adapter = EPWAdapter(epw_file)
    result = adapter.load()

    assert isinstance(result, ClimateData)


def test_epw_has_8760_rows(epw_file):
    adapter = EPWAdapter(epw_file)
    result = adapter.load()

    assert len(result.weather_df) == 8760


def test_epw_location_metadata(epw_file):
    adapter = EPWAdapter(epw_file)
    result = adapter.load()

    assert isinstance(result.latitude, float)
    assert isinstance(result.longitude, float)
    assert isinstance(result.location_name, str)
    assert len(result.location_name) > 0


@pytest.fixture
def epw_file():
    return "data/GBR_ENG_Chenies.AUTO.036740_TMYx.epw"