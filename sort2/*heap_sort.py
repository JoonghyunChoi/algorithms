import heapq

# 최대힙을 이용한 힙정렬
a = []
def heapSort(a):
    createHeap(a)
    print(a)
    N = len(a) - 1

    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)
        N -= 1

def createHeap(a):
    N = len(a) - 1
    for i in range(N//2, 0, -1):
        downheap(i, N)

def downheap(i, size):
    while i <= size//2:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1

        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k


# 최소힙을 이용한 힙정렬
heapq.heapify(a)
s = []
while a:
    s.append(heapq.heappop(a))
