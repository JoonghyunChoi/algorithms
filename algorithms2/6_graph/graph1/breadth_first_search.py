global a, visited
a = []
visited = [False] * len(a)

def bfs(u):
    visited[u] = True
    level = {u: 0}
    previous = {u: u}
    queue = [u]

    while queue:
        u = queue.pop(0)
        for v in a[u]:
            if not visited[v]:
                visited[v] = True
                level[v] = level[u] + 1
                previous[v] = u
                queue.append(v)