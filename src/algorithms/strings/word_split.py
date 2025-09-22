__author__ = 'Mihail Mihaylov'
"""
Problem:
Given a string `phrase` and a dictionary of words, return one valid split of the
phrase into dictionary words, or [] if impossible.

Examples:
    word_split("helloworld", {"hello", "world"}) -> ["hello", "world"]
    word_split("catsanddog", {"cat","cats","and","sand","dog"}) -> ["cats","and","dog"]

Notes:
- Deterministic DP solution (prefix scan), no greedy pitfalls.
- Time: O(n^2) worst-case; Space: O(n) for reconstruction.
"""

from typing import Collection, List


def word_split(phrase: str, dictionary: Collection[str]) -> List[str]:
    """
    Returns a valid segmentation of `phrase` into words from `dictionary`.

    :param phrase: Input string to segment.
    :param dictionary: Collection of valid words.
    :return: List of words forming the phrase, or [] if no segmentation exists.
    """
    n = len(phrase)
    words = set(dictionary)
    prev = [-1] * (n + 1)  # prev[i] = j means phrase[j:i] is a word and j is reachable
    prev[0] = 0

    for i in range(1, n + 1):
        # Scan all possible split points j < i
        for j in range(0, i):
            if prev[j] != -1 and phrase[j:i] in words:
                prev[i] = j
                break

    if prev[n] == -1:
        return []

    # Reconstruct words from prev[]
    out: List[str] = []
    i = n
    while i > 0:
        j = prev[i]
        out.append(phrase[j:i])
        i = j
    out.reverse()
    return out
