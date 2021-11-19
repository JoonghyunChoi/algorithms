def mergeSort(n, s, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2

    mergeSort(n, s, low, mid)
    mergeSort(n, s, mid+1, high)
    merge(n, s, low, mid, high)

def merge(n, s, low, mid, high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if (i <= mid and j <= high):
            if n[i] <= n[j]:
                s[k] = n[i]
                i += 1
            elif n[j] < n[i]:
                s[k] = n[j]
                j += 1
        elif i > mid:
            s[k] = n[j]
            j += 1
        elif j > high:
            s[k] = n[i]
            i += 1
    for k in range(low, high+1):
        n[k] = s[k]
