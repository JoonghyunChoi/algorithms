import sys

G = []
N = len(G)

def bellman_ford(s):
    d = [sys.maxsize] * N
    d[s] = 0
    previous = {0: None}

    for k in range(N - 1):
        for u in range(N):
            for v, w in list(G[u]):
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    previous[v] = u

    for u in range(N):
        for v, w in list(G[u]):
            if d[v] > d[u] + w:
                return False
