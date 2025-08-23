from typing import Any

def selection_sort(array: list[Any]) -> None:
    """
    Sort an array in-place using the selection sort algorithm.

    Selection sort works by repeatedly finding the minimum element from the unsorted
    portion of the array and placing it at the beginning of the sorted portion.
    The algorithm maintains two subarrays: sorted and unsorted.

    Args:
        array (list[Any]): The input array to be sorted (modified in-place)

    Time Complexity:
        O(n²) for all cases (best, average, and worst)
        where n is the length of the array

    Space Complexity:
        O(1) as it only uses a constant amount of extra space
    """
    n = len(array)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of unsorted part
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == "__main__":
    array = [64, 25, 12, 22, 11]
    selection_sort(array)
    print(f"Sorted array is: {array}")
