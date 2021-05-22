def binarySearch(a, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == a[mid]:
            return mid
        elif target < a[mid]:
            return binarySearch(a, target, low, mid-1)
        else:
            return binarySearch(a, target, mid+1, high)
