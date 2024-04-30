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
    message = ""
    for i in range(len(C)):
        for j in range(len(C[i])):
            message += f"{C[i][j]} "
        message += f"\n"
    return message
