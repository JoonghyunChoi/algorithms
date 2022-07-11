a = []
N = len(a)
visited = [False] * N
distance = {}
previous = {}

def bfs(u):
    visited[u] = True
    queue = [u]

    while queue:
        u = queue.pop(0)
        for v in a[u]:
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


q = []
def bfs2(q):
    if not q:
        return

    u = q.pop(0)
    for v in a[u]:
        if not visited[v]:
            visited[v] = True
            distance[v] = distance[u] + 1
            previous[v] = u
            q.append(v)
    bfs2(q)

for i in range(N):
    if not visited[i]:
        visited[i] = True
        distance[i] = 0
        previous[i] = None
        q.append(i)
        bfs2(q)