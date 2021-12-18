import unittest
from BlockChain.core.ChainNode import ChainNode


class ChainNodeTest(unittest.TestCase):

    def test_init_head_success(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)
        self.assertTrue(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNone(node.parent)

    def test_init_failure(self):
        """Initializing head with a parent should fail"""
        with self.assertRaises(ValueError):
            _ = ChainNode(1, parent=ChainNode(2), is_head=True)

    def test_init_child_success(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=False, parent=ChainNode(2, is_head=True))
        self.assertEqual(node.get_stored_value(), 1)
        self.assertFalse(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNotNone(node.parent)

    def test_init_child_failure(self):
        """Initialize a child without a parent"""
        with self.assertRaises(ValueError):
            _ = ChainNode(1)

    def test_get_stored_value(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)

    def test_parent_success(self):
        """Check if the parent is the same as the child"""
        parent = ChainNode(1, is_head=True)
        node = ChainNode(2, is_head=False, parent=parent)

        self.assertEqual(node.parent, parent)

    def test_parent_failure(self):
        """Check if parent assignment to number is invalid"""
        parent = 3
        with self.assertRaises(ValueError):
            _ = ChainNode(2, is_head=False, parent=parent)

    def test_next(self):
        """Check if the next is the same as the child"""
        parent = ChainNode(1, is_head=True)
        node = ChainNode(2, is_head=False, parent=parent)
        self.assertEqual(node, parent.next)

    def test_parent_success(self):
        """Check if the parent assignment is correct"""
        parent = ChainNode(1, is_head=True)
        node = ChainNode(2, is_head=False, parent=parent)

        self.assertEqual(node.parent, parent)
        p2 = ChainNode(3, is_head=True)
        node.parent = p2
        self.assertEqual(node.parent, p2)
        self.assertIsNone(parent.parent)

    def test_parent_failure(self):
        """Check if parent assignment to None is invalid"""
        with self.assertRaises(ValueError):
            _ = ChainNode(2, is_head=False, parent=None)
