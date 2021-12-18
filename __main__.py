from typing import Union
from pprint import pprint

from block_chain.core.contracts import Contract
from block_chain.core.transaction import Transaction
from block_chain.core.block_chain import HashBlockChain


def transact_when_alice_gt_50(current_state: dict, transaction: Transaction) -> bool:
    return current_state.get("alice", 0) > 50


def always_execute(current_state: dict, transaction: Transaction) -> bool:
    return True


if __name__ == "__main__":

    # All Transactions
    actions: list[Union[Transaction, Contract]] = [
        Contract(
            transact_when_alice_gt_50,
            Transaction("Bob", "Alice", 50),
            "Execute when Alice has > 50"
        ),

        Transaction("Bob", "Charlie", 50),
        Transaction("Alice", "Bob", 100),

        Contract(
            always_execute,
            Transaction("Dawn", "Bob", 75),
            "Execute after next transaction"
        ),

        Transaction("Bob", "Alice", 100),
        Transaction("Charlie", "Dawn", 75),
    ]

    # The HashBlockChain
    chain = HashBlockChain()

    # Execute actions
    for action in actions:
        # Show the action
        print(action)

        if type(action) == Contract:
            chain.add_contract(action)
        elif type(action) == Transaction:
            chain.add_transaction(action)
        else:
            raise Exception("Invalid action")

    # Final State
    pprint(chain.get_current_state())
