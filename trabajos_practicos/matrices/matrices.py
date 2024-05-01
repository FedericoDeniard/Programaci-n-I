# Desarrollar un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario.
# Validar las dimensiones de cada una para que sea consistente con el procedimiento
'''
Nombre: Federico
Apellido: Deniard
'''

from Packages.Package_Arrays.Matrices import *

A = [[6,4,-5],
     [9,8,4],
     [10,-3,9]]

B = [[-2,7,2],
     [4,-2,8],
     [6,-5,7]]

def multiply_array(A: list, B:list) -> str:
    """Verifies if the arrays can be multiplied

    Args:
        A (list): First array to multiply
        B (list): Second array to multiply

    Returns:
        str: Returns a message with the multyply of the array formatted or with a message that the arrays can't be multiplied
    """
    result = 0
    if  can_multiply(A,B):
        result = multiply_matrix(A,B)
    else:
        result = "Las matrices ingresadas no se pueden multiplicar"
    return result

print(multiply_array(A,B))
