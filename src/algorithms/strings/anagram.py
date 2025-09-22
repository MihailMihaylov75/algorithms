"""
Anagram checking algorithms.

Problem
-------
Given two strings `word_one` and `word_two`, determine whether they are anagrams:
they contain exactly the same multiset of characters after removing spaces and
ignoring case.

Assumptions
-----------
- Spaces are ignored.
- Comparison is case-insensitive.
- All other characters are compared literally (punctuation/numbers are kept).

Examples
--------
>>> is_anagram("rail safety", "fairy tales")
True
>>> is_anagram("Listen", "Silent")
True
>>> is_anagram("hello", "bello")
False

Complexity
----------
- is_anagram  : O(n log n) time (sorting), O(n) space.
- is_anagram2 : O(n) time (counting), O(k) space where k is the alphabet size.
"""

from __future__ import annotations

from collections import Counter

__author__ = "Mihail Mihaylov"
__all__ = ["is_anagram", "is_anagram2"]


def _normalize(value: str) -> str:
    """
    Returns a canonical form of the input suitable for anagram comparison.

    - Lower cases all letters.
    - Removes spaces only (keeps punctuation/numbers).

    Args:
        value: Input string.

    Returns:
        The normalized string.
    """
    return value.replace(" ", "").lower()


def is_anagram(word_one: str, word_two: str) -> bool:
    """
    Checks whether two words are anagrams using sorting.

    Args:
        word_one: First word.
        word_two: Second word.

    Returns:
        True if the inputs are anagrams, otherwise False.
    """
    a = _normalize(word_one)
    b = _normalize(word_two)
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)


def is_anagram2(word_one: str, word_two: str) -> bool:
    """
    Checks whether two words are anagrams using character counting.

    This is an O(n) alternative based on collections.Counter.

    Args:
        word_one: First word.
        word_two: Second word.

    Returns:
        True if the inputs are anagrams, otherwise False.
    """
    a = _normalize(word_one)
    b = _normalize(word_two)
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)
