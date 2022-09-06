def exchange_sort(a):
    n = len(a)
    for i in range(0, n):
        for j in range(i+1, n):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
    return a