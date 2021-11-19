x = []
chosen = [False] * (len(x)+1)
permutations = []
s = []

def permutation():
    if len(s) == len(x):
        t = s.copy()
        permutations.append(t)
    else:
        for i in range(1, len(x)+1):
            if chosen[i]:
                continue
            chosen[i] = True
            s.append(i)
            permutation()
            chosen[i] = False
            s.pop()
