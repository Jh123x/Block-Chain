import unittest

from BlockChain.utils.CheckHash import check_hash
from BlockChain.core.HashChainNode import HashChainNode


class CheckHashTest(unittest.TestCase):

    def test_parent_child_hash_success(self):
        """Check if the child's parent hash matches the parent's hash"""
        node1 = HashChainNode(1, is_head=True)
        node2 = HashChainNode(2, parent=node1)
        self.assertTrue(check_hash(node1, node2))

    def test_same_object_failure(self):
        """Check if the hash on the same object matches"""
        node1 = HashChainNode(1, is_head=True)
        self.assertFalse(check_hash(node1, node1))

    def test_same_value_diff_object_failure(self):
        """Check if invalid hashes do not match"""
        node1 = HashChainNode(1, is_head=True)
        node2 = HashChainNode(1, is_head=True)
        self.assertFalse(check_hash(node1, node2))
