__author__ = 'Mihail Mihaylov'
from src.algorithms.strings.balance_parentheses_check import balance_parentheses


def test_simple_balanced() -> None:
    assert balance_parentheses("()") is True


def test_mixed_balanced() -> None:
    assert balance_parentheses("()[]{}") is True


def test_unbalanced_wrong_order() -> None:
    assert balance_parentheses("(]") is False
    assert balance_parentheses("([)]") is False


def test_empty_string() -> None:
    assert balance_parentheses("") is True

