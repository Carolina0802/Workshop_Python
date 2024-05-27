from typing import List
from application.interfaces.mapper_config_repository import IDataRepository, IDataAdapter
from domain.entities import DataRecord

class CSVRepository(IDataRepository):
    def __init__(self, adapter: IDataAdapter, file_path: str):
        self.adapter = adapter
        self.file_path = file_path

    def read_data(self) -> List[DataRecord]:
        raw_data = self.adapter.load_csv(self.file_path)
        return self.adapter.adapt(raw_data)
