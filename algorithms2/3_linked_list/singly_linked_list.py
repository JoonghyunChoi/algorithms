class SinglyLinkedList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0


    def insert_front(self, item):
        if self.size == 0:
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, prev):
        prev.next = self.Node(item, prev.next)
        self.size += 1


    def delete_front(self):
        if self.size == 0:
            return -1
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, prev):
        if self.size == 0:
            return -1
        t = prev.next
        prev.next = t.next
        self.size -= 1


    def get(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return None

    def get_size(self):
        return self.size