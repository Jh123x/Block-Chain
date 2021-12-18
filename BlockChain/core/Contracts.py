from types import LambdaType
from .Transaction import Transaction


class Contract(object):
    def __init__(self, conditional: LambdaType, transaction: Transaction, name: str = "") -> None:
        """Smart contracts to be executed on the blockchain
            Signature of conditional function: def condition(Contract, current_state: dict, latest_transaction: Transaction) -> bool
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
        return self._transaction
