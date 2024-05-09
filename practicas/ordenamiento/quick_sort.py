def particion(array, first, last):
    pivot = array[last]
    last_index = first - 1
    for i in range(first, last):
        if array[i] < pivot:
            last_index += 1
            array[last_index],array[i] = array[i],array[last_index]
    last_index += 1
    array[last_index],array[last] = array[last],array[last_index]
    return last_index


def quick_sort(array, first, last):
    if first < last:
        pi = particion(array,first,last)
        quick_sort(array, pi + 1, last)
        quick_sort(array, first, pi - 1)