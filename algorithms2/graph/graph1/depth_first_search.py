a = []
visited = [False] * len(a)

def dfs(u, a):
    visited[u] = True
    for v in a[u]:
        if not visited[v]:
            dfs(v, a)


def dfs2(s, a):
    visited[s] = True
    stack = [s]

    while stack:
        u = stack.pop(-1)
        for v in a[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)