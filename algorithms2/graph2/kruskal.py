graph = []
graph.sort(key=lambda x: x[2])

def kruskal(n):
    mst = []
    tree_edges = 0
    mst_cost = 0

    while True:
        if tree_edges == n-1:
            break
        u, v, w = graph.pop(0)
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v))
            mst_cost += w
            tree_edges += 1

p = []
for i in range(len(graph)):
    p[i] = i

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1