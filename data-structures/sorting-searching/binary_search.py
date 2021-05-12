def binary_search(arr, ele):
    # track indexes
    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

def rec_binary_search(arr, ele):
    # base case for recursive implementation
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele)
            else:
                return rec_binary_search(arr[mid+1:], ele)

# list must already be sorted!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(arr, 4))
print(binary_search(arr, 12))
print(rec_binary_search(arr, 3))
print(rec_binary_search(arr, 15))