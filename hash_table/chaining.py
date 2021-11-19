class Chaining:
    class Node:
        def __init__(self, key, item, next):
            self.key = key
            self.item = item
            self.next = next

    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * size


    def hash(self, key):
        return key % self.size

    def put(self, key, item):
        h = self.hash(key)
        p = self.hashTable[h]
        while p != None:
            if key == p.key:
                p.item = item
                return
            p = p.next
        self.hashTable[h] = self.Node(key, item, self.hashTable[h])

    def get(self, key):
        h = self.hash(key)
        p = self.hashTable[h]
        while p != None:
            if key == p.key:
                return p.item
            p = p.next
        return None


  # delete()

    def print(self):
        for i in range(self.size):
            print(i)
            p = self.hashTable[i]
            while p != None:
                print(p.key, p.item, end=' ')
                p = p.next
            print()
