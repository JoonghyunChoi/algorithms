class Bitmask:
    def add(self, a, k):
        return a | (1 << k)

    def remove(self, a, k):
        return a & ~(1 << k)

    def toggle(self, a, k):
        return a ^ (1 << k)

    def included(self, a, k):
        return bool(a & (1 << k))

    def get_last(self, a):
        return a & (~a + 1)

    def remove_last(self, a):
        return a & (a - 1)

    def union(self, a, b):
        return a | b

    def intersection(self, a, b):
        return a & b

    def difference(self, a, b):
        return a & (~b)

    def symmetric_difference(self, a, b):
        return a ^ b

    def bit_count(self, a):
        count = 0
        while a:
            a &= a - 1
            count += 1
        return count

    def subset(self, a):
        result = []
        b = a
        while b:
            result.append(bin(b))
            b = (b - 1) & a
        return result