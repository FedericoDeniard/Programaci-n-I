numeros = [3, 6, 2, 8, 4, 6, 1, 9, 5]

# numeros = [5,2,7,5]


def partition(array: list, first: int, last: int) -> int:
    pivot = array[last]
    last_index = first - 1
    for i in range(first, last):
        if  array[i] < pivot:
            last_index += 1
            array[i], array[last_index] = array[last_index], array[i]
    last_index += 1
    array[last],array[last_index] = array[last_index],array[last]
    return last_index

partition(numeros,0,len(numeros)-1)
print(numeros)


def quick_sort(array: list, first: int, last: int):
    while first < last:
        pivot_index = partition(array, first, last)
        

quick_sort(numeros,0,len(numeros)-1)

print(numeros)
