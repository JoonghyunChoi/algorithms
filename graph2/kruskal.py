graph = []
graph.sort(key=lambda x: x[2])
mst = []
p = []
N = 0

def kruskal():
    edges = 0
    cost = 0

    while True:
        if edges == N-1:
            break
        u, v, w = graph.pop(0)
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v))
            cost += w
            edges += 1

for i in range(N):
    p[i] = i

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1
