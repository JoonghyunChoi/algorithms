def insertionSort(a):
    for i in range(0, len(a)-1, 1):
        for j in range(i, -1, -1):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]