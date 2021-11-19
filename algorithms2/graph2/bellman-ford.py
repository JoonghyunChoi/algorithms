import sys

def bellmanFord(s, graph):
    N = len(graph)
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}

    for k in range(N-1):
        for u in range(N):
            for v, w in list(graph[u]):
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    previous[v] = u

    for u in range(N):
        for v, w in list(graph[u]):
            if d[v] > d[u] + w:
                return False
