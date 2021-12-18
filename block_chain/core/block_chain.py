"""A hash block chain"""

from typing import Optional
from .contracts import Contract
from .transaction import Transaction
from .hash_chain_node import HashChainNode


class HashBlockChain:
    """A hash block chain"""
    def __init__(self, head: HashChainNode = None) -> None:
        """A block chain is a chain of hash chain nodes"""
        super().__init__()

        # Head and tail logic
        self.head: Optional['HashChainNode'] = head
        self.tail: Optional['HashChainNode'] = head

        # Keep track of contracts
        self.contracts: list[Contract] = []
        self._current_state: dict[str, int] = {}

        # Keep track of all users
        if head is None:
            return

        transaction: Transaction = head.get_stored_value()
        self._update_state_for_user(transaction.sender, -transaction.amount)
        self._update_state_for_user(transaction.recipient, transaction.amount)

    def get_current_state(self) -> dict:
        """Get a copy of the current state"""
        return self._current_state.copy()

    def _update_state_for_user(self, person_name: str, amount_change: int) -> None:
        """Update the state for a user"""
        if person_name not in self._current_state:
            self._current_state[person_name] = 0
        self._current_state[person_name] += amount_change

    def _add_transaction(self, transaction: Transaction):
        if self.head is None:
            self.head = HashChainNode(transaction, is_head=True)
            self.tail = self.head
        else:
            new_node = HashChainNode(transaction, self.tail)
            self.tail = new_node

        # Update current state
        self._update_state_for_user(transaction.sender, -transaction.amount)
        self._update_state_for_user(transaction.recipient, transaction.amount)

    def add_transaction(self, transaction: Transaction) -> None:
        """Add the transaction to the chain"""
        self._add_transaction(transaction)

        # Update apply contracts
        self._check_and_apply_contracts()

    def _check_and_apply_contracts(self) -> None:
        # Apply the contracts
        applied_contracts: list[Contract] = []

        for contract in self.contracts:
            if not contract.is_eligible(self._current_state, self.tail.get_stored_value()):
                continue
            self._add_transaction(contract.transaction)
            applied_contracts.append(contract)

        for contract in applied_contracts:
            self.contracts.remove(contract)

    def add_contract(self, contract: Contract) -> None:
        """Add the contract to the chain"""
        self.contracts.append(contract)
