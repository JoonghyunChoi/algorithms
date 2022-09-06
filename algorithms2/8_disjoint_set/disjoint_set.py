class DisjointSet:
    def __init__(self, a):
        global p
        p = list(range(len(a)))

    def find(self, u):
        if u != p[u]:
            p[u] = self.find(p[u])
        return p[u]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        p[root2] = root1