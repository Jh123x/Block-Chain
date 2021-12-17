from BlockChain.core.HashChainNode import HashChainNode
from BlockChain.core.Transaction import Transaction
from BlockChain.utils.CheckBalance import calculate_balance


if __name__ == "__main__":
    head = HashChainNode(Transaction('x', 'y', 20), is_head=True)
    next = HashChainNode(Transaction('y', 'z', 10), parent=head)
    next2 = HashChainNode(Transaction('z', 'x', 5), parent=next)

    # Comment / uncomment to corrupt hash
    # next._value = Transaction('x', 'z', 100)

    print(head)
    print(calculate_balance(head))
