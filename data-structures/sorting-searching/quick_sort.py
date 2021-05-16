#! usr/local/bin/env python3
'''
A quick sort first selects a value, which is called the pivot value. 
Although there are many different ways to choose the pivot value, we will simply use the first item in the list. 
The role of the pivot value is to assist with splitting the list. The actual position where the pivot value 
belongs in the final sorted list, commonly called the split point, will be used to divide the list for 
subsequent calls to the quick sort.
'''


def quick_sort(arr):

    arr = quick_sort_help(arr, 0, len(arr)-1)
    return arr


def quick_sort_help(arr, first, last):

    if first < last:

        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)

    return arr


def partition(arr, first, last):

    pivotvalue = arr[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


arr = [2, 5, 4, 6, 7, 3, 1, 4, 12, 11]
print('unsorted array: ', arr)
print('sorted array: ', quick_sort(arr))
