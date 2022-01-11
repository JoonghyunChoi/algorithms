n = []
combinations = []
used = [False] * (len(n)+1)
s = []

# 조합
def combination1(n, r):
    if len(s) == r:
        combinations.append(s.copy())
        return

    index = 0 if len(s) == 0 else s[-1]
    for i in range(index+1, len(n)+1):
        if used[i]:
            continue
        used[i] = True
        s.append(i)
        combination1(n, r)
        used[i] = False
        s.pop()


# 중복조합
def combination2(n, r):
    if len(s) == r:
        combinations.append(s.copy())
        return

    index = 1 if len(s) == 0 else s[-1]
    for i in range(index, len(n)+1):
        s.append(i)
        combination2(n, r)
        s.pop()
