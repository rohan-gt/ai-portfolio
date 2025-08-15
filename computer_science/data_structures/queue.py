from collections import deque
from typing import Any, Optional


class Queue:
    """A queue implementation using collections.deque."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self._items.popleft()
        return None

    def peek(self) -> Optional[Any]:
        """Return the front item from the queue without removing it."""
        if not self.is_empty():
            return self._items[0]
        return None

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from the queue."""
        self._items.clear()

    def __str__(self) -> str:
        """Return a string representation of the queue."""
        return str(list(self._items))


class PriorityQueue:
    """A priority queue implementation using a list."""

    def __init__(self) -> None:
        """Initialize an empty priority queue."""
        self._items: list[tuple[int, Any]] = []

    def enqueue(self, item: Any, priority: int) -> None:
        """Add an item with given priority to the queue."""
        self._items.append((priority, item))
        self._items.sort(reverse=True)  # Higher priority first

    def dequeue(self) -> Optional[Any]:
        """Remove and return the highest priority item."""
        if not self.is_empty():
            return self._items.pop(0)[1]
        return None

    def peek(self) -> Optional[Any]:
        """Return the highest priority item without removing it."""
        if not self.is_empty():
            return self._items[0][1]
        return None

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from the queue."""
        self._items.clear()

    def __str__(self) -> str:
        """Return a string representation of the priority queue."""
        return str([(p, item) for p, item in self._items])
