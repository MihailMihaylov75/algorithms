"""
Problem:
Compute n! (factorial of a non-negative integer n).

Definitions:
- Recursive: n! = n * (n-1)! with 0! = 1 and 1! = 1
- Iterative: multiply down from n to 1

Constraints:
- n must be a non-negative integer
- Recursive version is limited by Python's recursion depth

Examples:
    factorial_recursive(5) -> 120
    factorial_iterative(5) -> 120

Notes:
- Prefer the iterative version for large n to avoid RecursionError.
"""
from typing import Final

_MIN_N: Final[int] = 0


def _validate(n: int) -> None:
    """
    Validates the input domain for factorial.

    :param n: Candidate value for factorial.
    :raises TypeError: If n is not an int.
    :raises ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < _MIN_N:
        raise ValueError("n must be >= 0")


def factorial_recursive(n: int) -> int:
    """
    Computes factorial using recursion.

    :param n: Non-negative integer.
    :return: n! (factorial of n).

    Time Complexity: O(n)
    Space Complexity: O(n) due to call stack
    :raises TypeError: If n is not an int.
    :raises ValueError: If n < 0.
    """
    _validate(n)
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Computes factorial using an iterative loop.

    :param n: Non-negative integer.
    :return: n! (factorial of n).

    Time Complexity: O(n)
    Space Complexity: O(1)
    :raises TypeError: If n is not an int.
    :raises ValueError: If n < 0.
    """
    _validate(n)
    result = 1
    # range(n, 1, -1) multiplies n * (n-1) * ... * 2
    for k in range(n, 1, -1):
        result *= k
    return result

