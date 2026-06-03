from dataclasses import dataclass
import numpy as np



@dataclass
class TerrainData:
    elevation: np.ndarray
    transform: object
    crs: object
    width: int
    height: int
    nodata: float