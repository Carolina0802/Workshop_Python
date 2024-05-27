from abc import ABC, abstractmethod
from typing import List
from domain.entities import DataRecord

class IDataRepository(ABC):
    @abstractmethod
    def read_data(self) -> List[DataRecord]:
        pass

class IDataAdapter(ABC):
    @abstractmethod
    def adapt(self, data: List[dict]) -> List[DataRecord]:
        pass

    @abstractmethod
    def load_csv(self, file_path: str) -> List[dict]:
        pass
