import unittest
from BlockChain.core.HashChainNode import HashChainNode
from BlockChain.core.Transaction import Transaction
from BlockChain.utils.CheckBalance import calculate_balance

class CheckBalanceTest(unittest.TestCase):

    def create_hash_chain(self, *args:tuple[str, str, int]) -> HashChainNode:
        """Create a HashChainNode based on the args"""
        head = None
        curr = None
        for sender, recipient, amount in args:
            if head is None:
                node = HashChainNode(Transaction(sender, recipient, amount), is_head=True)
                head = node
            else: 
                node = HashChainNode(Transaction(sender, recipient, amount), parent=curr)
            curr = node
        return head


    def test_check_balance_values(self):
        """Check if the calculations is correct"""
        testcases = [
            (self.create_hash_chain(("1", "2", 1)), {"1": -1, "2": 1}),
            (self.create_hash_chain(("1", "3", 1)), {"1": -1, "3": 1}),
            (self.create_hash_chain(("2", "1", 5)), {"2": -5, "1": 5}),
            (self.create_hash_chain(("2", "1", 5), ("1", "2", 3)), {"2": -2, "1": 2}),
            (self.create_hash_chain(("2", "1", 5), ("1", "2", 5)), {"2": 0, "1": 0}),
        ]

        for chain, expected in testcases:
            self.assertEqual(calculate_balance(chain), expected)