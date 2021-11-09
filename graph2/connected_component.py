adj = []
N = len(adj)
visited = [False] * N
CC = []

def dfs(u):
    visited[u] = True
    cc.append(u)

    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        cc = []
        dfs(i)
        CC.append(cc)
