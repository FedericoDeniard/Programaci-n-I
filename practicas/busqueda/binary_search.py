def binary_search(array: list, value: int, start, end) -> int:
    index = None
    if start > end:
        return index  
    
    average =  (end + 1 + start) // 2

    if array[average] == value:
        index = average
        return index
    elif array[average] > value:
        return binary_search(array, value, start, average-1)
    elif array[average] < value:
        return binary_search(array, value, average+1,end)