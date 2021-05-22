V, E = 0, 0
v, w = 0, 0
i = 0
adj = [[0 for _ in range(V)] for _ in range(V)]

adj[i][v], adj[v][i] = 1, 1
adj[i][v], adj[v][i] = w, w
