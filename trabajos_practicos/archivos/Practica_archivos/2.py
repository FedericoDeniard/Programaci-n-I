""" 
2. Crear una función que reciba como parámetro el path de un archivo. 
La misma deberá leer el archivo del ejercicio anterior, solo dejando pasar a la lista los números múltiplos de 2.
"""
from Packages.Package_Input.Validate import validate_number

def get_numbers(path:str):
    with open(path,'r') as file:
        numbers = []
        for number in file:
            number = number.strip()
            if validate_number(number):
                number = int(number)
                if number % 2 == 0:
                    numbers.append(number)
    return numbers

print(get_numbers('trabajos_practicos/archivos/Practica_archivos/1_numbers.txt'))
