def adjacency_list(u, v, w, V, E):
    adj = [[] for _ in range(V)]
    for _ in range(E):
        adj[u].append(v)
        adj[v].append(u)