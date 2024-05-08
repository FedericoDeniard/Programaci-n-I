# Desarrollar un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario.
# Validar las dimensiones de cada una para que sea consistente con el procedimiento
'''
Nombre: Federico
Apellido: Deniard
'''

from Packages.Package_Arrays.Matrices import *
from Packages.Package_Input.Input import *

def print_array(array: list):
    """ Recieves an array and prints a formatted version of it.

    Args:
        array (list): The array you want to print.

    """
    message = "[ "
    for i in range(len(array)):
        for j in range(len(array[i])):
            message += f"{array[i][j]} "
        if j == len(array[i]) -1:
            if i == len(array[i]) -1:
                message += "]"
            else:
                message += f"\n"
    message = f"El producto de las dos matrices es:\n {message}"
    print(message)
    system("pause")

print_array(multiply_array())
