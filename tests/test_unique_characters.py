__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.unique_characters_in_string import is_unique


def test_unique_ascii_returns_true() -> None:
    assert is_unique("abc")


def test_duplicate_character_returns_false() -> None:
    assert not is_unique("abca")


def test_unicode_unique_returns_true() -> None:
    assert is_unique("asdrt")


def test_empty_string_returns_true() -> None:
    assert is_unique("")
