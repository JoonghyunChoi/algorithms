import heapq

class Node:
    def __init__(self, char='', frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None
chars = {}

def huffman(heap):
    n = huffmanTree(heap)

    huffmanCode(n, '')

    bits = 0
    for i in chars:
        bits += chars[i][0] * len(chars[i][1])
    return bits

def huffmanTree(heap):
    for id in range(1, len(heap)):
        p = heapq.heappop(heap)[2]
        q = heapq.heappop(heap)[2]

        r = Node()
        r.left = p
        r.right = q
        r.frequency = p.frequency + q.frequency

        heapq.heappush(heap, (r.frequency, id, r))
    r = heapq.heappop(heap)[2]
    return r

def huffmanCode(n, code):
    if n == None:
        return

    huffmanCode(n.left, code + '0')
    huffmanCode(n.right, code + '1')
    if n.char != '':
        chars[n.char] = (n.frequency, code)
