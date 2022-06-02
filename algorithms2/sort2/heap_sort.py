# 최대힙을 이용한 힙정렬
a = []
def heapSort(a):
    N = len(a) - 1
    for i in range(N//2, 0, -1):
        downheap(i, N)

    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)
        N -= 1

def downheap(p, N):
    while p <= N//2:
        c = 2 * p

        if c < N and a[c+1] > a[c]:
            c += 1
        if a[p] >= a[c]:
            break
        a[p], a[c] = a[c], a[p]
        p = c