def countingSort1(n):
    count = [0] * (max(n)+1)

    for i in range(len(n)):
        count[n[i]] += 1

    m = []
    for i in range(len(count)):
        for k in range(count[i]):
            m.append(i)
    return m


def countingSort2(n):
    N = len(n)
    count = [0] * (max(n)+1)

    for i in range(N):
        count[n[i]] += 1
    for j in range(1, max(n)+1):
        count[j] += count[j-1]

    m = [0] * (N+1)
    for i in range(N-1, -1, -1):
        t = n[i]
        m[count[t]] = n[i]
        count[t] -= 1

    m = m[1:]
    return m
