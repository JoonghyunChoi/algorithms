def floyd_warshall(a):
    N = len(a)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
    return a