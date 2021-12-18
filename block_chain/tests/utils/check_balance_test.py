"""Tests for calculate_balance function"""

import unittest
from block_chain.core.hash_chain_node import HashChainNode
from block_chain.core.transaction import Transaction
from block_chain.utils.check_balance import calculate_balance


def create_hash_chain(*args: tuple[str, str, int]) -> HashChainNode:
    """Create a HashChainNode based on the args"""
    head = None
    curr = None
    for sender, recipient, amount in args:
        if head is None:
            node = HashChainNode(Transaction(
                sender, recipient, amount), is_head=True)
            head = node
        else:
            node = HashChainNode(Transaction(
                sender, recipient, amount), parent=curr)
        curr = node
    return head


class CheckBalanceTest(unittest.TestCase):
    """Test for calculate_balance function"""

    def test_check_balance_values(self):
        """Check if the calculations is correct"""
        testcases = [
            (create_hash_chain(("1", "2", 1)), {"1": -1, "2": 1}),
            (create_hash_chain(("1", "3", 1)), {"1": -1, "3": 1}),
            (create_hash_chain(("2", "1", 5)), {"2": -5, "1": 5}),
            (create_hash_chain(("2", "1", 5),
             ("1", "2", 3)), {"2": -2, "1": 2}),
            (create_hash_chain(("2", "1", 5),
             ("1", "2", 5)), {"2": 0, "1": 0}),
        ]

        for chain, expected in testcases:
            self.assertEqual(calculate_balance(chain), expected)
