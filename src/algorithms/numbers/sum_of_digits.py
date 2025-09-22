__author__ = 'Mihail Mihaylov'
"""
Problem:
Return the sum of the decimal digits of a non-negative integer.

Examples:
    sum_of_digits(4321) -> 10
    sum_of_digits(0)    -> 0

Notes:
- Valid only for non-negative integers.
- Time: O(d) where d is number of digits. Space: O(1).
"""

def sum_of_digits(n: int) -> int:
    """
    Computes the sum of digits of n.

    :param n: Non-negative integer.
    :return: Sum of digits.
    :raises TypeError: If n is not int.
    :raises ValueError: If n < 0.
    """
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
