import sys

graph = []

def bellmanFord(s):
    N = len(graph)
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}

    for _ in range(N-1):
        for u in range(N):
            for v, w in graph[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    previous[v] = u

    for u in range(N):
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                return False