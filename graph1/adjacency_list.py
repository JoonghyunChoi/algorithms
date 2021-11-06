V, E = 0, 0
u, v = 0, 0
adj = [[] for _ in range(V)]

adj[u].append(v), adj[v].append(u)      # [v, w], [u, w]
