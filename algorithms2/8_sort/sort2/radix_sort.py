def radix_sort1(a):
    Length = len(a[0])
    R = 128
    N = len(a)
    b = [None] * N

    for d in range(Length-1, -1, -1):
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1
        for j in range(1, R):
            count[j] += count[j-1]

        for i in range(N):
            freqSum = count[ord(a[i][d])]
            b[freqSum] = a[i]
            freqSum += 1
        for i in range(N):
            a[i] = b[i]
    return a


def radix_sort2(a, low, high, d):
    R = 256
    N = len(a)
    b = [0] * N
    if high <= low:
        return

    count = [0] * (R+2)
    for i in range(low, high+1):
        count[pop(a[i], d)+2] += 1
    for j in range(0, R+1):
        count[j+1] += count[j]

    for i in range(low, high+1):
        freqSum = count[pop(a[i], d)]
        b[freqSum+1] = a[i]
        freqSum += 1

    for i in range(low, high+1):
        a[i] = b[i-low]
    for r in range(0, R+1):
        low = low + count[r]
        high = low + count[r+1] - 1
        radix_sort2(a, low, high, d+1)

def pop(str_, d):
    if d < len(str_):
        return ord(str_.pop(d))
    else:
        return -1