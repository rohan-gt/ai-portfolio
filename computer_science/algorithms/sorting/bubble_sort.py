from typing import Union


def bubble_sort(array: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Return a new sorted array using the bubble sort algorithm.

    Args:
        array (list[Union[int, float]]): The input array to be sorted

    Returns:
        list[Union[int, float]]: A new sorted array

    Time Complexity:
        O(n²) where n is the length of the array
        Best Case: O(n) when array is already sorted

    Space Complexity:
        O(n) as it creates a copy of the input array
    """
    # Create a copy of the input array to maintain immutability
    sorted_array = array.copy()
    n = len(sorted_array)

    # Traverse through all array elements
    for i in range(n):
        # Initialize flag that will allow the function to
        # terminate if no swaps are needed (array is sorted)
        swapped = False

        # Last i elements are already in place, so inner loop can avoid them
        for j in range(n - i - 1):
            # Compare adjacent elements and swap if needed
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                swapped = True

        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break

    return sorted_array


if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(array)
    print(f"Original array: {array}")
    print(f"Sorted array: {sorted_array}")
