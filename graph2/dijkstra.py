import sys
import heapq

G = []
N = len(G)

def dijkstra(s):
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {0: None}
    heap = []
    heapq.heappush(heap, (d[s], s))

    while heap:
        t, u = heapq.heappop(heap)
        d[u] = t
        for v, w in list(G[u]):
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                previous[v] = u
                heapq.heappush(heap, (d[v], v))
