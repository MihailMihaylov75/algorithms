"""
Problem:
Determine whether a string consists of all unique characters.

Examples:
    is_unique("abc")    -> True
    is_unique("abca")   -> False
    is_unique("")       -> True
    is_unique("абв")    -> True   # Unicode supported

Notes:
- Two implementations:
  1) is_unique: single pass with early exit using a 'seen' set (O(n) time, O(n) space).
  2) is_unique_set: compares lengths of 'set(text)' and 'text' (O(n) time, O(n) space).
"""

from typing import Set


def is_unique(text: str) -> bool:
    """
    Checks whether all characters in the input string are unique.

    :param text: Input string (Unicode-supported).
    :return: True if all characters are unique; False otherwise.

    Time Complexity: O(n)
    Space Complexity: O(min(n, alphabet))
    """
    seen: Set[str] = set()
    for ch in text:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def is_unique_set(text: str) -> bool:
    """
    Alternative implementation using set size comparison.

    :param text: Input string.
    :return: True if all characters are unique; False otherwise.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(set(text)) == len(text)
