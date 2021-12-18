"""Represents a contract on the chain"""

from types import LambdaType
from .transaction import Transaction


class Contract:
    """Represents a contract on the chain"""

    def __init__(self, conditional: LambdaType, transaction: Transaction, name: str = "") -> None:
        """Smart contracts to be executed on the blockchain
            Signature of conditional function:
                def condition(current_state: dict, latest_transaction: Transaction) -> bool
        """
        super().__init__()
        self.name: str = name
        self.conditional: LambdaType = conditional
        self._transaction: Transaction = transaction

    def is_eligible(self, current_state: dict, latest_transaction: Transaction) -> bool:
        """Applies the contract to the current state"""
        return self.conditional(current_state, latest_transaction)

    def __str__(self):
        """String representation of Contract"""
        return f"{self.name}: {self._transaction}"

    @property
    def transaction(self):
        """Retrieves the transaction of the contract"""
        return self._transaction
