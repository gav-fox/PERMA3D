from abc import ABC, abstractmethod
from perma3d.models import TerrainData


class BaseAdapter(ABC):

    @abstractmethod
    def load(self, filepath: str) -> TerrainData
        pass
    