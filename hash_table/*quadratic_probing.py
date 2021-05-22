class QuadraticProbing:
    def __init__(self, size):
        self.m = size
        self.T = [None] * size
        self.D = [None] * size
        self.n = 0

    def hash(self, key):
        return key % self.m

    def put(self, key, item):
        i0 = self.hash(key)
        i = i0
        j = 0
        while True:
            if self.T[i] == None:
                self.T[i] = key
                self.D[i] = item
                self.n += 1
                return
            if self.T[i] == key:
                self.D[i] = item
                return
            j += 1
            i = (i0 + j*j) % self.m
            if self.n > self.m:
                break

    def get(self, key):
        i0 = self.hash(key)
        i = i0
        j = 1
        while self.T[i] != None:
            if self.T[i] == key:
                return self.D[i]
            i = (i0 + j*j) % self.m
            j += 1
        return None

  # delete()

    def print(self):
        for i in range(self.m):
            print(i, self.T[i])
