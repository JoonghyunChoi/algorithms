x = 0
bits = ''
subsets = []

def bitmasking(x, n):
    global bits
    for i in range(n-1, -1, -1):
        if x & (1 << i):
            bits += '1'
        else:
            bits += '0'

def bitCount(x):
    if x == 0:
        return 0
    return (x & 1) + bitCount(x >> 1)

def bitSubset(x):
    subset = x
    while subset:
        subsets.append(bin(subset))
        subset = (subset - 1) & x
