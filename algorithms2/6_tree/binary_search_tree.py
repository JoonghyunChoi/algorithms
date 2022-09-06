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
        return self.get_item(self.root, key)

    def get_item(self, n, key):
        if n == None:
            return None
        if n.key > key:
            return self.get_item(n.left, key)
        elif n.key < key:
            return self.get_item(n.right, key)
        else:
            return n.value

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            return self.Node(key, value)
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        else:
            n.value = value
        return n

    def get_min(self):
        if self.root == None:
            return None
        return self.get_min_node(self.root)

    def get_min_node(self, n):
        if n.left == None:
            return n
        return self.get_min_node(n.left)

    def get_max(self):
        if self.root == None:
            return None
        return self.get_max_node(self.root)

    def get_max_node(self, n):
        if n.right == None:
            return n
        return self.get_max_node(n.right)


    def delete_min(self):
        if self.root == None:
            return -1
        self.root = self.delete_min_node(self.root)

    def delete_min_node(self, n):
        if n.left == None:
            return n.right
        n.left = self.delete_min_node(n.left)
        return n

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def delete_node(self, n, key):
        if n == None:
            return None
        if n.key > key:
            n.left = self.delete_node(n.left, key)
        elif n.key < key:
            n.right = self.delete_node(n.right, key)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right

            targetNode = n
            n = self.get_min_node(targetNode.right)   # 삭제될 노드의 왼쪽 서브트리의 최댓값을 이용하는 방법도 가능
            n.right = self.delete_min_node(targetNode.right)
            n.left = targetNode.left
        return n