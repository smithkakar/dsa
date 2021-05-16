'''
Insertion Sort builds the final sorted array (or list) one item at a time. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, 
or merge sort.
'''


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position = position - 1

        # print(current_value)
        # print(position)

        arr[position] = current_value

    return arr


arr = [3, 5, 4, 6, 8, 1, 2, 12, 41, 25]
print(insertion_sort(arr))
