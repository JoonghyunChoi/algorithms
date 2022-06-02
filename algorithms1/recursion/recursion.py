def recursion(n, base):
    if n == base:
        return n
    else:
        n += 0
        return recursion(n-1, base)