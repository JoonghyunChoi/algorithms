class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size
        self.data_table = [None] * size

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        h0 = self.hash(key)
        h = h0
        i = 0
        while True:
            if not self.hash_table[h]:
                self.hash_table[h] = key
                self.data_table[h] = value
                return
            if self.hash_table[h] == key:
                self.data_table[h] = value
                return
            i += 1
            h = (h0 + i) % self.size
            if h == h0:
                break

    def get(self, key):
        h0 = self.hash(key)
        h = h0
        i = 0
        while self.hash_table[h]:
            if self.hash_table[h] == key:
                return self.data_table[h]
            i += 1
            h = (h0 + i) % self.size
            if h == h0:
                return None
        return None