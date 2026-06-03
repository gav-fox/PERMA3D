from dataclasses import dataclass
from typing import Optional
import pandas as pd
import numpy as np



@dataclass
class TerrainData:
    elevation: np.ndarray
    transform: object
    crs: object
    width: int
    height: int
    nodata: Optional[float]


@dataclass
class ClimateData:
    weather_df: pd.DataFrame
    latitude: float
    longitude: float
    elevation: float
    timezone: str
    location_name: str