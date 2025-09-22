__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.sentence_reversal import reverse_words


def test_basic_two_words() -> None:
    assert reverse_words("Hello World") == "World Hello"


def test_collapses_whitespace_and_reverses() -> None:
    assert reverse_words("  a   b\t c ") == "c b a"


def test_unicode_words() -> None:
    assert reverse_words("I love python") == "python love I"


def test_empty_or_spaces_returns_empty() -> None:
    assert reverse_words("   ") == ""
