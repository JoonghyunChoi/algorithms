class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

m = []
class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, n):
        global m
        if n != None:
            m.append(n)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        global m
        if n != None:
            if n.left:
                self.inorder(n.left)
            m.append(n)
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            m.append(n)

    def levelorder(self, root):
        queue = []
        queue.append(root)
        while queue:
            n = queue.pop(0)
            m.append(n)
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
