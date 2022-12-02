def quick_sort(a):
    def partition(a, pivot, high):
        i = pivot+1
        j = high
        while i < j:
            while i < high and a[i] < a[pivot]:
                i += 1
            while j > pivot and a[j] > a[pivot]:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        a[pivot], a[j] = a[j], a[pivot]
        return j

    def _quick_sort(a, low, high):
        if low < high:
            pivot = partition(a, low, high)
            _quick_sort(a, low, pivot-1)
            _quick_sort(a, pivot+1, high)
        return a
    return _quick_sort(a, 0, len(a)-1)