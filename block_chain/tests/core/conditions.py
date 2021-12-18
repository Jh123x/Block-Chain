"""Conditions used for contract testing"""

from block_chain.core.transaction import Transaction


def condition_any_transaction(_: dict, __: Transaction):
    """Always true"""
    return True


def condition_transaction_gt_5(_: dict, latest_transaction: Transaction):
    """Check if latest transaction is more than 5"""
    return latest_transaction.amount > 5
