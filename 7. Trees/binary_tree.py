from linked_list import Queue


class BinaryTree:
    class _Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self, root_value):
        self.root = self._Node(root_value)


def preorder(node: BinaryTree._Node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node: BinaryTree._Node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)


def postorder(node: BinaryTree._Node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")


def levelorder(node: BinaryTree._Node):
    q = Queue()
    q.enqueue(node)
    print(q.first())
    while not q.is_empty():
        temp = q.dequeue()
        print(temp.value)
        if temp.left is not None:
            q.enqueue(temp.left)
        if temp.right is not None:
            q.enqueue(temp.right)


tree = BinaryTree(5)


tree.root.left = tree._Node(6)
tree.root.right = tree._Node(7)


print(tree.root.value)
print(tree.root.left.value)

preorder(tree.root)
inorder(tree.root)
postorder(tree.root)
levelorder(tree.root)
