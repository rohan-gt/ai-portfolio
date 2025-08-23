from typing import Any


def linear_search(array: list[Any], x: Any) -> int:
    """
    Perform a linear search to find an element in an array.

    This function implements the linear search algorithm that sequentially checks
    each element in the array until a match is found or the end of the array
    is reached.

    Args:
        array (list[Any]): The input array to search through
        x (Any): The target element to search for

    Returns:
        int: The index of the target element if found, -1 if not found

    Time Complexity:
        O(n) where n is the length of the array

    Space Complexity:
        O(1) as it uses only a constant amount of extra space
    """
    n = len(array)
    for i in range(n):
        if array[i] == x:
            return i

    return -1


if __name__ == "__main__":
    # Example usage with integers
    array = [2, 3, 4, 10, 40]
    x = 10
    result = linear_search(array, x)
    if result != -1:
        print(f"Element {x} is present at index {result}")
    else:
        print(f"Element {x} is not present in array")

    # Example with strings
    names = ["Alice", "Bob", "Charlie", "David"]
    target = "Charlie"
    result = linear_search(names, target)
    if result != -1:
        print(f"Name '{target}' found at index {result}")
    else:
        print(f"Name '{target}' not found in the list")
