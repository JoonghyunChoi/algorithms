V = 0
u, v, w = 0, 0, 0

adj = [[0 for _ in range(V)] for _ in range(V)]
adj[u][v] = 1
adj[v][u] = 1