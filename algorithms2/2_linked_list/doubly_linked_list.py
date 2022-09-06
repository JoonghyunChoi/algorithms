class DoublyLinkedList:
    class Node:
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def insert_before(self, item, next):
        t = next.prev
        n = self.Node(item, t, next)
        next.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, item, prev):
        t = prev.next
        n = self.Node(item, prev, t)
        t.prev = n
        prev.next = n
        self.size += 1

    def delete(self, n):
        if self.size == 0:
            return -1
        p = n.prev
        t = n.next
        p.next = t
        t.prev = p
        self.size -= 1

    def get_size(self):
        return self.size

    def print_all(self):
        if self.size == 0:
            return -1
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end=' ')
            else:
                print(p.item)
            p = p.next