a = []
n = len(a)
used = [False] * n
b = []
perms = []

def permutation1(a, k):
    if len(b) == k:
        perms.append(b[:])
        return

    for i in range(0, n):
        if not used[i]:
            used[i] = True
            b.append(a[i])
            permutation1(a, k)
            b.pop()
            used[i] = False


def permutation2(a, k):
    if len(b) == k:
        perms.append(b[:])
        return

    for i in range(0, n):
        b.append(a[i])
        permutation2(a, k)
        b.pop()