import heapq

# 최대힙을 이용한 힙정렬
n = []
def heapSort(n):
    size = len(n) - 1
    createHeap(n)

    for i in range(size):
        n[1], n[size] = n[size], n[1]
        downheap(1, size-1)
        size -= 1

def createHeap(n):
    size = len(n) - 1
    for i in range(size//2, 0, -1):
        downheap(i, size)

def downheap(p, size):
    while p <= size//2:
        c = 2*p

        if c < size and n[c+1] > n[c]:
            c += 1
        if n[p] >= n[c]:
            break
        n[p], n[c] = n[c], n[p]
        p = c


# 최소힙을 이용한 힙정렬
heapq.heapify(n)
s = []
while n:
    s.append(heapq.heappop(n))
