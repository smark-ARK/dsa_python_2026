class BinarySearchTree:
    class _Node:
        def __init__(self, value, left: None, right: None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, x):
        def _insert(node, value):
            if node is None:
                return self._Node(value)
            if value < node.vlue:
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

    def find_min(self): ...

    def find_max(self): ...

    def inorder_traversal(self): ...

    def preorder_traversal(self): ...

    def postorder_traversal(self): ...

    def height(self) -> int: ...

    def size(self) -> int: ...

    def is_empty(self) -> bool: ...

    def clear(self): ...
