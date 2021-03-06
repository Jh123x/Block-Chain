"""Transactions in the Chain"""

from hashlib import sha512


class Transaction:
    """A Transaction in the Chain"""

    def __init__(self, sender: str, recipient: str, amount: int) -> None:
        """Records a transaction between a sender and a recipient"""
        self.sender: str = sender
        self.recipient: str = recipient
        self.amount: int = amount

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if sender == recipient:
            raise ValueError("Sender and recipient cannot be the same")

    def __eq__(self, __o: object) -> bool:
        """Check if 2 transactions are equal"""
        return isinstance(__o, Transaction) and \
            hash(self) == hash(__o) and \
            self.sender == __o.sender and \
            self.recipient == __o.recipient and \
            self.amount == __o.amount

    def __str__(self):
        """String representation of a transaction"""
        return f"{self.sender} -> {self.recipient} {self.amount}"

    def __hash__(self):
        """Hash of a transaction"""
        return int(sha512(str(self).encode()).hexdigest(), 16)
