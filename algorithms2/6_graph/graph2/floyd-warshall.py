def floyd_warshall(a):
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = min(a[i][j], a[i][k]+a[k][j])
    return a