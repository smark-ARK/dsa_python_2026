import os
import importlib.util
import unittest

# locate the BST file (handles the directory name with space/dot)
bst_path = os.path.join(
    os.path.dirname(__file__), "..", "7. Trees", "binary_search_tree.py"
)
bst_path = os.path.normpath(bst_path)

spec = importlib.util.spec_from_file_location("bst_module", bst_path)
bst_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bst_module)
BinarySearchTree = bst_module.BinarySearchTree


class TestBasicBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        self.bst.insert(10)
        self.assertTrue(self.bst.search(10))
        self.assertFalse(self.bst.search(5))

    def test_delete(self):
        for v in (10, 5, 15):
            self.bst.insert(v)
        self.bst.delete(5)
        self.assertFalse(self.bst.search(5))


if __name__ == "__main__":
    unittest.main()
