from typing import Any, Optional


class Stack:
    """Stack implementation with LIFO (Last-In-First-Out) behavior."""

    def __init__(self) -> None:
        """Initializes an empty stack."""
        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """Pushes an item onto the top of the stack.

        Args:
            item (Any): The item to be pushed onto the stack.
        """
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        """Removes and returns the top item from the stack.

        Returns:
            Optional[Any]: The top item if stack is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self) -> Optional[Any]:
        """Returns the top item from the stack without removing it.

        Returns:
            Optional[Any]: The top item if stack is not empty, None otherwise.
        """
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self._items)

    def clear(self) -> None:
        """Removes all items from the stack."""
        self._items.clear()

    def __str__(self) -> str:
        """Returns a string representation of the stack.

        Returns:
            str: The string representation of the stack's contents.
        """
        return str(self._items)


if __name__ == "__main__":
    # Create a new stack
    stack = Stack()

    # Test stack operations
    print("Pushing items onto stack:")
    for item in [1, 2, 3, 4, 5]:
        stack.push(item)
        print(f"Pushed {item}, Stack: {stack}")

    print(f"\nPeek at top item: {stack.peek()}")

    print("\nPopping items from stack:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Remaining stack: {stack}")
