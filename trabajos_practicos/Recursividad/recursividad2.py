'''
Nombre: Federico
Apellido: Deniard
'''

#   Realizar una función recursiva que calcule la suma de los primeros números naturales 

def sum_number(number: int)->int:
    if number == 0:
        return 0
    else:
        result = number + sum_number(number - 1)
        return result

#   Realizar una función recursiva que calcule la potencia de un número

def calc_power(base: int, exponent: int)->int:
    if exponent == 2:
        return base * base

    else:
        result = base * calc_power(base = base, exponent= exponent - 1) 
        return result

#   Realizar una función recursiva que la suma de los dígitos de un numero:

def sum_digits(number: int)->int:
    if number < 10:
        return number
    else:
        resultado = (number % 10) + sum_digits(number // 10)
        return resultado

#   Realizar una función para calcular el número de Fibonacci de un número ingresado por consola.

def calc_fibonacci(number: int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        resultado = calc_fibonacci(number - 1) + calc_fibonacci(number - 2)
        return resultado