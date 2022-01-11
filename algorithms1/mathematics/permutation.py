n = []
permutations = []
used = [False] * (len(n)+1)
s = []

# 순열
def permutation1(n, r):
    if len(s) == r:
        permutations.append(s.copy())
        return

    for i in range(1, len(n)+1):
        if used[i]:
            continue
        used[i] = True
        s.append(i)
        permutation1(n, r)
        used[i] = False
        s.pop()


# 중복순열
def permutation2(n, r):
    if len(s) == r:
        permutations.append(s.copy())
        return

    for i in range(1, len(n)+1):
        s.append(i)
        permutation2(n, r)
        s.pop()
