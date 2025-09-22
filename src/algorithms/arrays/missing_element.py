"""
Problem:
Given two integer sequences `a` and `b` where `b` is `a` with exactly one element missing
(order may differ, duplicates allowed), return the missing element.

Examples:
    missing_element_sort([5, 5, 7, 7], [5, 7, 7]) -> 5
    missing_element_count([1, 2, 3, 4], [3, 1, 4]) -> 2

Constraints:
- Lengths must satisfy: len(a) = len(b) + 1
- Elements are integers; `b` is `a` minus exactly one occurrence (not a set difference)
- Duplicates may exist

Notes:
- Two reference implementations are provided:
  1) Sorting-based (O(n log n) time, O(1) extra if sorting in place; here we avoid mutation)
  2) Counting-based with a hashmap (O(n) time, O(n) space)
"""

from __future__ import annotations

from collections import defaultdict
from typing import DefaultDict, Iterable, List


def _validate_lengths(a: Iterable[int], b: Iterable[int]) -> None:
    """
    Asserts that len(a) = len(b) + 1; raises ValueError otherwise.

    :param a: First sequence.
    :param b: Second sequence (missing exactly one element from `a`).
    :raises ValueError: If the length relationship is not satisfied.
    """
    # Convert to lists once to support single pass and reuse
    if not isinstance(a, list):
        a = list(a)
    if not isinstance(b, list):
        b = list(b)
    if len(a) != len(b) + 1:
        raise ValueError("Lengths must satisfy len(a) = len(b) + 1.")


def missing_element_sort(a: Iterable[int], b: Iterable[int]) -> int:
    """
    Returns the missing element using a sorting approach.

    :param a: Sequence of integers.
    :param b: Same as `a` but with exactly one element removed (order irrelevant).
    :return: The missing integer.

    Time Complexity: O(n log n)
    Space Complexity: O(n) due to defensive copies for immutability.
    :raises ValueError: If lengths are invalid.
    """
    a_list: List[int] = list(a)
    b_list: List[int] = list(b)

    if len(a_list) != len(b_list) + 1:
        raise ValueError("Lengths must satisfy len(a) = len(b) + 1.")

    a_sorted = sorted(a_list)
    b_sorted = sorted(b_list)

    for x, y in zip(a_sorted, b_sorted):
        if x != y:
            return x
    return a_sorted[-1]


def missing_element_count(a: Iterable[int], b: Iterable[int]) -> int:
    """
    Returns the missing element using a counting (hashmap) approach.

    :param a: Sequence of integers.
    :param b: Same as `a` but with exactly one element removed (order irrelevant).
    :return: The missing integer.

    Time Complexity: O(n)
    Space Complexity: O(n)
    :raises ValueError: If lengths are invalid.
    """
    _validate_lengths(a, b)

    # Convert to lists once after validation so we can iterate multiple times
    a_list: List[int] = list(a) if not isinstance(a, list) else a
    b_list: List[int] = list(b) if not isinstance(b, list) else b

    counts: DefaultDict[int, int] = defaultdict(int)
    for num in b_list:
        counts[num] += 1

    for num in a_list:
        if counts[num] == 0:
            return num
        counts[num] -= 1

    # Should be unreachable if preconditions hold
    raise ValueError("No missing element found; check input preconditions.")
