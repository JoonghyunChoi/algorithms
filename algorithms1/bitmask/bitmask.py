def bitMasking(x, n):
    bits = ''
    for i in range(n-1, -1, -1):
        if x & (1 << i):
            bits += '1'
        else:
            bits += '0'
    return bits

def bitCount(x):
    if x == 0:
        return 0
    return (x & 1) + bitCount(x >> 1)

def bitSubset(x):
    subset = x
    subsets = []
    while subset:
        subsets.append(bin(subset))
        subset = (subset - 1) & x
    return subsets