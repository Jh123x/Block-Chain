from types import LambdaType
from .Transaction import Transaction
from .HashChainNode import HashChainNode


class Contract(object):
    def __init__(self, conditional: LambdaType, transaction: Transaction, name: str = "") -> None:
        """Smart contracts to be executed on the blockchain
            Signature of conditional function: def condition(Contract, current_state: dict, latest_transaction: Transaction) -> bool
        """
        super().__init__()
        self.name = name
        self.conditional = conditional
        self.transaction = transaction

    def is_eligible(self, current_state: dict, latest_transaction: Transaction) -> bool:
        """Applies the contract to the current state"""
        return self.conditional(current_state, latest_transaction)

    def force_apply_contract(self, tail_chain: HashChainNode) -> HashChainNode:
        """Apply the contract to the chain"""
        return HashChainNode(self.transaction, parent=tail_chain)

    def apply_contract(self, current_state: dict, latest_transaction: Transaction, tail_chain: HashChainNode) -> HashChainNode:
        """Apply the contract to the current state"""
        if not self.is_eligible(current_state, latest_transaction):
            raise ValueError("Contract not eligible")
        return self.force_apply_contract(tail_chain)
