from typing import Any


class Array:
    """A simple wrapper around Python's list to mimic array behavior."""

    def __init__(self, size: int, default_value: Any = None) -> None:
        """Initializes the array with a fixed size and default value.

        Args:
            size (int): The size of the array.
            default_value (Any, optional): The default value for each element. Defaults to None.
        """
        self.size = size
        self.data = [default_value] * size

    def append(self, value: Any) -> None:
        """Appends a value to the end of the array.

        Args:
            value (Any): The value to append.
        """
        self.data.append(value)
        self.size += 1

    def insert(self, index: int, value: Any) -> None:
        """Inserts a value at the specified index.

        Args:
            index (int): The index to insert the value at.
            value (Any): The value to insert.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if 0 <= index <= self.size:
            self.data.insert(index, value)
            self.size += 1
        else:
            raise IndexError("Array index out of bounds")

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of the value from the array.

        Args:
            value (Any): The value to remove.

        Raises:
            ValueError: If the value is not found in the array.
        """
        self.data.remove(value)
        self.size -= 1

    def clear(self) -> None:
        """Removes all elements from the array."""
        self.data.clear()
        self.size = 0

    def update(self, index: int, value: Any) -> None:
        """Updates the value at the specified index.

        Args:
            index (int): The index of the element to update.
            value (Any): The new value to set.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Array index out of bounds")

    def display(self) -> None:
        """Displays the elements of the array."""
        print(self.data)


if __name__ == "__main__":
    # Demonstrate the usage of the Array class
    arr = Array(5, default_value=0)
    print("Initial array:", arr)

    # Append element
    arr.append(20)
    print("After appending 20:", arr)

    # Insert element
    arr.insert(1, 15)
    print("After inserting 15 at index 1:", arr)

    # Delete element
    arr.delete(10)
    print("After removing 10:", arr)

    # Update element
    arr.update(2, 25)
    print("After updating index 2 to 25:", arr)

    # Display the array
    print("Displaying the array:")
    arr.display()

    # Clear the array
    arr.clear()
    print("After clearing the array:", arr)
