l = [2, 3, 1, 4, 5, 8, 9, 6, 7]


def search(arr, item, low, high):
    if low > high:
        return 'Not Found!'
    mid = (low + high) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return search(arr, item, low, mid-1)
    else:
        return search(arr, item, mid+1, high)


print(search(sorted(l), 2, 0, len(l)-1))
