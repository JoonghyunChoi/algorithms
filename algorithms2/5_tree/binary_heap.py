class BinaryHeap:
    def __init__(self, a):
        self.a = a
        self.n = len(a)-1

    def create_heap(self):
        for i in range(self.n//2, 0, -1):   # root index = 1, (n//2)+1부터 leaf
            self.downheap(i)

    def insert(self, x):
        self.n += 1
        self.a.append(x)
        self.upheap(self.n)

    def delete_min(self):
        if self.n == 0:
            return None
        m = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]

        del self.a[-1]
        self.n -= 1
        self.downheap(1)
        return m

    def downheap(self, p):
        while 2 * p <= self.n:
            c = 2 * p
            if c < self.n and self.a[c][0] > self.a[c+1][0]:
                c += 1
            if self.a[p][0] < self.a[c][0]:
                break
            self.a[p], self.a[c] = self.a[c], self.a[p]
            p = c

    def upheap(self, c):
        p = c // 2
        while c > 1 and self.a[p][0] > self.a[c][0]:
            self.a[c], self.a[p] = self.a[p], self.a[c]
            c = p