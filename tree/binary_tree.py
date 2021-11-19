class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self):
        self.root = None
        self.m = []


    def preorder(self, n):
        if n != None:
            self.m.append(n)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            return self.m

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            self.m.append(n)
            if n.right:
                self.inorder(n.right)
            return self.m

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.m.append(n)
            return self.m


    def levelorder(self, root):
        queue = []
        queue.append(root)
        while queue:
            n = queue.pop(0)
            self.m.append(n)
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)
        return self.m

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
