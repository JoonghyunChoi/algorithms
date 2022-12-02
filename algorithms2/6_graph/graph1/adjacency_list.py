def adjacency_list(V, E):  # edge list: a[e] = [u, v, w]
    a = [[] for _ in range(V)]
    for u, v in E:
        a[u].append(v)
        a[v].append(u)