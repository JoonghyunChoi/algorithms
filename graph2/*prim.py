import sys
G = []
N = len(G)

def prim(s):
    visited = [False] * N
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {s: 0}

    for k in range(N):
        m = -1
        min = sys.maxsize
        for i in range(N):
            if not visited[i] and d[i] < min:
                min = d[i]
                m = i
        visited[m] = True

        for v, w in list(G[m]):
            if not visited[v]:
                if w < d[v]:
                    d[v] = w
                    previous[v] = m
