def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming.

    Args:
        n: The position of the Fibonacci number to calculate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the base cases
    fib = [0] * (n + 1)
    fib[1] = 1

    # Compute the Fibonacci sequence up to n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n} is {fibonacci(n)}")
