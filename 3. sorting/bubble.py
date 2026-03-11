def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([5, 3, 1, 2, 1000, 100000, 10, 5.2, 7.5, -4]))
