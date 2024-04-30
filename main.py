# Desarrollar un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario.
# Validar las dimensiones de cada una para que sea consistente con el procedimiento
A = [[6,4,-5],
     [9,8,4],
     [10,-3,9],
    #  [0,0,0]
     ]

B = [[-2,7,2],
     [4,-2,8],
     [6,-5,7]]

def can_multiply(A: list, B: list) -> bool:
    rows_A = len(A)
    columns_B = len(B[0])
    validate = False
    if rows_A == columns_B:
        validate = True
    return validate

###
rows_A = len(A)
columns_B = len(B[0])
C = [[0]*columns_B for _ in range(rows_A)]
###

def multiply_matrix(A: list, B: list, C: list) -> list:
    for i in range(len(B)): # Recorremos las filas de B
        for j in range(len(B[i])): # Recorremos las columnas de B
            actual_cell = 0
            for k in range(len(B)):
                actual_cell += (A[i][k] * B[k][i])
            C[i][j] = actual_cell
    message= f"A= {A}\nC={C}"
    return message

print(multiply_matrix(A,B,C))

def multiply_array(A: list, B:list):
    message = ""
    result = 0
    if  can_multiply(A,B):
        rows_A = len(A)
        columns_B = len(B[0])
        C = [[0]*columns_B for _ in range(rows_A)]
    else:
        message = "Las matrices ingresadas no se pueden multiplicar"
        print(message)

# multiply_array(A,B)