class BinaryTree:
    def __init__(self):
        self.root = None
        self.visits = []

    def preorder(self, n):
        if n != None:
            self.visits.append(n)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
            return self.visits

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            self.visits.append(n)
            if n.right:
                self.inorder(n.right)
            return self.visits

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            self.visits.append(n)
            return self.visits

    def levelorder(self, root):
        queue = []
        queue.append(root)
        while queue:
            n = queue.pop(0)
            self.visits.append(n)
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)
        return self.visits

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1