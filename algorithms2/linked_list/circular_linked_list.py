class CircularLinkedList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.last = None
        self.size = 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.size == 0:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def delete(self):
        if self.size == 0:
            return -1
        n = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = n.next
        self.size -= 1

    def get_first(self):
        if self.size == 0:
            return -1
        f = self.last.next
        return f.item

    def get_size(self):
        return self.size

    def print_all(self):
        if self.size == 0:
            return -1
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, end=' ')
                p = p.next
            print(p.item)