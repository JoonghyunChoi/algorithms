V, E = 0, 0
u, v = 0, 0
adj = [[0 for _ in range(V)] for _ in range(V)]

adj[u][v], adj[v][u] = 1, 1     # w, w
