import sys
graph = []
N = len(graph)

def prim(s):
    visited = [False] * N
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: s}

    for k in range(N):
        m = -1
        min = sys.maxsize
        for i in range(N):
            if not visited[i] and d[i] < min:
                min = d[i]
                m = i
        visited[m] = True

        for u, w in list(graph[m]):
            if not visited[u]:
                if d[u] > w:
                    d[u] = w
                    previous[u] = m
