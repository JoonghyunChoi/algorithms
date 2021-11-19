class QuadraticProbing:
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
            i = (h + j*j) % self.size
            if j == 100:                    # 반복문 제한
                break

    def get(self, key):
        h = self.hash(key)
        i = h
        j = 1
        while self.hashTable[i] != None:
            if self.hashTable[i] == key:
                return self.dataTable[i]
            i = (h + j*j) % self.size
            j += 1
        return None


  # delete()

    def print(self):
        for i in range(self.size):
            print(i, self.hashTable[i])
