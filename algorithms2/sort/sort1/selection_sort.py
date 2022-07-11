def selection_sort(a):
    for i in range(0, len(a)-1):
        min_ = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_]:
                min_ = j
        a[i], a[min_] = a[min_], a[i]
    return a