def adjacency_list(u, v, V, E):
    a = [[] for _ in range(V)]
    for _ in range(E):
        a[u].append(v)
        a[v].append(u)


def edge_list(u, v, e, E):
    a = [[] for _ in range(E)]
    for _ in range(E):
        a[e].append([(u, v)])