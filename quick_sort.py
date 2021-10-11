'''
Two types of partition schemes:
    Hoare Partition --> start is pivot
    Lomuto Partition --> end is pivot and start is p index
    '''

# Here we solve this problem with Hoare Partition

import time

import random

def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] =arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements)-1

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start +=  1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  # left partition
        quick_sort(elements, pi + 1, end)  # right partition


# elements = [11, 9, 29, 7, 2, 15, 28]

elements = []

for i in range(0,5):
    n = random.randint(1,99)
    elements.append(n)

print('Elements before sorting: ', elements)

quick_sort(elements, 0, len(elements) - 1)
print('Elements after sorting: ', elements)

initial = time.process_time()
print(initial)


