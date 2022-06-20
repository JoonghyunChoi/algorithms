class Bitmask:
    def add(self, a, k):
        return a | (1 << k)

    def remove(self, a, k):
        return a & ~(1 << k)

    def toggle(self, a, k):
        return a ^ (1 << k)

    def is_included(self, a, k):
        return bool(a & (1 << k))

    def empty_set(self, a):
        a = 0
        return a

    def full_set(self, a, n):
        a = (1 << n) - 1
        return a

    def union(self, a, b):
        return a | b

    def intersection(self, a, b):
        return a & b

    def difference(self, a, b):
        return a & (~b)

    def symmetric_difference(self, a, b):
        return a ^ b

    def bit_count(self, a):
        if a == 0:
            return 0
        return (a & 1) + self.bit_count(a >> 1)

    def get_min(self, a):
        return a & (~a + 1)

    def remove_min(self, a):
        return a & (a - 1)

    def subsets(self, a):
        subset = a
        subsets_ = []
        while subset:
            subsets_.append(bin(subset))
            subset = (subset - 1) & a
        return subsets_