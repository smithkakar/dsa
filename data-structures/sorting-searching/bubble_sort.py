def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
print('unsorted array: ', arr)
print('sorted array: ', bubble_sort(arr))


def bubble_sort2(arr):
    for n in range(0, len(arr)):
        # Last n elements are already in place
        for i in range(len(arr)-n-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
print('unsorted array: ', arr)
print('sorted array: ', bubble_sort2(arr))