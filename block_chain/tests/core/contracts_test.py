"""Tests for the Contract class"""

import unittest
from block_chain.core.contracts import Contract
from block_chain.core.hash_chain_node import HashChainNode
from block_chain.core.transaction import Transaction
from .conditions import condition_any_transaction, condition_transaction_gt_5


class ContractTest(unittest.TestCase):
    """Tests for the Contract class"""
    TRANSACTION_CREATOR_A = Transaction("a", "b", 1)
    TRANSACTION_CREATOR_B = Transaction("b", "a", 2)

    def setUp(self):
        """Set up the conditions for the contract"""
        self.current_state = {
            "a": -2,
            "b": 2,
        }
        self.head = HashChainNode(Transaction("a", "b", 2), is_head=True)

    def test_eligible_success(self):
        """Test if the contract is eligible"""
        contract = Contract(
            condition_any_transaction,
            self.TRANSACTION_CREATOR_A
        )

        self.assertTrue(
            contract.is_eligible(
                self.current_state,
                self.head.get_stored_value()
            )
        )

    def test_eligibile_failure(self):
        """Test if the contract is not eligible"""
        contract = Contract(
            condition_transaction_gt_5,
            self.TRANSACTION_CREATOR_A
        )

        self.assertFalse(
            contract.is_eligible(
                self.current_state,
                self.head.get_stored_value()
            )
        )
