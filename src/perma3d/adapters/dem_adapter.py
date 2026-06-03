import rasterio
import numpy as np
from perma3d.adapters.base import BaseAdapter
from perma3d.models import TerrainData 


class DEMAdapter(BaseAdapter):
    
    def load(self, filepath):
        with rasterio.open(filepath) as dataset:
            elevation = dataset.read(1)
            transform = dataset.transform
            crs = dataset.crs
            width = dataset.width
            height = dataset.height
            nodata = dataset.nodata

        return TerrainData(
            elevation=elevation,
            transform=transform,
            crs=crs,
            width=width,
            height=height,
            nodata=nodata,
        ) 
        