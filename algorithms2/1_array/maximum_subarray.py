def kadane(a):
    n = len(a)
    s = m = a[0]

    for i in range(1, n):
        s = max(s+a[i], a[i])
        m = max(m, s)
    return m