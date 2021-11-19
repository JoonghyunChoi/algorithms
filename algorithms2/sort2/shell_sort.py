def shellSort(n):
    h = len(n)//2
    while h >= 1:
        for i in range(h, len(n)):              # h-sort
            j = i
            while j >= h and n[j-h] > n[j]:
                n[j], n[j-h] = n[j-h], n[j]
                j -= h
        h //= 2
