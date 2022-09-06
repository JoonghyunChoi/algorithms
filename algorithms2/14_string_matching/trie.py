class Trie:
    class Node:
        def __init__(self, key=''):
            self.key = key
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        self.insert_(self.root, word, 0)

    def insert_(self, current, word, index):
        if index == len(word):
            current.end = True
            return

        char = word[index]
        node = current.children.get(char, -1)
        if node == -1:
            node = self.Node(char)
            current.children[char] = node
        self.insert_(node, word, index+1)

    def search(self, word):
        return self.search_(self.root, word, 0)

    def search_(self, current, word, index):
        if index == len(word):
            return current.end

        char = word[index]
        node = current.children.get(char, -1)
        if node == -1:
            return False
        return self.search_(node, word, index+1)

    def prefix_search(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char, -1)
            if node == -1:
                return False
        words = []
        self.prefix_search_(node, word, words)
        return words

    def prefix_search_(self, current, word, words):
        if current.end:
            words.append(word)

        for char, node in current.children.items():
            self.prefix_search_(node, word+char, words)

    def delete(self, word):
        self.delete_(self.root, word, 0)

    def delete_(self, current, word, index):
        if index == len(word):
            if not current.end:
                return False
            current.end = False
            return len(current.children) == 0

        char = word[index]
        node = current.children.get(char, -1)
        if node == -1:
            return False
        deleted = self.delete_(node, word, index+1)

        if deleted:
            current.children.pop(char)
            return len(current.children) == 0
        return False