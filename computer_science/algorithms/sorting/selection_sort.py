from typing import Union


def selection_sort(array: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Return a new sorted array using the selection sort algorithm.

    Args:
        array (list[Union[int, float]]): The input array to be sorted

    Returns:
        list[Union[int, float]]: A new sorted array

    Time Complexity:
        O(n²) for all cases (best, average, and worst)

    Space Complexity:
        O(n) as it creates a copy of the input array
    """
    sorted_array = array.copy()
    n = len(sorted_array)

    # Iterate through each position in the array
    for i in range(n):
        # Assume the current position contains the minimum value
        min_idx = i

        # Find the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            # If we find a smaller element, update the minimum index
            if sorted_array[j] < sorted_array[min_idx]:
                min_idx = j

        # If we find a smaller element, swap it with the current position
        # This gradually builds up the sorted portion from left to right
        if min_idx != i:
            sorted_array[i], sorted_array[min_idx] = sorted_array[min_idx], sorted_array[i]

    return sorted_array


if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(array)
    print(f"Original array: {array}")
    print(f"Sorted array is: {sorted_array}")
