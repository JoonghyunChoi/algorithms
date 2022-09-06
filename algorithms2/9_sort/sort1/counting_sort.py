def counting_sort(a):
    n, k = len(a), max(a)
    count = [0] * (k+1)

    for i in range(n):
        count[a[i]] += 1

    p = 0
    for i in range(k+1):
        for _ in range(count[i]):
            a[p] = i
            p += 1
    return a


def counting_sort2(a):
    n = len(a)
    count = [0] * (max(a)+1)

    for i in range(n):
        count[a[i]] += 1
    for j in range(1, max(a)+1):
        count[j] += count[j-1]

    b = [0] * (n+1)
    for i in range(n-1, -1, -1):
        freqSum = count[a[i]]
        b[freqSum] = a[i]
        freqSum -= 1

    b = b[1:]
    return b