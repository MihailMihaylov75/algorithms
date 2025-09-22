__author__ = 'Mihail Mihaylov'
"""
Problem:
Return the sum 1 + 2 + ... + n for a non-negative integer n. For n = 0 -> 0.

Examples:
    recursive_sum(5) -> 15
    recursive_sum(0) -> 0

Notes:
- Valid only for non-negative integers.
- Time: O(n), Space: O(n) due to recursion depth.
"""

def recursive_sum(n: int) -> int:
    """
    Computes the sum 1..n recursively.

    :param n: Non-negative integer.
    :return: Sum from 1 to n (0 if n == 0).
    :raises TypeError: If n is not int.
    :raises ValueError: If n < 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    return 0 if n == 0 else n + recursive_sum(n - 1)
