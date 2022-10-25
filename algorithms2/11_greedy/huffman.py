import heapq

class Huffman:
    class Node:
        def __init__(self, char='', frequency=0):
            self.char = char
            self.frequency = frequency
            self.left = None
            self.right = None
    def __init__(self):
        self.chars = {}

    def huffman_tree(self, queue):
        for id in range(1, len(queue)):
            p = heapq.heappop(queue)[2]
            q = heapq.heappop(queue)[2]
            r = self.Node()

            r.left = p
            r.right = q
            r.frequency = p.frequency + q.frequency
            heapq.heappush(queue, (r.frequency, id, r))
        r = heapq.heappop(queue)[2]
        return r

    def huffman_code(self, n, code):
        if n == None:
            return
        self.huffman_code(n.left, code+'0')
        self.huffman_code(n.right, code+'1')

        if n.char != '':
            self.chars[n.char] = (n.frequency, code)

    def __call__(self, queue):
        n = self.huffman_tree(queue)
        self.huffman_code(n, '')

        bits = 0
        for char in self.chars:
            bits += self.chars[char][0] * len(self.chars[char][1])
        return bits