subsets = []

def subset(k, n, b):
    if k == n+1:
        subsets.append(b[:])
        return
    b.append(k)
    subset(k+1, n, b)
    b.pop()
    subset(k+1, n, b)