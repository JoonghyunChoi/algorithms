def kadane(a):
    n = len(a)
    s = m = 0
    for i in range(n):
        s = max(0, s+a[i])
        m = max(m, s)
    return m