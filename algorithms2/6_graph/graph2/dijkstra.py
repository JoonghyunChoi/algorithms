import heapq

def dijkstra(s, a):
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
        visited[u] = True  # u is in SP

        for v, w in a[u]:
            if not visited[v] and d[u] + w < d[v]:
                d[v] = d[u] + w
                previous[v] = u


def dijkstra(s, a):
    n = len(a)
    inf = float('inf')
    d = [inf] * n
    d[s] = 0
    previous = {s: s}
    heap = []
    heapq.heappush(heap, (d[s], s))

    while heap:
        _, u = heapq.heappop(heap)
        for v, w in a[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                previous[v] = u
                heapq.heappush(heap, (d[v], v))