adj = []
N = len(adj)
visited = [False] * N

def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        dfs(i)
