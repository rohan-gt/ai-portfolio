from collections import deque
from typing import Any, Optional, Tuple


class Queue:
    """Queue implementation with FIFO (First-In-First-Out) behavior."""

    def __init__(self) -> None:
        """Initializes an empty queue using collections.deque for O(1) operations."""
        self._items: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Adds an item to the back of the queue.

        Args:
            item (Any): The item to be added to the queue.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        """Removes and returns the front item from the queue.

        Returns:
            Optional[Any]: The front item if queue is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items.popleft()
        return None

    def peek(self) -> Optional[Any]:
        """Returns the front item from the queue without removing it.

        Returns:
            Optional[Any]: The front item if queue is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items[0]
        return None

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)

    def clear(self) -> None:
        """Removes all items from the queue."""
        self._items.clear()

    def __str__(self) -> str:
        """Returns a string representation of the queue.

        Returns:
            str: String representation of the queue's contents.
        """
        return str(list(self._items))


class PriorityQueue:
    """Priority Queue implementation where items are processed based on priority."""

    def __init__(self) -> None:
        """Initializes an empty priority queue."""
        self._items: list[Tuple[int, Any]] = []

    def enqueue(self, item: Any, priority: int) -> None:
        """Adds an item with given priority to the queue.

        Higher priority numbers have higher priority (are processed first).

        Args:
            item (Any): The item to be added to the queue.
            priority (int): Priority of the item (higher number = higher priority).
        """
        self._items.append((priority, item))
        self._items.sort(reverse=True)  # Higher priority first

    def dequeue(self) -> Optional[Any]:
        """Removes and returns the highest priority item.

        Returns:
            Optional[Any]: The highest priority item if queue is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items.pop(0)[1]
        return None

    def peek(self) -> Optional[Any]:
        """Returns the highest priority item without removing it.

        Returns:
            Optional[Any]: The highest priority item if queue is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items[0][1]
        return None

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self._items)

    def clear(self) -> None:
        """Removes all items from the queue."""
        self._items.clear()

    def __str__(self) -> str:
        """Returns a string representation of the priority queue.

        Returns:
            str: String representation showing items and their priorities.
        """
        return str([(p, item) for p, item in self._items])


if __name__ == "__main__":
    # Test regular Queue
    print("Testing Queue:")
    queue = Queue()
    for item in ["first", "second", "third"]:
        queue.enqueue(item)
        print(f"Enqueued {item}, Queue: {queue}")

    print(f"\nPeek at front item: {queue.peek()}")

    print("\nDequeueing items:")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}, Queue: {queue}")

    # Test PriorityQueue
    print("\nTesting PriorityQueue:")
    pq = PriorityQueue()
    items = [("low priority", 1), ("medium priority", 2), ("high priority", 3)]

    for item, priority in items:
        pq.enqueue(item, priority)
        print(f"Enqueued '{item}' with priority {priority}, PriorityQueue: {pq}")

    print(f"\nPeek at highest priority item: {pq.peek()}")

    print("\nDequeueing items:")
    while not pq.is_empty():
        print(f"Dequeued: {pq.dequeue()}, PriorityQueue: {pq}")
