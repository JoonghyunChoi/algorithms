a = []
permutations = []
used = [False] * (len(a)+1)
b = []

# 순열
def permutation1(a, r):
    if len(b) == r:
        permutations.append(b.copy())
        return

    for i in range(1, len(a)+1):
        if used[i]:
            continue
        used[i] = True
        b.append(i)
        permutation1(a, r)
        used[i] = False
        b.pop()


# 중복순열
def permutation2(a, r):
    if len(b) == r:
        permutations.append(b.copy())
        return

    for i in range(1, len(a)+1):
        b.append(i)
        permutation2(a, r)
        b.pop()