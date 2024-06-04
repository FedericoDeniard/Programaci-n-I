from Packages.Package_Input.Input import *
from trabajos_practicos.CRUD.Package_crud.read import show_employee
import json

def new_employee(employees: list,max_employees: int, last_id: list):
    clear_screen()
    if len(employees) < max_employees:
        positions = ["Gerente","Supervisor","Analista","Encargado","Asistente"]
        id = last_id[0] + 1
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
        print(show_employee(employee))
        confirm = get_confirm()
        if confirm:
            employees.append(employee)
            last_id[0] = id
            print(f"{name} {lastname} agregado con éxito.")
            input("Presione una tecla para continuar...")
        else:
            print("Carga cancelada.")
            input("Presione una tecla para continuar...")
    else:
        print("No podemos agregar más empleados al sistema")
        input("Presione una tecla para continuar...")
    clear_screen()

def save_employees(employees:list,path = 'empleados.csv'):
    file_text = ""
    for employee in employees:
        message = f"{employee["id"]},{employee["name"]},{employee["lastname"]},{employee["dni"]},{employee["position"]},{employee["salary"]}\n"
        file_text += message  
    with open(path,'w') as file:
        file.write(file_text)

def save_deleted_employees(deleted_employees: list, path = 'empleados_bajas.json'):
    with open(path,'w') as file:
        file = json.dump(deleted_employees,file,indent=2)

def save_config(path: str, data: dict):
    with open(path,'w') as config:
        config = json.dump(data,config,indent=2)
