subsets = []
s = []

def subset(n, k):
    if k == len(n)+1:
        subsets.append(s.copy())
    else:
        s.append(k)
        subset(n, k+1)
        s.pop()
        subset(n, k+1)
