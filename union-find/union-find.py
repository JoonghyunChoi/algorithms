p = []
level = []

for i in range(len(p)):
    p[i] = i
    level[i] = 1

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    u = find(u)
    v = find(v)

    if level[u] > level[v]:
        u, v = v, u
    p[u] = v

    if level[u] == level[v]:
        level[v] += 1
