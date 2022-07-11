def binary_search(n, a):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if n == a[mid]:
            return mid
        elif n < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search2(n, a, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if n == a[mid]:
        return mid
    elif n < a[mid]:
        return binary_search2(n, a, left, mid-1)
    else:
        return binary_search2(n, a, mid+1, right)