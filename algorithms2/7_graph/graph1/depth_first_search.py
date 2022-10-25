global a, visited
a = []
visited = [False] * len(a)

def dfs(u):
    visited[u] = True

    for v in a[u]:
        if not visited[v]:
            dfs(v)


def dfs(u):
    visited[u] = True
    stack = [u]

    while stack:
        u = stack.pop()
        for v in a[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)