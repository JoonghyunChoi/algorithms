def topological_sort(a):
    visited = [False] * len(a)
    b = []

    def dfs(u):
        visited[u] = True

        for v in a[u]:
            if not visited[v]:
                dfs(v)
        b.append(u)

    for i in range(len(a)):
        if not visited[i]:
            dfs(i)
    b.reverse()
    return b