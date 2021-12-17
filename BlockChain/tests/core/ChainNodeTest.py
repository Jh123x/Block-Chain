import unittest
from BlockChain.core.ChainNode import ChainNode


class ChainNodeTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_init_head_success(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)
        self.assertTrue(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNone(node.parent)

    def test_init_failure(self):
        """Initializing head with a parent should fail"""
        try:
            _ = ChainNode(1, parent=ChainNode(2), is_head=True)
        except ValueError:
            return
        else:
            self.fail("ValueError not raised")

    def test_init_child_success(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=False, parent=ChainNode(2, is_head=True))
        self.assertEqual(node.get_stored_value(), 1)
        self.assertFalse(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNotNone(node.parent)

    def test_init_child_failure(self):
        """Initialize a child without a parent"""
        try:
            node = ChainNode(1)
        except ValueError:
            return
        else:
            self.fail(f"ValueError not raised: {node}")

    def test_get_stored_value(self):
        """Check if the values of the chain is stored correctly"""
        node = ChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)

    def test_parent(self):
        """Check if the parent is the same as the child"""
        parent = ChainNode(1, is_head=True)
        node = ChainNode(2, is_head=False, parent=parent)

        self.assertEqual(node.parent, parent)

    def test_next(self):
        """Check if the next is the same as the child"""
        parent = ChainNode(1, is_head=True)
        node = ChainNode(2, is_head=False, parent=parent)
        self.assertEqual(node, parent.next)
