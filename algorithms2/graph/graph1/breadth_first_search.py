a = []
visited = [False] * len(a)

def bfs(s, a):
    visited[s] = True
    distance = {s: 0}
    previous = {s: None}
    queue = [s]

    while queue:
        u = queue.pop(0)
        for v in a[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                previous[v] = u
                queue.append(v)


def bfs2(q):
    if not q:
        return

    u = q.pop(0)
    for v in a[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)
    bfs2(q)