col = {}
count = 0

def queens(i, n):
    global col, count
    for j in range(1, n+1):
        col[i+1] = j
        if promising(i+1):
            if i+1 == n:
                count = count + 1
            else:
                queens(i+1, n)

def promising(i):
    global col
    k = 1
    switch = True
    while (k < i and switch):
        if (col[i] == col[k] or abs(col[i] - col[k]) == i - k):
            switch = False
        k = k + 1
    return switch
