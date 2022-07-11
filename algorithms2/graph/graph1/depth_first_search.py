a = []
N = len(a)
visited = [False] * N

def dfs(u):
    visited[u] = True

    for v in a[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        dfs(i)


def dfs2(u):
    visited[u] = True
    stack = [u]

    while stack:
        u = stack.pop(-1)
        for v in a[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

for i in range(N):
    if not visited[i]:
        dfs2(i)