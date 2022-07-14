def connected_component(a):
    visited = [False] * len(a)
    CCs = []

    def dfs(u):
        visited[u] = True
        CC.append(u)

        for v in a[u]:
            if not visited[v]:
                dfs(v)

    for i in range(len(a)):
        if not visited[i]:
            CC = []
            dfs(i)
            CCs.append(CC)
    return CCs