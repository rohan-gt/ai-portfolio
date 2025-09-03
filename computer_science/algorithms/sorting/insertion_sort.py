from typing import Union


def insertion_sort(array: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Return a new sorted array using the insertion sort algorithm.

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

    # Start from the second element (index 1) since first element
    # is considered as sorted portion initially
    for i in range(1, len(sorted_array)):
        # Move elements that are greater than current element
        # to one position ahead of their current position
        for j in range(i - 1, -1, -1):
            # Compare adjacent elements and shift larger ones right
            if sorted_array[j] > sorted_array[j + 1]:
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
            else:
                # Stop if we find a smaller element (array is sorted up to this point)
                break

    return sorted_array

if __name__ == "__main__":
    array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(array)
    print(f"Original array: {array}")
    print(f"Sorted array: {sorted_array}")
