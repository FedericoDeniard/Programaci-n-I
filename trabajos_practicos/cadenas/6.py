"""
Nombre: Federico
Apellido: Deniard

6) Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.

Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.
"""

def count_sub_strings(text: str, search: str) -> int:
    search_length = len(search)
    count = 0
    for i in range(len(text)):
        if text[i:i+search_length] == search:
            count += 1
    return count