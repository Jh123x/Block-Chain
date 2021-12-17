import unittest
from BlockChain.core.HashChainNode import HashChainNode


class HashChainNodeTest(unittest.TestCase):

    def test_init_head_success(self):
        """Check if the values of the chain is stored correctly"""
        node = HashChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)
        self.assertTrue(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNone(node.parent)

    def test_init_failure(self):
        """Initializing head with a parent should fail"""
        try:
            _ = HashChainNode(1, parent=HashChainNode(2), is_head=True)
        except ValueError:
            return
        else:
            self.fail("ValueError not raised")

    def test_init_child_success(self):
        """Check if the values of the chain is stored correctly"""
        node = HashChainNode(
            1, is_head=False, parent=HashChainNode(2, is_head=True))
        self.assertEqual(node.get_stored_value(), 1)
        self.assertFalse(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNotNone(node.parent)

    def test_init_child_failure(self):
        """Initialize a child without a parent"""
        try:
            node = HashChainNode(1)
        except ValueError:
            return
        else:
            self.fail(f"ValueError not raised: {node}")

    def test_get_stored_value(self):
        """Check if the values of the chain is stored correctly"""
        node = HashChainNode(1, is_head=True)
        self.assertEqual(node.get_stored_value(), 1)

    def test_parent(self):
        """Check if the parent is the same as the child"""
        parent = HashChainNode(1, is_head=True)
        node = HashChainNode(2, parent=parent)
        self.assertEqual(node.parent, parent)

    def test_next(self):
        """Check if the next is the same as the child"""
        parent = HashChainNode(1, is_head=True)
        node = HashChainNode(2, is_head=False, parent=parent)
        self.assertEqual(node, parent.next)

    def test_set_parent_changes_hash(self):
        """Check if the hash is updated when a new parent is set"""
        head = HashChainNode(1, is_head=True)
        head2 = HashChainNode(3, is_head=True)

        child = HashChainNode(2, parent=head)
        self.assertEqual(child.get_stored_value(), 2)
        self.assertEqual(child.parent_hash, hash(head.get_stored_value()), f"{child.parent_hash} != {hash(head.get_stored_value())}")

        child.parent = head2
        self.assertEqual(child.parent_hash, hash(head2.get_stored_value()))
