import heapq

class Node:
    def __init__(self, char = '', frequency = 0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

heap = []
code = {}
def huffman(n):
    for i in range(n-1):
        p = heapq.heappop(heap)[2]
        q = heapq.heappop(heap)[2]

        r = Node()
        r.left = p
        r.right = q
        r.frequency = p.frequency + q.frequency
        heapq.heappush(heap, (r.frequency, n+i, r))

    r = heapq.heappop(heap)[2]
    return r

def traversal(n, s):
    if n == None:
        return

    traversal(n.left, s + '0')
    traversal(n.right, s + '1')
    if n.char != '':
        code[n.char] = (n.frequency, s)

def bits():
    n = len(heap)
    traversal(huffman(n), '')

    bits = 0
    for i in code:
        bits += code[i][0] * len(code[i][1])
    return bits
