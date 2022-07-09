D = []
N = len(D)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]