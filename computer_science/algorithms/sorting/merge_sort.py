from typing import Any

def merge_sort(array: list[Any]) -> None:
    """
    Sort an array in-place using the merge sort algorithm.

    Merge sort uses the divide-and-conquer strategy. It divides the input array into
    two halves, recursively sorts them, and then merges the sorted halves to
    produce a sorted array.

    Args:
        array (list[Any]): The input array to be sorted (modified in-place)

    Time Complexity:
        O(n log n) for all cases (best, average, and worst)
        where n is the length of the array

    Space Complexity:
        O(n) as it requires additional space for merging
    """
    if len(array) > 1:
        # Divide the array into two halves
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        # Initialize pointers for merging
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Check for remaining elements in left half
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Check for remaining elements in right half
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    merge_sort(array)
    print(f"Sorted array is: {array}")
