class Chaining:
    class Node:
        def __init__(self, key, value, next):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        h = self.hash(key)
        p = self.hash_table[h]
        while p:
            if key == p.key:
                p.value = value
                return
            p = p.next
        self.hash_table[h] = self.Node(key, value, self.hash_table[h])

    def get(self, key):
        h = self.hash(key)
        p = self.hash_table[h]
        while p:
            if key == p.key:
                return p.value
            p = p.next
        return None