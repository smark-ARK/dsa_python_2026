def binary_search_rec(arr, target, l, r):
    if l > r:
        return -1
    mid = (l + r) // 2
    print(l, r, mid)
    if target < arr[mid]:
        return binary_search_rec(arr, target, l, mid - 1)
    elif target > arr[mid]:
        return binary_search_rec(arr, target, mid + 1, r)
    else:
        return mid


a = [1, 2, 3, 4, 5, 6]

print(binary_search_rec(a, 5, 0, len(a) - 1))
