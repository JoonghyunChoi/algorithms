def binarySearch(a, target):
    low = 0
    high = len(a) - 1

    while low < high:
        mid = (low + high) // 2
        if target == a[mid]:
            return mid
        elif target < a[mid]:
            high = mid - 1
        else:
            low = mid + 1


def binarySearch2(a, target, low, high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if target == a[mid]:
        return mid
    elif target < a[mid]:
        return binarySearch2(a, target, low, mid-1)
    else:
        return binarySearch2(a, target, mid+1, high)