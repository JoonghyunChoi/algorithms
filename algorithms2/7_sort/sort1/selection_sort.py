def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a