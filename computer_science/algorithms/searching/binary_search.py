from typing import Any


def binary_search_iterative(array: list[Any], x: Any) -> int:
    """
    Perform binary search iteratively to find an element in a sorted array.

    Args:
        array (list[Any]): The sorted input array to search through
        x (Any): The target element to search for

    Returns:
        int: The index of the target element if found, -1 if not found

    Time Complexity:
        O(log n) where n is the length of the array

    Space Complexity:
        O(1) as it uses only a constant amount of extra space

    Note:
        The array must be sorted in ascending order for binary search to work correctly.
    """
    lower = 0
    upper = len(array) - 1

    while lower <= upper:
        # Calculate middle point, using // for integer division
        middle = (upper + lower) // 2

        if array[middle] < x:
            # Search in right subarray
            lower = middle + 1
        elif array[middle] > x:
            # Search in left subarray
            upper = middle - 1
        else:
            return middle

    return -1


def binary_search_recursive(array: list[Any], x: Any, lower: int = None, upper: int = None) -> int:
    """
    Perform binary search recursively to find an element in a sorted array.

    Args:
        array (list[Any]): The sorted input array to search through
        x (Any): The target element to search for
        lower (int, optional): The lower bound index of the search range. Defaults to start of array.
        upper (int, optional): The upper bound index of the search range. Defaults to end of array.

    Returns:
        int: The index of the target element if found, -1 if not found

    Time Complexity:
        O(log n) where n is the length of the array

    Space Complexity:
        O(log n) due to the recursive call stack

    Note:
        The array must be sorted in ascending order for binary search to work correctly.
    """
    # Initialize lower and upper for first call
    if lower is None:
        lower = 0
    if upper is None:
        upper = len(array) - 1

    # If the search range is valid
    if lower <= upper:
        # Calculate middle point
        middle = (upper + lower) // 2

        # If element is present at the middle
        if array[middle] == x:
            return middle
        # If element is greater than middle, search in right subarray
        elif array[middle] > x:
            return binary_search_recursive(array, x, lower, middle - 1)
        # If element is smaller than middle, search in left subarray
        else:
            return binary_search_recursive(array, x, middle + 1, upper)

    # Element is not present in array
    return -1


if __name__ == "__main__":
    # Example usage with a sorted array of integers
    array = [2, 3, 4, 10, 40]
    x = 10

    # Test iterative binary search
    result = binary_search_iterative(array, x)
    if result != -1:
        print(f"Element {x} is present at index {result} (iterative)")
    else:
        print(f"Element {x} is not present in array (iterative)")

    # Test recursive binary search
    result = binary_search_recursive(array, x)
    if result != -1:
        print(f"Element {x} is present at index {result} (recursive)")
    else:
        print(f"Element {x} is not present in array (recursive)")

    # Example with a non-existent element
    x = 15
    result = binary_search_iterative(array, x)
    if result != -1:
        print(f"Element {x} is present at index {result} (iterative)")
    else:
        print(f"Element {x} is not present in array (iterative)")
