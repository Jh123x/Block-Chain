from typing import Any, Optional


class ChainNode(object):
    def __init__(self, value: Any, parent: 'ChainNode' = None, is_head: bool = False) -> None:
        """A chain node is a node in a chain"""
        super().__init__()
        self.is_head = False
        self._parent = parent

        if is_head and parent is not None:
            raise ValueError("Head nodes cannot have a parent")

        if parent is not None:
            parent.next = self

        self._value = value
        self._next = None

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
        self._parent = value
