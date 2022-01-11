class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Slist:
    def __init__(self):
        self.head = None
        self.size = 0


    def insertBefore(self, item):
        if self.size == 0:
            self.head = Node(item, None)
        else:
            self.head = Node(item, self.head)
        self.size += 1

    def insertAfter(self, item, prev):
        prev.next = Node(item, prev.next)
        self.size += 1


    def deleteBefore(self):
        if self.size == 0:
            return -1
        else:
            self.head = self.head.next
            self.size -= 1

    def deleteAfter(self, prev):
        if self.size == 0:
            return -1
        t = prev.next
        prev.next = t.next
        self.size -= 1


    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def getSize(self):
        return self.size


    def print(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, end=' ')
            else:
                print(p.item)
            p = p.next