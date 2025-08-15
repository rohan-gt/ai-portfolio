from typing import Any, Optional


class Stack:
    """A stack implementation using a Python list."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self) -> Optional[Any]:
        """Return the top item from the stack without removing it."""
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()

    def __str__(self) -> str:
        """Return a string representation of the stack."""
        return str(self._items)
