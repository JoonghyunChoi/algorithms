# LSD 기수정렬
def radix_sort1(a):
    Length = len(a[0])
    R = 128
    N = len(a)
    b = [None] * N

    for d in range(Length-1, -1, -1):
        counts = [0] * (R+1)
        for i in range(N):
            counts[ord(a[i][d])+1] += 1
        for j in range(1, R):
            counts[j] += counts[j-1]

        for i in range(N):
            freqSum = counts[ord(a[i][d])]
            b[freqSum] = a[i]
            freqSum += 1
        for i in range(N):
            a[i] = b[i]


# MSD 기수정렬
def radix_sort2(a, low, high, d):
    R = 256
    N = len(a)
    b = [0] * N
    if high <= low:
        return

    counts = [0] * (R+2)
    for i in range(low, high+1):
        counts[pop(a[i], d)+2] += 1
    for j in range(0, R+1):
        counts[j+1] += counts[j]

    for i in range(low, high+1):
        freqSum = counts[pop(a[i], d)]
        b[freqSum+1] = a[i]
        freqSum += 1

    for i in range(low, high+1):
        a[i] = b[i-low]
    for r in range(0, R+1):
        low = low + counts[r]
        high = low + counts[r+1] - 1
        radix_sort2(a, low, high, d+1)

def pop(str, d):
    if d < len(str):
        return ord(str.pop(d))
    else:
        return -1