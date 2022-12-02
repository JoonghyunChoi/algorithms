def kruskal(n, a):
    def _kruskal(n, a):
        global p
        p = list(range(n))
        a.sort(key=lambda x: x[2])
        mst, edges, cost = [], 0, 0

        while edges != n-1:
            u, v, w = a.pop(0)
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v))
                cost += w
                edges += 1
        return cost

    def find(u):
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1
    return _kruskal(n, a)