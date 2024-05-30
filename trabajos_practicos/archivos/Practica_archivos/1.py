""" 
1. Crear una función que reciba como parámetros una lista de números y el path de un archivo. 
La misma deberá guardar la lista en un archivo de texto.
"""
import random

integers_numbers = [random.randint(1,100) for _ in range(100)]

def write_numbers(path: str, numbers: list):
    with open(path, 'w') as file:
        for number in numbers:
            file.write(f'{number}\n')

write_numbers('trabajos_practicos/archivos/Practica_archivos/1_numbers.txt',integers_numbers)