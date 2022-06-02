def mergeSort(a, b, low, high):
    if high <= low:
        return

    mid = low + (high - low) // 2
    mergeSort(a, b, low, mid)
    mergeSort(a, b, mid+1, high)
    merge(a, b, low, mid, high)

def merge(a, b, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if (i <= mid and j <= high):
            if a[i] <= a[j]:
                b[k] = a[i]
                i += 1
            elif a[j] < a[i]:
                b[k] = a[j]
                j += 1
        elif i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]