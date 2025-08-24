from typing import Any


def insertion_sort(array: list[Any]) -> None:
    """
    Sort an array in-place using the insertion sort algorithm.

    Insertion sort builds the final sorted array one item at a time by repeatedly
    taking elements from the unsorted portion and inserting them into their correct
    position in the sorted portion.

    Args:
        array (list[Any]): The input array to be sorted (modified in-place)

    Time Complexity:
        O(n²) where n is the length of the array
        Best Case: O(n) when array is already sorted

    Space Complexity:
        O(1) as it only uses a constant amount of extra space
    """
    n = len(array)

    # Start from the second element (index 1)
    for i in range(1, n):
        # Move backwards through the sorted portion
        for j in range(i - 1, -1, -1):
            # If current element is greater than next element, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    insertion_sort(array)
    print(f"Sorted array is: {array}")
