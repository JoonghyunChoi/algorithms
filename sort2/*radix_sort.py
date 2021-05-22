# LSD 기수정렬
def radixSort(a):
    WIDTH = len(a[0])-1
    N = len(a)
    R = 128
    temp = [None] * N

    for d in range(WIDTH, -1, -1):
        count = [0] * (R+1)
        for i in range(N):
            count[ord(a[i][d])+1] += 1
        for j in range(1, R):
            count[j] += count[j-1]

        for i in range(N):
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N):
            a[i] = temp[i]
