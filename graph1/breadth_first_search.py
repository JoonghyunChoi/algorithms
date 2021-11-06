# 큐를 이용한 BFS
adj = []
N = len(adj)
visited = [False] * N
distance = {}
previous = {}

def bfs(v):
    queue = []
    visited[v] = True
    queue.append(v)

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                distance[u] = distance[v] + 1
                previous[u] = v
                queue.append(u)

for i in range(N):
    if not visited[i]:
        distance[i] = 0
        previous[i] = None
        bfs(i)


# 재귀를 이용한 BFS
def bfs(q):
    if not q:
        return

    v = q.pop(0)
    for u in adj[v]:
        if not visited[u]:
            visited[u] = True
            distance[u] = distance[v] + 1
            previous[u] = v
            q.append(u)
    bfs(q)

q = []
for i in range(N):
    if not visited[i]:
        visited[i] = True
        distance[i] = 0
        previous[i] = None
        q.append(i)
        bfs(q)
