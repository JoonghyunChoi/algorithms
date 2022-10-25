global b, n, used, perms
a, b = [], []
n = len(a)
used = [False] * n
perms = []

def perm1(a, k):
    if len(b) == k:
        perms.append(b[:])
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            b.append(a[i])
            perm1(a, k)
            b.pop()
            used[i] = False


def perm2(a, k):
    if len(b) == k:
        perms.append(b[:])
        return

    for i in range(n):
        b.append(a[i])
        perm2(a, k)
        b.pop()