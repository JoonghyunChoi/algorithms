# memoization
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


# tabulation
def fib(n):
    fibs = {}
    for k in range(1, n+1):
        if k <= 2:
            fibs[k] = 1
        else:
            fibs[k] = fibs[k-1] + fibs[k-2]
    return fibs[n]