import sys
import heapq

def dijkstra(s, a):
    N = len(a)
    visited = [False] * N
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}

    for _ in range(N):
        m = -1
        min_ = sys.maxsize
        for i in range(N):
            if not visited[i] and d[i] < min_:
                min_ = d[i]
                m = i
        visited[m] = True

        for u, w in a[m]:
            if not visited[u]:
                if d[m] + w < d[u]:
                    d[u] = d[m] + w
                    previous[u] = m


def dijkstra2(s, a):
    d = [sys.maxsize] * len(a)
    d[s] = 0
    previous = {s: s}
    queue = []
    heapq.heappush(queue, (d[s], s))

    while queue:
        d_u, u = heapq.heappop(queue)
        for v, w in a[u]:
            if d_u + w < d[v]:
                d[v] = d_u + w
                previous[v] = u
                heapq.heappush(queue, (d[v], v))