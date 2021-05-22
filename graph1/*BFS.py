adj = []
N = len(adj)
visited = [False] * N
level = {}
previous = {}

def bfs(u):
    queue = []
    visited[u] = True
    queue.append(u)

    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                previous[v] = u
                level[v] = level[u] + 1
                queue.append(v)

for i in range(N):
    if not visited[i]:
        level[i] = 0
        previous[i] = None
        bfs(i)
