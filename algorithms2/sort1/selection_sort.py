def selectionSort(n):
    for i in range(0, len(n)-1):
        min = i
        for j in range(i+1, len(n)):
            if n[min] > n[j]:
                min = j
        n[i], n[min] = n[min], n[i]
