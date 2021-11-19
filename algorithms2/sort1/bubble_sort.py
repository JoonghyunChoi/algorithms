def bubbleSort(n):
    for i in range(0, len(n)-1):
        for j in range(0, len(n)-1-i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
