# backward direction
def topological_sort(a):
    n = len(a)
    visited = [False] * n
    b = []

    def dfs(u, b):
        visited[u] = True

        for v in a[u]:
            if not visited[v]:
                dfs(v, b)
        b.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i, b)
    return b[::-1]


# forward direction
def topological_sort(a):
    n = len(a)
    queue = []
    indegree = []
    b = []

    for u in range(n):
        if indegree[u] == 0:
            queue.append(u)

    while queue:
        u = queue.pop(0)
        b.append(u)
        for v in a[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return b