from Packages.Package_Input.Input import *
from os import system

def new_array() -> list:
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
    """Multiplies 2 arrays withouth caring about validation

    Args:
        A (list): First Array
        B (list): Second Array

    Returns:
        str: Returns the result formatted
    """

    rows_A = len(A)
    columns_B = len(B[0])
    C = [[0]*columns_B for _ in range(rows_A)]
    
    for i in range(len(C)): # Recorremos las filas de B
        for j in range(len(C[0])): # Recorremos las columnas de B
            actual_cell = 0
            for k in range(len(A[0])): 
                valor_A = A[i][k]   
                valor_B = B[k][j]
                multiplicacion = valor_A * valor_B
                actual_cell += multiplicacion
            C[i][j] = actual_cell

    return C

def multiply_array() -> list:
    print("Primera matriz")
    A = new_array()
    system("cls")
    print("Segunda matriz")
    B = new_array()
    system("cls")
    result = 0
    if  can_multiply(A,B):
        result = multiply_matrix(A,B)
    else:
        print("Las matrices ingresadas no se pueden multiplicar")
        result = []
    return result
