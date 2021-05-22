def fib(n):
    fib = {}
    for k in range(1, n+1):
        if k <= 2:
            fib[k] = 1
        else:
            fib[k] = fib[k-1] + fib[k-2]
    return fib[n]
