"""
Timing Merge Sort vs Insertion Sort
Shane Jose
"""

import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0


    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def insertion_sort(data_list):

    for index in range(1, len(data_list)):
        key = data_list[index]
        j = index - 1

        while j >= 0 and key < data_list[j]:
            data_list[j+1] = data_list[j]
            j -= 1

        data_list[j+1] = key



## Used this input for Experiment 1
#experiment_list =[10,20,40,60,70,80,90,100]

## Used this input for Experiment 2
experiment_list = [80,81,82,83,84,85,86,87,88,89,90]

merge_sort_times = []
insertion_sort_times = []

for n in experiment_list:
    arr = [random.randint(0, 1000) for _ in range(n)]

    # Time merge sort
    merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1000)
    merge_sort_times.append(merge_sort_time)

    # Time insertion sort
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1000)
    insertion_sort_times.append(insertion_sort_time)

print("Merge Sort Times: ", merge_sort_times)
print("Insertion Sort Times: ", insertion_sort_times)















