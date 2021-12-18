"""Checks if the hash is on the child is the same as the parent"""

from block_chain.core.hash_chain_node import HashChainNode


def check_hash(parent: HashChainNode, child: HashChainNode) -> bool:
    """Check the hash of the child matches the parents hash"""
    return hash(parent.get_stored_value()) == child.parent_hash
