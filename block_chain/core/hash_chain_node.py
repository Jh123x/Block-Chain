"""A HashChainNode for the hash chain"""

from typing import Any, Optional
from .chain_node import ChainNode


class HashChainNode(ChainNode):
    """A HashChainNode for the hash chain"""

    def __init__(self, value: Any, parent: 'ChainNode' = None, is_head: bool = False) -> None:
        """A hash chain node is a chain node with a hash value"""
        self._is_init: bool = True
        super().__init__(value, parent, is_head=is_head)
        if self.parent is not None:
            self.parent_hash: Optional[int] = hash(
                self.parent.get_stored_value())
        else:
            self.parent_hash: Optional[int] = None
        self._is_init: bool = False

    @property
    def parent(self) -> Optional['HashChainNode']:
        """Retrieves the parent if the hash value is correct"""
        if self.is_head:
            return None

        if self._is_init:
            return self._parent

        if self.parent_hash != hash(self._parent.get_stored_value()):
            raise ValueError(
                f"Parent hash does not match: {self.parent_hash} \
                != {hash(self._parent.get_stored_value())}")

        return self._parent

    @parent.setter
    def parent(self, value: 'HashChainNode') -> None:
        """Sets the new parent and recomputes the hash value"""
        if not isinstance(value, HashChainNode):
            raise ValueError("Parent must be a HashChainNode")

        if value is None and not self.is_head:
            raise ValueError("Child Nodes must have a parent")

        self._parent = value

        self.parent_hash = hash(value.get_stored_value())
        value.next = self

    def __str__(self) -> str:
        """String representation of the hash chain node"""
        return f"HashChainNode {'(head)' if self.is_head else ''}: \
            {str(self._value)} -> {str(self.next)}"
