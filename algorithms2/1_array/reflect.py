def reflect1(a):
    n = len(a)
    for i in range(0, n//2):
        a[i], a[n-1-i] = a[n-1-i], a[i]

def reflect2(a):
    n = len(a)
    for i in range(n):
        for j in range(n//2):
            a[i][j], a[i][-1-j] = a[i][-1-j], a[i][j]