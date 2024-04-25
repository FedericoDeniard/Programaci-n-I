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
    
x = sum_number(5)
print(x)
