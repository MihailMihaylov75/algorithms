__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.numbers.factorial import factorial_recursive, factorial_iterative


def test_recursive_zero_returns_one() -> None:
    assert factorial_recursive(0) == 1


def test_iterative_one_returns_one() -> None:
    assert factorial_iterative(1) == 1


def test_recursive_small_value() -> None:
    assert factorial_recursive(5) == 120


def test_iterative_small_value() -> None:
    assert factorial_iterative(6) == 720


def test_recursive_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        factorial_recursive(-1)


# disable-error-code=arg-type
def test_iterative_type_error_on_float() -> None:
    with pytest.raises(TypeError):
        factorial_iterative(3.14)
