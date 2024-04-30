from Packages.Package_Arrays.Especificas import *

def get_positives_negatives_amount(array: list)->str:
    """Returns the amount of positives, negatives and zeros (if exists)

    Args:
        array (list): The array you're going to check

    Returns:
        str: A string with the amount of positives, negatives and zeros
    """
    positives = 0
    negatives = 0
    zeros = 0
    for i in range(len(array)):
        if check_positive(array[i]):
            positives += 1
        elif check_positive(array[i]) == False:
            negatives += 1
        else:
            zeros += 1
    message = f"Positivos: {positives}\nNegativos: {negatives}"
    if zeros > 0:
        message += f"\nCeros: {zeros}"
    return message

def sum_numbers(array: list,universal=None)->int:
    """Returns the sum of the numbers from an array

    Args:
        array (list): The array you're going to sum
        universal (bool, optional): Defaults to True. Can be changed to True (even) or False (odd) to sum only those

    Returns:
        int: returns the result of the sum
    """
    even_sum = 0
    odd_sum = 0
    for i in range(len(array)):
        if check_parity(array[i]):
            even_sum += array[i]
        else:
            odd_sum += array[i]
    if universal == True:
        result = even_sum
    elif universal == False:
        result = odd_sum
    else:
        total = even_sum + odd_sum
        result = total
    return result

def get_max(array: list, universal:bool)->int:
    """Returns the max number of the array.

    Args:
        array (list): The array you are going to compare
        universal (bool): Define True if you want to get evens or False otherwise

    Returns:
        int: _description_
    """
    even_max = False
    odd_max = False
    first_even = True
    first_odd = True
    for i in range(len(array)):
        if first_even == True or array[i] > even_max and check_parity(array[i]):
            even_max = array[i]
            first_even = False
        elif first_odd == True or array[i] > odd_max and not check_parity(array[i]):
            odd_max = array[i]
            first_odd = False
    if universal == True:
        result = even_max
        even_odd = "par"
    elif universal == False:
        result = odd_max
        even_odd = "impar"
    if result == False:
        result = f"No hay numeros {even_odd}"
    return result

def str_list(array: list, universal=None)->str:
    """Returns a str with each element from a list enumerated

    Args:
        array (list): The array you want to enumerate
        universal (_type_, optional): Defaults to None returns the whole list. If True returns only even numbers. If False returns only odd numbers.

    Returns:
        str: _description_
    """
    message = ""
    position = 1
    if universal == True:
        for i in range(len(array)):
            if check_parity(array[i]):
                message += f"\n{position}. {array[i]}"
                position += 1
    elif universal == False:
        for i in range(len(array)):
            if not check_parity(array[i]):
                message += f"\n{position}. {array[i]}"
                position += 1
    else:
        for i in range(len(array)):
            message += f"\n{position}. {array[i]}"
            position += 1
    return message

def get_arrays_at(array: list, universal=None)->str:
    """Returns the positions and the value.

    Args:
        array (list): The list you are going to enumerate
        universal (_type_, optional): Defaults to None returns every list's item, if True returns even positions, if False returns odd positions.

    Returns:
        str: Returns a variable which contains a string
    """
    message = ""
    if universal == True:
        for i in range(len(array)):
            if check_parity(i+1):
                message += f"\n{i+1}. {array[i]}"
    elif universal == False:
        for i in range(len(array)):
            if not check_parity(i+1):
                message += f"\n{i+1}. {array[i]}"
    else:
        for i in range(len(array)):
            message += f"\n{i+1}. {array[i]}"
    return message