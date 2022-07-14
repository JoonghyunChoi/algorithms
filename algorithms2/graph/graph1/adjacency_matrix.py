def adjacency_matrix(u, v, V, E):
    a = [[0 for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        a[u][v] = 1
        a[v][u] = 1