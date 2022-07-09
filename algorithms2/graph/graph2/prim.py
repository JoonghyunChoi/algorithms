import sys

graph = []

def prim(s):
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
                if w < d[u]:
                    d[u] = w
                    previous[u] = m