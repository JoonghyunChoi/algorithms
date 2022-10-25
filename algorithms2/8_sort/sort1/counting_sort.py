def counting_sort(a):
    n, m = len(a), max(a)
    count = [0] * (m+1)

    for i in range(n):
        count[a[i]] += 1

    p = 0
    for k in range(m+1):
        for _ in range(count[k]):
            a[p] = k
            p += 1
    return a