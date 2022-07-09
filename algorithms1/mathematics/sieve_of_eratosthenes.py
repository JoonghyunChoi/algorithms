def prime(n):
    a = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    return [i for i in range(2, n+1) if a[i] == True]


def prime2(a, n):
    a = set(a) - set(range(2))
    for i in range(2, int(n**0.5)+1):
        a -= set(range(i*2, max(a)+1, i))
    return sorted(a)


def divisor(n):
    a = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            a.append(i)
            if i != (n//i):
                a.append(n//i)
    return sorted(a)