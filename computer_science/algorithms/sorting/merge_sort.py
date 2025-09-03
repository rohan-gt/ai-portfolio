from typing import Union


def merge(left: list[Union[int, float]], right: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        left (list[Union[int, float]]): First sorted array
        right (list[Union[int, float]]): Second sorted array

    Returns:
        list[Union[int, float]]: A new sorted array containing all elements from both input arrays

    Space Complexity:
        O(n) where n is the total length of both input arrays
    """
    sorted_array = []
    i = j = 0

    # Compare elements from both arrays and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add any remaining elements (if any)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


def merge_sort(array: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Return a new sorted array using the merge sort algorithm.

    Args:
        array (list[Union[int, float]]): The input array of numbers to be sorted

    Returns:
        list[Union[int, float]]: A new sorted array

    Time Complexity:
        O(n log n) for all cases (best, average, and worst)

    Space Complexity:
        O(n) for storing temporary arrays during merging
        O(log n) additional space for the recursive call stack
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(array) <= 1:
        return array.copy()

    # Divide step: split array into two roughly equal halves
    # This ensures O(log n) levels of recursion
    mid = len(array) // 2

    # Recursively sort the left and right halves
    # Each recursive call works on a subset of the original array
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge step: combine two sorted arrays into one
    # This is where the actual combining of sorted sequences happens
    return merge(left, right)


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    sorted_array = merge_sort(array)
    print(f"Original array: {array}")
    print(f"Sorted array: {sorted_array}")
