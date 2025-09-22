__author__ = 'Mihail Mihaylov'
"""
Problem:
Generate all permutations of a string with (assumed) distinct characters.

Examples:
    permutations("abc") -> ["abc","acb","bac","bca","cab","cba"] (order may vary)

Notes:
- If the string has duplicate characters, duplicates will appear in the output.
- Time: O(n * n!) total; Space: O(n * n!) for the result.
"""

from typing import List


def permutations(s: str) -> List[str]:
    """
    Returns all permutations of `s` (assumes distinct chars).

    :param s: Input string.
    :return: List of permutations (order not guaranteed).
    """
    if len(s) <= 1:
        return [s]
    out: List[str] = []
    for i, ch in enumerate(s):
        for perm in permutations(s[:i] + s[i + 1:]):
            out.append(ch + perm)
    return out
