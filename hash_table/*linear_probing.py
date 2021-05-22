class LinearProbing:
    def __init__(self, size):
        self.m = size
        self.T = [None] * size
        self.D = [None] * size

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
                return
            if self.T[i] == key:
                self.D[i] = item
                return
            j += 1
            i = (i0 + j) % self.m
            if i == i0:
                break

    def get(self, key):
        i0 = self.hash(key)
        i = i0
        j = 0
        while self.T[i] != None:
            if self.T[i] == key:
                return self.D[i]
            j += 1
            i = (i0 + j) % self.m
            if i == i0:
                return None
        return None

  # delete()

    def print(self):
        for i in range(self.m):
            print(i, self.T[i])
