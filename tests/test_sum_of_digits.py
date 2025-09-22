import pytest

from src.algorithms.numbers.sum_of_digits import sum_of_digits


def test_sum_of_digits_basic() -> None:
    assert sum_of_digits(4321) == 10


def test_sum_of_digits_zero() -> None:
    assert sum_of_digits(0) == 0


def test_sum_of_digits_negative_raises() -> None:
    with pytest.raises(ValueError):
        sum_of_digits(-7)
