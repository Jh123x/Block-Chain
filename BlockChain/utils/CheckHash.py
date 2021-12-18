from BlockChain.core.HashChainNode import HashChainNode


def check_hash(parent: HashChainNode, child: HashChainNode) -> bool:
    return hash(parent.get_stored_value()) == child.parent_hash
