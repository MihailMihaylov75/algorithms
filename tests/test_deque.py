__author__ = 'Mihail Mihaylov'
import pytest
from src.algorithms.structures.deque import Deque


def test_add_and_remove_front(empty_deque: Deque[int]) -> None:
    empty_deque.add_front(1)
    assert empty_deque.remove_front() == 1


def test_add_and_remove_rear(empty_deque: Deque[int]) -> None:
    empty_deque.add_rear(2)
    assert empty_deque.remove_rear() == 2


def test_size_increases_and_decreases(empty_deque: Deque[int]) -> None:
    empty_deque.add_front(1)
    empty_deque.add_rear(2)
    assert empty_deque.size() == 2


def test_remove_from_empty_raises(empty_deque: Deque[int]) -> None:
    with pytest.raises(IndexError):
        empty_deque.remove_front()

