# 재귀를 이용한 DFS
adj = []
N = len(adj)
visited = [False] * N
def dfs(v):
    visited[v] = True

    for u in adj[v]:
        if not visited[u]:
            dfs(u)

for i in range(N):
    if not visited[i]:
        dfs(i)


# 스택을 이용한 DFS
def dfs(v):
    stack = []
    visited[v] = True
    stack.append(v)

    while stack:
        v = stack.pop()
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)

for i in range(N):
    if not visited[i]:
        dfs(i)
