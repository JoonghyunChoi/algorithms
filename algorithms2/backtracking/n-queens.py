col = {}
queens = []

def nQueens(i, n):
    if promising(i):
        if i == n:
            for k in range(1, n+1):
                queens.append(col[k])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                nQueens(i+1, n)

# col[i]는 i행에 있는 여왕말의 열
def promising(i):
    k = 1
    check = True
    while k < i and check:
        if col[i] == col[k] or abs(col[i]-col[k]) == i - k:
            check = False
        k += 1
    return check