
from Packages.Package_Input.Input import *
from random import *
from Packages.Package_System.system import *

def create_id(ids: list) -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    id = ""
    for i in range(5):
        id += letters[randint(0, 25)]

    for j in range(5):
        id += str(randint(0, 9))
    
    
    for k in range(len(ids)):
        if id == ids[k]:
            id = create_id(ids)

    return id

def check_id(id: str, ids: list) -> bool:
    is_valid = False
    for i in range(len(ids)):
        if id == ids[i]:
            is_valid = True
    return is_valid

def login(data_base, max_attempts = 0 ):
    is_valid = False
    attempt = 1
    id = get_string("Ingrese su numero de legajo: ",10,10)
    clear_screen()
    while not check_id(id, data_base):
        if attempt == max_attempts:
            print("Se llego a los intentos maximos")
            return is_valid
        print("El numero de legajo no es valido")
        id = get_string("Ingrese su numero de legajo: ",10,10)
        attempt += 1
    is_valid = True
    return is_valid

def load_payment(array: list):
    print(f"Bienvenido al gestor de recaudacion de viaje")
    bus_line = get_int(message="Ingrese la linea a cargar: ", error_message="Ingrese una linea valida (1 al 3)",min=1, max=3 )
    bus = get_int(message=f"Ingrese el colectivo de la linea {bus_line} a cargar: ", error_message=f"Ingrese un colectivo valido (1 al 5)",min=1, max=5)
    payment = get_int("Ingrese el total recaudado (Solo numeros): ","Ingrese el numero sin ningun simbolo")
    array[bus_line-1][bus-1] += payment
    return array
    

def show_lines_buses_payments(array: list):
    clear_screen()
    for i in range(len(array)):
        print("")
        for j in range(len(array[i])):
            print(f"Linea {i + 1}, colectivo {j + 1}: {array[i][j]} ")
    input("Presione una tecla para continuar..\n")


def show_lines_payments(array:list):
    clear_screen()
    for i in range(len(array)):
        total = 0
        for j in range(len(array[i])):
            total += array[i][j]
        print(f"Linea {i + 1}: {total}")
    input("Presione una tecla para continuar..\n")

def show_buses_payments(array:list):
    clear_screen()
    bus_index = 1
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f"Coche {bus_index}: {array[i][j]}")
    input("Presione una tecla para continuar..\n")

def show_payments(array: list):
    clear_screen()
    total = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            total += array[i][j]
    print(f"Total: {total}")
    input("Presione una tecla para continuar..\n")
