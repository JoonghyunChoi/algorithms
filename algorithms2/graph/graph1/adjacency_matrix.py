def adjacency_matrix(u, v, w, V, E):
    adj = [[0 for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        adj[u][v] = 1
        adj[v][u] = 1