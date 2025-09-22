"""
Problem:
Reverse the order of words in a sentence. Consecutive whitespace is collapsed
to a single space, and leading/trailing whitespace is removed.

Examples:
    reverse_words("Hello   world")        -> "world Hello"
    reverse_words("  a\tb  c ")           -> "c b a"
    reverse_words("")                     -> ""
    reverse_words("   ")                  -> ""

Notes:
- Splitting relies on str.split() (splits on any whitespace, collapses runs).
- Time Complexity: O(n)
- Space Complexity: O(n)  (for the list of words and the output string)
"""


def reverse_words(text: str) -> str:
    """
    Returns the input string with word order reversed, using single spaces
    between words (whitespace collapsed).

    :param text: Input string (may contain any whitespace).
    :return: String with reversed word order and normalized spacing.
    """
    words: list[str] = text.split()
    words.reverse()
    return " ".join(words)


def reverse_words_alt(text: str) -> str:
    """
    Alternate implementation using slicing.

    :param text: Input string.
    :return: String with reversed word order and normalized spacing.
    """
    return " ".join(text.split()[::-1])
