from hashlib import sha512

class Transaction(object):
    def __init__(self, sender: str, recipient: str, amount: int) -> None:
        """Records a transaction between a sender and a recipient"""
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if sender == recipient:
            raise ValueError("Sender and recipient cannot be the same")

    def __eq__(self, __o: object) -> bool:
        return self.sender == __o.sender and self.recipient == __o.recipient and self.amount == __o.amount

    def __str__(self):
        """String representation of a transaction"""
        return f"{self.sender} -> {self.recipient} {self.amount}"

    def __hash__(self):
        """Hash of a transaction"""
        return int(sha512(str(self).encode()).hexdigest(), 16)