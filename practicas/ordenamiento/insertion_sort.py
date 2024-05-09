import time

numbers = [3, 6, 2, 8, 4, 6, 1, 9, 5]

def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]

# insertion_sort(numbers)
# print(numbers)