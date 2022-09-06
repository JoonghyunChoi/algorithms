def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1):   # (n-1, -1, -1)
        for j in range(0, n-1-i):   # (0, i)
            if a[j+1] < a[j]:
                a[j], a[j+1] = a[j+1], a[j]
    return a