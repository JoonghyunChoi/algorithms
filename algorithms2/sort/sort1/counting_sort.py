def counting_sort(a):
    counts = [0] * (max(a)+1)

    for i in range(len(a)):
        counts[a[i]] += 1

    b = []
    for i in range(len(counts)):
        for _ in range(counts[i]):
            b.append(i)
    return b


def counting_sort2(a):
    N = len(a)
    counts = [0] * (max(a)+1)

    for i in range(N):
        counts[a[i]] += 1
    for j in range(1, max(a)+1):
        counts[j] += counts[j-1]

    b = [0] * (N+1)
    for i in range(N-1, -1, -1):
        freqSum = counts[a[i]]
        b[freqSum] = a[i]
        freqSum -= 1

    b = b[1:]
    return b