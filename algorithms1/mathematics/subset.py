subsets = []
b = []

def subset(a, k):
    if k == len(a) + 1:
        subsets.append(b.copy())
    else:
        b.append(k)
        subset(a, k+1)
        b.pop()
        subset(a, k+1)