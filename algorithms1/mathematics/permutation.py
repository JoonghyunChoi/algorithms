a = []
permutations = []
used = [False] * (len(a)+1)
b = []

# 순열
def permutation(a, k):
    if len(b) == k:
        permutations.append(b.copy())
        return

    for i in range(1, len(a)+1):
        if used[i]:
            continue
        used[i] = True
        b.append(i)
        permutation(a, k)
        used[i] = False
        b.pop()


# 중복순열
def permutation2(a, k):
    if len(b) == k:
        permutations.append(b.copy())
        return

    for i in range(1, len(a)+1):
        b.append(i)
        permutation2(a, k)
        b.pop()