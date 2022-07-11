def heap_sort(a):
    N = len(a) - 1
    for i in range(N//2, 0, -1):
        downheap(i, N, a)

    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1, a)
        N -= 1

def downheap(p, N, a):
    while p <= N//2:
        c = 2 * p

        if c < N and a[c+1] > a[c]:
            c += 1
        if a[p] >= a[c]:
            break
        a[p], a[c] = a[c], a[p]
        p = c