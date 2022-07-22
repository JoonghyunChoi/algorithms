a = []
used = [False] * (len(a)+1)
permutations = []

def permutation1(k, a, b):
    if len(b) == k:
        permutations.append(b[:])
        return

    for i in range(1, len(a)+1):
        if not used[i]:
            used[i] = True
            b.append(i)
            permutation1(k, a, b)
            used[i] = False
            b.pop()


def permutation2(k, a, b):
    if len(b) == k:
        permutations.append(b[:])
        return

    for i in range(1, len(a)+1):
        b.append(i)
        permutation2(k, a, b)
        b.pop()