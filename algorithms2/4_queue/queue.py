queue = []
def add(x):
    queue.append(x)
def remove():
    if len(queue) != 0:
        return queue.pop(0)
def peek():
    if len(queue) != 0:
        return queue.pop(0)