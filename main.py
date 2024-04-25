'''
Nombre: Federico
Apellido: Deniard
'''
 
from Packages.Package_Input.Input import *

x = get_float(message="Ingrese un numero: ", error_message="El numero no es valido", attempts=0, min=0, max=10)
print(f"El numero ingresado es: {x}")

y = get_string("Ingrese un texto: ")
print(y)