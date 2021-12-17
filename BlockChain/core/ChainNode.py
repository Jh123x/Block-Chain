from typing import Any, Optional


class ChainNode(object):
    def __init__(self, value: Any, parent: 'ChainNode' = None, is_head: bool = False) -> None:
        """A chain node is a node in a chain"""
        super().__init__()
        self.is_head = is_head
        self._parent = parent

        self._is_valid_chain(parent, is_head)

        if parent is not None:
            parent.next = self

        self._value = value
        self._next = None

    def _is_valid_chain(self, parent, is_head):
        """Checks if the chain is valid"""
        if is_head and parent is not None:
            raise ValueError("Head nodes cannot have a parent")

        if not is_head and parent is None:
            raise ValueError("Non-head nodes must have a parent")

        if not issubclass(type(parent), ChainNode) and parent is not None:
            raise ValueError("Parent must be a ChainNode")

    def get_stored_value(self) -> Any:
        """Gets the value stored in the node"""
        return self._value

    @property
    def next(self) -> Optional['ChainNode']:
        """Returns the next"""
        return self._next

    @next.setter
    def next(self, value: 'ChainNode') -> None:
        self._next = value

    @property
    def parent(self) -> Optional['ChainNode']:
        return self._parent

    @parent.setter
    def parent(self, value: 'ChainNode') -> None:
        if not isinstance(value, ChainNode):
            raise ValueError("Parent must be a ChainNode")
        self._parent = value

    def __str__(self):
        return f"ChainNode: {str(self._value)} -> {str(self._next)}"
