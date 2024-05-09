numbers = [2, 4, 7, 9, 12, 14, 17, 19, 22, 25, 28, 30, 33, 36, 39, 42, 45, 47, 50, 53]

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

print(binary_search(numbers, 13,0,len(numbers)-1))

