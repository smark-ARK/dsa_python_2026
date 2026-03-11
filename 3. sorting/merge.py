def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    k = l
    tarr = [0] * (r + 1)
    while i <= mid and j <= r:
        print(arr[i], arr[j])
        if arr[i] < arr[j]:
            tarr[k] = arr[i]
            i += 1
        else:
            tarr[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        tarr[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        tarr[k] = arr[j]
        j += 1
        k += 1
    print(arr, tarr)
    for m in range(l, r + 1):
        arr[m] = tarr[m]


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


arr = [5, 3, 1, 2, 1000, 100000, 10, 5.2, 7.5, -4]

merge_sort(arr, 0, len(arr) - 1)

print(arr)
