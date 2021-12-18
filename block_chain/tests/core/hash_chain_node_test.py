"""Tests for the `HashChainNode` class"""

import unittest
from block_chain.core.hash_chain_node import HashChainNode


class HashChainNodeTest(unittest.TestCase):
    """Tests for the `HashChainNode` class"""

    def test_init_child_success(self):
        """Check if the values of the chain is stored correctly"""
        node = HashChainNode(
            1, is_head=False, parent=HashChainNode(2, is_head=True))
        self.assertEqual(node.get_stored_value(), 1)
        self.assertFalse(node.is_head)
        self.assertIsNone(node.next)
        self.assertIsNotNone(node.parent)

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
        self.assertEqual(
            child.parent_hash,
            hash(
                head.get_stored_value(
                )
            ),
            f"{child.parent_hash} != {hash(head.get_stored_value())}"
        )

        child.parent = head2
        self.assertEqual(child.parent_hash, hash(head2.get_stored_value()))
