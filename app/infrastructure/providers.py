from infrastructure.adapters.csv_adapter import CSVAdapter
from infrastructure.repositories.csv_repository import CSVRepository
from application.services.service import CSVService

def configure_dependencies(file_path: str):
    # Crear el adaptador
    adapter = CSVAdapter()
    
    # Crear el repositorio con el adaptador inyectado
    repository = CSVRepository(adapter, file_path)
    
    # Crear el servicio con el repositorio inyectado
    service = CSVService(repository)
    
    return service
