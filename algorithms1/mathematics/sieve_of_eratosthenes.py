def primes(n):
    a = [True] * (n+1)

    for i in range(2, int(n**0.5)+1):
        if a[i] == True:
            for j in range(2*i, n+1, i):
                a[j] = False
    return [i for i in range(2, n+1) if a[i] == True]