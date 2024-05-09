def selection_sort(array):
    for i in range(len(array) - 1):
        small = array[i]
        small_index = i
        for j in range(i + 1,len(array)):
            if array[j] < small:
                small = array[j]
                small_index = j
        array[i],array[small_index] = array[small_index],array[i]
