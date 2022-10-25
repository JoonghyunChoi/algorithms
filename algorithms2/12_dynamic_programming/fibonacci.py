# memoization
dp = {}
def fib(n):
    if n in dp:
        return dp[n]
    else:
        if n <= 2:
            dp[n] = 1
        else:
            dp[n] = fib(n-1) + fib(n-2)
        return dp[n]


# tabulation
def fib(n):
    dp = [0] * (n+1)

    for k in range(1, n+1):
        if k <= 2:
            dp[k] = 1
        else:
            dp[k] = dp[k-1] + dp[k-2]
    return dp[n]