from Packages.Package_Input.Input import *
from os import system

def new_array() -> list:
    """Asks how many rows and colums are in the array, in order to set them.

    Returns:
        list: returns a list with the array.
    """
    rows = get_int("Ingrese la cantidad de filas del array: ")
    columns = get_int("Ingrese la cantidad de columnas del array: ")
    array = [[0] * columns for _ in range(rows)]
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j] = get_int(f"Ingrese el valor de la posicion [{i+1}][{j+1}]: ")

    return array


def can_multiply(A: list, B: list) -> bool:
    """Checks if the arrays can be multiplied

    Args:
        A (list): First array
        B (list): Second array

    Returns:
        bool: returns True if can be multiplied, False otherwise
    """
    columns_A = len(A[0])
    rows_B = len(B)
    validate = False
    if columns_A == rows_B:
        validate = True
    return validate

def multiply_matrix(A: list, B: list) -> str:
    """Multiplies 2 arrays without caring about validation

    Args:
        A (list): First Array
        B (list): Second Array

    Returns:
        str: Returns the result formatted between A and B
    """

    rows_A = len(A)
    columns_B = len(B[0])
    C = [[0]*columns_B for _ in range(rows_A)]
    
    for i in range(len(C)): # Recorremos las filas de C
        for j in range(len(C[0])): # Recorremos las columnas de C
            actual_cell = 0
            for k in range(len(A[0])): # Recorremos las columnas de A
                valor_A = A[i][k]   # Cambiamos de columna
                valor_B = B[k][j]   # Cambiamos de fila
                multiplicacion = valor_A * valor_B
                actual_cell += multiplicacion
            C[i][j] = actual_cell

    return C

def multiply_array() -> list:
    """ Calls other array methods and if succesfull, returns the product between, otherwise, returns an empty array.

    Returns:
        list: _description_
    """
    print("Primera matriz")
    A = new_array()
    system("cls")
    print("Segunda matriz")
    B = new_array()
    system("cls")
    if  can_multiply(A,B):
        result = multiply_matrix(A,B)
    else:
        result = []
    return result