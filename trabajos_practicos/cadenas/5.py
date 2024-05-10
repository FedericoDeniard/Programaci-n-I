"""
Nombre: Federico
Apellido: Deniard

5) Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
    Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
"""

def delete_vowels(string: str) -> str:
    vowels = "AaEeIiOoUu"
    result_message = ""
    for i in range(len(string)):
        is_vowel = False
        for j in range(len(vowels)):
            if string[i] == vowels[j]:
                is_vowel = True
                continue
        if not is_vowel:
            result_message += string[i]
    return result_message