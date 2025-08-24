def least_common_subsequence(X: str, Y: str) -> int:
    """
    Calculate the length of the longest common subsequence (LCS) of two strings.

    Args:
        X: The first string.
        Y: The second string.

    Returns:
        The length of the LCS of X and Y.
    """
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of LCS
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the LCS table in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(f"Length of LCS is {least_common_subsequence(X, Y)}")
