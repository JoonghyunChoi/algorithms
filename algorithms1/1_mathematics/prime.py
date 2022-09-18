def divisor(n):
    i = 1
    result = []
    while i * i < n:
        if n % i == 0:
            result.extend((i, n//i))
        i += 1
    if i * i == n:
        result.append(i)
    return result


def prime(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve