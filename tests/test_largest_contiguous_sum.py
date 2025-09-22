__author__ = 'Mihail Mihaylov'
from src.algorithms.arrays.largest_contiguous_sum import largest_contiguous_sum


def test_mixed_numbers_returns_correct_max_sum() -> None:
    assert largest_contiguous_sum([1, -2, 3, 4, -1, 2, -5, 4]) == 8


def test_all_negative_returns_largest_element() -> None:
    assert largest_contiguous_sum([-2, -3, -1, -5]) == -1


def test_single_element_returns_itself() -> None:
    assert largest_contiguous_sum([5]) == 5


def test_empty_list_returns_zero() -> None:
    assert largest_contiguous_sum([]) == 0
