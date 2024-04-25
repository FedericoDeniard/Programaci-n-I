'''
Nombre: Federico
Apellido: Deniard
'''
x = [15, -5, 10, -100, 20, 30, -50, 5, 25, -10, 0, 40, -20, -30, 35, 40]
nombres = ["Sofía", "Juan", "Valentina", "Miguel", "Isabella", "Carlos", "María", "Alejandro", "Camila", "Diego", "Lucía", "José", "Emma", "David", "Ana", "Sofía", "Carlos", "Juan"]


#1 Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

def get_average(array: list) -> int:
    """Recieves a list of integers and returns it's average

    Args:
        array (list): Must be an array of numbers

    Returns:
        int : The average of the number's list
    """
    array_sum = 0
    for i in range(len(array)):
        array_sum += array[i]
    average = array_sum / len(array)
    return average

'''print(get_average(x))'''

#2 Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def get_average_from_positives(array: list) -> int:
    """Recieves a list of integers and returns the average of positive's numbers

    Args:
        array (list): Must be an array of numbers

    Returns:
        int: The average of the positive's numbers
    """
    array_sum = 0
    positives_number = 0
    for i in range(len(array)):
        if array[i] > 0:
            array_sum += array[i]
            positives_number += 1
    average = array_sum / positives_number
    return average


'''print(get_average_from_positives(x))'''

#3 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def get_product(array: list) -> int:
    """Calcs the multiplication of the numbers from a list

    Args:
        array (list): Must be an array of numbers

    Returns:
        int: Returns the product of the multiplication from all of the numbers on the array
    """
    first_number = True
    product = 0
    for i in range(len(array)):
        if first_number:
            product = array[i]
            first_number = False
        else:
            product *= array[i]
    return product

'''print(get_product(x))'''

#4 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def get_max_position(array: list) -> int:
    """Recieves an array of integers and returns the position where the maximun value is

    Args:
        array (list): Must be an array of integers

    Returns:
        int: Returns the position where the maximun number is
    """
    max_number = 0
    max_position = 0
    for i in range(len(array)):
        if i == 0 or array[i] > max_number:
            max_number = array[i]
            max_position = i
            
    return max_position

'''print(get_max_position(x))'''

#5 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def get_maximun_positions(array: list) -> int:
    """Recieves an array of integers and returns the position where the maximun value/s are

    Args:
        array (list): Must be an array of integers

    Returns:
        int: Returns the position where the maximun numbers are
    """
    max_number = 0
    max_positions = ""
    for i in range(len(array)):
        if i == 0 or array[i] > max_number:
            max_number = array[i]
    for i in range(len(array)):
        if max_number == array[i]:
            max_positions += f"{i} "

    return max_positions

print(get_maximun_positions(x))

#6 ##########################################################################################################################################################

'''Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo.
La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo
y luego retornar la cantidad total de reemplazos realizados.'''

def reemplazar_nombres(array: list, search: str, replace: str) -> int:
    """Recieves an array of names, the function will find every name that matches the search and replace it with the replace arg, returns the total of times the names were replaced

    Args:
        array (list): Must contain only strings. And has to be an array
        search (str): That's the name that will be replaced
        replace (str): That's the name that will replace the search

    Returns:
        int: Returns the total of times the names were replaced
    """
    times_changed = 0
    for i in range(len(array)):
        if array[i] == search:
            array[i] = replace
            times_changed += 1
    return times_changed
