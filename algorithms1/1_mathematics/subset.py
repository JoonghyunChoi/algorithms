global b, n, subsets
a, b = [], []
n = len(a)
subsets = []

def subset(a, s):
    if s == n:
        subsets.append(b[:])
        return

    b.append(a[s])
    subset(a, s+1)
    b.pop()
    subset(a, s+1)