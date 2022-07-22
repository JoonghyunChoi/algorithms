a = []
used = [False] * (len(a)+1)
combinations = []

def combination1(k, a, b):
    if len(b) == k:
        combinations.append(b[:])
        return

    i = 0 if len(b) == 0 else b[-1]
    for j in range(i+1, len(a)+1):
        if not used[j]:
            used[j] = True
            b.append(j)
            combination1(k, a, b)
            used[j] = False
            b.pop()


def combination2(k, a, b):
    if len(b) == k:
        combinations.append(b[:])
        return

    i = 1 if len(b) == 0 else b[-1]
    for j in range(i, len(a)+1):
        b.append(j)
        combination2(k, a, b)
        b.pop()