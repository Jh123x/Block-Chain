from typing import Any, Optional
from .ChainNode import ChainNode


class HashChainNode(ChainNode):

    def __init__(self, value: Any, parent: 'ChainNode' = None, is_head: bool = False) -> None:
        """A hash chain node is a chain node with a hash value"""
        self.is_init = True
        super().__init__(value, parent, is_head=is_head)

        if self.parent is not None:
            self.parent_hash = hash(self.parent.get_stored_value())
        else:
            self.parent_hash = None

        self.is_init = False
        del self.is_init

    @property
    def parent(self) -> Optional['ChainNode']:
        """Retrieves the parent if the hash value is correct"""
        parent = super().parent
        if parent is None or self.is_init or self.parent_hash == hash(parent.get_stored_value()):
            return parent
        raise ValueError("Parent hash does not match")

    @parent.setter
    def parent(self, value: 'ChainNode') -> None:
        """Sets the new parent and recomputes the hash value"""
        super().parent = value
        if value is not None:
            self.parent_hash = hash(self.parent.get_stored_value())
            return
        self.parent_hash = None

    def __str__(self):
        return f"HashChainNode {'(head)' if self.is_head else ''}: {str(self._value)} -> {str(self.next)}"
