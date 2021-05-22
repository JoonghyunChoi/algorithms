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
