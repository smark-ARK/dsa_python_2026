class BinarySearchTree:
    class _Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, x):
        def _insert(node, value):
            if node is None:
                return self._Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            if value > node.value:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value=x)

    def delete(self, x):
        def _delete(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if (node.left is None) and (node.right is None):
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    succ = node.right
                    while succ.left:
                        succ = succ.left
                    node.value = succ.value
                    node.right = _delete(node.right, succ.value)

            return node

        self.root = _delete(self.root, x)

    def search(self, x):
        def _search(node, value):
            if node is None:
                return False
            if value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
            else:
                return True

        return _search(self.root, x)

    def contains(self, value) -> bool: ...

    def find_min(self):
        if self.root is None:
            raise Exception("Tree is Empty")
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.value

    def find_max(self):
        if self.root is None:
            raise Exception("Tree is Empty")
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.value

    def inorder_traversal(self):
        res = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            res.append(node.value)
            _inorder(node.right)

        _inorder(self.root)
        return res

    def preorder_traversal(self):
        res = []

        def _preorder(node):
            if node is None:
                return
            res.append(node.value)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        return res

    def postorder_traversal(self):
        res = []

        def _preorder(node):
            if node is None:
                return
            _preorder(node.left)
            res.append(node.value)
            _preorder(node.right)

        _preorder(self.root)
        return res

    def height(self) -> int:
        def _height(node):
            if not node:
                return -1

            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def size(self) -> int: ...

    def is_empty(self) -> bool:
        return self.root is None

    def clear(self):
        self.root = None


if __name__ == "__main__":
    # quick runtime example (does not modify implementation)
    bst = BinarySearchTree()
    # print("min", bst.find_min())
    for v in [7, 3, 9, 1, 5]:
        bst.insert(v)
    print("search 7:", bst.search(7))
    print("search 42:", bst.search(42))
    bst.delete(3)
    print("search 3 after delete:", bst.search(3))
    print("min", bst.find_min())
    print("max", bst.find_max())
    print("Inorder Traversal", bst.inorder_traversal())
    print("preorder Traversal", bst.preorder_traversal())
    print("postorder Traversal", bst.postorder_traversal())
    print("height", bst.height())
    print("is_empty", bst.is_empty())
