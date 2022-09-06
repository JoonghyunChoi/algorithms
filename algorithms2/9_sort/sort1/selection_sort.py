def selection_sort(a):
    n = len(a)
    for i in range(0, n):
        min_ = i
        for j in range(i+1, n):
            if a[j] < a[min_]:
                min_ = j
        a[i], a[min_] = a[min_], a[i]
    return a