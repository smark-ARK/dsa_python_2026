def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        p = i
        for j in range(i + 1, n):
            if arr[j] < arr[p]:
                p = j
        arr[i], arr[p] = arr[p], arr[i]
    return arr


print(selection_sort([5, 3, 1, 2, 1000, 100000, 10, 5.2, 7.5, -4]))
