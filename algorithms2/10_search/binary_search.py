def binary_search(a, x):
    n = len(a)
    lo = 0
    hi = n-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(a, x):
    n = len(a)
    lo = 0
    hi = n

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(a, x):
    n = len(a)
    lo = 0
    hi = n

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo