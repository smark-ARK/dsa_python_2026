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


class TestBSTMinMax(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_find_min_max_on_empty_raises(self):
        with self.assertRaises(Exception):
            self.bst.find_min()
        with self.assertRaises(Exception):
            self.bst.find_max()

    def test_find_min_max_after_inserts(self):
        for v in (7, 3, 9, 1, 5):
            self.bst.insert(v)
        self.assertEqual(self.bst.find_min(), 1)
        self.assertEqual(self.bst.find_max(), 9)

    def test_find_min_after_delete(self):
        for v in (5, 2, 8, 1, 9):
            self.bst.insert(v)
        self.bst.delete(1)
        self.assertEqual(self.bst.find_min(), 2)

    def test_find_max_after_delete(self):
        for v in (5, 2, 8, 1, 9):
            self.bst.insert(v)
        self.bst.delete(9)
        self.assertEqual(self.bst.find_max(), 8)


if __name__ == "__main__":
    unittest.main()
