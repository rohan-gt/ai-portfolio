from typing import Any


def partition(array: list[Any], low: int, high: int) -> int:
    """
    Partition the array using the last element as the pivot.

    This function takes the last element as the pivot, places the pivot at its correct
    position in the sorted array, and places all smaller elements to the left of
    the pivot and all greater elements to the right of the pivot.

    Args:
        array (list[Any]): The array to be partitioned
        low (int): Starting index of the partition
        high (int): Ending index of the partition

    Returns:
        int: The final position of the pivot element

    Note:
        This function modifies the array in-place
    """
    # Choose the rightmost element as pivot
    pivot = array[high]
    i = low - 1  # Index of smaller element

    # Place all elements smaller than pivot to the left side
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1  # Increment index of smaller element
            array[i], array[j] = array[j], array[i]

    # Place pivot in its final position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array: list[Any], low: int = None, high: int = None) -> None:
    """
    Sort an array in-place using the quicksort algorithm.

    Quicksort uses a divide-and-conquer strategy. It works by selecting a 'pivot'
    element and partitioning the array around it such that smaller elements are on
    the left and larger elements are on the right.

    Args:
        array (List[T]): The input array to be sorted (modified in-place)
        low (int, optional): Starting index of the sort range. Defaults to 0
        high (int, optional): Ending index of the sort range. Defaults to len(array)-1

    Time Complexity:
        Average Case: O(n log n)
        Worst Case: O(n²) when array is already sorted
        Best Case: O(n log n)

    Space Complexity:
        O(log n) due to the recursive call stack

    Example:
        >>> arr = [10, 7, 8, 9, 1, 5]
        >>> quick_sort(arr)
        >>> print(arr)
        [1, 5, 7, 8, 9, 10]
    """
    # Initialize default values for first call
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if low < high:
        # Get partition index and sort sub-arrays
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)


if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quick_sort(array)
    print(f"Sorted array is: {array}")
