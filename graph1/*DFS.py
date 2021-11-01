# 재귀를 이용한 DFS
adj = []
N = len(adj)
visited = [False] * N
def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

for i in range(N):
    if not visited[i]:
        dfs(i)


# 스택을 이용한 DFS
def dfs(u):
    stack = []
    stack.append(u)

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.extend(adj[v])

for i in range(N):
    if not visited[i]:
        dfs(i)
