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
    # Traverse through 1 to len(array)
    for i in range(1, len(array)):
        # Element to be inserted into sorted portion
        key = array[i]

        # Move elements of array[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Place key in its correct position
        array[j + 1] = key


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    insertion_sort(array)
    print(f"Sorted array is: {array}")
