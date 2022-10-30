global n, b, subsets
a = []
n = len(a)
b = []
subsets = []

def subset(a, idx):
    if idx == n:
        subsets.append(b[:])
        return

    b.append(a[idx])
    subset(a, idx+1)
    b.pop()
    subset(a, idx+1)