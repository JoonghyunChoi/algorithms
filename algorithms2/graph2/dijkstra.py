import sys
import heapq

graph = []

def dijkstra1(s):
    N = len(graph)
    visited = [False] * N
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}

    for _ in range(N):
        m = -1
        min = sys.maxsize
        for i in range(N):
            if not visited[i] and d[i] < min:
                min = d[i]
                m = i
        visited[m] = True

        for u, w in graph[m]:
            if not visited[u]:
                if d[m] + w < d[u]:
                    d[u] = d[m] + w
                    previous[u] = m


def dijkstra2(s):
    d = [sys.maxsize] * len(graph)
    d[s] = 0
    previous = {s: s}
    queue = []
    heapq.heappush(queue, (d[s], s))

    while queue:
        d_u, u = heapq.heappop(queue)
        for v, w in graph[u]:
            if d_u + w < d[v]:
                d[v] = d_u + w
                previous[v] = u
                heapq.heappush(queue, (d[v], v))