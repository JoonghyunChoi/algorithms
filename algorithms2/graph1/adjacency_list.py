V = 0
u, v, w = 0, 0, 0

adj = [[] for _ in range(V)]
adj[u].append(v)
adj[v].append(u)