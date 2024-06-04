
"""
Nombre: Federico
Apellido: Deniard
"""
from Packages.Package_Input.Input import *
from trabajos_practicos.CRUD.Package_crud.read import *
from trabajos_practicos.CRUD.Package_crud.update import *
from trabajos_practicos.CRUD.Package_crud.delete import *
from trabajos_practicos.CRUD.Package_crud.create import *

def menu():
    employees = fetch_employees('trabajos_practicos/CRUD/empleados.csv')
    deleted_employees = fetch_deleted('trabajos_practicos/CRUD/deleted.json')
    config = get_config('trabajos_practicos/CRUD/config.json')
    last_id = [config["last_id"]]
    last_report = [config["last_report"]]

    max_employees = 20
    while True:
        option = get_int(message="1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Filtrar sueldo\n9. Reporte apellido\n10. Salir\n",min=1,max=10)
        match option:
            case 1:
                new_employee(employees,max_employees,last_id)
            case 2:
                update_employee(employees)
            case 3:
                delete_employee(employees,deleted_employees)
            case 4:
                print(show_employees(employees))
                input("Presione una tecla para continuar...")
            case 5:
                clear_screen()
                print(f"El salario promedio es de: {get_average_salary(employees)}")
                input("Presione una tecla para continuar...")
                clear_screen()
            case 6:
                search_dni(employees)
            case 7:
                sort_array(employees)
            case 8:
                salary_report(filter_salary(employees),last_report)
            case 9:
                salary_report(filter_lastname(employees),last_report)

            case 10:
                clear_screen()
                save_employees(employees,'trabajos_practicos/CRUD/empleados.csv')
                save_deleted_employees(deleted_employees,'trabajos_practicos/CRUD/deleted.json')
                save_config('trabajos_practicos/CRUD/config.json',{"last_id": last_id,"last_report":last_report})
                break

menu()