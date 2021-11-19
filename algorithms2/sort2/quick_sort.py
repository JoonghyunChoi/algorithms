def quickSort(n, low, high):
    if low < high:
        pivot = partition(n, low, high)

        quickSort(n, low, pivot-1)
        quickSort(n, pivot+1, high)

def partition(n, pivot, high):
    i = pivot+1
    j = high
    while True:
        while i < high and n[i] < n[pivot]:
            i += 1
        while j > pivot and n[j] > n[pivot]:
            j -= 1
        if i >= j:
            break

        n[i], n[j] = n[j], n[i]
        i += 1
        j -= 1

    n[pivot], n[j] = n[j], n[pivot]
    return j
