a = []
n = len(a)
used = [False] * n
b = []
combs = []

def combination1(a, k, idx):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(idx, n):
        if not used[i]:
            used[i] = True
            b.append(a[i])
            combination1(a, k, i+1)
            b.pop()
            used[i] = False


def combination2(a, k, idx):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(idx, n):
        b.append(a[i])
        combination2(a, k, i)
        b.pop()