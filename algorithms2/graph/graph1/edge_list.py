def edge_list(u, v, w, e, E):
    edges = [[] for _ in range(E)]
    for _ in range(E):
        edges[e].append([(u, v)])