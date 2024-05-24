from Packages.Package_Input.Input import *
from Packages.Package_System.system import *

def check_id(employees: list, id: int):
    is_valid = None
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            is_valid = i
            break
    return is_valid

def check_dni(employees:list, dni: int):
    is_valid = None
    for i in range(len(employees)):
        if employees[i]["dni"] == dni:
            is_valid = i
            break
    return is_valid


def show_employee(employee:dict):
    print(f"{employee["name"]:^15}|{employee["lastname"]:^15}|{employee["position"]:^15}|{employee["salary"]:^15}")

def show_employees(employees: list):
    header = ["Nombre","Apellido","Puesto","Salario"]
    print(f"{header[0]:^15}|{header[1]:^15}|{header[2]:^15}|{header[3]:^15}")
    for employee in employees:
        show_employee(employee)

def get_average_salary(employees:list):
    storage = 0
    for employee in employees:
        storage += employee["salary"]
    return storage / len(employees)

def search_dni(employees: list):
    dni = get_int("Ingrese el DNI: ",min=5000000,max=9999999)
    index_dni = check_dni(employees,dni)
    if index_dni != None:
        show_employee(employees[index_dni])
        input("Presione una tecla para continuar...")
        clear_screen()
    else:
        print(f"No se econtró empleado con el dni {dni}.")
        input("Presione una tecla para continuar...")
        clear_screen()

def sort_array(employees:list):
    option = get_int(message="Ordenar empleados según:\n1. Nombre\n2. Apellido\n3. Salario\n4. Cancelar\n")
    order = get_int(message="Ordenar lista de forma:\n1.Ascendente\n2.Descendente\n3. Cancelar\n")
    options = ["name","lastname","salary"]
    quick_sort(employees,0,len(employees)-1,options[option - 1])
    if order == 2:
        employees.reverse()
    show_employees(employees)
    input("Presione una tecla para continuar...")
    clear_screen()

def particion(employees:list, first, last,key: str):
    pivot = employees[last][key]
    last_index = first - 1
    for i in range(first, last):
        if employees[i][key] < pivot:
            last_index += 1
            employees[last_index],employees[i] = employees[i],employees[last_index]
    last_index += 1
    employees[last_index],employees[last] = employees[last],employees[last_index]
    return last_index


def quick_sort(employees, first, last,key:str):
    if first < last:
        pi = particion(employees,first,last,key)
        quick_sort(employees, pi + 1, last,key)
        quick_sort(employees, first, pi - 1,key)
