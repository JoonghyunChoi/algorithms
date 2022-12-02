stack = []
def push(x):
    stack.append(x)
def pop():
    if len(stack) != 0:
        return stack.pop(-1)
def peek():
    if len(stack) != 0:
        return stack[-1]