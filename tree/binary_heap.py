# 최소힙
class BinaryHeap:
    def __init__(self, n):
        self.n = n
        self.size = len(n) - 1

    def createHeap(self):
        for i in range(self.size//2, 0, -1):        # (size//2)+1부터는 이파리들
            self.downheap(i)

    def insert(self, item):
        self.size += 1
        self.n.append(item)
        self.upheap(self.size)

    def deleteMin(self):
        if self.size == 0:
            return None
        min = self.n[1]
        self.n[1], self.n[-1] = self.n[-1], self.n[1]
        del self.n[-1]
        self.size -= 1
        self.downheap(1)
        return min


    def downheap(self, p):
        while p <= self.size//2:
            c = 2*p

            if c < self.size and self.n[c+1][0] < self.n[c][0]:
                c += 1
            if self.n[p][0] < self.n[c][0]:
                break
            self.n[p], self.n[c] = self.n[c], self.n[p]
            p = c

    def upheap(self, c):
        p = c//2

        while c > 1 and self.n[c][0] < self.n[p][0]:
            self.n[c], self.n[p] = self.n[p], self.n[c]
            c = p

    def print(self):
        for i in range(1, self.size+1):
            print(self.n[i][0], self.n[i][1], end=' ')
