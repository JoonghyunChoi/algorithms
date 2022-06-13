adj = []
N = len(adj)
visited = [False] * N
CCs = []

def dfs(u):
    visited[u] = True
    CC.append(u)

    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        CC = []
        dfs(i)
        CCs.append(CC)