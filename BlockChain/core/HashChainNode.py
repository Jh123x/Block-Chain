from ctypes import resize
import hashlib
from types import FunctionType
from typing import Any, Optional
from .ChainNode import ChainNode


class HashChainNode(ChainNode):

    @staticmethod
    def hash(chain: 'ChainNode', hash_function: FunctionType = hashlib.sha512) -> int:
        """
        The hash function is applied to the value of the node.
        Returns None if the chain has no value
        """
        if chain is None:
            return None
        return hash_function(chain.get_stored_value().encode()).hexdigest()

    def __init__(self, value: Any, parent: 'ChainNode' = None, is_head: bool = False) -> None:
        """A hash chain node is a chain node with a hash value"""
        self.is_init = True
        super().__init__(value, parent, is_head=is_head)
        self.parent_hash = HashChainNode.hash(self.parent)
        self.is_init = False
        del self.is_init

    @property
    def parent(self) -> Optional['ChainNode']:
        """Retrieves the parent if the hash value is correct"""
        parent = super().parent
        if self.is_init or parent is None or self.parent_hash == HashChainNode.hash(parent):
            return parent
        raise ValueError("Parent hash does not match")

    @parent.setter
    def parent(self, value: 'ChainNode') -> None:
        """Sets the new parent and recomputes the hash value"""
        super().parent = value
        self.parent_hash = HashChainNode.hash(self.parent)
