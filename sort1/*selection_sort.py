def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
