def bellman_ford(s, a):
    n = len(a)
    inf = float('inf')
    d = [inf] * n
    d[s] = 0
    previous = {s: s}

    for _ in range(n-1):
        for u in range(n):
            for v, w in a[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    previous[v] = u

    for u in range(n):
        for v, w in a[u]:
            if d[u] + w < d[v]:
                return False