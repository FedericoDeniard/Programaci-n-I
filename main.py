from Packages.Package_Input.Input import *
from trabajos_practicos.CRUD.Package_crud.read import *
from trabajos_practicos.CRUD.Package_crud.update import *
from trabajos_practicos.CRUD.Package_crud.delete import *
from trabajos_practicos.CRUD.Package_crud.create import *




"""
ID : Incremental
Nombre
Apellido
DNI
Puesto
Salario
"""

def menu():
    employees = [
    {
        "id": 1,
        "name": "John",
        "lastname": "Doe",
        "dni": 5461247,
        "position": "Gerente",
        "salary": 500000
    },
    {
        "id": 2,
        "name": "Jane",
        "lastname": "Smith",
        "dni": 9876543,
        "position": "Supervisor",
        "salary": 450000
    },
    {
        "id": 3,
        "name": "Alice",
        "lastname": "Johnson",
        "dni": 5234567,
        "position": "Analista",
        "salary": 400700
    },
    {
        "id": 4,
        "name": "Bob",
        "lastname": "Brown",
        "dni": 8765432,
        "position": "Encargado",
        "salary": 428000
    },
    {
        "id": 5,
        "name": "Emily",
        "lastname": "Davis",
        "dni": 6357924,
        "position": "Asistente",
        "salary": 385000
    },
    {
        "id": 6,
        "name": "Michael",
        "lastname": "Wilson",
        "dni": 9468135,
        "position": "Gerente",
        "salary": 524000
    },
    {
        "id": 7,
        "name": "Samantha",
        "lastname": "Martinez",
        "dni": 569851,
        "position": "Supervisor",
        "salary": 478000
    },
    {
        "id": 8,
        "name": "David",
        "lastname": "Garcia",
        "dni": 7854123,
        "position": "Analista",
        "salary": 415000
    },
    {
        "id": 9,
        "name": "Linda",
        "lastname": "Rodriguez",
        "dni": 7597536,
        "position": "Encargado",
        "salary": 435000
    },
    {
        "id": 10,
        "name": "Christopher",
        "lastname": "Lopez",
        "dni": 6543219,
        "position": "Asistente",
        "salary": 392000
    }
]

    max_employees = 1
    while True:
        option = get_int(message="1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Salir\n")
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
                print(get_average_salary(employees))
                input("Presione una tecla para continuar...")
                clear_screen()
            case 6:
                search_dni(employees)
            case 7:
                sort_array(employees)
            case 8:
                break

menu()