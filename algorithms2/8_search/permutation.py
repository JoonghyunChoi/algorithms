global n, b, used, perms
a = []
n = len(a)
b = []
used = [False] * n
perms = []

def perm1(a, k):
    if len(b) == k:
        perms.append(b[:])
        return

    for i in range(n):
        if not used[i]:
            b.append(a[i])
            used[i] = True
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