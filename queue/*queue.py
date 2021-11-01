# 배열을 이용한 큐
queue = []
def add1(item):
    queue.append(item)

def remove1():
    if len(queue) != 0:
        item = queue.pop(0)
        return item

def printQueue1():
    for i in range(len(queue)):
        print(queue[i], end=' ')
    print()


# 단순연결리스트를 이용한 큐
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

front = None
rear = None
size = 0

def add2(item):
    global front
    global rear
    global size

    n = Node(item, None)
    if size == 0:
        front = n
    else:
        rear.next = n
    rear = n
    size += 1

def remove2():
    global front
    global rear
    global size

    if size != 0:
        front = front.next
        size -= 1
        if size == 0:
            rear = None

def printQueue2():
    p = front
    while p:
        if p.next != None:
            print(p.item, end=' ')
        else:
            print(p.item)
        p = p.next
