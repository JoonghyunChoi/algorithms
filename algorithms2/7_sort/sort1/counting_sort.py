def counting_sort(a):
    n, _max = len(a), max(a)
    count = [0] * (_max+1)

    for i in range(n):
        count[a[i]] += 1

    p = 0
    for k in range(_max+1):
        for _ in range(count[k]):
            a[p] = k
            p += 1
    return a