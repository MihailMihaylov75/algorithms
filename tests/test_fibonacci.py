__author__ = 'Mihail Mihaylov'
from itertools import islice

import pytest

from src.algorithms.numbers.fibonacci import (
    fib_iterative,
    fib_recursive,
    fib_sequence,
    fibonacci_generator,
)


def test_iterative_small_value() -> None:
    assert fib_iterative(6) == 8


def test_recursive_small_value() -> None:
    assert fib_recursive(5) == 5


def test_sequence_first_five() -> None:
    assert fib_sequence(5) == [0, 1, 1, 2, 3]


def test_generator_first_five() -> None:
    assert list(islice(fibonacci_generator(), 5)) == [0, 1, 1, 2, 3]


def test_iterative_negative_raises_value_error() -> None:
    with pytest.raises(ValueError):
        fib_iterative(-1)  # negative index
