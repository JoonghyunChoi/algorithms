adj = []
N = len(adj)
visited = [False] * N
connected_components = []

def dfs(u):
    visited[u] = True
    connected_component.append(u)

    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        connected_component = []
        dfs(i)
        connected_components.append(connected_component)