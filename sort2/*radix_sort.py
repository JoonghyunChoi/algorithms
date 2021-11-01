# LSD 기수정렬
def radixSort1(n):
    stringWidth = len(n[0])
    R = 128
    N = len(n)
    s = [None] * N

    for d in range(stringWidth-1, -1, -1):
        count = [0] * (R+1)
        for i in range(N):
            count[ord(n[i][d])+1] += 1
        for r in range(1, R):
            count[r] += count[r-1]

        for i in range(N):
            t = ord(n[i][d])
            s[count[t]] = n[i]
            count[t] += 1

        for i in range(N):
            n[i] = s[i]


# MSD 기수정렬
def radixSort2(n, low, high, d):
    R = 256
    N = len(n)
    s = [0] * N

    if high <= low:
        return
    count = [0] * (R+2)
    for i in range(low, high+1):
        count[pop(n[i], d)+2] += 1
    for r in range(0, R+1):
        count[r+1] += count[r]
    for i in range(low, high+1):
        t = pop(n[i], d)
        s[count[t]+1] = n[i]
        count[t] += 1

    for i in range(low, high+1):
        n[i] = s[i-low]
    for r in range(0, R+1):
        radixSort2(n, low + count[r], low + count[r+1] - 1, d+1)

def pop(str, d):
    if d < len(str):
        return ord(str.pop(d))
    else:
        return -1
