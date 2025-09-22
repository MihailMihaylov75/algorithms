__author__ = 'Mihail Mihaylov'

from src.algorithms.arrays.array_pair_sum import array_pair_sum


def test_basic_case() -> None:
    assert array_pair_sum([1, 3, 2, 2], 4) == 2  # (1,3), (2,2)


def test_no_pairs() -> None:
    assert array_pair_sum([1, 2, 3], 10) == 0


def test_with_negatives() -> None:
    assert array_pair_sum([0, -1, 2, -3, 1], -2) == 1  # (-3,1)


def test_empty_list() -> None:
    assert array_pair_sum([], 5) == 0
