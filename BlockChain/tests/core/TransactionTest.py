import unittest

from BlockChain.core.Transaction import Transaction


class TransactionTest(unittest.TestCase):
    def test_init_success(self):
        """Check if the values of the transaction is stored correctly"""
        transaction = Transaction("1", "2", 3)
        self.assertEqual(transaction.sender, "1")
        self.assertEqual(transaction.recipient, "2")
        self.assertEqual(transaction.amount, 3)

    def test_str_repr(self):
        """Check if the string representation is correct"""
        transaction = Transaction("1", "2", 3)
        self.assertEqual(str(transaction), "1 -> 2 3")

    def test_equal_transaction_success(self):
        """Check if 2 similar transactions are equal"""
        transaction = Transaction("1", "2", 3)
        self.assertEqual(transaction, Transaction("1", "2", 3))

    def test_equal_transaction_not_equal(self):
        """Check if 2 different objects are different"""
        transaction = Transaction("1", "2", 3)
        self.assertNotEqual(transaction, Transaction("1", "3", 3))
        self.assertNotEqual(transaction, hash(transaction))
