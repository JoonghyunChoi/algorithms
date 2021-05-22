class Chaining:
    class Node:
        def __init__(self, key, item, next):
            self.key = key
            self.item = item
            self.next = next

    def __init__(self, size):
        self.m = size
        self.T = [None] * size

    def hash(self, key):
        return key % self.m

    def put(self, key, item):
        i = self.hash(key)
        p = self.T[i]
        while p != None:
            if key == p.key:
                p.item = item
                return
            p = p.next

        self.T[i] = self.Node(key, item, self.T[i])

    def get(self, key):
        i = self.hash(key)
        p = self.T[i]
        while p != None:
            if key == p.key:
                return p.item
            p = p.next
        return None

  # delete()

    def print(self):
        for i in range(self.m):
            print(i)

            p = self.T[i]
            while p != None:
                print(p.key, p.item, end=' ')
                p = p.next
            print()
