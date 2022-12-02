def adjacency_matrix(V, E):
    a = [[0] * V for _ in range(V)]
    for u, v in E:
        a[u][v] = 1
        a[v][u] = 1