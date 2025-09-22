__author__ = 'Mihail Mihaylov'
import pytest

from src.algorithms.numbers.coin_change_min import min_coins_memo


def test_min_coins_usa_63_cents() -> None:
    assert min_coins_memo(63, [1, 5, 10, 25]) == 6


def test_min_coins_zero_target() -> None:
    assert min_coins_memo(0, [2, 3]) == 0


def test_min_coins_impossible_raises() -> None:
    with pytest.raises(ValueError):
        min_coins_memo(3, [2])  # cannot make 3 with coin 2
