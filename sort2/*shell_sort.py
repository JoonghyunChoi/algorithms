def shellSort(a):
    h = len(a)//2
    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j-h] > a[j]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h //= 2
