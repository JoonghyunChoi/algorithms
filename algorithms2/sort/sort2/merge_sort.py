def merge_sort(a):
    def merge(a, b, low, mid, high):
        i = low
        j = mid + 1
        for k in range(low, high+1):
            if i <= mid and j <= high:
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

    def merge_sort_(a, b, low, high):
        if high <= low:
            return

        mid = low + (high - low) // 2
        merge_sort_(a, b, low, mid)
        merge_sort_(a, b, mid+1, high)
        merge(a, b, low, mid, high)
        return a
    b, low, high = [None]*len(a), 0, len(a)-1
    return merge_sort_(a, b, low, high)