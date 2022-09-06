def transpose1(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

def transpose2(a):
    r, c = len(a), len(a[0])
    b = [[0]*r for _ in range(c)]
    for j in range(c):
        for i in range(r):
            b[j][i] = a[i][j]