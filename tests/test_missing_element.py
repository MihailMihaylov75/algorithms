__author__ = 'Mihail Mihaylov'
from src.algorithms.arrays.missing_element import missing_element_sort, missing_element_count
import pytest


def test_sort_finds_missing_with_duplicates() -> None:
    assert missing_element_sort([5, 5, 7, 7], [5, 7, 7]) == 5


def test_count_finds_missing_unsorted() -> None:
    assert missing_element_count([1, 2, 3, 4], [3, 1, 4]) == 2


def test_sort_handles_negative_numbers() -> None:
    assert missing_element_sort([0, -1, -1], [0, -1]) == -1


def test_count_raises_on_invalid_lengths() -> None:
    with pytest.raises(ValueError):
        missing_element_count([1, 2], [1, 2])  # not len(b)+1
