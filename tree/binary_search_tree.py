class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def get(self, k):
        return self.getItem(self.root, k)

    def getItem(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.getItem(n.left, k)
        elif n.key < k:
            return self.getItem(n.right, k)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.putItem(self.root, key, value)

    def putItem(self, n, key, value):
        if n == None:
            return Node(key, value)
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
        return self.getMinimum(self.root)

    def getMinimum(self, n):
        if n.left == None:
            return n
        return self.getMinimum(n.left)

    def getMax(self):
        if self.root == None:
            return None
        return self.getMaximum(self.root)

    def getMaximum(self, n):
        if n.right == None:
            return n
        return self.getMaximum(n.right)


    def deleteMin(self):
        if self.root == None:
            return -1
        self.root = self.deleteMinNode(self.root)

    def deleteMinNode(self, n):
        if n.left == None:
            return n.right
        n.left = self.deleteMinNode(n.left)
        return n

    def delete(self, k):
        self.root = self.deleteNode(self.root, k)

    def deleteNode(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.deleteNode(n.left, k)
        elif n.key < k:
            n.right = self.deleteNode(n.right, k)
        else:
            if n.left == None:
                return n.right

            if n.right == None:
                return n.left

            targetNode = n
            n = self.getMinimum(targetNode.right)           # 삭제될 노드의 왼쪽 서브트리의 최댓값을 이용하는 방법도 가능
            n.left = targetNode.left
            n.right = self.deleteMinNode(targetNode.right)
        return n
