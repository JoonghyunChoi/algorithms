class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

front = None
rear = None
size = 0

def add(item):
    global front
    global rear
    global size

    node = Node(item, None)
    if size == 0:
        front = node
    else:
        rear.next = node
    rear = node
    size += 1

def remove():
    global front
    global rear
    global size

    if size != 0:
        front = front.next
        size -= 1
        if size == 0:
            rear = None

def printQueue():
    p = front
    while p:
        if p.next != None:
            print(p.item, end=' ')
        else:
            print(p.item)
        p = p.next
