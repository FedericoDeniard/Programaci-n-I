from random import *
from Packages.Package_Input.Input import *
from os import system

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
    system("cls")
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
    system("cls")
    for i in range(len(array)):
        print("")
        for j in range(len(array[i])):
            print(f"Linea {i + 1}, colectivo {j + 1}: {array[i][j]} ")
    system("pause")


def show_lines_payments(array:list):
    system("cls")
    for i in range(len(array)):
        total = 0
        for j in range(len(array[i])):
            total += array[i][j]
        print(f"Linea {i + 1}: {total}")
    system("pause")

def show_buses_payments(array:list):
    system("cls")
    bus_index = 1
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(f"Coche {bus_index}: {array[i][j]}")
    system("pause")

def show_payments(array: list):
    system("cls")
    total = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            total += array[i][j]
    print(f"Total: {total}")
    system("pause")

def main():
    drivers = 15
    bus_lines = 3
    buses = 5
    buses_array = [[0] * buses for _ in range(bus_lines) ]
    drivers_id = [[0] for _ in range(drivers)]

    for i in range(drivers):
        drivers_id[i] = create_id(drivers_id)

    is_loged = None

    while True:
        print(drivers_id)
        print(buses_array)
        menu = get_int(message="1. Iniciar sesion \n2. Mostrar la recaudacion de cada coche y linea \n3. Calcular y mostrar recaudacion por linea \n4. Calcular y mostrar recaudacion por coche \n5. Calcular y mostrar la recaudacion total. \n6. Salir \n",min=1,max=6, error_message=f"La opcion no se encuentra en el menu")
        match menu:
            case 1:
                is_loged = login(drivers_id,3)
                while True:
                    buses_array = load_payment(buses_array)
                    print(buses_array)
                    keep_loading = None
                    while keep_loading != "S" and keep_loading != "N":
                        keep_loading = input("¿Desea cargar otro pago? (S/N): ")
                    match keep_loading:
                        case "S":
                            system("cls")
                        case "N":
                            break
                    system("pause")
            case 2:
                if is_loged:
                    show_lines_buses_payments(buses_array)
                else:
                    print("Debes iniciar sesión para continuar.")
                    system("pause")
                    system("cls")

            case 3:
                if is_loged:
                    show_lines_payments(buses_array)
                else:
                    print("Debes iniciar sesión para continuar.")
                    system("pause")
                    system("cls")

            case 4:
                if is_loged:
                    show_buses_payments(buses_array)
                else:
                    print("Debes iniciar sesión para continuar.")
                    system("pause")
                    system("cls")

            case 5:
                if is_loged:
                    show_payments(buses_array)
                else:
                    print("Debes iniciar sesión para continuar.")
                    system("pause")
                    system("cls")

            case 6:
                break

main()
