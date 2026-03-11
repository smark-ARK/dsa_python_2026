def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        c_value = arr[i]
        c = i
        while c > 0 and arr[c - 1] > c_value:
            arr[c] = arr[c - 1]
            c -= 1
        arr[c] = c_value
    return arr


print(insertion_sort([5, 3, 1, 2, 1000, 100000, 10, 5.2, 7.5, -4]))
