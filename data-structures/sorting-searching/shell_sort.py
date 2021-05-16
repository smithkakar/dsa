'''
The shell sort improves on the insertion sort by breaking the original list into a number of smaller sublists, 
each of which is sorted using an insertion sort. The unique way that these sublists are chosen 
is the key to the shell sort. 
Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i, 
sometimes called the gap, to create a sublist by choosing all items that are i items apart.
'''


def shell_sort(arr):
    sublistcount = len(arr) // 2
    print('before iteration of gap insertion: ', arr)

    # while we have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            arr = gap_insertion_sort(arr, start, sublistcount)
            print('after iteration of gap insertion:  ', arr)
        sublistcount = sublistcount // 2

    return arr


def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position-gap] > current_value:
            # print(f'{arr[position - gap]} > {current_value}')
            # print('swapping elements !!!')
            arr[position] = arr[position-gap]
            position = position - gap

        arr[position] = current_value

    return arr


arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]
print(shell_sort(arr))
