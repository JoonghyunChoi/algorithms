adj = []
N = len(adj)
visited = [False] * N
order = []

def dfs(u):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs(v)
    order.append(u)

for i in range(N):
    if not visited[i]:
        dfs(i)
order.reverse()
