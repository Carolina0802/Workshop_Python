import csv
from typing import List
from application.interfaces.mapper_config_repository import IDataAdapter
from domain.entities import DataRecord

class CSVAdapter(IDataAdapter):
    def adapt(self, data: List[dict]) -> List[DataRecord]:
        return [DataRecord(
            name=item['name'],
            age=int(item['age']),
            balance=float(item['balance']),
            is_active=item['is_active'].lower() in ['true', '1', 'yes'],
            join_date=item['join_date']
        ) for item in data]

    def load_csv(self, file_path: str) -> List[dict]:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
