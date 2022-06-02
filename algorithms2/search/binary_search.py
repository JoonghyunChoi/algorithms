# 반복문을 이용한 이진탐색
def binarySearch1(a, target):
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


# 재귀를 이용한 이진탐색
def binarySearch2(a, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == a[mid]:
            return mid
        elif target < a[mid]:
            return binarySearch2(a, target, low, mid-1)
        else:
            return binarySearch2(a, target, mid+1, high)