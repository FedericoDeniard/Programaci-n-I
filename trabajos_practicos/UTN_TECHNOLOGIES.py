'''
Nombre: Federico
Apellido: Deniard

Determinar:
    1. Cantidad de empleados de genero masculino que votaron por IOT o AI cuya edad este entre 25 y 50 inclusive
    2. Porcentaje de empleados que no votaron por AI, siempre y cuando su genero no sea femenino o su edad este entre los 33 y 40.
    3. Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese genero
'''

from Packages.Package_Input.Input import *
from Packages.Package_Input.Validate import validate_number
from os import system


employees = 1

def survey(employees_amount: int) -> list:
    """

    Args:
        employees_amount (int): The amount of employees to be surveyed

    Returns:
        list: An array with all surveyed employees information
    """
    system("cls")
    employees_list = [[0]* 4 for _ in range(employees_amount)]
    for i in range(employees_amount):
        employees_list[i][0] = get_string(f"Empleado {i+1}. Ingrese su nombre: ")
        employees_list[i][1] = get_int(message=f"Empleado {i+1}. Ingrese su edad: ",error_message="Edad no valida",min=18,max=100)
        while employees_list[i][2] != "M" and employees_list[i][2] != "F" and employees_list[i][2] != "O":
            employees_list[i][2] = get_string(f"Empleado {i+1}. Ingrese su género ('M': Masculino, 'F': Femenino, 'O': Otro): ",1)
        while employees_list[i][3] != "AI" and employees_list[i][3] != "VR" and employees_list[i][3] != "IOT":
            employees_list[i][3] = get_string(f"Empleado {i+1}. Ingrese la aplicación que quiere desarrollar (AI / VR / IOT): ",3)
        system("cls")

    first_message = 0
    second_message = 0
    third_message = ""
    
    max_age = get_max_number([employee[1] for employee in employees_list])
    for j in range(len(employees_list)):
        if validate_number(employees_list[j][1], 25, 50) and employees_list[j][3]!= "RV" and employees_list[j][2] == "M":
            first_message += 1
        if employees_list[j][3] != "AI" and employees_list[j][2] != "F" and not validate_number(employees_list[j][1],33,40):
            second_message += 1
        if max_age == employees_list[j][1] and employees_list[j][2] == "M":
            third_message = f"{employees_list[j][0]} votó por {employees_list[j][3]} y tiene {employees_list[j][1]} años"
    
    second_message = (second_message / employees_amount) * 100
    
    system("cls")
    print(f"Cantidad de empleados de genero masculino que votaron por IOT o AI cuya edad este entre 25 y 50 inclusive: {first_message}\nPorcentaje de empleados que no votaron por AI, siempre y cuando su genero no sea femenino o su edad este entre los 33 y 40: {second_message}%\n{third_message}")
    return employees_list

