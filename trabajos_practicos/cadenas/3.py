"""
Nombre: Federico
Apellido: Deniard

3) Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. 
Deberá retornar un valor booleano indicando lo sucedido.
"""

def is_palindrome(string: str) -> bool:
    result = False
    reversed_string = ""
    for i in range(len(string)-1,-1,-1):
        reversed_string += string[i]
    if reversed_string == string:
        result = True
    return result