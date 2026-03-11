def partition(arr, l, h):
    p = arr[l]
    i, j = l, h

    while True:
        # Move i right until we find element >= pivot
        while i < h and arr[i] <= p:
            i += 1

        # Move j left until we find element <= pivot
        while j > l and arr[j] > p:
            j -= 1

        # If pointers crossed, partitioning is done
        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quick_sort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        quick_sort(arr, l, pi - 1)
        quick_sort(arr, pi + 1, h)


arr = [5, 3, 1, 2, 1000, 100000, 10, 5.2, 7.5, -4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
# [-4, 1, 2, 3, 5, 5.2, 7.5, 10, 1000, 100000]
