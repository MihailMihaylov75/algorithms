__author__ = 'Mihail Mihaylov'
"""
Problem:
Reverse a string using recursion.

Examples:
    reverse_string_recursive("abc") -> "cba"
    reverse_string_recursive("")    -> ""

Notes:
- Recursive; for very long strings prefer iterative slicing for safety.
- Time: O(n), Space: O(n) due to recursion depth.
"""

def reverse_string_recursive(s: str) -> str:
    """
    Reverses a string recursively.

    :param s: Input string.
    :return: Reversed string.
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]
