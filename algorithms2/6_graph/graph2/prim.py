def prim(s, a):
    n = len(a)
    visited = [False] * n
    inf = float('inf')
    d = [inf] * n
    d[s] = 0
    previous = {s: s}

    for _ in range(n):
        u = -1
        m = inf
        for i in range(n):
            if not visited[i] and d[i] < m:
                m = d[i]
                u = i
        visited[u] = True  # u is in MST

        for v, w in a[u]:  # v in not in MST
            if not visited[v] and w < d[v]:
                d[v] = w
                previous[v] = u