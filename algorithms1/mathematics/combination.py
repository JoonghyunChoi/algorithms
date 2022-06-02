a = [1, 2, 3]
combinations = []
used = [False] * (len(a)+1)
b = []

# 조합
def combination1(a, r):
    if len(b) == r:
        combinations.append(b.copy())
        return

    i = 0 if len(b) == 0 else b[-1]
    for j in range(i+1, len(a)+1):
        if used[j]:
            continue
        used[j] = True
        b.append(j)
        combination1(a, r)
        used[j] = False
        b.pop()


# 중복조합
def combination2(a, r):
    if len(b) == r:
        combinations.append(b.copy())
        return

    i = 1 if len(b) == 0 else b[-1]
    for j in range(i, len(a)+1):
        b.append(j)
        combination2(a, r)
        b.pop()