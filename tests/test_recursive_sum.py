import pytest

from src.algorithms.numbers.recursive_sum import recursive_sum


def test_recursive_sum_basic() -> None:
    assert recursive_sum(5) == 15


def test_recursive_sum_zero() -> None:
    assert recursive_sum(0) == 0


def test_recursive_sum_negative_raises() -> None:
    with pytest.raises(ValueError):
        recursive_sum(-1)
