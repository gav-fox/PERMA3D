import pytest
from pathlib import Path
from perma3d.adapters.dem_adapter import DEMAdapter
from perma3d.models import TerrainData


def test_dem_adapter_returns_terrain_data():
    filepath = Path("data/TL00.asc")
    adapter = DEMAdapter()
    result = adapter.load(filepath)
    assert isinstance(result, TerrainData)


def test_dem_adapter_elevation_not_empty():
    filepath = Path("data/TL00.asc")
    adapter = DEMAdapter()
    result = adapter.load(filepath)
    assert result.elevation.size > 0
