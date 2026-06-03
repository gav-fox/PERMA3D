import pvlib
from perma3d.adapters.base import BaseAdapter
from perma3d.models import ClimateData


class EPWAdapter(BaseAdapter):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self) -> ClimateData:
        weather_df, metadata = pvlib.iotools.read_epw(self.filepath)

        return ClimateData(
            weather_df=weather_df,
            latitude=float(metadata["latitude"]),
            longitude=float(metadata["longitude"]),
            elevation=float(metadata["altitude"]),
            timezone=str(metadata["TZ"]),
            location_name=f"{metadata['city']}, {metadata['country']}",
        )