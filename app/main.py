from infrastructure.providers import configure_dependencies

def main():
    csv_file_path = 'resources/data.csv'
    
    # Configurar dependencias y obtener el servicio
    service = configure_dependencies(csv_file_path)
    
    # Usar el servicio para obtener y mostrar los datos
    data = service.get_data()
    for record in data:
        print(record.name, record.age, record.balance, record.is_active, record.join_date)

if __name__ == '__main__':
    main()
