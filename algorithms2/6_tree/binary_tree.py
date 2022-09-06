class BinaryTree:
    def __init__(self):
        self.root = None
        self.b = []

    def preorder(self, n):
        if n:
            self.b.append(n)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            return self.b

    def inorder(self, n):
        if n:
            if n.left:
                self.inorder(n.left)
            self.b.append(n)
            if n.right:
                self.inorder(n.right)
            return self.b

    def postorder(self, n):
        if n:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.b.append(n)
            return self.b

    def levelorder(self, root):
        queue = [root]
        while queue:
            n = queue.pop(0)
            self.b.append(n)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return self.b

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1