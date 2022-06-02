# 큐를 이용한 BFS
adj = []
N = len(adj)
visited = [False] * N
distance = {}
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
                distance[v] = distance[u] + 1
                previous[v] = u
                queue.append(v)

for i in range(N):
    if not visited[i]:
        distance[i] = 0
        previous[i] = None
        bfs(i)


# 재귀를 이용한 BFS
q = []

def bfs(q):
    if not q:
        return

    u = q.pop(0)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            distance[v] = distance[u] + 1
            previous[v] = u
            q.append(v)
    bfs(q)

for i in range(N):
    if not visited[i]:
        visited[i] = True
        distance[i] = 0
        previous[i] = None
        q.append(i)
        bfs(q)