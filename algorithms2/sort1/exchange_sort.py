def exchangeSort(n):
    for i in range(0, len(n)-1):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
