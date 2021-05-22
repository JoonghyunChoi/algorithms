adj = []
N = len(adj)
visited = [False] * N

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
