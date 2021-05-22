G = []
G.sort(key=lambda x: x[2])
mst = []
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

while len(mst) < len(G)-1:
    u, v, w = G.pop(0)
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, w))
