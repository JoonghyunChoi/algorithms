class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

top = None
size = 0

def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1

def pop():
    global top
    global size
    if size != 0:
        topItem = top.item
        top = top.next
        size -= 1
        return topItem

def peek():
    if size != 0:
        return top.item

def printStack():
    p = top
    while p:
        if p.next != None:
            print(p.item, end=' ')
        else:
            print(p.item)
        p = p.next
