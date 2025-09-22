__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.balance_parentheses_check import balance_parentheses


def test_simple_balanced() -> None:
    assert balance_parentheses("()")


def test_unbalanced_wrong_type() -> None:
    assert not balance_parentheses("(]")


def test_unbalanced_wrong_order() -> None:
    assert not balance_parentheses("([)]")


def test_empty_string_is_balanced() -> None:
    assert balance_parentheses("")

