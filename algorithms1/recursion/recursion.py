def recursion(n, base):
    if n == base:
        return n
    else:
        n *= 1
        return recursion(n-1, base)