def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the array for the quick sort algorithm.

    Args:
        arr: The array to be partitioned.
        low: The starting index of the partition.
        high: The ending index of the partition.

    Returns:
        The partition index.
    """
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: list[int], low: int, high: int) -> None:
    """
    Sort an array of integers using the quick sort algorithm.

    Args:
        arr: A list of integers to be sorted.
        low: The starting index of the sort.
        high: The ending index of the sort.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array is:", arr)
