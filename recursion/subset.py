x = []
subsets = []
s = []

def subset(k):
    if k == len(x)+1:
        t = s.copy()
        subsets.append(t)
    else:
        s.append(k)
        subset(k+1)
        s.pop()
        subset(k+1)
