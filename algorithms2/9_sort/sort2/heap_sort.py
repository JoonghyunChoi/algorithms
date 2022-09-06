def heap_sort(a):
    def create_heap(a):
        n = len(a) - 1
        for i in range(n//2, 0, -1):
            downheap(i, n, a)

    def downheap(p, n, a):
        while 2 * p <= n:
            c = 2 * p
            if c < n and a[c] < a[c+1]:
                c += 1
            if a[p] >= a[c]:
                break
            a[p], a[c] = a[c], a[p]
            p = c

    def heap_sort_(a):
        create_heap(a)

        n = len(a) - 1
        for i in range(n):
            a[1], a[n] = a[n], a[1]
            downheap(1, n-1, a)
            n -= 1
        return a
    return heap_sort_(a)