from typing import Any


class Array:
    """Canonical array implementation with standard DSA operations."""

    def __init__(self, size: int) -> None:
        """Initializes an empty array with a fixed size.

        Args:
            size (int): Maximum capacity of the array.
        """
        self._size = size
        self._array = [None] * size
        self._count = 0

    def get(self, index: int) -> Any:
        """Returns the element at the specified index.

        Args:
            index (int): Index of the element to access.

        Raises:
            IndexError: If index is out of bounds.

        Returns:
            Any: Value at the specified index.
        """
        if 0 <= index < self._count:
            return self._array[index]
        raise IndexError("Array index out of bounds")

    def set(self, index: int, value: Any) -> None:
        """Updates the element at the specified index.

        Args:
            index (int): Index of the element to update.
            value (Any): New value to set.

        Raises:
            IndexError: If index is out of bounds.
        """
        if 0 <= index < self._count:
            self._array[index] = value
        else:
            raise IndexError("Array index out of bounds")

    def insert(self, index: int, value: Any) -> None:
        """Inserts a value at the specified index, shifting elements right.

        Args:
            index (int): Index to insert at.
            value (Any): Value to insert.

        Raises:
            IndexError: If index is out of bounds.
            OverflowError: If array is full.
        """
        if not (0 <= index <= self._count):
            raise IndexError("Array index out of bounds")
        if self._count >= self._size:
            raise OverflowError("Array is full")
        for i in range(self._count, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = value
        self._count += 1

    def delete(self, index: int) -> None:
        """Deletes the element at the specified index, shifting elements left.

        Args:
            index (int): Index of the element to delete.

        Raises:
            IndexError: If index is out of bounds.
        """
        if not (0 <= index < self._count):
            raise IndexError("Array index out of bounds")
        for i in range(index, self._count - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._count - 1] = None
        self._count -= 1

    def traverse(self) -> None:
        """Prints all elements of the array in order."""
        print([self._array[i] for i in range(self._count)])

    def size(self) -> int:
        """Returns the current number of elements in the array."""
        return self._count


if __name__ == "__main__":
    # Initialize array
    arr = Array(size=5)
    print("Initialized array:")
    arr.traverse()

    # Insert elements
    arr.insert(0, 5)
    arr.insert(1, 10)
    arr.insert(1, 7)
    print("After inserts:")
    arr.traverse()

    # Update element
    arr.set(1, 15)
    print("After update:")
    arr.traverse()

    # Delete element
    arr.delete(0)
    print("After delete:")
    arr.traverse()

    # Size of array
    print("Current size:", arr.size())
