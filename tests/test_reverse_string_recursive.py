__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.reverse_string_recursive import reverse_string_recursive


def test_reverse_recursive_basic() -> None:
    assert reverse_string_recursive("more") == "erom"
