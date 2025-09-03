from typing import Union


def quick_sort(array: list[Union[int, float]]) -> list[Union[int, float]]:
    """
    Return a new sorted array using the quicksort algorithm.

    Args:
        array (list[Union[int, float]]): The input array to be sorted

    Returns:
        list[Union[int, float]]: A new sorted array

    Time Complexity:
        Average Case: O(n log n)
        Worst Case: O(n²)

    Space Complexity:
        Average Case: O(log n) for recursive call stack
        Worst Case: O(n) for recursive call stack and array copies
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(array) <= 1:
        return array.copy()

    # Create a copy of the input array to maintain immutability
    sorted_array = array.copy()

    # Choose the middle element as pivot (could also choose first, last, or random)
    pivot = sorted_array[len(sorted_array) // 2]

    # Partition the array into three parts:
    # Elements less than pivot
    left = [x for x in sorted_array if x < pivot]
    # Elements equal to pivot
    middle = [x for x in sorted_array if x == pivot]
    # Elements greater than pivot
    right = [x for x in sorted_array if x > pivot]

    # Recursively sort the left and right partitions and combine with middle
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    sorted_array = quick_sort(array)
    print(f"Original array: {array}")
    print(f"Sorted array: {sorted_array}")
