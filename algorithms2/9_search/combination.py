global n, b, used, combs
a = []
n = len(a)
b = []
used = [False] * n
combs = []

def comb1(a, idx, k):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(idx, n):
        if not used[i]:
            b.append(a[i])
            used[i] = True
            comb1(a, i+1, k)
            b.pop()
            used[i] = False


def comb2(a, idx, k):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(idx, n):
        b.append(a[i])
        comb2(a, i, k)
        b.pop()