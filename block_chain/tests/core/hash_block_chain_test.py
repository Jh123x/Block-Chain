"""Tests for the HashBlockChain class"""

import unittest

from block_chain.core.contracts import Contract
from block_chain.core.transaction import Transaction
from block_chain.core.block_chain import HashBlockChain
from block_chain.core.hash_chain_node import HashChainNode

from .conditions import condition_any_transaction, condition_transaction_gt_5


class HashBlockChainTest(unittest.TestCase):
    """Tests for the HashBlockChain class"""

    def setUp(self):
        """Set up for each of the unit tests"""
        self.blockchain = HashBlockChain()
        self.blockchain.add_transaction(Transaction("a", "b", 2))
        self.current_state = {
            "a": -2,
            "b": 2,
        }
        return super().setUp()

    def tearDown(self) -> None:
        """Tear down for each of the unit tests"""
        del self.blockchain
        del self.current_state
        return super().tearDown()

    def test_add_block_chain(self):
        """Create chain from node"""
        blockchain = HashBlockChain(HashChainNode(
            Transaction("a", "b", 2), is_head=True))
        expected = {
            'a': -2,
            'b': 2,
        }
        self.assertEqual(blockchain.get_current_state(), expected)
        blockchain.add_transaction(Transaction("a", "b", 2))

    def test_check_current_state(self):
        """Check if the current state is correct"""
        self.assertEqual(
            self.current_state, self.blockchain.get_current_state()
        )

    def test_add_transaction(self):
        """Check if the add transaction method works"""
        self.blockchain.add_transaction(Transaction("b", "a", 2))

        expected = {
            "a": 0,
            "b": 0,
        }
        self.assertTrue(
            expected == self.blockchain.get_current_state(),
            f"{self.blockchain.get_current_state()} != {expected}"
        )

    def test_add_contract_success(self):
        """Check if adding the contract works"""
        contract = Contract(condition_any_transaction,
                            Transaction("a", "b", 2))
        self.blockchain.add_contract(contract)

        self.blockchain.add_transaction(Transaction("b", "a", 2))
        self.assertTrue(self.current_state,
                        self.blockchain.get_current_state())

        self.blockchain.add_transaction(Transaction("b", "c", 5))
        expected = {
            "a": -2,
            "b": -3,
            "c": 5,
        }
        self.assertEqual(expected, self.blockchain.get_current_state())

    def test_add_contract_not_fulfilled(self):
        """Checking if not eligible contract does not run"""
        contract = Contract(
            condition_transaction_gt_5, Transaction("a", "b", 100))
        self.blockchain.add_contract(contract)

        self.assertEqual(self.current_state,
                         self.blockchain.get_current_state())
        self.blockchain.add_transaction(Transaction("b", "c", 2))
        expected = {
            "a": -2,
            "b": 0,
            "c": 2,
        }
        self.assertEqual(expected, self.blockchain.get_current_state())
