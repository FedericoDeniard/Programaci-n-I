'''
Nombre: Federico
Apellido: Deniard
'''
 
from Packages.Package_Input.Input import *
from Packages.Package_Arrays.Array_Generales import *
from os import system

first_item = False
numbers = [False] * 10
while True:
    options = input("1. Ingresar numeros\n2. Mostrar la cantidad de positivos y negativos\n3. Mostrar la sumatoria de los pares\n4. Mostrar el mayor de los impares\n5. Listar todos los numeros ingresados\n6. Listar todos los numeros pares\n7. Listar los numeros en posiciones impares\n8. Salir\n")
    options = int(options)
    
    match options:
        case 1:
            for i in range(len(numbers)):
                numbers[i] = get_int(message="Ingrese un numero entre -1000 y 1000: ", error_message="El numero no es valido", min=-1000, max=1000)
            first_item = True
        case 2:
            if first_item == True:

                print(get_positives_negatives_amount(numbers))
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 3:
            if first_item == True:
                print(f"La suma de los numeros pares es: {sum_numbers(array=numbers, universal=True)} ")
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 4:
            if first_item == True:
                print(f"El numero impar más grande es : {get_max(numbers,False)}")
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 5:
            if first_item == True:
                print(str_list(numbers))
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 6:
            if first_item == True:
                print(str_list(numbers,True))
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 7:
            if first_item == True:
                print(get_arrays_at(numbers,False))
            else:
                print("Error. Los numeros no han sido ingresados.")
        case 8:
            break
        case _:
            print("El numero ingresado no es valido")
    system("pause")
    system("cls")

