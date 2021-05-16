#!/usr/local/bin/env python3
'''
The selection sort improves on the bubble sort by making only one exchange for every pass 
through the list. In order to do this, a selection sort looks for the largest value 
as it makes a pass and, after completing the pass, places it in the proper location. 
As with a bubble sort, after the first pass, the largest item is in the correct place. 
After the second pass, the next largest is in place. This process continues and 
requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.
'''


def selection_sort(arr):
    for slot in range(len(arr)-1, 0, -1):
        maxPosition = 0

        for loc in range(1, slot+1):
            if arr[loc] > arr[maxPosition]:
                maxPosition = loc
        # swap only when largest element is found in a pass
        temp = arr[slot]
        arr[slot] = arr[maxPosition]
        arr[maxPosition] = temp

    return arr


arr = [3, 5, 2, 7, 6, 8, 12, 40, 21]
print('unsorted array: ', arr)
print('sorted array: ', selection_sort(arr))
