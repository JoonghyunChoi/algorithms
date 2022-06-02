class BinarySearchTree:
    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None


    def get(self, key):
        return self.getItem(self.root, key)

    def getItem(self, n, key):
        if n == None:
            return None
        if n.key > key:
            return self.getItem(n.left, key)
        elif n.key < key:
            return self.getItem(n.right, key)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.putItem(self.root, key, value)

    def putItem(self, n, key, value):
        if n == None:
            return self.Node(key, value)
        if n.key > key:
            n.left = self.putItem(n.left, key, value)
        elif n.key < key:
            n.right = self.putItem(n.right, key, value)
        else:
            n.value = value
        return n


    def getMin(self):
        if self.root == None:
            return None
        return self.getMinNode(self.root)

    def getMinNode(self, n):
        if n.left == None:
            return n
        return self.getMinNode(n.left)

    def getMax(self):
        if self.root == None:
            return None
        return self.getMaxNode(self.root)

    def getMaxNode(self, n):
        if n.right == None:
            return n
        return self.getMaxNode(n.right)


    def deleteMin(self):
        if self.root == None:
            return -1
        self.root = self.deleteMinNode(self.root)

    def deleteMinNode(self, n):
        if n.left == None:
            return n.right
        n.left = self.deleteMinNode(n.left)
        return n

    def delete(self, key):
        self.root = self.deleteNode(self.root, key)

    def deleteNode(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self.deleteNode(n.left, key)
        elif n.key < key:
            n.right = self.deleteNode(n.right, key)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right

            targetNode = n
            n = self.getMinNode(targetNode.right)           # 삭제될 노드의 왼쪽 서브트리의 최댓값을 이용하는 방법도 가능
            n.right = self.deleteMinNode(targetNode.right)
            n.left = targetNode.left
        return n