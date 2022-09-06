def topological_sort1(s, a):
    visited = [False] * len(a)
    b = []

    def dfs(u):
        visited[u] = True
        for v in a[u]:
            if not visited[v]:
                dfs(v)
        b.append(u)
    dfs(s)
    b.reverse()
    return b


def topological_sort2(a, indegree):
    queue = []
    b = []
    for u in range(len(a)+1):
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