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
        return self._get(self.root, key)

    def _get(self, n, key):
        if not n:
            return None
        if n.key > key:
            return self._get(n.left, key)
        elif n.key < key:
            return self._get(n.right, key)
        else:
            return n.value

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, n, key, value):
        if not n:
            return self.Node(key, value)
        if n.key > key:
            n.left = self._put(n.left, key, value)
        elif n.key < key:
            n.right = self._put(n.right, key, value)
        else:
            n.value = value
        return n


    def get_min(self):
        if not self.root:
            return None
        return self._get_min(self.root)

    def _get_min(self, n):
        if not n.left:
            return n
        return self._get_min(n.left)

    def get_max(self):
        if not self.root:
            return None
        return self._get_max(self.root)

    def _get_max(self, n):
        if not n.right:
            return n
        return self._get_max(n.right)


    def delete_min(self):
        if not self.root:
            return -1
        self.root = self._delete_min(self.root)

    def _delete_min(self, n):
        if not n.left:
            return n.right
        n.left = self._delete_min(n.left)
        return n

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, n, key):
        if not n:
            return None
        if n.key > key:
            n.left = self._delete(n.left, key)
        elif n.key < key:
            n.right = self._delete(n.right, key)
        else:
            if not n.right:
                return n.left
            if not n.left:
                return n.right

            removal_target = n
            n = self._get_min(removal_target.right)
            n.right = self._delete_min(removal_target.right)
            n.left = removal_target.left
        return n