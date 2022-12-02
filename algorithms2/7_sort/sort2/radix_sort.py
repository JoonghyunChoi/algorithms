def lsd_sort(a):
    length = len(a[0])
    n = len(a)
    r = 128
    b = [None] * n

    for d in range(length-1, -1, -1):
        count = [0] * (r+1)
        for i in range(n):
            count[ord(a[i][d])+1] += 1
        for j in range(1, r):
            count[j] += count[j-1]

        for i in range(n):
            p = ord(a[i][d])
            b[count[p]] = a[i]
            count[p] += 1

        for i in range(n):
            a[i] = b[i]
    return a