def prime(n):
    a = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    primes = [i for i in range(2, n+1) if a[i] == True]
    return primes


def prime2(n, a):
    a = set(a) - {0, 1}
    for i in range(2, int(n**0.5)+1):
        a -= set(range(2*i, max(a)+1, i))
    primes = sorted(a)
    return primes


def divisor(n):
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(i)
            if (n//i) != i:
                a.append(n//i)
    divisors = sorted(a)
    return divisors