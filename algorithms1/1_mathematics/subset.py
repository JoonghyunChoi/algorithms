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


def subset2(a):
    subsets = [[]]
    for x in a:
        subsets += [subset + [x] for subset in subsets]
    return subsets