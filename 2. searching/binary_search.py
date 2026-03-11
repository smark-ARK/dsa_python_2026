def binary_search(arr, target):
    arr.sort()
    n = len(arr)
    l = 0
    r = n
    while l <= r:
        cur = (l + r) // 2
        if target < arr[cur]:
            r = cur - 1
        elif target > arr[cur]:
            l = cur + 1
        else:
            return cur
    else:
        return -1


a = [1, 2, 3, 4, 5, 6]

print(binary_search(a, 1))
