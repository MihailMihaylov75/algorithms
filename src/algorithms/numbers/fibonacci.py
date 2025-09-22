"""
Problem:
Compute Fibonacci numbers and sequences.

Provided APIs:
- fibonacci_generator(): infinite generator yielding 0, 1, 1, 2, 3, ...
- fib_iterative(n): returns the n-th Fibonacci number (n >= 0)
- fib_recursive(n): same via naive recursion (educational)
- fib_sequence(n): returns a list with the first n Fibonacci numbers

Constraints:
- n must be a non-negative integer
- Recursive version is exponential and limited by recursion depth

Examples:
    fib_iterative(5)   -> 5
    fib_recursive(6)   -> 8
    fib_sequence(5)    -> [0, 1, 1, 2, 3]
"""

from collections.abc import Iterator
from typing import Final

_MIN_N: Final[int] = 0


def _validate(n: int) -> None:
    """
    Validates the input domain for Fibonacci functions.

    :param n: Candidate value (index or length).
    :raises TypeError: If n is not an int.
    :raises ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < _MIN_N:
        raise ValueError("n must be >= 0")


def fibonacci_generator() -> Iterator[int]:
    """
    Infinite Fibonacci generator.

    :return: Iterator yielding the sequence 0, 1, 1, 2, 3, ...
    Time Complexity per next(): O(1)
    Space Complexity: O(1)
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_iterative(n: int) -> int:
    """
    Computes the n-th Fibonacci number using an iterative loop.

    :param n: Non-negative index (0-based).
    :return: The n-th Fibonacci number.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    _validate(n)
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_recursive(n: int) -> int:
    """
    Computes the n-th Fibonacci number using naive recursion.

    :param n: Non-negative index (0-based).
    :return: The n-th Fibonacci number.
    Time Complexity: O(phi^n) (educational only)
    Space Complexity: O(n) due to call stack
    """
    _validate(n)
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_sequence(n: int) -> list[int]:
    """
    Returns the first n Fibonacci numbers as a list.

    :param n: Number of terms to produce (n >= 0).
    :return: List with the first n Fibonacci numbers.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    _validate(n)
    seq: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq
