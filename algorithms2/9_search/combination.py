global b, n, used, combs
a, b = [], []
n = len(a)
used = [False] * n
combs = []

def comb1(a, k, s):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(s, n):
        if not used[i]:
            used[i] = True
            b.append(a[i])
            comb1(a, k, i+1)
            b.pop()
            used[i] = False


def comb2(a, k, s):
    if len(b) == k:
        combs.append(b[:])
        return

    for i in range(s, n):
        b.append(a[i])
        comb2(a, k, i)
        b.pop()