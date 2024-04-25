"""
Nombre: Federico
Apellido: Deniard
Ejercicio: Funciones_01
"""

#1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def get_number(message: str, min: int, max:int) -> int:
    """Returns a number after validating

    Args:
        message (str): Message for the number you're asking for
        min (int): min number's range
        max (int): max number's range

    Returns:
        int: a validated number
    """
    number = input(message)
    number = int(number)
    while number < min or number > max:
        number = input(message)
        number = int(number)
    
    return number   

number = get_number("Ingrese un numero", 5,10)
print(f"Tu numero es {number}")

# number = get_number()

#2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def get_float() ->float:
    number = input("Type a float: ")
    while not number.isdecimal():
        number = input("Type a float: ")
    return float(number)

# float = get_float()

#3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
def get_name() -> str:
    name = input("Enter your name: ")
    while not name.isalpha():
        name = input("Enter your name: ")
    return name 

# name = get_name()

#4 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
#5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def get_circle_area(radio: int) -> int :
    """Defines the area of a circle

    Args:
        radio (int): Circle's radio

    Returns:
        int: Circle's area result
    """
    pi = 3.1416
    area = pi * radio ** 2
    return area

# area = get_circle_area(number)
# print(f"el area del circulo es: {area}")

#6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def find_parity(number: int) -> None:
    """Defines if a number is even or odd

    Args:
        number (int): Number we are going to work with
    """
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

# find_parity(number)

#7 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def get_highest_number(x:int, y:int , z:int) -> int:
    """Compares 3 numbers and returns the highest

    Args:
        x (int): first number to compare
        y (int): second number to compare
        z (int): third number to compare

    Returns:
        int: Highest number
    """
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

'''
x = get_number()
y = get_number()
z = get_number()

highest_number = get_highest_number(x,y,z)
print(highest_number)'''

#8 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def get_power(base: int, exponent: int):
    return base**exponent

'''
result = get_power(5,2)
print(result)
'''

