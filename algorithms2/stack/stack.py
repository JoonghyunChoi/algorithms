# stack
stack = []
def push(item):
    stack.append(item)

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

def peek():
    if len(stack) != 0:
        return stack[-1]


# stack2
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

top = None
size = 0
def push(item):
    global top, size

    top = Node(item, top)
    size += 1

def pop():
    global top, size

    if size != 0:
        topItem = top.item
        top = top.next
        size -= 1
        return topItem

def peek():
    if size != 0:
        return top.item

def print_all():
    p = top
    while p:
        if p.next != None:
            print(p.item, end=' ')
        else:
            print(p.item)
        p = p.next