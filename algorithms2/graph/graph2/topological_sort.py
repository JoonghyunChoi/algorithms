a = []
N = len(a)
visited = [False] * N
b = []

def dfs(u):
    visited[u] = True

    for v in a[u]:
        if not visited[v]:
            dfs(v)
    b.append(u)

for i in range(N):
    if not visited[i]:
        dfs(i)
b.reverse()