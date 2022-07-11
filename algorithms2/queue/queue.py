# queue
queue = []
def add(item):
    queue.append(item)

def remove():
    if len(queue) != 0:
        item = queue.pop(0)
        return item

def printAll():
    for i in range(len(queue)):
        print(queue[i], end=' ')
    print()


# queue2
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

front = None
rear = None
size = 0
def add(item):
    global front, rear, size

    n = Node(item, None)
    if size == 0:
        front = n
    else:
        rear.next = n
    rear = n
    size += 1

def remove():
    global front, rear, size

    if size != 0:
        front = front.next
        size -= 1
        if size == 0:
            rear = None

def printAll():
    p = front
    while p:
        if p.next != None:
            print(p.item, end=' ')
        else:
            print(p.item)
        p = p.next