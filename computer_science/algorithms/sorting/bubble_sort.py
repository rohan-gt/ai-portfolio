from typing import Any


def bubble_sort(array: list[Any]) -> None:
    """
    Sort an array in-place using the bubble sort algorithm.

    Bubble sort works by repeatedly stepping through the list, comparing adjacent
    elements and swapping them if they are in the wrong order. The pass through
    the list is repeated until no swaps are needed.

    Args:
        array (list[Any]): The input array to be sorted (modified in-place)

    Time Complexity:
        O(n²) where n is the length of the array
        Best Case: O(n) when array is already sorted

    Space Complexity:
        O(1) as it only uses a constant amount of extra space
    """
    n = len(array)
    for i in range(n):
        # Flag to optimize for already sorted arrays
        swapped = False

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        # If no swaps occurred, array is sorted
        if not swapped:
            break


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(array)
    print(f"Sorted array is: {array}")
