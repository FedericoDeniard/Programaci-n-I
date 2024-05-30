""" 
4. Crear una función llamada contar_elementos que recibe como parámetro el path de un archivo de texto que contiene un poema. 
La función deberá contar la cantidad de líneas, la cantidad de palabras y la cantidad de caracteres que contiene el poema. 
La función retornará un diccionario con los datos obtenidos.   
"""

def count_elements(path:str):
    with open(path,'r') as file:
        lines = file.readlines()
        words = 0
        characters = 0
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            word = lines[i].split()
            words += len(word)
            for i in word:
                characters += len(i)

        print(len(lines))
        print(words)
        print(characters)

count_elements('trabajos_practicos/archivos/Practica_archivos/poema.txt')