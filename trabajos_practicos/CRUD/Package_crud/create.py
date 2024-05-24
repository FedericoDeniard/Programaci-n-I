from Packages.Package_Input.Input import *
from trabajos_practicos.CRUD.Package_crud.read import show_employee

def id_generator(employees: list) -> int:
    if len(employees) > 0:
        id = employees[-1]["id"] + 1
    else:
        id = 1

def new_employee(employees: list,max_employees):
    if len(employees) < max_employees:
        positions = ["Gerente","Supervisor","Analista","Encargado","Asistente"]
        id = id_generator(employees)
        name = get_string(message="Nombre del empleado: ",min_length=4)
        name = name.capitalize()
        lastname = get_string(message="Apellido del empleado: ",min_length=4)
        lastname = lastname.capitalize()
        dni = get_int(message="DNI del empleado: ",min=5000000,max=9999999)
        position = get_string(message="Puesto del empleado: ",min_length=7,max_length=10)
        position = position.capitalize()
        while position not in positions:
            position = get_string(message="Puesto del empleado: ",min_length=7,max_length=10)
        position = position.capitalize()
        salary = get_int(message="Salario del empleado: ",min=234315,max=10000000)
        
        employee = {"id":id,"name":name,"lastname":lastname,"dni":dni,"position":position,"salary":salary}
        show_employee(employee)
        confirm = get_confirm()
        if confirm:
            employees.append(employee)
            print(f"{name} {lastname} agregado con éxito.")
            input("Presione una tecla para continuar...")
        else:
            print("Carga cancelada.")
            input("Presione una tecla para continuar...")
    else:
        print("No podemos agregar más empleados al sistema")
        input("Presione una tecla para continuar...")
    clear_screen()

    return id