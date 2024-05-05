from Packages.Package_Input.Input import *
from Packages.Package_Buses.buses import *
from os import system

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
                system("cls")
                break

main()
