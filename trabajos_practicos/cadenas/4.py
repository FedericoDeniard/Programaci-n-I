"""
Nombre: Federico
Apellido: Deniard

4) Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
"""

def delete_repeated(string:str) -> str:
    result_message = string[0]
    for i in range(1,len(string)):
        if string[i] != string[i-1]:
            result_message += string[i]
    return result_message

print(delete_repeated("hoooolaa"))