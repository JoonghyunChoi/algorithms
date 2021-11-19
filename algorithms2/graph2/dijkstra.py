import sys
import heapq

def dijkstra(s, graph):
    N = len(graph)
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}
    heap = []
    heapq.heappush(heap, (d[s], s))

    while heap:
        t, u = heapq.heappop(heap)
        d[u] = t
        for v, w in list(graph[u]):
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                previous[v] = u
                heapq.heappush(heap, (d[v], v))
