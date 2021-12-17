from BlockChain.core.HashChainNode import HashChainNode


if __name__ == "__main__":
    head = HashChainNode('x, y $20', is_head=True)
    next = HashChainNode('y, z $10', parent=head)
    next2 = HashChainNode('z, x $5', parent=next)

    # Comment / uncomment to corrupt hash
    # next._value = "z, y $10"

    curr = head
    curr_hash = None
    while True:

        # Print the current node
        print(f"Current Value:{curr.get_stored_value()}")

        # Check if there is a child
        if curr.next is None:
            print(f"No next node to check for hash")
            break

        # Check if the hash is correct from the child
        child = curr.next
        print(f"Hash match: {child.parent_hash == HashChainNode.hash(curr)}\n")

        # Go to the next part of the chain
        curr = curr.next
