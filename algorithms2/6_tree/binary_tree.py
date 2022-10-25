class BinaryTree:
    def __init__(self):
        self.root = None
        self.path = []

    def preorder(self, n):
        if n:
            self.path.append(n)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            return self.path

    def inorder(self, n):
        if n:
            if n.left:
                self.inorder(n.left)
            self.path.append(n)
            if n.right:
                self.inorder(n.right)
            return self.path

    def postorder(self, n):
        if n:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.path.append(n)
            return self.path

    def levelorder(self, root):
        queue = [root]
        while queue:
            n = queue.pop(0)
            self.path.append(n)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return self.path

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1