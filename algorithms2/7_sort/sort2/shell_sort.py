def shell_sort(a):
    n = len(a)
    h = n // 2
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h //= 2
    return a