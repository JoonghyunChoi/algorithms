class Heap:
    def __init__(self, a):
        self.a = a
        self.n = len(a) - 1

    def createHeap(self):
        for i in range(self.n//2, 0, -1):
            self.downheap(i)

    def insert(self, item):
        self.n += 1
        self.a.append(item)
        self.upheap(self.n)

    def deleteMin(self):
        if self.n == 0:
            return None

        min = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.n -= 1

        self.downheap(1)
        return min


    def downheap(self, i):
        while i <= self.n//2:
            k = 2*i
            if k < self.n and self.a[k][0] > self.a[k+1][0]:
                k += 1

            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    def upheap(self, j):
        while j > 1 and self.a[j//2][0] > self.a[j][0]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2

    def print(self):
        for i in range(1, self.n+1):
            print(self.a[i][0], self.a[i][1], end=' ')
