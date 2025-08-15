def knapsack(W: int, wt: list[int], val: list[int], n: int) -> int:
    """
    Solve the knapsack problem using dynamic programming.

    Args:
        W: The maximum weight capacity of the knapsack.
        wt: A list of weights of the items.
        val: A list of values of the items.
        n: The number of items.

    Returns:
        The maximum value that can be put in a knapsack of capacity W.
    """
    # Create a 2D array to store the maximum value that can be obtained
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table K[][] in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(f"Maximum value in Knapsack is {knapsack(W, wt, val, n)}")
