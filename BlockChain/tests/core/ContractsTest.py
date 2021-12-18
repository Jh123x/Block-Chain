import unittest
from BlockChain.core.Contracts import Contract
from BlockChain.core.HashChainNode import HashChainNode
from BlockChain.core.Transaction import Transaction


class ContractTest(unittest.TestCase):

    @staticmethod
    def CONDITION_A_ANY_TRANSACTION(
        _: dict, __: Transaction): return True

    @staticmethod
    def CONDITION_B_TRANSACTION_MORE_THAN_5(
        _: dict, latest_transaction: Transaction): return latest_transaction.amount > 5

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
        c = Contract(
            self.CONDITION_A_ANY_TRANSACTION,
            self.TRANSACTION_CREATOR_A
        )

        self.assertTrue(
            c.is_eligible(
                self.current_state,
                self.head.get_stored_value()
            )
        )

    def test_eligibile_failure(self):
        """Test if the contract is not eligible"""
        c = Contract(
            self.CONDITION_B_TRANSACTION_MORE_THAN_5,
            self.TRANSACTION_CREATOR_A
        )

        self.assertFalse(
            c.is_eligible(
                self.current_state,
                self.head.get_stored_value()
            )
        )

