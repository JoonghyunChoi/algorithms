class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.hashTable = [None] * size
        self.dataTable = [None] * size

    def hash(self, key):
        return key % self.size

    def put(self, key, item):
        h = self.hash(key)
        i = h
        j = 0
        while True:
            if self.hashTable[i] == None:
                self.hashTable[i] = key
                self.dataTable[i] = item
                return
            if self.hashTable[i] == key:
                self.dataTable[i] = item
                return
            j += 1
            i = (h + j) % self.size
            if i == h:
                break

    def get(self, key):
        h = self.hash(key)
        i = h
        j = 0
        while self.hashTable[i] != None:
            if self.hashTable[i] == key:
                return self.dataTable[i]
            j += 1
            i = (h + j) % self.size
            if i == h:
                return None
        return None

    # def delete()

    def print_all(self):
        for i in range(self.size):
            print(i, self.hashTable[i])