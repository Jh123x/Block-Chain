from .CheckHash import check_hash

from BlockChain.core.Transaction import Transaction
from BlockChain.core.HashChainNode import HashChainNode


def calculate_balance(head: HashChainNode) -> dict[str, int]:
    """Calcualte the balance of all the users in the chain"""
    amount_by_user = {}

    if not head.is_head or head is None:
        raise ValueError("Invalid chain head")

    curr = head
    while True:
        value = curr.get_stored_value()

        if not isinstance(value, Transaction):
            raise ValueError("Invalid transaction")

        users = [value.sender, value.recipient]
        for user in users:
            if user not in amount_by_user:
                amount_by_user[user] = 0

        amount_by_user[value.sender] -= value.amount
        amount_by_user[value.recipient] += value.amount

        if curr.next is None:
            break

        # Check the hash
        if not check_hash(curr, curr.next):
            raise ValueError("Invalid chain")

        # Go to the next node
        curr = curr.next

    return amount_by_user
