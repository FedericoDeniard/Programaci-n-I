from Packages.Package_Input.Input import *
from Packages.Package_System.system import *
import re
import json
from datetime import *

def check_id(employees: list, id: int):
    is_valid = None
    for i in range(len(employees)):
        if employees[i]["id"] == id:
            is_valid = i
            break
    return is_valid

def get_config(path: str) -> dict:
    with open(path,'r') as config:
        content = json.load(config)
    return content

def check_dni(employees:list, dni: int):
    is_valid = None
    for i in range(len(employees)):
        if employees[i]["dni"] == dni:
            is_valid = i
            break
    return is_valid

def show_employee(employee:dict):
    employee_string = f"{employee["name"]:^15}|{employee["lastname"]:^15}|{employee["position"]:^15}|{employee["salary"]:^15}"
    return employee_string

def show_employees(employees: list):
    message = []
    message.append(f"{"Nombre":^15}|{"Apellido":^15}|{"Puesto":^15}|{"Salario":^15}")
    
    for employee in employees:
        message.append(show_employee(employee))
    clear_screen()
    return "\n".join(message)

def get_average_salary(employees:list):
    storage = 0
    for employee in employees:
        storage += employee["salary"]
    return storage / len(employees)

def search_dni(employees: list):
    clear_screen()
    dni = get_int("Ingrese el DNI: ",min=5000000,max=9999999)
    index_dni = check_dni(employees,dni)
    if index_dni != None:
        print(show_employee(employees[index_dni]))
        input("Presione una tecla para continuar...")
        clear_screen()
    else:
        print(f"No se econtró empleado con el dni {dni}.")
        input("Presione una tecla para continuar...")
        clear_screen()

def sort_array(employees:list):
    clear_screen()
    while True:
        option = get_int(message="Ordenar empleados según:\n1. Nombre\n2. Apellido\n3. Salario\n4. Cancelar\n",min=1,max=4)
        if option == 4:
            break
        clear_screen()
        order = get_int(message="Ordenar lista de forma:\n1.Ascendente\n2.Descendente\n3. Cancelar\n",min=1,max=4)
        clear_screen()
        if order == 3:
            break
        options = ["name","lastname","salary"]
        quick_sort(employees,0,len(employees)-1,options[option - 1])
        if order == 2:
            employees.reverse()
        break
    input("Lista odenada con éxito.\nPresione una tecla para continuar...")
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

def fetch_employees(path = 'empleados.csv') -> list:
    with open(path,'r') as file:
        employees = []
        for line in file:
            employee = re.split(',|\n',line)
            employee_dict = {"id":int(employee[0]),"name":employee[1],"lastname":employee[2],"dni":int(employee[3]),"position":employee[4],"salary":int(employee[5])}
            employees.append(employee_dict)

    return employees

def fetch_deleted(path = 'empleados_bajas.json') -> list:
    with open(path,'r') as file:
        deleted_employees = json.load(file)
    return deleted_employees

def salary_report(employees: list, last_report: list):
    today = datetime.now().strftime("%Y/%m/%d")
    message = f"Reporte N°: {last_report[0]}\nFecha: {today}\nCantidad de coincidencias: {len(employees)}"
    clear_screen()
    print(message)
    print(show_employees(employees))
    input("Presione una tecla para continuar...")
    last_report[0] = last_report[0] + 1
    with open('trabajos_practicos/CRUD/reports/reports.txt','a') as report:
        report.write(message +'\n' + show_employees(employees)+'\n'  +'-' * 60 + '\n')

def filter_salary(employees: list):
    salary = get_int(message="Se mostraran todos los salarios superiores a lo que ingrese.\nIngrese el salario mínimo a filtrar: ",min=234315,max=10000000)
    filtered_employees = []
    for employee in employees:
        if employee["salary"] > salary:
            filtered_employees.append(employee)
    return filtered_employees

def filter_lastname(employees: list):
    lastname = get_string("Ingrese el apellido a buscar:").capitalize()
    filtered_employees = []
    for employee in employees:
        if employee["lastname"] == lastname:
            filtered_employees.append(employee)
    return filtered_employees