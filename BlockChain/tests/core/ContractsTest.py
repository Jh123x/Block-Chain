import unittest
from BlockChain.core.Contracts import Contract
from BlockChain.core.HashChainNode import HashChainNode
from BlockChain.core.Transaction import Transaction


class ContractTest(unittest.TestCase):
    def CONDITION_A_ANY_TRANSACTION(
        contract: Contract, _: dict, __: Transaction): return True

    def CONDITION_B_TRANSACTION_MORE_THAN_5(
        contract: Contract, _: dict, latest_transaction: Transaction): return latest_transaction.amount > 5

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

    def test_apply_contract_success(self):
        """Test the application of contracts"""
        c = Contract(
            self.CONDITION_A_ANY_TRANSACTION,
            self.TRANSACTION_CREATOR_A
        )

        node = c.apply_contract(
            self.current_state,
            self.head.get_stored_value(),
            self.head
        )

        self.assertEqual(node.parent, self.head)

    def test_apply_contract_failure(self):
        """Test the application of contracts"""
        c = Contract(
            self.CONDITION_B_TRANSACTION_MORE_THAN_5,
            self.TRANSACTION_CREATOR_A
        )

        try:
            _ = c.apply_contract(
                self.current_state,
                self.head.get_stored_value(),
                self.head
            )
        except ValueError:
            return
        else:
            self.fail("Expected ValueError as contract is not eligible")

    def test_force_apply_contract_success(self):
        """Test the application of contracts"""
        c = Contract(
            self.CONDITION_B_TRANSACTION_MORE_THAN_5,
            self.TRANSACTION_CREATOR_A
        )

        node = c.force_apply_contract(self.head)

        self.assertIsNotNone(node)
        self.assertEqual(self.head, node.parent)

    def test_force_apply_contract_success_2(self):
        """Test the application of contracts"""
        c = Contract(
            self.CONDITION_A_ANY_TRANSACTION,
            self.TRANSACTION_CREATOR_A
        )

        node = c.force_apply_contract(self.head)

        self.assertIsNotNone(node)
        self.assertEqual(self.head, node.parent)
