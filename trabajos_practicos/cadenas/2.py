"""
Nombre: Federico
Apellido: Deniard

2) Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia 
de dicho caracter, o -1 en caso de que no esté
"""

def find_character(string: str, search: str) -> int:
    index = -1
    for i in range(len(string)):
        if string[i] == search:
            index = i + 1 # Le sumo 1 para mostrar al usuario (que cuenta desde 1)
            break
    return index

print(find_character("hola", "o"))

