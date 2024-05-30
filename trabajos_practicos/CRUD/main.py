
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
    employees = []

    max_employees = 20
    while True:
        option = get_int(message="1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Filtrar sueldo\n9. Informe sueldo\n10. Salir\n")
        match option:
            case 1:
                new_employee(employees,max_employees)
            case 2:
                update_employee(employees)
            case 3:
                delete_employee(employees)
            case 4:
                show_employees(employees)
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
                salary_report(filter_salary(employees))
            case 9:
                clear_screen()
                break

menu()