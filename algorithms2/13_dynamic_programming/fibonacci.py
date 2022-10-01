# memoization
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    else:
        if n <= 2:
            f = 1
        else:
            f = fib(n-1) + fib(n-2)
        memo[n] = f
        return f


# tabulation
def fib2(n):
    fib = {}
    for k in range(1, n+1):
        if k <= 2:
            fib[k] = 1
        else:
            fib[k] = fib[k-1] + fib[k-2]
    return fib[n]