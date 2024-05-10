"""
Nombre: Federico
Apellido: Deniard

1) Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una.
La función retornara una matriz indicando en la columna 1 cada vocal y en la columna 2 la cantidad.
"""

def count_vowels(string: str)->list:
    vowels = 'aeiou'
    vowels_count = [[vowels[i], 0] for i in range(len(vowels))]
    vowels = "aAeEiIoOuU"

    for i in range(len(string)):
        for j in range(len(vowels)):
            if string[i] == vowels[j]:
                for k in range(len(vowels_count)):
                    if vowels_count[k][0] == string[i] or vowels[j-1] == vowels_count[k][0]:
                        vowels_count[k][1] += 1
    return vowels_count

print(count_vowels("murcielaguito  "))