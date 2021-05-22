def binarySearch(a, target):
    low = 0
    high = len(a) - 1

    while high >= low:
        mid = int((low + high) / 2)
        if a[mid] == target:
            return mid
        elif target < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
