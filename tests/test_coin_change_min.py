__author__ = 'Mihail Mihaylov'
import pytest

from src.algorithms.numbers.coin_change_min import min_coins_memo, min_coins_naive


def test_min_coins_usa_63_cents() -> None:
    assert min_coins_memo(63, [1, 5, 10, 25]) == 6


def test_min_coins_zero_target() -> None:
    assert min_coins_memo(0, [2, 3]) == 0


def test_min_coins_impossible_raises() -> None:
    with pytest.raises(ValueError):
        min_coins_memo(3, [2])  # cannot make 3 with coin 2


def test_memo_negative_target_raises() -> None:
    with pytest.raises(ValueError):
        min_coins_memo(-1, [1, 2])


def test_memo_no_valid_denoms_raises() -> None:
    with pytest.raises(ValueError):
        min_coins_memo(5, [])  # empty coins and target > 0


def test_memo_zero_and_no_valid_coins_returns_zero() -> None:
    assert min_coins_memo(0, [0, -1]) == 0  # edge: zero target


def test_naive_simple_solution() -> None:
    assert min_coins_naive(6, [1, 3, 4]) == 2  # 3+3


def test_naive_impossible_raises() -> None:
    with pytest.raises(ValueError):
        min_coins_naive(3, [2])
