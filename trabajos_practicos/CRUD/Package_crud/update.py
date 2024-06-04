from Packages.Package_Input.Input import *
from trabajos_practicos.CRUD.Package_crud.read import *

def update_employee(employees: list):
    clear_screen()
    id = get_int("Ingrese el ID del empleado a modificar: ")
    id_valid = check_id(employees,id)
    if id_valid != None:
        employee_copy = {
            "id": employees[id_valid]["id"],
            "name": employees[id_valid]["name"],
            "lastname": employees[id_valid]["lastname"],
            "dni": employees[id_valid]["dni"],
            "position": employees[id_valid]["position"],
            "salary" : employees[id_valid]["salary"]
        }

        while True:
            print(show_employee(employee_copy))
            option = get_int(message="¿Que desea modificar?\n1. Nombre\n2. Apellido\n3. DNI\n4. Puesto\n5. Salario\n6. Guardar\n7. Cancelar\n",min=1,max=7)
            clear_screen()
            match option:
                case 1:
                    update_name(employee_copy)
                case 2:
                    update_lastname(employee_copy)
                case 3:
                    update_dni(employee_copy)
                case 4:
                    update_position(employee_copy)
                case 5:
                    update_salary(employee_copy)
                case 6:
                    clear_screen()
                    print(f"Nuevos valores")            
                    print(show_employee(employee_copy))
                    if get_confirm():
                        employees[id_valid] = employee_copy
                        break
                case 7:
                    if get_confirm():
                        print("Carga cancelada")
                        break
    else:
        print(f"No se encontró empleado con id {id}")
    clear_screen()
        
def update_name(employee: dict):
    name = get_string(message="Ingrese el nuevo nombre del empleado: ",min_length=4)
    name = name.capitalize()
    employee["name"] = name
    print("Nombre cambiado con éxito.")
    input("Presione una tecla para continuar...")
    clear_screen()

def update_lastname(employee: dict):
    lastname = get_string(message="Ingrese el nuevo appelido del empleado: ",min_length=4)
    lastname = lastname.capitalize()
    employee["lastname"] = lastname
    print("Apellido cambiado con éxito.")
    input("Presione una tecla para continuar...")
    clear_screen()

def update_dni(employee:dict):
    dni = get_int(message="Ingrese el nuevo DNI del empleado: ",min=5000000,max=9999999)
    employee["dni"] = dni
    print("DNI cambiado con éxito.")
    input("Presione una tecla para continuar...")
    clear_screen()

def update_position(employee:dict):
    positions = ["Gerente","Supervisor","Analista","Encargado","Asistente"]
    position = get_string(message="Ingrese el nuevo puesto del empleado: ",min_length=7,max_length=10)
    position = position.capitalize()
    while position not in positions:
        position = get_string(message="Ingrese el nuevo puesto del empleado: ",min_length=7,max_length=10)
    position = position.capitalize()
    employee["position"] = position
    print("Puesto cambiado con éxito.")
    input("Presione una tecla para continuar...")
    clear_screen()

def update_salary(employee:dict):
    salary = get_int(message="Ingrese el nuevo salario del empleado: ",min=234315,max=10000000)
    employee["salary"] = salary
    print("Salario cambiado con éxito.")
    input("Presione una tecla para continuar...")
    clear_screen()